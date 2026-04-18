# CLAUDE CODE SPEC: Comprehensive Literature Review Execution

**Owner:** Vignesh Ravichandran, DHI
**Task:** Execute exhaustive, deduplicated literature search across 12 themes for a lung cancer multi-omics + AI/ML review paper. Produce an EndNote-ready reference library plus theme-level analysis notes ready for manuscript writing.
**Runtime:** Budget 8–14 hours of autonomous execution. Do not stop early. Be ambitious about paper counts.
**Next step after completion:** Manuscript writing — your output is the evidence base.

---

## 0. How to use this spec

1. Read this entire document before starting.
2. Also read, if present in the working directory: `PROJECT_MASTER_CONTEXT.md`, `Literature_Review_Plan.md`, `Outline_for_Review_Paper.docx`. These give background context. This spec is authoritative where they conflict.
3. Work autonomously. Do not pause to ask for confirmation unless you encounter a genuine blocker (API outage, permission error, ambiguous output format).
4. Create all outputs in a `lit_review/` directory under the working directory.
5. Commit progress frequently. Each theme completion is a natural commit point.
6. When you finish, produce a final `SUMMARY.md` with totals, highlights, and known gaps.

---

## 1. Mission statement

Build the most comprehensive evidence base possible for a narrative review on **multi-omics integration and AI/ML in lung cancer — strengths, gaps, and translational opportunities**, with a highlighted section on sex, smoking status, subtype, and ancestry stratification.

Primary target journal: *npj Precision Oncology*. Secondary: *Briefings in Bioinformatics*, *Molecular Cancer*, *Cancer Research*, *Translational Lung Cancer Research*.

The review needs substantial breadth. Better to over-collect and triage than under-collect and redo.

---

## 2. Scope and boundaries

**In scope:**
- Lung cancer broadly — NSCLC (LUAD, LUSC, large cell), SCLC, mixed histology, pre-neoplastic lesions
- All omics layers: genomics, transcriptomics, epigenomics, proteomics, metabolomics, pharmacogenomics, single-cell, spatial
- AI/ML applications in lung cancer and transferable pan-oncology ML methods
- Methods papers for multi-omics integration (pan-cancer included since methods transfer)
- Sex/gender, smoking status, ancestry, environmental exposure literature
- Liquid biopsy, ctDNA, cfDNA methylation
- Drug repurposing, pharmacogenomics, real-world treatment outcomes

**Out of scope:**
- Non-lung primary research that does not inform methods or comparison
- Case reports
- Conference proceedings (except AACR/ASCO/ESMO/WCLC which are in scope as abstracts)
- Retracted papers (flag them separately)
- Predatory journal publications (flag and exclude — see list in Section 9)

**Time frame:**
- Landmark/foundational papers: any year
- Primary evidence: 2018–2026 preferred
- Fast-moving areas (foundation models, LLMs, spatial omics): 2022–2026 only

**Languages:** English only.

---

## 3. Technical approach

### 3.1 Primary data sources

**NCBI E-utilities (PubMed):** Primary source.
- Base URL: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`
- `esearch.fcgi` for searches, `efetch.fcgi` for metadata
- Rate limit: 3 req/sec without key, 10 req/sec with API key
- Get an API key at `https://www.ncbi.nlm.nih.gov/account/` if not already set — it triples throughput
- Use XML return format for `efetch`, parse with `lxml` or `xml.etree`

**bioRxiv/medRxiv API:** For preprints
- Base URL: `https://api.biorxiv.org/`
- Endpoint: `/details/biorxiv/{DOI}` and `/pubs/biorxiv/{date}/{date}`
- No auth required

**Europe PMC API:** Complementary to PubMed, covers some non-PubMed journals
- Base URL: `https://www.ebi.ac.uk/europepmc/webservices/rest/`
- Endpoint: `search?query={query}&resulttype=core&format=json`
- Good for finding papers PubMed missed

**Semantic Scholar API:** For citation counts and ranking
- Base URL: `https://api.semanticscholar.org/graph/v1/`
- Endpoint: `/paper/{DOI}?fields=citationCount,influentialCitationCount,tldr`
- Rate limit: 100 req/5 min without key. Request key at semanticscholar.org/product/api
- Use for ranking papers within themes by influence

**CrossRef API:** For DOI resolution and citation network
- Base URL: `https://api.crossref.org/`
- Useful for filling metadata gaps

### 3.2 Environment setup

```bash
# Install dependencies
pip install requests lxml pandas tqdm rispy python-Levenshtein
```

### 3.3 Rate limiting and caching

