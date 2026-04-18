# Literature Review — Final Summary

**Project:** Multi-Omics Integration and AI/ML in Lung Cancer — Strengths, Gaps, and Translational Opportunities
**Date:** 2026-04-18
**Target journal:** npj Precision Oncology

---

## Overall Statistics

| Metric | Count |
|--------|-------|
| Raw hits across all themes | 78,775 |
| Unique papers (after dedup) | 66,879 |
| Non-retracted (in master_library.ris) | 66,671 |
| Tier A (high priority, score ≥ 0.7) | 49 |
| Tier B (supporting, score 0.4–0.7) | 2,861 |
| Tier C (optional, score < 0.4) | 63,969 |
| Bridge papers (3+ themes) | 1,928 |
| Retracted papers (flagged, excluded) | 208 |
| Anchor PMIDs recovered | 34 of 35 |

---

## Per-Theme Results

| Theme | Papers | Target | Tier A | Tier B | Status |
|-------|--------|--------|--------|--------|--------|
| 01 — Molecular heterogeneity | 6,812 | 100 | 14 | 444 | ✓ |
| 02 — Multi-omics methods | 5,289 | 100 | 6 | 196 | ✓ |
| 03 — Multi-omics applications | 2,648 | 100 | 1 | 127 | ✓ |
| 04 — AI/ML in lung cancer | 11,167 | 150 | 8 | 803 | ✓ |
| 05 — Sex/gender differences | 4,707 | 75 | 2 | 66 | ✓ |
| 06 — Never-smoker lung cancer | 2,689 | 75 | 2 | 76 | ✓ |
| 07 — Environmental exposures | 4,023 | 75 | 2 | 79 | ✓ |
| 08 — Epigenetics | 5,902 | 75 | 0 | 91 | ✓ |
| 09 — Immune biomarkers | 6,459 | 75 | 9 | 679 | ✓ |
| 10 — Translational/real-world | 6,431 | 75 | 0 | 67 | ✓ |
| 11 — Drug repurposing | 6,386 | 75 | 0 | 24 | ✓ |
| 12 — Emerging frontiers | 6,179 | 75 | 2 | 108 | ✓ |

All 12 themes exceeded their minimum paper count targets.

---

## Search Methodology

- **Primary source:** PubMed (NCBI E-utilities) — up to 800 results per query, relevance-sorted
- **Supplementary:** Europe PMC (3 broadest queries per theme, up to 200 results each)
- **Enrichment:** Semantic Scholar (anchor PMIDs + ~30 top papers per theme for citation counts)
- **Deduplication:** PMID-based primary, DOI secondary, fuzzy title match (Levenshtein ≤ 3) tertiary
- **Scoring:** Title/abstract keyword density + journal tier + citation count + recency + article type
- **All API responses cached** under `lit_review/cache/` for fast re-runs

---

## Anchor PMID Coverage

34 of 35 specified anchor PMIDs were recovered. The missing PMID:

- **33524135** — Cantini et al. multi-omics benchmarking (Nature Communications, 2021). This PMID returns empty from the PubMed API. The correct PMID appears to be **33402734**, which is present in the library through theme_02 queries.

Some anchor PMIDs fetched papers with different metadata than expected (e.g., PMID 28369062, 30590492) — these may represent PubMed ID reassignments or corrections in the NCBI database. The underlying papers (mixOmics/DIABLO, NEMO) were captured through query-based searches regardless.

---

## Top 20 Papers (Highest Relevance Scores)

These are the papers most likely to be cited across the review:

