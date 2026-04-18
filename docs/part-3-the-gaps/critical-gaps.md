# What No One Has Done Yet

> *The gaps identified below are not merely absences in the literature -- they are the strongest original contributions this review can make to the field. A review that only summarizes existing knowledge is a textbook. A review that maps the uncharted territory is a roadmap.*

---

## The Two Highest-Priority Gaps

These two findings emerged independently across multiple themes and represent the review's most powerful original contribution.

### 1. Sex-Stratified Multi-Omics Analyses Are Nearly Absent

Across themes 01 (Molecular Heterogeneity), 03 (Multi-Omics Applications), 04 (AI/ML), and 05 (Sex/Gender), we found that virtually no multi-omics study has systematically stratified results by biological sex. This is not a niche concern -- it is a blind spot affecting the validity of subtype classifications, drug response predictions, and biomarker panels that are implicitly trained on sex-mixed cohorts.

The evidence for sex-linked biological differences in lung cancer is strong: women have higher EGFR mutation rates, estrogen receptor signaling modulates tumor biology [PMID: [11905727](https://pubmed.ncbi.nlm.nih.gov/11905727/); PMID: [38607364](https://pubmed.ncbi.nlm.nih.gov/38607364/)], and immunotherapy outcomes may differ by sex [PMID: [29778737](https://pubmed.ncbi.nlm.nih.gov/29778737/)]. Yet the major proteogenomic studies (CPTAC, East Asian cohorts), the AI/ML models for subtype classification, and the multi-omics integration benchmarks all report sex-pooled results. The consequence is that molecular subtypes, prognostic signatures, and drug response models may perform differently in men and women -- but we have no way of knowing, because the stratified analyses have not been done.

**What the manuscript should argue:** Sex-stratified multi-omics analysis should be a standard requirement, not an optional subgroup analysis. The pharmacogenomic databases (GDSC, CCLE) should report sex-stratified drug response data. AI/ML models should report performance metrics separately by sex.

### 2. No Multi-Omics Study Has Focused on NSCLC in Never-Smokers

Despite never-smoker lung cancer accounting for 10-25% of all lung cancers globally -- and rising in incidence -- the intersection of multi-omics integration (Theme 03) with never-smoker biology (Theme 06) is an empty set. Every existing multi-omics NSCLC study pools smokers and never-smokers together, diluting the signal from a population with fundamentally different driver mutations, mutational signatures, and tumor microenvironment characteristics.

Zhang et al. [PMID: [34493867](https://pubmed.ncbi.nlm.nih.gov/34493867/)] demonstrated that never-smoker LUAD comprises three genomically distinct subtypes (piano, mezzo, forte). Yet none of the CPTAC proteogenomic studies, none of the multi-omics subtyping studies, and none of the spatial omics studies have been designed specifically around these subtypes. The proteogenomic characterization of East Asian never-smokers by Chen et al. [PMID: [32649875](https://pubmed.ncbi.nlm.nih.gov/32649875/)] comes closest but was not a dedicated multi-omics integration study.

**What the manuscript should argue:** A dedicated, multi-ethnic, multi-omics study of never-smoker NSCLC -- integrating genomics, transcriptomics, proteomics, epigenomics, and spatial profiling -- is among the most impactful studies that could be conducted in lung cancer research today.

---

## High-Priority Gaps

| Gap | Where it emerged | Why it matters for the field |
|:---|:---:|:---|
| **Exposome-to-molecular-subtype mapping is absent** | Themes 06, 07 | We know PM2.5 causes lung cancer. We know never-smoker LUAD has three subtypes. No one has connected which exposures produce which subtypes. The Martinez-Ruiz PM2.5-EGFR promotion model [PMID: [37046093](https://pubmed.ncbi.nlm.nih.gov/37046093/)] is the only molecular bridge between environmental exposure and subtype-specific biology. |
| **AI fairness/bias assessment rarely performed in oncology** | Theme 04 | Foundation models trained predominantly on Western cohorts are being deployed globally. Sex-stratified AI model evaluation is virtually absent. AI tools for never-smoker NSCLC do not exist. The generalizability crisis in medical AI is well-documented but unresolved in oncology specifically. |
| **Few ML models validated on multi-ethnic, multi-institutional cohorts** | Themes 04, 10 | External validation studies consistently show performance degradation. Most published AI models have been developed and validated within single institutions or single ancestry populations. |
| **Composite immune biomarker panels not standardized** | Theme 09 | Despite a decade of research showing that PD-L1, TMB, gene expression signatures, and microbiome composition each contribute partial predictive information, no composite panel has reached guideline status for clinical use. |
| **Drug repurposing predictions rarely translate to clinical trials** | Theme 11 | Computational drug repurposing generates many candidates. Very few reach clinical validation. The translation bottleneck is not computational -- it is experimental and regulatory. |

---

## Moderate-Priority Gaps

| Gap | Where it emerged | Why it matters |
|:---|:---:|:---|
| **Cost-effectiveness of multi-omics precision oncology not established** | Theme 10 | Without health-economic evidence, payers will not cover multi-omics testing at scale. The clinical utility argument is necessary but not sufficient. |
| **Single-cell epigenomics in lung cancer is limited** | Themes 08, 12 | Bulk epigenomic studies cannot resolve cell-type-specific regulatory mechanisms. The intersection of single-cell resolution with epigenomic profiling in lung cancer is nearly empty. |
| **Spatial omics in never-smoker lung cancer is absent** | Themes 06, 12 | The spatial architecture of the tumor microenvironment in the most common form of never-smoker LUAD has never been mapped. |
| **Pre-neoplastic lesion molecular evolution poorly understood** | Theme 01 | We classify lung cancer subtypes at diagnosis, but the molecular events that determine subtype commitment during premalignant evolution are largely unknown. |
| **Longitudinal molecular profiling through treatment is sparse** | Themes 01, 08, 12 | Most molecular studies are cross-sectional snapshots. Understanding treatment-driven evolution requires serial sampling and multi-omics profiling. |
| **miRNA/lncRNA prognostic signatures have reproducibility concerns** | Theme 08 | The 76 retractions in our epigenetics collection are quantifiable evidence of a reproducibility crisis. Many published non-coding RNA biomarker associations may not hold up under independent validation. |
| **Pregnancy-associated lung cancer molecularly understudied** | Theme 05 | An important and understudied clinical scenario where hormonal, immunological, and molecular factors intersect. |

---

## The Retraction Signal as a Gap

The 208 retracted papers identified across this collection are not just a quality control statistic -- they point to specific areas of the literature where evidence quality should be treated with caution.

| Theme | Retracted | Interpretation |
|:---|---:|:---|
| 08 Epigenetics | **76** | Crisis-level. Concentrated in miRNA/lncRNA prognostic signatures. The field needs pre-registered validation studies. |
| 01 Molecular Heterogeneity | 50 | Elevated but spread across subtypes -- no single hotspot. |
| 04 AI/ML | 30 | Moderate. Some in radiomics, some in prognostic modeling. |
| 11 Drug Repurposing | 28 | Moderate. Network pharmacology area flagged. |
| 09 Immune Biomarkers | 14 | Expected background rate for a large corpus. |
| All others | 10 total | Clean. |

**What the manuscript should argue:** The concentration of retractions in non-coding RNA biomarker studies should be explicitly discussed as evidence for the need for rigorous, pre-registered validation frameworks. The review should recommend specific reproducibility standards (independent validation cohorts, pre-registered analysis plans, code/data sharing) for future biomarker studies.
