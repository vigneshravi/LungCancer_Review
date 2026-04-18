"""Process a single theme: search, fetch, score, write outputs."""

import json
import os
import sys
import time

# Add scripts dir to path
sys.path.insert(0, os.path.dirname(__file__))

from config import THEMES, ANCHOR_PMIDS, ALL_ANCHOR_PMIDS, PREDATORY_PUBLISHERS, FLAGGED_PUBLISHERS
from search import pubmed_search, pubmed_fetch, europepmc_search, semantic_scholar_enrich
from scoring import score_paper, assign_tier
from dedup import deduplicate_papers
from write_ris import write_ris_file, write_papers_csv


def process_theme(theme_id):
    """Process a single theme end-to-end."""
    theme = THEMES[theme_id]
    theme_name = theme["name"]
    theme_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "themes", theme["dir"])
    os.makedirs(theme_dir, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Processing {theme_id}: {theme_name}")
    print(f"{'='*60}")

    all_pmids = set()
    query_results = {}

    # Step 1: Run PubMed queries
    print(f"\n--- PubMed Searches ---")
    for i, query in enumerate(theme["queries"], 1):
        print(f"  Query {i}/{len(theme['queries'])}: {query[:70]}...")
        pmids = pubmed_search(query)
        print(f"    → {len(pmids)} results")
        query_results[query] = {"pubmed": len(pmids)}
        all_pmids.update(pmids)

    # Step 2: Add anchor PMIDs
    anchors = ANCHOR_PMIDS.get(theme_id, [])
    for a in anchors:
        all_pmids.add(a)
    print(f"\n  Total unique PMIDs (incl. anchors): {len(all_pmids)}")

    # Step 3: Fetch metadata from PubMed
    print(f"\n--- Fetching PubMed metadata ({len(all_pmids)} papers) ---")
    pmid_list = sorted(all_pmids)
    papers = pubmed_fetch(pmid_list)
    print(f"  Fetched {len(papers)} papers")

    # Step 4: Filter — remove papers without abstracts (unless anchor)
    anchor_set = set(anchors)
    filtered = []
    no_abstract = 0
    for p in papers:
        if not p.get("abstract") and p["pmid"] not in anchor_set:
            no_abstract += 1
            continue
        # Check predatory
        journal = p.get("journal", "")
        is_predatory = any(pub.lower() in journal.lower() for pub in PREDATORY_PUBLISHERS)
        if is_predatory:
            p["notes"] = (p.get("notes", "") + " FLAGGED: predatory publisher").strip()
            continue
        # Flag Hindawi
        if any(pub.lower() in journal.lower() for pub in FLAGGED_PUBLISHERS):
            p["notes"] = (p.get("notes", "") + " FLAGGED: Hindawi — manual review").strip()

        # English only
        if p.get("language", "eng") != "eng" and p["pmid"] not in anchor_set:
            continue

        filtered.append(p)

    print(f"  Filtered: {no_abstract} no-abstract, kept {len(filtered)}")

    # Step 5: Europe PMC supplementary (2-3 broadest queries)
    print(f"\n--- Europe PMC supplementary searches ---")
    epmc_count = 0
    broad_queries = theme["queries"][:3]
    existing_pmids = {p["pmid"] for p in filtered}
    for query in broad_queries:
        epmc_papers = europepmc_search(query, page_size=200, max_pages=1)
        new_epmc = [p for p in epmc_papers if p.get("pmid") and p["pmid"] not in existing_pmids and p.get("abstract")]
        for p in new_epmc:
            existing_pmids.add(p["pmid"])
        filtered.extend(new_epmc)
        epmc_count += len(new_epmc)
        query_results[query]["europepmc"] = len(epmc_papers)
        print(f"  Europe PMC: {query[:50]}... → {len(new_epmc)} new papers")

    # Step 6: Tag all papers with this theme
    for p in filtered:
        if theme_id not in p.get("themes", []):
            p.setdefault("themes", []).append(theme_id)

    # Step 7: Deduplicate within theme
    unique_papers, dedup_stats = deduplicate_papers(filtered)
    print(f"\n  After dedup: {len(unique_papers)} unique papers")

    # Step 8: Enrich with Semantic Scholar (anchors + small sample)
    print(f"\n--- Semantic Scholar enrichment ---")
    priority_papers = [p for p in unique_papers if p["pmid"] in anchor_set]
    other_papers = [p for p in unique_papers if p["pmid"] not in anchor_set]
    to_enrich = priority_papers + other_papers[:min(30, len(other_papers))]
    if to_enrich:
        semantic_scholar_enrich(to_enrich)
        print(f"  Enriched {len(to_enrich)} papers")

    # Step 9: Score and tier
    print(f"\n--- Scoring ---")
    keywords = theme["keywords"]
    for p in unique_papers:
        s = score_paper(p, theme_id, keywords)
        p["relevance_score"] = s
        p["priority_tier"] = assign_tier(s)
        if not p.get("theme_primary"):
            p["theme_primary"] = theme_id

    # Sort by score descending
    unique_papers.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)

    tier_a = [p for p in unique_papers if p["priority_tier"] == "A"]
    tier_b = [p for p in unique_papers if p["priority_tier"] == "B"]
    tier_c = [p for p in unique_papers if p["priority_tier"] == "C"]
    print(f"  Tier A: {len(tier_a)}, Tier B: {len(tier_b)}, Tier C: {len(tier_c)}")

    # Step 10: Write outputs
    print(f"\n--- Writing outputs ---")

    # papers.csv
    write_papers_csv(unique_papers, os.path.join(theme_dir, "papers.csv"))

    # papers.ris
    write_ris_file(unique_papers, os.path.join(theme_dir, "papers.ris"))

    # queries_run.md
    with open(os.path.join(theme_dir, "queries_run.md"), "w") as f:
        f.write(f"# Queries Run — {theme_id}: {theme_name}\n\n")
        for query, counts in query_results.items():
            f.write(f"- `{query}`\n")
            for source, count in counts.items():
                f.write(f"  - {source}: {count} results\n")

    # papers.md — annotated list
    with open(os.path.join(theme_dir, "papers.md"), "w") as f:
        f.write(f"# {theme_id.replace('_', ' ').title()} — {theme_name}\n\n")
        f.write(f"**Total papers: {len(unique_papers)}**\n")
        f.write(f"**Tier A (high priority): {len(tier_a)}**\n")
        f.write(f"**Tier B (supporting): {len(tier_b)}**\n")
        f.write(f"**Tier C (optional): {len(tier_c)}**\n\n---\n\n")

        f.write("## Tier A — Must cite\n\n")
        for i, p in enumerate(tier_a, 1):
            _write_paper_entry(f, i, p)

        f.write("\n## Tier B — Supporting\n\n")
        for i, p in enumerate(tier_b, 1):
            _write_paper_entry(f, i, p)

        f.write("\n## Tier C — Optional\n\n")
        for i, p in enumerate(tier_c[:30], 1):  # Limit C listing
            _write_paper_entry(f, i, p)
        if len(tier_c) > 30:
            f.write(f"\n*... and {len(tier_c) - 30} more Tier C papers (see papers.csv)*\n")

    # Save papers as JSON for later merging
    papers_json_path = os.path.join(theme_dir, "papers.json")
    with open(papers_json_path, "w") as f:
        json.dump(unique_papers, f, indent=2, default=str)

    retracted = [p for p in unique_papers if p.get("is_retracted")]

    print(f"\n  ✓ {theme_id} complete: {len(unique_papers)} papers")
    print(f"    Target: {theme['min_target']}, Achieved: {len(unique_papers)}")
    if len(unique_papers) < theme["min_target"]:
        print(f"    ⚠ Below target by {theme['min_target'] - len(unique_papers)}")

    return {
        "theme_id": theme_id,
        "theme_name": theme_name,
        "total": len(unique_papers),
        "tier_a": len(tier_a),
        "tier_b": len(tier_b),
        "tier_c": len(tier_c),
        "target": theme["min_target"],
        "retracted": len(retracted),
        "papers": unique_papers,
    }


