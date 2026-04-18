"""Deduplication functions."""

from Levenshtein import distance as levenshtein_distance


def deduplicate_papers(papers):
    """Deduplicate a list of paper dicts. Returns (unique_papers, dedup_stats)."""
    seen_pmids = {}
    seen_dois = {}
    duplicates_doi = 0
    duplicates_title = 0

    for paper in papers:
        pmid = paper.get("pmid", "")
        doi = (paper.get("doi", "") or "").lower().strip().replace("https://doi.org/", "").replace("http://doi.org/", "")
        title = paper.get("title", "").lower().strip()
        first_author = paper.get("authors_first", "").lower().strip()
        year = paper.get("year", 0)

        # Check PMID
        if pmid and pmid in seen_pmids:
            existing = seen_pmids[pmid]
            _merge_paper(existing, paper)
            continue

        # Check DOI
        if doi and doi in seen_dois:
            existing = seen_dois[doi]
            _merge_paper(existing, paper)
            duplicates_doi += 1
            continue

        # Check title + first author + year (fuzzy)
        found_dup = False
        if title and len(title) > 20:
            for existing_pmid, existing in seen_pmids.items():
                existing_title = existing.get("title", "").lower().strip()
                if existing_title and len(existing_title) > 20:
                    existing_year = existing.get("year", 0)
                    if year and existing_year and abs(year - existing_year) <= 1:
                        if levenshtein_distance(title, existing_title) <= 3:
                            _merge_paper(existing, paper)
                            duplicates_title += 1
                            found_dup = True
                            break
            if found_dup:
                continue

        # New paper
        if pmid:
            seen_pmids[pmid] = paper
        if doi:
            seen_dois[doi] = paper

    unique = list(seen_pmids.values())
    stats = {
        "duplicates_doi": duplicates_doi,
        "duplicates_title": duplicates_title,
        "unique_count": len(unique),
    }
    return unique, stats


def _merge_paper(existing, new_paper):
    """Merge metadata from new_paper into existing."""
    # Merge themes
    for t in new_paper.get("themes", []):
        if t not in existing.get("themes", []):
            existing.setdefault("themes", []).append(t)

    # Merge queries_matched
    for q in new_paper.get("queries_matched", []):
        if q not in existing.get("queries_matched", []):
            existing.setdefault("queries_matched", []).append(q)

    # Take higher citation count
    if (new_paper.get("citation_count", 0) or 0) > (existing.get("citation_count", 0) or 0):
        existing["citation_count"] = new_paper["citation_count"]
        existing["influential_citations"] = new_paper.get("influential_citations", 0)

    # Fill missing fields
    for field in ["abstract", "doi", "pmcid", "tldr"]:
        if not existing.get(field) and new_paper.get(field):
            existing[field] = new_paper[field]

    # Take higher score
    if (new_paper.get("relevance_score", 0) or 0) > (existing.get("relevance_score", 0) or 0):
        existing["relevance_score"] = new_paper["relevance_score"]
        existing["priority_tier"] = new_paper.get("priority_tier", existing.get("priority_tier", "C"))