- Cache ALL API responses to `lit_review/cache/{api}/{hash}.json`
- Respect rate limits with `time.sleep()` between calls
- Use exponential backoff on 429/503 errors
- On resume, check cache first before re-calling APIs

### 3.4 Parallelization

Process themes in parallel where safe. Use `concurrent.futures.ThreadPoolExecutor` with `max_workers=4`. Do not parallelize individual PubMed calls within the same theme — that will trigger rate limits.

---

## 4. Deliverables structure

Create this exact directory structure:

```
lit_review/
├── metadata/
│   ├── all_papers.json          # All unique papers, indexed by PMID
│   ├── all_papers.csv           # Flat table, one row per paper
│   ├── dedup_report.md          # What was deduped and why
│   └── retracted_flagged.csv    # Any retractions found
├── themes/
│   ├── theme_01_heterogeneity/
│   │   ├── papers.md            # Annotated markdown with findings
│   │   ├── papers.ris           # RIS file for EndNote import
│   │   ├── papers.csv           # Flat table for this theme
│   │   ├── section_notes.md     # Synthesized findings, ready to inform writing
│   │   └── queries_run.md       # Queries executed, hit counts
│   ├── theme_02_methods/
│   ├── theme_03_applications/
│   ├── theme_04_ai_ml/
│   ├── theme_05_sex/
│   ├── theme_06_never_smoker/
│   ├── theme_07_environment/
│   ├── theme_08_epigenetics/
│   ├── theme_09_immune_biomarkers/
│   ├── theme_10_translational/
│   ├── theme_11_drug_repurposing/
│   └── theme_12_emerging_frontiers/
├── master/
│   ├── master_library.ris       # All themes combined, deduplicated — PRIMARY ENDNOTE IMPORT
│   ├── master_library.csv       # Combined flat table
│   ├── theme_tags.csv           # PMID → list of themes (papers can span multiple)
│   └── high_priority.csv        # Top ~300-500 papers flagged as highest priority
├── cache/                       # API response cache (gitignore this)
├── scripts/                     # Any Python scripts you create
│   ├── search.py
│   ├── fetch.py
│   ├── dedup.py
│   ├── write_ris.py
│   └── synthesize.py
├── search_log/
│   ├── queries_run.md           # All queries executed, with hit counts per API
│   ├── failed_queries.md        # Queries that errored or returned 0
│   └── progress.log             # Running log
├── SUMMARY.md                   # Final summary — write this last
└── README.md                    # Brief orientation
```

---

## 5. Per-paper data schema

Every paper gets these fields. Missing values = empty string, not null.

```python
{
    "pmid": "25079552",
    "doi": "10.1038/nature13385",
    "pmcid": "PMC4231481",
    "title": "Comprehensive molecular profiling of lung adenocarcinoma",
    "abstract": "...",                    # Full abstract text
    "authors_first": "Collisson",          # First author last name
    "authors_last": "Meyerson",            # Last author last name
    "authors_all": "Collisson EA, ...",    # All authors, AMA format
    "journal": "Nature",
    "journal_iso": "Nature",
    "year": 2014,
    "month": 7,
    "day": 9,
    "volume": "511",
    "issue": "7511",
    "pages": "543-50",
    "mesh_terms": ["Adenocarcinoma of Lung", ...],
    "keywords": [...],
    "article_types": ["Journal Article", "Research Support..."],
    "language": "eng",
    "citation_count": 2847,                # From Semantic Scholar if available
    "influential_citations": 412,          # From Semantic Scholar if available
    "tldr": "...",                         # From Semantic Scholar if available
    "source_api": "pubmed",                # pubmed | biorxiv | europepmc
    "is_preprint": false,
    "is_retracted": false,
    "retraction_notice": "",
    "themes": ["theme_01", "theme_03"],    # Can be multiple
    "theme_primary": "theme_01",           # Best single fit
    "relevance_score": 0.87,               # Computed, see Section 7
    "priority_tier": "A",                  # A | B | C — see Section 7
    "queries_matched": ["LUAD molecular", "TCGA lung adenocarcinoma"],
    "notes": ""                            # Any special flags
}
```

---

## 6. The 12 themes — queries and targets

Each theme has a **minimum target**. Hit it or exceed it substantially. These are floors, not ceilings.

### Theme 01 — Lung cancer molecular heterogeneity foundations

**Minimum target: 100 papers**

**Purpose:** Landmark and recent characterization of lung cancer molecular landscapes across LUAD, LUSC, SCLC, mixed histology, and pre-neoplastic lesions.

