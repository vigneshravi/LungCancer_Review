"""Build master library: cross-theme dedup, master RIS, theme tags, high priority."""

import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from config import THEMES, ANCHOR_PMIDS, ALL_ANCHOR_PMIDS
from dedup import deduplicate_papers
from scoring import score_paper, assign_tier
from write_ris import write_ris_file, write_papers_csv

BASE = os.path.dirname(os.path.dirname(__file__))


def load_all_theme_papers():
    """Load papers from all theme JSON files."""
    all_papers = []
    theme_counts = {}
    for theme_id, theme in sorted(THEMES.items()):
        path = os.path.join(BASE, "themes", theme["dir"], "papers.json")
        if not os.path.exists(path):
            print(f"  ⚠ Missing {path}")
            continue
        with open(path) as f:
            papers = json.load(f)
        theme_counts[theme_id] = len(papers)
        # Ensure theme tag
        for p in papers:
            if theme_id not in p.get("themes", []):
                p.setdefault("themes", []).append(theme_id)
        all_papers.extend(papers)
        print(f"  Loaded {len(papers)} from {theme_id}")
    return all_papers, theme_counts


def main():
    print("=" * 60)
    print("Building Master Library")
    print("=" * 60)

    # Step 1: Load all papers
    print("\n--- Loading all theme papers ---")
    all_papers, theme_counts = load_all_theme_papers()
    raw_total = len(all_papers)
    print(f"\n  Raw total (with duplicates): {raw_total}")

    # Step 2: Deduplicate
    print("\n--- Cross-theme deduplication ---")
    unique_papers, dedup_stats = deduplicate_papers(all_papers)
    print(f"  Unique papers: {len(unique_papers)}")
    print(f"  Deduped via DOI: {dedup_stats['duplicates_doi']}")
    print(f"  Deduped via title: {dedup_stats['duplicates_title']}")

    # Step 3: Re-score with best theme assignment
    print("\n--- Re-scoring ---")
    for p in unique_papers:
        best_score = 0
        best_theme = ""
        for theme_id in p.get("themes", []):
            theme = THEMES.get(theme_id)
            if theme:
                s = score_paper(p, theme_id, theme["keywords"])
                if s > best_score:
                    best_score = s
                    best_theme = theme_id
        p["relevance_score"] = best_score
        p["priority_tier"] = assign_tier(best_score)
        if best_theme:
            p["theme_primary"] = best_theme

    # Sort by score
    unique_papers.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)

    tier_a = [p for p in unique_papers if p["priority_tier"] == "A"]
    tier_b = [p for p in unique_papers if p["priority_tier"] == "B"]
    tier_c = [p for p in unique_papers if p["priority_tier"] == "C"]

    print(f"  Tier A: {len(tier_a)}, Tier B: {len(tier_b)}, Tier C: {len(tier_c)}")

    # Step 4: Identify retracted
    retracted = [p for p in unique_papers if p.get("is_retracted")]
    print(f"  Retracted: {len(retracted)}")

    # Step 5: Bridge papers (3+ themes)
    bridge = [p for p in unique_papers if len(p.get("themes", [])) >= 3]
    print(f"  Bridge papers (3+ themes): {len(bridge)}")

    # Step 6: Write outputs
    master_dir = os.path.join(BASE, "master")
    metadata_dir = os.path.join(BASE, "metadata")
    os.makedirs(master_dir, exist_ok=True)
    os.makedirs(metadata_dir, exist_ok=True)

    # Master RIS
    print("\n--- Writing master_library.ris ---")
    # Only include non-retracted papers for the main library
    non_retracted = [p for p in unique_papers if not p.get("is_retracted")]
    write_ris_file(non_retracted, os.path.join(master_dir, "master_library.ris"))
    print(f"  Written {len(non_retracted)} papers to RIS")

    # Master CSV
    write_papers_csv(non_retracted, os.path.join(master_dir, "master_library.csv"))

    # High priority CSV
    write_papers_csv(tier_a + tier_b[:300], os.path.join(master_dir, "high_priority.csv"))

    # Theme tags CSV
    with open(os.path.join(master_dir, "theme_tags.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["pmid", "themes", "theme_primary"])
        for p in non_retracted:
            writer.writerow([
                p.get("pmid", ""),
                "; ".join(p.get("themes", [])),
                p.get("theme_primary", ""),
            ])

    # All papers JSON
    with open(os.path.join(metadata_dir, "all_papers.json"), "w") as f:
        json.dump({p["pmid"]: p for p in unique_papers}, f, indent=1, default=str)

    # All papers CSV
    write_papers_csv(unique_papers, os.path.join(metadata_dir, "all_papers.csv"))

    # Retracted CSV
    if retracted:
        write_papers_csv(retracted, os.path.join(metadata_dir, "retracted_flagged.csv"))

    # Dedup report
    with open(os.path.join(metadata_dir, "dedup_report.md"), "w") as f:
        f.write("# Deduplication Report\n\n")
        f.write(f"- **Total raw hits across all themes:** {raw_total}\n")
        f.write(f"- **Unique by PMID:** {len(unique_papers)}\n")
        f.write(f"- **Additional dedupe via DOI:** {dedup_stats['duplicates_doi']}\n")
        f.write(f"- **Additional dedupe via title fuzzy match:** {dedup_stats['duplicates_title']}\n")
        f.write(f"- **Final unique papers:** {len(unique_papers)}\n")
        f.write(f"- **Retracted (excluded from main library):** {len(retracted)}\n")
        f.write(f"- **Non-retracted in master library:** {len(non_retracted)}\n\n")

        f.write("## Per-theme counts (before cross-theme dedup)\n\n")
        for theme_id in sorted(theme_counts.keys()):
            target = THEMES[theme_id]["min_target"]
            count = theme_counts[theme_id]
            status = "✓" if count >= target else "⚠"
            f.write(f"- {theme_id}: {count} papers (target: {target}) {status}\n")

        f.write(f"\n## Bridge papers (appearing in 3+ themes): {len(bridge)}\n\n")
        for p in bridge[:50]:
            themes = ", ".join(p.get("themes", []))
            f.write(f"- PMID {p['pmid']}: {p.get('title', '')[:70]}... [{themes}]\n")
        if len(bridge) > 50:
            f.write(f"\n*... and {len(bridge) - 50} more bridge papers*\n")

    # Verify anchors
    print("\n--- Verifying anchor PMIDs ---")
    library_pmids = {p["pmid"] for p in unique_papers}
    missing_anchors = []
    for pmid in ALL_ANCHOR_PMIDS:
        if pmid not in library_pmids:
            missing_anchors.append(pmid)
            print(f"  ⚠ Missing anchor: {pmid}")
    if not missing_anchors:
        print("  ✓ All anchor PMIDs present")
    else:
        print(f"  ⚠ {len(missing_anchors)} anchor PMIDs missing")

    print("\n" + "=" * 60)
    print(f"Master library complete!")
    print(f"  Total unique papers: {len(unique_papers)}")
    print(f"  Non-retracted in RIS: {len(non_retracted)}")
    print(f"  Tier A: {len(tier_a)}")
    print(f"  Tier B: {len(tier_b)}")
    print(f"  Tier C: {len(tier_c)}")
    print(f"  Bridge papers: {len(bridge)}")
    print(f"  Retracted: {len(retracted)}")
    print("=" * 60)

    return {
        "raw_total": raw_total,
        "unique_total": len(unique_papers),
        "non_retracted": len(non_retracted),
        "tier_a": len(tier_a),
        "tier_b": len(tier_b),
        "tier_c": len(tier_c),
        "bridge": len(bridge),
        "retracted": len(retracted),
        "missing_anchors": missing_anchors,
        "theme_counts": theme_counts,
    }


if __name__ == "__main__":
    stats = main()
    print("\n" + json.dumps({k: v for k, v in stats.items()}, indent=2))