def _write_paper_entry(f, i, p):
    """Write a single paper entry to markdown."""
    doi_link = f"[{p['doi']}](https://doi.org/{p['doi']})" if p.get("doi") else "N/A"
    f.write(f"### {i}. {p.get('authors_first', 'Unknown')} et al. {p.get('year', '')} — {p.get('title', '')[:80]}\n\n")
    f.write(f"**PMID:** {p.get('pmid', '')} | **DOI:** {doi_link} | **Journal:** *{p.get('journal', '')}* | **Score:** {p.get('relevance_score', 0):.2f}\n\n")
    if p.get("citation_count"):
        f.write(f"**Citations:** {p['citation_count']}")
        if p.get("influential_citations"):
            f.write(f" (influential: {p['influential_citations']})")
        f.write("\n\n")
    themes = p.get("themes", [])
    if len(themes) > 1:
        f.write(f"**Also fits:** {', '.join(themes)}\n\n")
    if p.get("notes"):
        f.write(f"**Notes:** {p['notes']}\n\n")
    f.write("---\n\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_theme.py <theme_id>")
        sys.exit(1)
    theme_id = sys.argv[1]
    if theme_id not in THEMES:
        print(f"Unknown theme: {theme_id}")
        sys.exit(1)
    result = process_theme(theme_id)
    print(json.dumps({k: v for k, v in result.items() if k != "papers"}, indent=2))
