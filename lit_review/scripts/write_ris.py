"""Write RIS files for EndNote import."""

import rispy


def paper_to_ris_entry(paper):
    """Convert a paper dict to a rispy-compatible dict."""
    entry = {
        "type_of_reference": "JOUR",
        "title": paper.get("title", ""),
        "year": str(paper.get("year", "")),
        "journal_name": paper.get("journal", ""),
        "alternate_title3": paper.get("journal_iso", ""),
        "volume": paper.get("volume", ""),
        "number": paper.get("issue", ""),
        "doi": paper.get("doi", ""),
        "abstract": paper.get("abstract", ""),
    }

    # Authors
    authors = []
    all_authors = paper.get("authors_all", "")
    if all_authors:
        for a in all_authors.split(","):
            a = a.strip()
            if a:
                authors.append(a)
    if authors:
        entry["authors"] = authors

    # Pages
    pages = paper.get("pages", "")
    if pages and "-" in pages:
        parts = pages.split("-", 1)
        entry["start_page"] = parts[0].strip()
        entry["end_page"] = parts[1].strip()
    elif pages:
        entry["start_page"] = pages

    # PMID in notes
    pmid = paper.get("pmid", "")
    themes = ", ".join(paper.get("themes", []))
    tier = paper.get("priority_tier", "C")
    score = paper.get("relevance_score", 0)
    notes = f"PMID: {pmid} | Theme: {themes} | Priority: {tier} | Score: {score:.2f}"
    if paper.get("notes"):
        notes += f" | {paper['notes']}"
    entry["notes_abstract"] = notes

    # Keywords
    kws = paper.get("keywords", [])
    if kws:
        entry["keywords"] = kws

    return entry


def write_ris_file(papers, filepath):
    """Write a list of papers to a RIS file."""
    entries = [paper_to_ris_entry(p) for p in papers]
    with open(filepath, "w", encoding="utf-8") as f:
        rispy.dump(entries, f)


def write_papers_csv(papers, filepath):
    """Write papers to CSV."""
    import csv
    if not papers:
        return

    fieldnames = [
        "pmid", "doi", "pmcid", "title", "authors_first", "authors_last",
        "journal", "journal_iso", "year", "month", "volume", "issue", "pages",
        "citation_count", "influential_citations", "source_api",
        "is_preprint", "is_retracted", "themes", "theme_primary",
        "relevance_score", "priority_tier", "notes",
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for p in papers:
            row = dict(p)
            row["themes"] = "; ".join(p.get("themes", []))
            row["queries_matched"] = "; ".join(p.get("queries_matched", []))
            writer.writerow(row)
