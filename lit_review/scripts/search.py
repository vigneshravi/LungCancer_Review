"""PubMed, Europe PMC, and bioRxiv search functions with caching."""

import hashlib
import json
import os
import time
import requests
from lxml import etree

from config import (
    NCBI_EMAIL, NCBI_API_KEY, PUBMED_BASE, EUROPEPMC_BASE,
    PUBMED_DELAY, EUROPEPMC_DELAY, CACHE_DIR,
)


def _cache_path(api, query):
    h = hashlib.md5(query.encode()).hexdigest()
    d = os.path.join(CACHE_DIR, api)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, f"{h}.json")


def _load_cache(api, query):
    p = _cache_path(api, query)
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return None


def _save_cache(api, query, data):
    p = _cache_path(api, query)
    with open(p, "w") as f:
        json.dump(data, f)


def pubmed_search(query, retmax=800):
    """Search PubMed and return list of PMIDs (capped for efficiency)."""
    cache_key = f"search_v2:{query}:{retmax}"
    cached = _load_cache("pubmed", cache_key)
    if cached is not None:
        return cached

    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json",
        "email": NCBI_EMAIL,
        "sort": "relevance",
    }
    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    for attempt in range(3):
        try:
            time.sleep(PUBMED_DELAY)
            r = requests.get(PUBMED_BASE + "esearch.fcgi", params=params, timeout=30)
            if r.status_code == 429:
                time.sleep(2 ** (attempt + 1))
                continue
            r.raise_for_status()
            data = r.json()
            pmids = data.get("esearchresult", {}).get("idlist", [])
            _save_cache("pubmed", cache_key, pmids)
            return pmids
        except Exception as e:
            if attempt == 2:
                print(f"  [ERROR] PubMed search failed for: {query[:60]}... — {e}")
                return []
            time.sleep(2 ** (attempt + 1))
    return []


def pubmed_fetch(pmids):
    """Fetch metadata for a list of PMIDs. Returns list of parsed paper dicts."""
    if not pmids:
        return []

    papers = []
    batch_size = 200
    for i in range(0, len(pmids), batch_size):
        batch = pmids[i:i + batch_size]
        batch_key = f"fetch:{','.join(sorted(batch))}"
        cached = _load_cache("pubmed", batch_key)
        if cached is not None:
            papers.extend(cached)
            continue

        params = {
            "db": "pubmed",
            "id": ",".join(batch),
            "retmode": "xml",
            "rettype": "full",
            "email": NCBI_EMAIL,
        }
        if NCBI_API_KEY:
            params["api_key"] = NCBI_API_KEY

        for attempt in range(3):
            try:
                time.sleep(PUBMED_DELAY)
                r = requests.get(PUBMED_BASE + "efetch.fcgi", params=params, timeout=60)
                if r.status_code == 429:
                    time.sleep(2 ** (attempt + 1))
                    continue
                r.raise_for_status()
                batch_papers = _parse_pubmed_xml(r.content)
                _save_cache("pubmed", batch_key, batch_papers)
                papers.extend(batch_papers)
                break
            except Exception as e:
                if attempt == 2:
                    print(f"  [ERROR] PubMed fetch failed for batch {i}–{i+len(batch)}: {e}")
                time.sleep(2 ** (attempt + 1))

    return papers


def _parse_pubmed_xml(xml_bytes):
    """Parse PubMed XML into list of paper dicts."""
    papers = []
    try:
        root = etree.fromstring(xml_bytes)
    except Exception:
        return papers

    for article in root.findall(".//PubmedArticle"):
        try:
            paper = _parse_single_article(article)
            if paper:
                papers.append(paper)
        except Exception:
            continue
    return papers