**Queries (run each on PubMed, store all hits, dedupe):**
```
1. (lung adenocarcinoma[MeSH] OR LUAD) AND (molecular subtype OR multi-omics OR integrative)
2. (lung squamous cell carcinoma OR LUSC) AND (molecular OR genomic) AND subtype
3. "small cell lung cancer" AND (genomic OR molecular subtype)
4. "small cell lung cancer" AND (ASCL1 OR NEUROD1 OR POU2F3 OR YAP1)
5. NSCLC AND (genomic landscape OR mutational landscape)
6. lung adenocarcinoma AND (EGFR OR KRAS OR TP53 OR ALK) AND (co-mutation OR comutation)
7. lung cancer AND tumor heterogeneity AND molecular
8. lung cancer AND driver mutation AND subtype
9. "lung adenocarcinoma in situ" OR "minimally invasive adenocarcinoma"
10. TCGA AND lung AND (genomic OR molecular)
11. lung cancer AND proteogenomic
12. lung cancer AND histologic transformation
```

**Must-include anchor PMIDs (fetch these specifically):**
- `25079552` — TCGA LUAD 2014
- `22960745` — TCGA LUSC 2012
- `26168399` — George SCLC 2015
- `31406302` — Skoulidis co-mutation review 2019
- `32649874` — Gillette CPTAC LUAD 2020
- `32649875` — Chen East Asia proteogenomics 2020
- `32649877` — Xu LUAD proteogenomics 2020
- `38181741` — Liu SCLC proteogenomics 2024
- `30926931` — Rudin SCLC subtype classification 2019
- `33011388` — Gay SCLC subtype therapeutic vulnerabilities 2021

### Theme 02 — Multi-omics integration methods

**Minimum target: 100 papers**

**Purpose:** Methods layer. Pan-cancer methods included since methods transfer to lung.

**Queries:**
```
1. multi-omics integration AND (benchmark OR comparison OR evaluation)
2. "MOVICS" OR "DIABLO" OR "iCluster" OR "MOFA" OR "NEMO"
3. "similarity network fusion" OR "SNF" cancer
4. multi-omics clustering AND consensus
5. integrative omics AND method AND cancer
6. multi-omics AND deep learning AND integration
7. variational autoencoder AND multi-omics
8. graph neural network AND multi-omics AND cancer
9. multi-modal AND deep learning AND cancer
10. multi-omics factor analysis
11. joint NMF AND multi-omics
12. "late integration" OR "early integration" multi-omics cancer
13. canonical correlation analysis AND omics
14. Bayesian AND multi-omics AND cancer
```

**Anchor PMIDs:**
- `32185779` — MOVICS Bioinformatics 2020
- `28369062` — mixOmics DIABLO 2017
- `19759197` — iCluster 2009
- `24464287` — Similarity Network Fusion Nature Methods 2014
- `32393329` — MOFA+ Genome Biology 2020
- `30590492` — NEMO Bioinformatics 2019
- `33524135` — Cantini benchmarking Nature Comms 2021

### Theme 03 — Multi-omics applications in lung cancer

**Minimum target: 100 papers**

**Queries:**
```
1. multi-omics AND lung cancer AND (subtype OR classification OR clustering)
2. proteogenomic AND lung cancer
3. integrative AND (transcriptome OR methylome OR proteome) AND (LUAD OR LUSC OR SCLC)
4. multi-platform AND lung adenocarcinoma
5. multi-omics AND NSCLC AND immunotherapy
6. multi-omics AND lung cancer AND prognosis
7. multi-omics AND lung cancer AND drug response
8. integrative genomics AND lung cancer AND survival
9. multi-omics AND tumor microenvironment AND lung
10. multi-omics AND radiation therapy AND lung
11. proteogenomics AND NSCLC AND driver
12. multi-omics AND early detection AND lung
```

### Theme 04 — AI/ML in lung cancer and oncology

**Minimum target: 150 papers** (largest theme — biggest evidence base)

**Purpose:** Covers 8 subthemes. Evidence for the ML spine. Include transferable pan-oncology ML methods.

**Subthemes and queries:**

*4a. ML for lung cancer molecular subtyping:*
```
1. machine learning AND lung cancer AND (subtype OR classification)
2. deep learning AND NSCLC AND classification
3. unsupervised learning AND lung cancer AND molecular
```

*4b. Deep learning on histopathology:*
```
4. deep learning AND lung cancer AND histopathology
5. convolutional neural network AND NSCLC AND pathology
6. whole slide image AND lung cancer AND deep learning
7. self-supervised learning AND pathology AND cancer
```

