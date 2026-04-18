"""Relevance scoring and priority tier assignment."""

import math
from config import TIER1_JOURNALS, TIER2_JOURNALS, TIER3_JOURNALS, ANCHOR_PMIDS


def score_paper(paper, theme_id, theme_keywords):
    """Compute relevance score for a paper within a theme."""
    # Anchor bonus
    if paper["pmid"] in ANCHOR_PMIDS.get(theme_id, []):
        return 1.0

    score = 0.0

    title = paper.get("title", "").lower()
    title_hits = sum(1 for kw in theme_keywords if kw.lower() in title)
    score += min(0.3, title_hits * 0.1)

    abstract = paper.get("abstract", "").lower()
    abstract_hits = sum(1 for kw in theme_keywords if kw.lower() in abstract)
    score += min(0.2, abstract_hits * 0.02)

    journal = paper.get("journal", "")
    if journal in TIER1_JOURNALS:
        score += 0.25
    elif journal in TIER2_JOURNALS:
        score += 0.15
    elif journal in TIER3_JOURNALS:
        score += 0.05

    cites = paper.get("citation_count", 0) or 0
    if cites > 0:
        score += min(0.2, math.log10(cites + 1) * 0.05)

    year = paper.get("year", 0) or 0
    if year >= 2023:
        score += 0.05

    article_types = paper.get("article_types", [])
    if "Review" in article_types or "Meta-Analysis" in article_types:
        score += 0.05

    return min(1.0, score)


def assign_tier(score):
    """Assign priority tier based on score."""
    if score >= 0.7:
        return "A"
    elif score >= 0.4:
        return "B"
    else:
        return "C"
