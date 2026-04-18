# The Scale of This Search

> *"Better to over-collect and triage than under-collect and redo."*

We interrogated **three major biomedical databases** -- PubMed, Europe PMC, and Semantic Scholar -- with **213 structured queries** spanning every dimension of the lung cancer multi-omics and AI/ML landscape.

---

## The Funnel

```
                    T H E   F U N N E L

        +-----------------------------------------+
        |                                         |
        |         78,775  Raw API Hits             |
        |                                         |
        +-------------------+---------------------+
                            |
                     -11,896 duplicates
                            |
        +-------------------v---------------------+
        |                                         |
        |       66,879  Unique Papers              |
        |                                         |
        +------+----------+----------+------------+
               |          |          |
          +----v---+ +----v----+ +--v------+       +----------+
          | Tier A | | Tier B  | | Tier C  |       | Retracted|
          |   49   | |  2,861  | | 63,969  |       |   208    |
          | Must   | | Strong  | | Back-   |       | Excluded |
          | Cite   | | Support | | ground  |       |          |
          +--------+ +---------+ +---------+       +----------+
```

---

## By the Numbers

| | Metric | Value |
|:---:|:---|---:|
| | Total raw hits | **78,775** |
| | Unique after deduplication | **66,879** |
| | Non-retracted (master RIS) | **66,671** |
| **A** | **Must-cite papers** (score >= 0.7) | **49** |
| **B** | **Supporting evidence** (score 0.4--0.7) | **2,861** |
| C | Background reference (score < 0.4) | 63,969 |
| | Bridge papers spanning 3+ themes | 1,928 |
| | Retracted papers flagged and excluded | 208 |
| | Anchor PMIDs recovered | 34 / 35 |

---

## Search Architecture

- **Primary source:** PubMed (NCBI E-utilities) -- up to 800 results per query, relevance-sorted
- **Supplementary:** Europe PMC -- 3 broadest queries per theme, up to 200 results each
- **Enrichment:** Semantic Scholar -- anchor PMIDs + ~30 top papers per theme for citation counts
- **Deduplication:** PMID-based primary, DOI secondary, fuzzy title match (Levenshtein distance <= 3) tertiary
- **Scoring:** Title/abstract keyword density + journal tier + citation count + recency + article type
- **Caching:** All API responses cached for reproducible re-runs