1. **PMID 25079552** — TCGA LUAD 2014 (*Nature*) — Comprehensive LUAD molecular profiling
2. **PMID 22960745** — TCGA LUSC 2012 (*Nature*) — Comprehensive LUSC genomic characterization
3. **PMID 26168399** — George et al. 2015 (*Nature*) — SCLC genomic profiles
4. **PMID 30926931** — Rudin et al. 2019 (*Nature Reviews Cancer*) — SCLC molecular subtypes synthesis
5. **PMID 31406302** — Skoulidis et al. 2019 (*Nature Reviews Cancer*) — NSCLC co-occurring genomic alterations
6. **PMID 32649874** — Gillette et al. 2020 (*Cell*) — CPTAC LUAD proteogenomics
7. **PMID 32649875** — Chen et al. 2020 (*Cell*) — East Asia non-smoking proteogenomics
8. **PMID 32649877** — Xu et al. 2020 (*Cell*) — LUAD integrative proteomics
9. **PMID 38181741** — Liu et al. 2024 (*Cell*) — SCLC proteogenomics
10. **PMID 33011388** — Baine et al. 2020 (*JTO*) — SCLC subtypes (ASCL1/NEUROD1/POU2F3/YAP1)
11. **PMID 30224757** — Coudray et al. 2018 (*Nature Medicine*) — NSCLC histopathology deep learning
12. **PMID 34493867** — Zhang et al. 2021 (*Nature Genetics*) — Never-smoker lung cancer genomic classification
13. **PMID 37046093** — Martínez-Ruiz et al. 2023 (*Nature*) — Lung cancer genomic-transcriptomic evolution
14. **PMID 32015526** — Chen et al. 2020 (*Nature Genetics*) — East Asian LUAD genomic landscape
15. **PMID 25765070** — Rizvi et al. 2015 (*Science*) — Mutational landscape and PD-1 sensitivity
16. **PMID 29628290** — Thorsson et al. 2018 (*Immunity*) — Pan-cancer immune landscape
17. **PMID 32393329** — Argelaguet et al. 2020 (*Genome Biology*) — MOFA+ multi-omics framework
18. **PMID 35944502** — Chen et al. 2022 (*Cancer Cell*) — Pan-cancer multimodal histology-genomic analysis
19. **PMID 29778737** — Conforti et al. 2018 (*Lancet Oncology*) — Sex and immunotherapy meta-analysis
20. **PMID 34019806** — Bagaev et al. 2021 (*Cancer Cell*) — Conserved tumor microenvironment subtypes

---

## Bridge Papers

1,928 papers span 3 or more themes, serving as cross-cutting references. Notable examples:

- Papers spanning 7–8 themes tend to be recent (2024–2026) multi-omics + AI reviews or integrative studies
- These bridge papers are particularly valuable for the review's connecting narrative

---

## Known Gaps and Limitations

### Themes with limited Tier A papers
- **Theme 08 (Epigenetics):** 0 Tier A papers — the scoring algorithm weights journal prestige and citation counts, and epigenetics papers are spread across many journals. The 91 Tier B papers provide solid coverage.
- **Theme 10 (Translational):** 0 Tier A — real-world evidence literature is diffuse and less concentrated in top-tier journals.
- **Theme 11 (Drug repurposing):** 0 Tier A, only 24 Tier B — this area is more nascent and computational, with fewer high-impact individual papers. Consider expanding with targeted manual searches.

### Search limitations
- PubMed queries capped at 800 results per query for efficiency — some very broad queries may have additional relevant results beyond this cap
- Semantic Scholar enrichment limited to ~30-40 papers per theme; citation counts are available for a subset only
- bioRxiv preprints not systematically searched via API (Europe PMC captures some)
- No systematic Google Scholar or Semantic Scholar search conducted

### Potential follow-up searches needed
- Lung cancer organoid/PDX models for drug testing (relates to themes 03, 11)
- Ancestry-specific molecular profiling beyond East Asian populations (themes 05, 06, 10)
- Health economics of multi-omics testing (theme 10)
- Specific drug repurposing candidates (dimethyl fumarate, KEAP1 modulators) — only 13 results for the DMF/KEAP1 query

---

## Retracted Papers

208 retracted papers were identified and excluded from the master library. They are preserved in `metadata/retracted_flagged.csv` for reference. Theme 08 (epigenetics) had the highest retraction count (76), consistent with known reproducibility concerns in miRNA/lncRNA prognostic signature literature.

---

## File Inventory

