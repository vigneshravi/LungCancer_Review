# Literature Review — Multi-Omics + AI/ML in Lung Cancer

This directory contains the comprehensive evidence base for a narrative review on
multi-omics integration and AI/ML in lung cancer, with emphasis on sex, smoking status,
subtype, and ancestry stratification.

## Quick Start

1. **For EndNote import:** Open `master/master_library.ris` — this is the primary deliverable containing 66,671 non-retracted papers.
2. **For high-priority papers:** See `master/high_priority.csv` for Tier A + top Tier B papers.
3. **For manuscript writing:** Read `themes/theme_XX_*/section_notes.md` for synthesized findings per theme.
4. **For overall summary:** Read `SUMMARY.md`.

## Directory Structure

- `master/` — Combined, deduplicated master library (RIS, CSV, theme tags)
- `metadata/` — All papers JSON/CSV, dedup report, retracted papers
- `themes/` — Per-theme papers, RIS files, synthesis notes, query logs
- `scripts/` — Python search/fetch/score/dedup pipeline
- `search_log/` — Query logs and progress tracking
- `cache/` — API response cache (gitignored)

## Themes

| # | Theme | Papers |
|---|-------|--------|
| 01 | Lung cancer molecular heterogeneity | 6,812 |
| 02 | Multi-omics integration methods | 5,289 |
| 03 | Multi-omics applications in lung cancer | 2,648 |
| 04 | AI/ML in lung cancer and oncology | 11,167 |
| 05 | Sex and gender differences | 4,707 |
| 06 | Never-smoker lung cancer | 2,689 |
| 07 | Environmental exposures | 4,023 |
| 08 | Epigenetics | 5,902 |
| 09 | Immune biomarkers and immunotherapy | 6,459 |
| 10 | Translational/real-world outcomes | 6,431 |
| 11 | Drug repurposing | 6,386 |
| 12 | Emerging frontiers (scRNA, spatial, liquid biopsy) | 6,179 |

## Re-running

```bash
cd lit_review/scripts
pip install requests lxml pandas tqdm rispy python-Levenshtein

# Run a single theme
python run_theme.py theme_01

# Generate synthesis notes
python synthesize.py all

# Build master library
python build_master.py
```

Cache is preserved between runs for efficiency.