def _parse_single_article(article):
    """Parse a single PubmedArticle element."""
    medline = article.find(".//MedlineCitation")
    if medline is None:
        return None

    pmid_el = medline.find("PMID")
    pmid = pmid_el.text if pmid_el is not None else ""
    if not pmid:
        return None

    art = medline.find("Article")
    if art is None:
        return None

    # Title
    title_el = art.find("ArticleTitle")
    title = "".join(title_el.itertext()) if title_el is not None else ""

    # Abstract
    abstract_parts = []
    abstract_el = art.find("Abstract")
    if abstract_el is not None:
        for at in abstract_el.findall("AbstractText"):
            label = at.get("Label", "")
            text = "".join(at.itertext())
            if label:
                abstract_parts.append(f"{label}: {text}")
            else:
                abstract_parts.append(text)
    abstract = " ".join(abstract_parts)

    # Authors
    authors_list = []
    author_els = art.findall(".//Author")
    for au in author_els:
        ln = au.find("LastName")
        fn = au.find("ForeName")
        if ln is not None:
            name = ln.text or ""
            if fn is not None and fn.text:
                # Get initials
                parts = (fn.text or "").split()
                initials = "".join(p[0] for p in parts if p)
                name += f" {initials}"
            authors_list.append(name)

    authors_first = ""
    authors_last = ""
    if authors_list:
        first_au = art.find(".//Author")
        if first_au is not None:
            ln = first_au.find("LastName")
            authors_first = ln.text if ln is not None else ""
        last_au = author_els[-1] if author_els else None
        if last_au is not None:
            ln = last_au.find("LastName")
            authors_last = ln.text if ln is not None else ""

    # Journal
    journal_el = art.find(".//Journal/Title")
    journal = journal_el.text if journal_el is not None else ""
    journal_iso_el = art.find(".//Journal/ISOAbbreviation")
    journal_iso = journal_iso_el.text if journal_iso_el is not None else ""

    # Date
    pub_date = art.find(".//Journal/JournalIssue/PubDate")
    year, month, day = 0, 0, 0
    if pub_date is not None:
        y = pub_date.find("Year")
        m = pub_date.find("Month")
        d = pub_date.find("Day")
        if y is not None and y.text:
            try:
                year = int(y.text)
            except ValueError:
                pass
        if m is not None and m.text:
            month_map = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
                         "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
            try:
                month = int(m.text)
            except ValueError:
                month = month_map.get(m.text, 0)
        if d is not None and d.text:
            try:
                day = int(d.text)
            except ValueError:
                pass

    # Volume, Issue, Pages
    vol_el = art.find(".//Journal/JournalIssue/Volume")
    volume = vol_el.text if vol_el is not None else ""
    iss_el = art.find(".//Journal/JournalIssue/Issue")
    issue = iss_el.text if iss_el is not None else ""
    pages_el = art.find(".//Pagination/MedlinePgn")
    pages = pages_el.text if pages_el is not None else ""

    # DOI
    doi = ""
    for eid in art.findall(".//ELocationID"):
        if eid.get("EIdType") == "doi":
            doi = eid.text or ""
            break
    if not doi:
        # Check ArticleIdList
        aid_list = article.find(".//PubmedData/ArticleIdList")
        if aid_list is not None:
            for aid in aid_list.findall("ArticleId"):
                if aid.get("IdType") == "doi":
                    doi = aid.text or ""
                    break

    # PMCID
    pmcid = ""
    aid_list = article.find(".//PubmedData/ArticleIdList")
    if aid_list is not None:
        for aid in aid_list.findall("ArticleId"):
            if aid.get("IdType") == "pmc":
                pmcid = aid.text or ""
                break

    # MeSH terms
    mesh_terms = []
    for mh in medline.findall(".//MeshHeading/DescriptorName"):
        if mh.text:
            mesh_terms.append(mh.text)

    # Keywords
    keywords = []
    for kw in medline.findall(".//KeywordList/Keyword"):
        if kw.text:
            keywords.append(kw.text)

    # Article types
    article_types = []
    for pt in art.findall(".//PublicationTypeList/PublicationType"):
        if pt.text:
            article_types.append(pt.text)

    # Language
    lang_el = art.find("Language")
    language = lang_el.text if lang_el is not None else "eng"

    # Retraction check
    is_retracted = "Retracted Publication" in article_types

    return {
        "pmid": pmid,
        "doi": doi,
        "pmcid": pmcid,
        "title": title,
        "abstract": abstract,
        "authors_first": authors_first,
        "authors_last": authors_last,
        "authors_all": ", ".join(authors_list),
        "journal": journal,
        "journal_iso": journal_iso,
        "year": year,
        "month": month,
        "day": day,
        "volume": volume,
        "issue": issue,
        "pages": pages,
        "mesh_terms": mesh_terms,
        "keywords": keywords,
        "article_types": article_types,
        "language": language,
        "citation_count": 0,
        "influential_citations": 0,
        "tldr": "",
        "source_api": "pubmed",
        "is_preprint": False,
        "is_retracted": is_retracted,
        "retraction_notice": "",
        "themes": [],
        "theme_primary": "",
        "relevance_score": 0.0,
        "priority_tier": "C",
        "queries_matched": [],
        "notes": "",
    }