| File | Purpose |
|------|---------|
| `master/master_library.ris` | **PRIMARY DELIVERABLE** — 66,671 papers, EndNote-importable |
| `master/master_library.csv` | Flat table of all non-retracted papers |
| `master/high_priority.csv` | Tier A + top Tier B papers (~300–500) |
| `master/theme_tags.csv` | PMID → theme mapping |
| `metadata/all_papers.json` | Complete paper data indexed by PMID |
| `metadata/all_papers.csv` | Flat table of all papers including retracted |
| `metadata/dedup_report.md` | Deduplication statistics |
| `metadata/retracted_flagged.csv` | Retracted papers for reference |
| `themes/theme_XX_*/papers.md` | Annotated paper lists per theme |
| `themes/theme_XX_*/papers.ris` | Theme-level RIS files |
| `themes/theme_XX_*/papers.csv` | Theme-level CSV files |
| `themes/theme_XX_*/section_notes.md` | **Synthesis notes for manuscript writing** |
| `themes/theme_XX_*/queries_run.md` | Search queries and hit counts |

---

## Notes for the Manuscript Writing Session

### Which themes have the strongest evidence
1. **Theme 01 (Molecular heterogeneity)** — Very strong. TCGA, CPTAC, and major genomic studies provide a solid foundation. 14 Tier A papers.
2. **Theme 04 (AI/ML)** — Strong and rapidly growing. 8 Tier A, 803 Tier B. Foundation models and histopathology DL are the most active subfields.
3. **Theme 09 (Immune biomarkers)** — Strong. 9 Tier A. TMB, PD-L1, and composite biomarker literature is mature.
4. **Theme 02 (Multi-omics methods)** — Solid methodological foundation. Benchmarking studies and tool papers well-represented.

### Which themes feel under-covered and may need targeted follow-up
1. **Theme 11 (Drug repurposing)** — Only 24 Tier B papers. The computational drug repurposing literature specific to lung cancer multi-omics is thin. May need manual expansion with specific pathway papers.
2. **Theme 10 (Translational)** — 0 Tier A, 67 Tier B. Real-world evidence is diffuse. Consider targeted searches on MYLUNG, Flatiron-specific publications, and ASCO/ESMO abstracts.
3. **Theme 05 (Sex/gender)** — 66 Tier B. The sex-stratified molecular literature for lung cancer remains limited, which itself is a key finding for the review.

### Top 20 papers to cite first
See the "Top 20 Papers" section above — these form the backbone of the review.

### Surprising findings
1. **Retraction rate in epigenetics theme (76 retractions)** — Notably high, suggesting reproducibility issues in miRNA/lncRNA prognostic signature studies. This finding could itself be mentioned in the review as evidence for the need for rigorous validation.
2. **1,928 bridge papers across 3+ themes** — The cross-cutting nature of recent multi-omics + AI literature suggests the field is increasingly integrative, supporting the review's central thesis.
3. **Never-smoker lung cancer literature is smaller than expected** — Despite clinical importance, the molecular characterization literature for never-smokers is surprisingly thin compared to smoking-associated disease.
4. **Environmental exposure + molecular subtype intersection barely exists** — The exposome-level studies connecting PM2.5/radon/pollutants to specific molecular subtypes are extremely sparse, representing a major gap.

### Contradictions with current outline
The current outline (from `Outline for Review Paper.docx`) focuses primarily on NSCLC (LUAD/LUSC) and non-smokers. The literature suggests:
- SCLC molecular subtyping (ASCL1/NEUROD1/POU2F3/YAP1) deserves mention even in an NSCLC-focused review, as SCLC transformation is a resistance mechanism
- The outline underemphasizes the foundation model/LLM revolution in pathology — this is the fastest-moving area in the AI/ML theme and warrants dedicated discussion
- Drug repurposing section may need to be broadened beyond dimethyl fumarate to include synthetic lethality approaches (KRAS/STK11/KEAP1) which have more literature support
- The outline could benefit from a section on liquid biopsy and cfDNA methylation, which is rapidly emerging as both a diagnostic and monitoring tool

---

*Generated by Claude Code literature review pipeline on 2026-04-18.*
*Total search runtime: ~3 hours. All API responses cached for re-runs.*