*4c. Radiomics and radiogenomics:*
```
8. radiogenomics AND lung cancer
9. radiomics AND NSCLC AND (survival OR response)
10. radiomics AND immunotherapy AND lung
```

*4d. ICI response prediction:*
```
11. artificial intelligence AND immunotherapy response AND (lung OR NSCLC)
12. machine learning AND checkpoint inhibitor AND lung cancer
13. deep learning AND PD-L1 AND lung
```

*4e. Foundation models and LLMs:*
```
14. foundation model AND (pathology OR oncology)
15. large language model AND oncology
16. transformer AND pathology AND cancer
17. vision language model AND pathology
```

*4f. Multi-modal and multi-omics ML:*
```
18. multi-modal AND deep learning AND oncology
19. multi-omics AND machine learning AND cancer
20. fusion model AND cancer AND outcome
```

*4g. Survival and outcome prediction:*
```
21. deep learning AND survival AND lung cancer
22. machine learning AND prognosis AND NSCLC
23. neural network AND survival prediction AND cancer
```

*4h. Reproducibility, bias, validation:*
```
24. external validation AND machine learning AND cancer
25. bias AND machine learning AND clinical AND cancer
26. reproducibility AND AI AND oncology
27. generalizability AND deep learning AND medical imaging
```

**Anchor PMIDs:**
- `30224757` — Coudray NSCLC histopath deep learning Nat Med 2018
- `35944502` — Chen pan-cancer multimodal Cancer Cell 2022
- `39294368` — CHIEF foundation model Nature 2024
- `39030412` — Virchow foundation model Nat Med 2024
- `36108632` — Lipkova multimodal AI Cancer Cell 2022
- `35512792` — Boehm multimodal oncology Nature Reviews Cancer 2022

### Theme 05 — Sex and gender differences in lung cancer

**Minimum target: 75 papers**

**Queries:**
```
1. sex differences AND lung cancer AND (molecular OR outcome)
2. estrogen receptor AND (NSCLC OR lung adenocarcinoma)
3. gender disparity AND immunotherapy AND lung cancer
4. female AND lung adenocarcinoma AND EGFR AND never smoker
5. sex hormone AND lung cancer
6. pregnancy AND lung cancer
7. sex chromosome AND cancer AND lung
8. Y chromosome loss AND lung cancer
9. gender AND survival AND NSCLC
10. women AND lung cancer AND epidemiology
11. sex-specific AND biomarker AND lung cancer
```

**Anchor PMIDs:**
- `29778737` — Conforti sex + ICI meta-analysis Lancet Oncol 2018
- `32350439` — Rubin sex differences cancer Nat Rev Cancer 2020

### Theme 06 — Never-smoker lung cancer

**Minimum target: 75 papers**

**Queries:**
```
1. never smoker AND lung cancer AND (genomic OR molecular)
2. non-smoking lung adenocarcinoma AND (Asian OR East Asian)
3. EGFR mutation AND never smoker AND epidemiology
4. lung cancer etiology AND never smoker
5. ALK fusion AND never smoker
6. ROS1 AND never smoker AND lung
7. lung cancer AND light smoker AND molecular
8. tumor microenvironment AND never smoker AND lung
9. immunotherapy response AND never smoker AND lung
10. lung cancer AND mutational signature AND smoking
11. second-hand smoke AND lung cancer
12. never-smoker AND brain metastasis AND lung
```

**Anchor PMIDs:**
- `17667967` — Sun never smoker foundational Nat Rev Cancer 2007
- `34493867` — Zhang never smoker genomic classification Nat Genet 2021

### Theme 07 — Environmental exposures and lung cancer

**Minimum target: 75 papers**

**Queries:**
```
1. PM2.5 AND lung cancer AND (mutation OR epigenetic OR EGFR)
2. radon AND lung cancer AND (molecular OR risk)
3. air pollution AND lung cancer AND incidence
4. occupational exposure AND lung cancer
5. asbestos AND lung cancer AND molecular
6. indoor air pollution AND lung cancer
7. cooking fume AND lung cancer
8. secondhand smoke AND lung cancer AND molecular
9. diesel exhaust AND lung cancer
10. PFAS AND cancer AND lung
11. exposome AND lung cancer
12. silica AND lung cancer
13. pollution AND EGFR mutation AND lung
14. wildfire smoke AND cancer
```

**Anchor PMIDs:**
- `37046093` — Hill PM2.5 EGFR lung adenocarcinoma Nature 2023
- `23900102` — Raaschou-Nielsen air pollution Lancet Oncol 2013

### Theme 08 — Epigenetics in lung cancer

**Minimum target: 75 papers**