def europepmc_search(query, page_size=500, max_pages=3):
    """Search Europe PMC, return list of paper dicts."""
    cache_key = f"epmc_search:{query}"
    cached = _load_cache("europepmc", cache_key)
    if cached is not None:
        return cached

    papers = []
    cursor = "*"
    for page in range(max_pages):
        params = {
            "query": query,
            "resultType": "core",
            "format": "json",
            "pageSize": page_size,
            "cursorMark": cursor,
        }
        for attempt in range(3):
            try:
                time.sleep(EUROPEPMC_DELAY)
                r = requests.get(EUROPEPMC_BASE + "search", params=params, timeout=30)
                if r.status_code == 429:
                    time.sleep(2 ** (attempt + 1))
                    continue
                r.raise_for_status()
                data = r.json()
                results = data.get("resultList", {}).get("result", [])
                if not results:
                    break

                for res in results:
                    pmid = res.get("pmid", "")
                    if not pmid:
                        continue
                    paper = {
                        "pmid": str(pmid),
                        "doi": res.get("doi", ""),
                        "pmcid": res.get("pmcid", ""),
                        "title": res.get("title", ""),
                        "abstract": res.get("abstractText", ""),
                        "authors_first": res.get("authorString", "").split(",")[0].strip().split()[-1] if res.get("authorString") else "",
                        "authors_last": "",
                        "authors_all": res.get("authorString", ""),
                        "journal": res.get("journalTitle", ""),
                        "journal_iso": res.get("journalTitle", ""),
                        "year": int(res.get("pubYear", 0)) if res.get("pubYear") else 0,
                        "month": 0,
                        "day": 0,
                        "volume": res.get("journalVolume", ""),
                        "issue": res.get("issue", ""),
                        "pages": res.get("pageInfo", ""),
                        "mesh_terms": [],
                        "keywords": [],
                        "article_types": [res.get("pubType", "")],
                        "language": res.get("language", "eng"),
                        "citation_count": int(res.get("citedByCount", 0)),
                        "influential_citations": 0,
                        "tldr": "",
                        "source_api": "europepmc",
                        "is_preprint": res.get("source", "") == "PPR",
                        "is_retracted": False,
                        "retraction_notice": "",
                        "themes": [],
                        "theme_primary": "",
                        "relevance_score": 0.0,
                        "priority_tier": "C",
                        "queries_matched": [],
                        "notes": "",
                    }
                    papers.append(paper)

                next_cursor = data.get("nextCursorMark", "")
                if not next_cursor or next_cursor == cursor:
                    break
                cursor = next_cursor
                break
            except Exception as e:
                if attempt == 2:
                    print(f"  [ERROR] Europe PMC search failed: {e}")
                time.sleep(2 ** (attempt + 1))

    _save_cache("europepmc", cache_key, papers)
    return papers


def semantic_scholar_enrich(papers, batch_size=50):
    """Enrich papers with Semantic Scholar citation data."""
    from config import SS_DELAY, SEMANTIC_SCHOLAR_API_KEY

    for i in range(0, len(papers), batch_size):
        batch = papers[i:i + batch_size]
        dois = [p["doi"] for p in batch if p.get("doi")]
        pmids = [p["pmid"] for p in batch if p.get("pmid") and not p.get("doi")]

        for paper in batch:
            identifier = None
            if paper.get("doi"):
                identifier = f"DOI:{paper['doi']}"
            elif paper.get("pmid"):
                identifier = f"PMID:{paper['pmid']}"
            else:
                continue

            cache_key = f"ss:{identifier}"
            cached = _load_cache("semanticscholar", cache_key)
            if cached is not None:
                paper["citation_count"] = cached.get("citationCount", 0) or 0
                paper["influential_citations"] = cached.get("influentialCitationCount", 0) or 0
                paper["tldr"] = cached.get("tldr", {}).get("text", "") if cached.get("tldr") else ""
                continue

            url = f"https://api.semanticscholar.org/graph/v1/paper/{identifier}"
            params = {"fields": "citationCount,influentialCitationCount,tldr"}
            headers = {}
            if SEMANTIC_SCHOLAR_API_KEY:
                headers["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY

            for attempt in range(3):
                try:
                    time.sleep(SS_DELAY)
                    r = requests.get(url, params=params, headers=headers, timeout=15)
                    if r.status_code == 429:
                        time.sleep(10)
                        continue
                    if r.status_code == 404:
                        _save_cache("semanticscholar", cache_key, {})
                        break
                    r.raise_for_status()
                    data = r.json()
                    _save_cache("semanticscholar", cache_key, data)
                    paper["citation_count"] = data.get("citationCount", 0) or 0
                    paper["influential_citations"] = data.get("influentialCitationCount", 0) or 0
                    tldr = data.get("tldr")
                    paper["tldr"] = tldr.get("text", "") if isinstance(tldr, dict) else ""
                    break
                except Exception:
                    if attempt == 2:
                        break
                    time.sleep(2 ** (attempt + 1))

    return papers
