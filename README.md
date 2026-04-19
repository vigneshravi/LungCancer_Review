<div align="center">

# Lung Cancer Multi-Omics & AI/ML Literature Review

### A Systematic Literature Intelligence Report

[![GitBook](https://img.shields.io/badge/Read_the_GitBook-blue?style=for-the-badge&logo=gitbook&logoColor=white)](https://vigneshravi.github.io/LungCancer_Review/)
[![Papers](https://img.shields.io/badge/Papers-66%2C879-blue?style=for-the-badge)](lit_review/master/)
[![Themes](https://img.shields.io/badge/Themes-12-coral?style=for-the-badge&color=e8655a)](docs/part-2-the-landscape/)
[![PMIDs Verified](https://img.shields.io/badge/PMIDs_Verified-155%2F155-green?style=for-the-badge&color=4caf7d)](docs/pmid-verification-report.md)
[![Target](https://img.shields.io/badge/Journal-npj_Precision_Oncology-gold?style=for-the-badge&color=d4a843)](https://www.nature.com/npjprecisiononcology/)

---

**[Read the full report on GitBook](https://vigneshravi.github.io/LungCancer_Review/)**

**66,879 unique papers** | **12 thematic chapters** | **213 queries** | **3 databases** | **155 verified citations**

*Mapping the evidence landscape for multi-omics integration and AI/ML in lung cancer -- strengths, gaps, and translational opportunities.*

**Vignesh Ravichandran** | Digital Health Institute, Rutgers University

</div>

---

## Read the Full Report

**[Read the full GitBook here: https://vigneshravi.github.io/LungCancer_Review/](https://vigneshravi.github.io/LungCancer_Review/)**

The GitBook contains 12 book-chapter-length narrative syntheses, each with a NotebookLM-generated infographic, inline PMID-linked citations, and detailed analysis of consensus, controversy, and gaps.

Browse the chapters:

| | Chapter | What it covers |
|:---:|:---|:---|
| I | [**Molecular Heterogeneity**](docs/part-2-the-landscape/01-molecular-heterogeneity.md) | TCGA/CPTAC atlas, LUAD vs LUSC vs SCLC taxonomy, co-mutation biology, proteogenomics |
| II | [**Multi-Omics Methods**](docs/part-2-the-landscape/02-multi-omics-methods.md) | iCluster, SNF, MOFA+, deep learning integration, benchmarking studies |
| III | [**Multi-Omics Applications**](docs/part-2-the-landscape/03-multi-omics-applications.md) | Proteogenomic subtyping, TME characterization, prognostic signatures |
| IV | [**AI/ML in Lung Cancer**](docs/part-2-the-landscape/04-ai-ml.md) | Histopathology DL, foundation models, radiomics, ICI prediction, validation crisis |
| V | [**Sex & Gender Differences**](docs/part-2-the-landscape/05-sex-gender.md) | Estrogen receptor biology, immunotherapy sex effects, the gap as a finding |
| VI | [**Never-Smoker Lung Cancer**](docs/part-2-the-landscape/06-never-smoker.md) | Piano/mezzo/forte subtypes, mutational signatures, cold microenvironment |
| VII | [**Environmental Exposures**](docs/part-2-the-landscape/07-environmental.md) | PM2.5 promotional mechanism, radon, asbestos, indoor pollution |
| VIII | [**Epigenetics**](docs/part-2-the-landscape/08-epigenetics.md) | Methylation, chromatin remodeling, ncRNA crisis (76 retractions), cfDNA |
| IX | [**Immune Biomarkers**](docs/part-2-the-landscape/09-immune-biomarkers.md) | TMB, PD-L1, Immunophenoscore, TME archetypes, microbiome |
| X | [**Translational Bottleneck**](docs/part-2-the-landscape/10-translational.md) | Biomarker testing disparities, RWE, molecular tumor boards |
| XI | [**Drug Repurposing**](docs/part-2-the-landscape/11-drug-repurposing.md) | CMap, DGIdb, synthetic lethality, KRAS/STK11/KEAP1 targeting |
| XII | [**Emerging Frontiers**](docs/part-2-the-landscape/12-emerging-frontiers.md) | scRNA-seq atlases, spatial omics, liquid biopsy, metabolomics |

Also see:
- [**Critical Gaps**](docs/part-3-the-gaps/critical-gaps.md) -- The review's strongest original contributions
- [**Surprising Findings**](docs/part-3-the-gaps/surprising-findings.md) -- 8 insights that should shape the manuscript
- [**PMID Verification Report**](docs/pmid-verification-report.md) -- All 155 citations verified against PubMed

---

## Key Findings at a Glance

### The Numbers

| Metric | Value |
|:---|---:|
| Raw API hits across all themes | 78,775 |
| Unique papers after deduplication | **66,879** |
| Tier A (must-cite, score >= 0.7) | 49 |
| Tier B (supporting, score 0.4-0.7) | 2,861 |
| Bridge papers (span 3+ themes) | 1,928 |
| Retracted papers (flagged, excluded) | 208 |

### The Most Important Gaps

1. **Sex-stratified multi-omics analyses are nearly absent** -- No multi-omics study has systematically stratified by sex
2. **No multi-omics study has focused on NSCLC in never-smokers** -- Despite 10-25% of all lung cancers arising in never-smokers
3. **Exposome-to-subtype mapping does not exist** -- We know PM2.5 causes lung cancer; we don't know which subtypes
4. **AI fairness assessment is rarely performed** -- Foundation models trained on Western cohorts deployed globally without equity audits
5. **76 retractions in epigenetics** -- Concentrated in miRNA/lncRNA prognostic signatures, signaling a reproducibility crisis

---

## Repository Structure

```
LungCancer_Review/
+-- README.md                              # This file
+-- LITERATURE_REVIEW_DASHBOARD.md         # Full styled dashboard with results
+-- book.json                              # GitBook configuration
+-- docs/                                  # GitBook chapters
|   +-- SUMMARY.md                         # Table of contents
|   +-- styles/custom.css                  # Custom GitBook theme (teal/coral/gold)
|   +-- figures/                           # NotebookLM infographics (12 PNGs)
|   +-- part-1-the-search/                 # Search methodology and overview
|   +-- part-2-the-landscape/              # 12 theme chapters with citations
|   +-- part-3-the-gaps/                   # Critical gaps and surprising findings
|   +-- part-4-the-library/                # File access guide
|   +-- pmid-verification-report.md        # 155/155 PMIDs verified
+-- lit_review/                            # Raw literature data
|   +-- master/                            # Deduplicated master library
|   |   +-- master_library.csv             # All papers (flat table)
|   |   +-- high_priority.csv              # Tier A + top Tier B
|   |   +-- theme_tags.csv                 # PMID -> theme mapping
|   +-- metadata/                          # Dedup reports, retracted papers
|   +-- themes/theme_XX_*/                 # Per-theme papers, RIS, synthesis notes
|   +-- scripts/                           # Python search/fetch/score/dedup pipeline
|   +-- cache/                             # API response cache (gitignored)
+-- CLAUDE_CODE_LITREVIEW_SPEC.md          # Original search specification
```

---

## How to Use

### For manuscript writing
Start with the [chapter synthesis notes](docs/part-2-the-landscape/) -- they are written at book-chapter length with inline citations ready for extraction.

### For reference management
Import `lit_review/master/master_library.csv` or theme-level `.ris` files into your reference manager.

### For extending the search
```bash
cd lit_review/scripts
pip install requests lxml pandas tqdm rispy python-Levenshtein
python run_theme.py theme_01  # Re-run a theme
python synthesize.py all       # Regenerate synthesis notes
python build_master.py         # Rebuild master library
```

---

## Citation

If you use this literature review in your work, please cite:

> Ravichandran V. *Lung Cancer Multi-Omics & AI/ML Literature Review: A Systematic Evidence Base.* Digital Health Institute, Rutgers University. April 2026. Available at: https://github.com/vigneshravi/LungCancer_Review

---

## License

This is an academic research project. The literature review content, synthesis notes, and analysis are original work. All cited papers belong to their respective authors and publishers. PMIDs link to PubMed for access to original abstracts.

---

<div align="center">

*Built with Claude Code | 177 PubMed queries + 36 Europe PMC queries | Infographics by NotebookLM*

</div>