**Queries:**
```
1. DNA methylation AND lung cancer AND (subtype OR survival OR prognosis)
2. epigenetic AND lung adenocarcinoma AND molecular
3. miRNA AND lung cancer AND (prognosis OR therapy)
4. histone modification AND lung cancer
5. chromatin accessibility AND lung cancer
6. ATAC-seq AND lung cancer
7. lncRNA AND lung cancer AND prognosis
8. methylation signature AND NSCLC AND biomarker
9. epigenome-wide association AND lung cancer
10. circRNA AND lung cancer
11. AHRR hypomethylation AND lung
12. cfDNA methylation AND lung cancer
13. enhancer AND lung cancer
```

### Theme 09 — Immune biomarkers and immunotherapy response

**Minimum target: 75 papers**

**Queries:**
```
1. PD-L1 AND NSCLC AND (limitation OR heterogeneity OR resistance)
2. tumor mutational burden AND immunotherapy AND lung cancer
3. "Immunophenoscore" OR "Tempus IPS"
4. immune subtype AND pan-cancer
5. tumor microenvironment AND immunotherapy AND NSCLC
6. HLA AND immunotherapy response
7. gene expression signature AND immunotherapy AND lung
8. neoantigen AND lung cancer AND immunotherapy
9. MSI AND lung cancer AND immunotherapy
10. T cell inflamed AND lung cancer
11. Thorsson immune landscape cancer
12. Bagaev conserved microenvironment
13. Charoentong immunogenomic
14. STK11 AND KEAP1 AND immunotherapy AND NSCLC
15. gut microbiome AND immunotherapy AND response
```

**Anchor PMIDs:**
- `29628290` — Thorsson immune landscape Immunity 2018
- `28052254` — Charoentong Immunophenoscore Cell Reports 2017
- `34019806` — Bagaev conserved microenvironment Cancer Cell 2021
- `25765070` — Rizvi mutational landscape PD-1 Science 2015
- `33479125` — Litchfield pan-cancer ICI meta Cell 2021

### Theme 10 — Targeted therapy access, translational bottleneck, real-world outcomes

**Minimum target: 75 papers**

**Queries:**
```
1. precision oncology AND real-world AND lung cancer
2. targeted therapy AND utilization AND NSCLC
3. biomarker testing AND disparity AND lung cancer
4. clinical trial representation AND (women OR minority) AND cancer
5. health disparity AND lung cancer
6. molecular tumor board AND outcome
7. real-world evidence AND NSCLC AND immunotherapy
8. implementation science AND precision oncology
9. access AND targeted therapy AND oncology
10. guideline adherence AND NSCLC
11. ancestry AND clinical trial AND cancer
12. socioeconomic AND lung cancer AND outcome
13. Flatiron AND NSCLC
14. MYLUNG consortium
15. EGFR TKI AND treatment landscape
16. KRAS G12C AND sotorasib OR adagrasib
```

### Theme 11 — Drug repurposing in oncology

**Minimum target: 75 papers**

**Queries:**
```
1. drug repurposing AND cancer AND (computational OR multi-omics)
2. drug-gene interaction AND cancer AND prediction
3. "dimethyl fumarate" AND KEAP1 AND cancer
4. connectivity map AND cancer
5. pharmacogenomic AND lung cancer
6. GDSC AND drug response AND cancer
7. CCLE AND drug AND lung
8. drug sensitivity AND lung cancer AND biomarker
9. synthetic lethality AND lung cancer
10. network pharmacology AND cancer
11. DGIdb drug gene interaction
12. repositioning AND oncology
13. PRISM drug screen
14. drug combination AND lung cancer AND computational
```

### Theme 12 — Single-cell, spatial, metabolomic, liquid biopsy frontiers

**Minimum target: 75 papers**

**Subthemes (12a–12e):**

*12a. Single-cell:*
```
1. single-cell RNA AND lung cancer AND heterogeneity
2. single-cell AND NSCLC AND tumor microenvironment
3. scRNA-seq AND lung adenocarcinoma
```

*12b. Spatial omics:*
```
4. spatial transcriptomics AND lung cancer
5. spatial proteomics AND lung cancer
6. imaging mass cytometry AND lung cancer
7. Visium AND lung cancer
8. CODEX AND lung cancer
```

*12c. Metabolomics:*
```
9. metabolomics AND lung cancer AND biomarker
10. lipidomics AND lung cancer
11. tryptophan metabolism AND lung cancer
```

*12d. Liquid biopsy:*
```
12. liquid biopsy AND lung cancer AND (methylation OR ctDNA)
13. cfDNA AND lung cancer AND early detection
14. minimal residual disease AND lung cancer
15. CAPP-Seq AND lung
```

