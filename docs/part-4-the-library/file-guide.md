# How to Use This Library

> *66,671 non-retracted papers, organized, scored, and ready for manuscript writing.*

---

## Quick Access Guide

| What you need to do | Where to go |
|:---|:---|
| **Import the full reference library into EndNote** | `lit_review/master/master_library.ris` -- 66,671 papers |
| **Review only the highest-priority papers** | `lit_review/master/high_priority.csv` -- Tier A + top Tier B |
| **See which themes each paper belongs to** | `lit_review/master/theme_tags.csv` |
| **Start writing a manuscript section** | `lit_review/themes/theme_XX_*/section_notes.md` |
| **Browse papers for a specific theme** | `lit_review/themes/theme_XX_*/papers.md` -- annotated markdown |
| **Check for retracted papers before citing** | `lit_review/metadata/retracted_flagged.csv` |
| **Understand deduplication** | `lit_review/metadata/dedup_report.md` |
| **See exact search queries and hit counts** | `lit_review/themes/theme_XX_*/queries_run.md` |
| **Re-run or extend the pipeline** | `lit_review/scripts/` -- Python engine |

---

## Understanding the Tier System

| Tier | Score Range | What it means | How to use it |
|:---:|:---:|:---|:---|
| **A** | >= 0.7 | Must-cite. Anchor papers, high-impact journals, heavily cited. | Cite these in the manuscript. They define the field. |
| **B** | 0.4 -- 0.7 | Strong supporting evidence. Good journals, relevant findings. | Use selectively to support specific claims. |
| **C** | < 0.4 | Background reference. May be tangentially relevant. | Consult if you need additional evidence for a specific point. |

---

## Re-Running the Pipeline

```bash
cd lit_review/scripts

# Install dependencies
pip install requests lxml pandas tqdm rispy python-Levenshtein

# Run a single theme
python run_theme.py theme_01

# Generate synthesis notes for all themes
python synthesize.py all

# Build the master library
python build_master.py
```

All API responses are cached under `lit_review/cache/`. Re-runs use cached data automatically.