*12e. Microbiome:*
```
16. microbiome AND lung cancer
17. gut microbiome AND immunotherapy AND lung
```

**Anchor PMIDs:**
- `29988129` — Lambrechts stromal phenotype Nat Med 2018
- `32015526` — Chabon CAPP-Seq Nature 2020

---

## 7. Relevance scoring and priority tiers

For each paper, compute a relevance score (0.0 to 1.0) per theme it fits. Use this heuristic:

```python
def score_paper(paper, theme_keywords):
    score = 0.0

    # Anchor PMID bonus (paper is in must-include list)
    if paper['pmid'] in ANCHOR_PMIDS[theme]:
        return 1.0

    # Title keyword density
    title = paper['title'].lower()
    title_hits = sum(1 for kw in theme_keywords if kw in title)
    score += min(0.3, title_hits * 0.1)

    # Abstract keyword density
    abstract = paper['abstract'].lower()
    abstract_hits = sum(1 for kw in theme_keywords if kw in abstract)
    score += min(0.2, abstract_hits * 0.02)

    # Journal quality (use a tiered list)
    if paper['journal'] in TIER1_JOURNALS:
        score += 0.25
    elif paper['journal'] in TIER2_JOURNALS:
        score += 0.15
    elif paper['journal'] in TIER3_JOURNALS:
        score += 0.05

    # Citation count (log-scaled)
    import math
    cites = paper.get('citation_count', 0)
    if cites > 0:
        score += min(0.2, math.log10(cites + 1) * 0.05)

    # Recency bonus for fast-moving areas
    if paper['year'] >= 2023:
        score += 0.05

    # Review/meta-analysis modest bonus
    if 'Review' in paper['article_types'] or 'Meta-Analysis' in paper['article_types']:
        score += 0.05

    return min(1.0, score)
```

**Tier journal lists:**
- **Tier 1:** Nature, Cell, Science, Nature Medicine, Cancer Cell, Nature Genetics, Nature Cancer, Nature Methods, Nature Communications, Cell Reports, Immunity, NEJM, Lancet, JAMA, Lancet Oncology, JCO, Cancer Cell, Nature Reviews Cancer, Nature Reviews Clinical Oncology, Nature Reviews Drug Discovery
- **Tier 2:** Cancer Research, Clinical Cancer Research, Genome Medicine, Genome Biology, Bioinformatics, Briefings in Bioinformatics, npj Precision Oncology, Annals of Oncology, JTO, Molecular Cancer, NAR, Cell Reports Medicine
- **Tier 3:** Frontiers in Oncology, Frontiers in Immunology, Scientific Reports, PLoS ONE, Cancers (MDPI), Int J Mol Sci, BMC Cancer, Journal of Translational Medicine, Translational Lung Cancer Research, Lung Cancer

**Priority tiers for the final library:**
- **Tier A (high priority):** Score ≥ 0.7 OR is an anchor PMID. Target ~300–500 total across all themes.
- **Tier B (supporting):** Score 0.4–0.7. The bulk of the final library.
- **Tier C (optional):** Score < 0.4. Kept in the library but not flagged for writing phase.

---

## 8. Deduplication

Papers cross themes. Dedupe aggressively:

1. **Primary key:** PMID
2. **Secondary check:** DOI (case-insensitive, strip https://)
3. **Tertiary check:** Title + first author + year (fuzzy match with Levenshtein distance ≤ 3 on title)
4. When duplicates found, **merge** — keep the union of themes, queries matched, and notes

Write a `dedup_report.md` listing:
- Total raw hits: N
- Unique by PMID: N
- Additional dedupe via DOI: N
- Additional dedupe via title: N
- Final unique papers: N
- Papers spanning 3+ themes: N (list them — these are the "bridge" papers)

---

## 9. Quality filters

### 9.1 Exclude:
- Papers with no abstract (likely non-research)
- Retracted papers (fetch retraction info via PubMed — field `<PublicationType>Retracted Publication</PublicationType>`) — flag in `retracted_flagged.csv` but do not include in main library
- Clear predatory journal output:

**Known predatory/low-quality publishers to exclude or flag:**
- OMICS International
- Bentham Open (not Bentham Science — just the Open imprint)
- Scientific Research Publishing (SCIRP)
- Hindawi (flag but don't auto-exclude — some legitimate journals there)
- Check against Beall's list and DOAJ — if uncertain, flag for manual review

### 9.2 Flag but include:
- Preprints (mark `is_preprint: true`)
- Non-English translations of papers (rare in PubMed but possible)
- Papers with only abstracts available (conference abstracts)

### 9.3 Note specially:
- Papers by the project's own group (Vignesh Ravichandran, Suchismita Ray, Rutgers) — flag with `is_author_affiliated: true`
- Papers from institutional cohorts outside TCGA — noteworthy for the review

---

## 10. Output formats

### 10.1 RIS (EndNote import) — the primary deliverable

```
TY  - JOUR
AU  - Collisson, Eric A
AU  - Campbell, Joshua D
AU  - Brooks, Angela N
PY  - 2014
TI  - Comprehensive molecular profiling of lung adenocarcinoma
JO  - Nature
JF  - Nature
VL  - 511
IS  - 7511
SP  - 543
EP  - 550
DO  - 10.1038/nature13385
PM  - 25079552
AB  - Adenocarcinoma of the lung is the leading cause of cancer death worldwide...
KW  - Lung adenocarcinoma
KW  - TCGA
KW  - Multi-omics
N1  - Theme: theme_01_heterogeneity; theme_03_applications | Priority: A | Score: 1.0
ER  -
```

Use `rispy` library for writing. Do not hand-roll the format.

### 10.2 CSV — for Excel/review

Flat table with all schema fields from Section 5. One row per paper. UTF-8, comma-separated, quoted strings.

### 10.3 Markdown annotated — for human review per theme

```markdown
# Theme 01 — Lung cancer molecular heterogeneity foundations

**Total papers: 112**
**Tier A (high priority): 18**
**Tier B (supporting): 71**
**Tier C (optional): 23**

---

## Tier A — Must cite

### 1. Collisson et al. 2014 — TCGA LUAD landmark

**PMID:** 25079552 | **DOI:** [10.1038/nature13385](https://doi.org/10.1038/nature13385) | **Journal:** *Nature* | **Score:** 1.00

**Key finding (paraphrased):** Molecular profiling of 230 resected LUAD tumors integrating mRNA, miRNA, methylation, protein, and somatic mutation data. Established subtypes and key driver oncogenes for the field.

**Relevance:** Foundational anchor. Establishes the baseline for every subsequent multi-omics LUAD study.

**Also fits:** theme_03_applications

---

### 2. [next paper]
...
```

### 10.4 section_notes.md — synthesis for writing

For each theme, after the paper list, write a synthesized summary (500–1000 words) paraphrasing what the literature says. This is the raw material for manuscript writing.

Structure:
```markdown
# Theme 01 — Synthesis

## What the literature establishes
[paraphrased summary of main findings across papers]

## Where consensus exists
[areas of agreement]

## Where the field disagrees or is uncertain
[controversies, contradictions]

## Gaps and open questions
[what's missing]

## Candidate citations for the review
[ranked list of 15–30 PMIDs most likely to be cited]

## Notes for the writing phase
[any flags — bridge papers, controversial claims, must-discuss]
```

**COPYRIGHT CRITICAL:** Paraphrase everything. No direct quotes from abstracts longer than 15 words. No more than one quote per source. This applies to ALL synthesis text.

---

## 11. Copyright and attribution requirements

This is non-negotiable.

- **Never reproduce abstract text verbatim.** Always paraphrase.
- **Maximum one direct quote per source, under 15 words.** Prefer zero quotes.
- **Every paper cited in markdown must include its DOI as a link.**
- **Verify every PMID** Do not hallucinate
- Format: `[10.1038/nature13385](https://doi.org/10.1038/nature13385)`
- Attribution: The synthesis notes should cite findings to specific PMIDs, not present them as Claude's original insight.
- When writing synthesis text, treat findings as "Author et al. [PMID] found that..." rather than quoting the abstract.

---

## 12. Workflow and checkpoints

### Phase 1: Setup (≤30 min)
1. Create directory structure
2. Install dependencies
3. Verify NCBI API key works (or proceed without, slower)
4. Read anchor PMIDs and fetch their metadata first — these are the "must-haves"

### Phase 2: Execute searches (6–10 hours)
For each theme, in order 1 → 12:
1. Run all queries for the theme, collect PMIDs
2. Dedupe within theme
3. Bulk-fetch metadata via `efetch` (batches of 200 PMIDs)
4. Enrich with Semantic Scholar citation counts (batches of 100)
5. Check bioRxiv/medRxiv for recent preprints with same query terms
6. Check Europe PMC for any PubMed misses on 2–3 broadest queries
7. Score all papers for relevance
8. Assign priority tier
9. Write theme-level outputs (markdown, CSV, RIS)
10. Write synthesis notes (`section_notes.md`) — **this is the expensive step**
11. Commit to git
12. Log progress

### Phase 3: Deduplication and master library (1–2 hours)
1. Combine all theme CSVs into `all_papers.csv`
2. Dedupe across themes by PMID → DOI → title fuzzy
3. Write `dedup_report.md`
4. Produce `master_library.ris` — THE primary deliverable for EndNote
5. Produce `theme_tags.csv` — PMID to themes mapping
6. Produce `high_priority.csv` — all Tier A papers across themes

### Phase 4: Summary and handoff (≤1 hour)
1. Write `SUMMARY.md` with:
   - Total papers collected (raw, deduped, by tier)
   - Per-theme counts vs. targets
   - Themes that hit the target, themes that did not (flag for manual review)
   - Bridge papers (appearing in 3+ themes)
   - Known gaps — queries that returned little, suggestive of under-covered areas
   - Top 20 papers overall by score (the likely workhorses of the manuscript)
   - Notes for manuscript writing phase — including the Claude Code session
2. Write `README.md` with brief orientation
3. Final git commit

---

## 13. Checkpointing and recovery

- Commit to git after each theme completes. Commit message: `Theme {NN}: {name} — {count} papers collected`
- On API errors, retry 3x with exponential backoff, then skip and log to `failed_queries.md`
- If runtime approaches 14 hours total, prioritize finishing deduplication and `SUMMARY.md` over perfecting synthesis notes for later themes
- All API responses are cached under `lit_review/cache/` — if the run is interrupted, a re-run should be much faster

---

## 14. What NOT to do

- **Do not stop to ask for confirmation** on paper inclusion decisions. Use the tier system — borderline papers go to Tier C.
- **Do not skimp on paper counts.** If a theme looks light, add more queries — expand synonyms, try different angles, go to Europe PMC.
- **Do not write the manuscript.** Your job is the evidence base and synthesis notes. Writing is a separate phase.
- **Do not trust a single source.** Cross-check PubMed vs. Europe PMC for broad queries to catch misses.
- **Do not quote abstracts verbatim.** Paraphrase everything.
- **Do not delete the cache directory** at the end — keeping it means a re-run is fast and cheap.
- **Do not exclude preprints.** Flag them, include them.
- **Do not auto-reject MDPI or Hindawi journals.** Flag them for manual review — some (like *Cancers*, *Int J Mol Sci*) publish legitimate work.

---

## 15. Success criteria

You are done when:
- [ ] All 12 themes have hit their minimum target paper count
- [ ] All anchor PMIDs are present in the library
- [ ] `master_library.ris` imports cleanly into EndNote (test it if possible)
- [ ] `SUMMARY.md` exists and is comprehensive
- [ ] All section_notes.md files are written
- [ ] Git log shows a clean commit history with one commit per theme plus setup/summary
- [ ] Total unique papers: ≥ 900 (target ~1200–1500 before dedup)
- [ ] Tier A papers: ~300–500
- [ ] Retractions identified and moved to `retracted_flagged.csv`
- [ ] No copyright violations (check `section_notes.md` files for any verbatim abstract text)

---

## 16. After you finish

Leave a message at the end of `SUMMARY.md` titled "Notes for the manuscript writing session" covering:
- Which themes have the strongest evidence
- Which themes feel under-covered and may need targeted follow-up searches
- The top 20 papers you would cite first if given only 20 slots
- Any surprising findings that should reshape the review's argument
- Anything you found that contradicts the current outline (see `Outline_for_Review_Paper.docx` if present)

---

## 17. Environment variables and credentials

Set these before running if not already set:

```bash
export NCBI_API_KEY="your_ncbi_api_key"            # Optional but recommended
export NCBI_EMAIL="vignesh@rutgers.edu"            # Required by NCBI
export SEMANTIC_SCHOLAR_API_KEY="your_ss_api_key"  # Optional
```

If NCBI email is not set, use `vignesh.ravichandran@rutgers.edu` as a placeholder — NCBI requires an email for API access.

---

## 18. Final notes

This is a real deliverable for a real doctoral paper. Quality of output directly affects publication success. Be thorough. When in doubt, collect more rather than less. The synthesis notes are the bridge to manuscript writing — they should be as good as you can make them.

If you discover the scope needs adjustment mid-run, note it in `progress.log` but complete the run as specified. Scope changes happen between runs, not during.

Good luck. Ship a great evidence base.

---

*End of spec. Total expected runtime: 8–14 hours. Expected output size: 900–1500 unique papers, ~300–500 Tier A, ~6000–12000 lines of synthesis notes across 12 themes.*
