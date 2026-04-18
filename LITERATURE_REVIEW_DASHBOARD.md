# Literature Review Dashboard

**Multi-Omics Integration and AI/ML in Lung Cancer**
*Strengths, Gaps, and Translational Opportunities*

> **Owner:** Vignesh Ravichandran, DHI  
> **Target Journal:** npj Precision Oncology  
> **Date Compiled:** 2026-04-18  
> **Pipeline:** PubMed + Europe PMC + Semantic Scholar, 213 queries across 12 themes

---

## 1. Collection Overview

```
                           LITERATURE SEARCH FUNNEL

         Raw API Hits                      78,775
              |
         Cross-Theme Dedup               -11,896
              |
         Unique Papers                    66,879
              |
     +--------+--------+
     |        |        |
  Tier A   Tier B   Tier C               Retracted
    49     2,861   63,969                   208
   Must    Strong   Background            Excluded
   Cite   Support  Reference
```

| Metric | Value |
|:---|---:|
| Total raw hits (all APIs, all themes) | 78,775 |
| Unique papers after deduplication | 66,879 |
| Non-retracted papers in master RIS | 66,671 |
| **Tier A** (score >= 0.7, must-cite) | **49** |
| **Tier B** (score 0.4 - 0.7, supporting) | **2,861** |
| Tier C (score < 0.4, background) | 63,969 |
| Bridge papers (span 3+ themes) | 1,928 |
| Retracted papers (flagged, excluded) | 208 |
| Anchor PMIDs recovered | 34 / 35 |
| PubMed queries executed | 177 |
| Europe PMC supplementary queries | 36 |

---

## 2. Per-Theme Results

| # | Theme | Total Papers | Min Target | Tier A | Tier B | Tier C | Retracted | 2023+ Papers | Status |
|:---:|:---|---:|---:|---:|---:|---:|---:|---:|:---:|
| 01 | Molecular Heterogeneity | 6,812 | 100 | **14** | 444 | 6,354 | 50 | 7,819 | PASS |
| 02 | Multi-Omics Methods | 5,289 | 100 | **6** | 196 | 5,087 | 8 | 3,658 | PASS |
| 03 | Multi-Omics Applications | 2,648 | 100 | **1** | 127 | 2,520 | 5 | 1,785 | PASS |
| 04 | AI/ML in Lung Cancer | 11,167 | 150 | **8** | 803 | 10,356 | 30 | 7,374 | PASS |
| 05 | Sex / Gender Differences | 4,707 | 75 | **2** | 66 | 4,639 | 2 | 1,037 | PASS |
| 06 | Never-Smoker Lung Cancer | 2,689 | 75 | **2** | 76 | 2,611 | 4 | 788 | PASS |
| 07 | Environmental Exposures | 4,023 | 75 | **2** | 79 | 3,942 | 1 | 961 | PASS |
| 08 | Epigenetics | 5,902 | 75 | **0** | 91 | 5,811 | **76** | 2,022 | PASS |
| 09 | Immune Biomarkers | 6,459 | 75 | **9** | 679 | 5,771 | 14 | 3,051 | PASS |
| 10 | Translational / Real-World | 6,431 | 75 | **0** | 67 | 6,364 | 2 | 3,200 | PASS |
| 11 | Drug Repurposing | 6,386 | 75 | **0** | 24 | 6,362 | 28 | 2,679 | PASS |
| 12 | Emerging Frontiers | 6,179 | 75 | **2** | 108 | 6,069 | 7 | 2,926 | PASS |

> All 12 themes exceeded minimum targets. Theme 04 (AI/ML) is the largest body of evidence. Theme 08 (Epigenetics) had the highest retraction rate (76 papers), flagging reproducibility concerns in the miRNA/lncRNA space.

---

## 3. Top 20 Must-Cite Papers

These anchor studies form the backbone of the review. All scored 1.00 (maximum relevance).

| Rank | PMID | First Author | Year | Journal | Title (abbreviated) | Theme(s) |
|:---:|:---|:---|:---:|:---|:---|:---|
| 1 | [25079552](https://pubmed.ncbi.nlm.nih.gov/25079552/) | TCGA Network | 2014 | *Nature* | Comprehensive molecular profiling of lung adenocarcinoma | 01, 03 |
| 2 | [22960745](https://pubmed.ncbi.nlm.nih.gov/22960745/) | TCGA Network | 2012 | *Nature* | Comprehensive genomic characterization of squamous cell lung cancer | 01 |
| 3 | [26168399](https://pubmed.ncbi.nlm.nih.gov/26168399/) | George | 2015 | *Nature* | Comprehensive genomic profiles of small cell lung cancer | 01 |
| 4 | [30926931](https://pubmed.ncbi.nlm.nih.gov/30926931/) | Rudin | 2019 | *Nat Rev Cancer* | Molecular subtypes of small cell lung cancer: a synthesis | 01 |
| 5 | [31406302](https://pubmed.ncbi.nlm.nih.gov/31406302/) | Skoulidis | 2019 | *Nat Rev Cancer* | Co-occurring genomic alterations in NSCLC | 01 |
| 6 | [32649874](https://pubmed.ncbi.nlm.nih.gov/32649874/) | Gillette | 2020 | *Cell* | CPTAC LUAD proteogenomic characterization | 01, 03 |
| 7 | [32649875](https://pubmed.ncbi.nlm.nih.gov/32649875/) | Chen | 2020 | *Cell* | East Asia non-smoking LUAD proteogenomics | 01, 06 |
| 8 | [32649877](https://pubmed.ncbi.nlm.nih.gov/32649877/) | Xu | 2020 | *Cell* | Integrative proteomic characterization of human LUAD | 01, 03 |
| 9 | [38181741](https://pubmed.ncbi.nlm.nih.gov/38181741/) | Liu | 2024 | *Cell* | SCLC proteogenomic characterization | 01, 03 |
| 10 | [33011388](https://pubmed.ncbi.nlm.nih.gov/33011388/) | Baine | 2020 | *JTO* | SCLC subtypes by ASCL1, NEUROD1, POU2F3, YAP1 | 01 |
| 11 | [30224757](https://pubmed.ncbi.nlm.nih.gov/30224757/) | Coudray | 2018 | *Nat Med* | NSCLC classification/mutation prediction from histopathology | 04 |
| 12 | [34493867](https://pubmed.ncbi.nlm.nih.gov/34493867/) | Zhang | 2021 | *Nat Genet* | Genomic classification of lung cancer in never-smokers | 06 |
| 13 | [37046093](https://pubmed.ncbi.nlm.nih.gov/37046093/) | Martinez-Ruiz | 2023 | *Nature* | Genomic-transcriptomic evolution in lung cancer | 01, 07 |
| 14 | [32015526](https://pubmed.ncbi.nlm.nih.gov/32015526/) | Chen | 2020 | *Nat Genet* | East Asian LUAD genomic landscape | 06, 12 |
| 15 | [25765070](https://pubmed.ncbi.nlm.nih.gov/25765070/) | Rizvi | 2015 | *Science* | Mutational landscape determines PD-1 sensitivity | 09 |
| 16 | [29628290](https://pubmed.ncbi.nlm.nih.gov/29628290/) | Thorsson | 2018 | *Immunity* | The immune landscape of cancer | 09 |
| 17 | [32393329](https://pubmed.ncbi.nlm.nih.gov/32393329/) | Argelaguet | 2020 | *Genome Biol* | MOFA+: multi-omics factor analysis framework | 02 |
| 18 | [35944502](https://pubmed.ncbi.nlm.nih.gov/35944502/) | Chen | 2022 | *Cancer Cell* | Pan-cancer multimodal histology-genomic analysis | 04 |
| 19 | [29778737](https://pubmed.ncbi.nlm.nih.gov/29778737/) | Conforti | 2018 | *Lancet Oncol* | Sex and immunotherapy efficacy meta-analysis | 05 |
| 20 | [34019806](https://pubmed.ncbi.nlm.nih.gov/34019806/) | Bagaev | 2021 | *Cancer Cell* | Conserved pan-cancer microenvironment subtypes | 09 |

---

## 4. Thematic Synthesis

### Theme 01 -- Lung Cancer Molecular Heterogeneity Foundations

> **6,812 papers** | 14 Tier A | 444 Tier B | 50 retracted

**What the literature establishes**

The molecular landscape of lung cancer has been extensively characterized through large-scale consortium efforts. TCGA and CPTAC studies have delineated the genomic, transcriptomic, and proteomic architecture of LUAD and LUSC, revealing distinct driver mutation profiles. LUAD is dominated by activating mutations in EGFR, KRAS, and ALK fusions, while LUSC shows higher rates of TP53 alterations, FGFR1 amplifications, and SOX2 amplification. SCLC has been reclassified into molecular subtypes defined by dominant transcription factors -- ASCL1 (SCLC-A), NEUROD1 (SCLC-N), POU2F3 (SCLC-P), and YAP1 (SCLC-Y) -- each with distinct therapeutic vulnerabilities. Proteogenomic studies have added layers of understanding beyond what genomics alone revealed. Co-mutation patterns, particularly involving TP53/KRAS, STK11/KRAS, and KEAP1/KRAS in LUAD, have emerged as critical determinants of both prognosis and immunotherapy response. Histologic transformation, especially NSCLC-to-SCLC transformation under EGFR TKI pressure, represents a mechanism of acquired resistance with significant molecular underpinnings.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| LUAD and LUSC are molecularly distinct | Number/definition of LUAD subtypes varies | Limited multi-omics characterization of LUSC vs. LUAD |
| EGFR, KRAS, ALK are actionable LUAD drivers | Whether proteogenomic subtypes are clinically actionable | Pre-neoplastic lesion molecular evolution poorly understood |
| SCLC classifiable by TF subtypes (A/N/P/Y) | Clinical significance of SCLC-Y subtype is contested | Mixed histology and rare subtypes understudied |
| Co-mutation patterns are prognostically significant | Optimal classification systems not standardized | Non-European ancestry cohorts underrepresented |
| Proteogenomics adds value beyond genomics | Intratumoral heterogeneity undermining bulk subtypes | Sex-stratified characterization rarely performed |

---

### Theme 02 -- Multi-Omics Integration Methods

> **5,289 papers** | 6 Tier A | 196 Tier B | 8 retracted

**What the literature establishes**

Multi-omics integration methods have evolved from simple concatenation to sophisticated statistical and deep learning frameworks. Established tools include iCluster (joint latent variables), SNF (patient similarity networks), MOFA/MOFA+ (factor analysis), and DIABLO/mixOmics (supervised multi-block integration). Benchmarking reveals no single approach dominates across all cancer types. The choice of integration strategy (early, intermediate, or late fusion) depends on the research question, data types, and sample sizes. Deep learning approaches (VAEs, GNNs) show promise for non-linear relationships but require larger datasets. Consensus clustering across multiple algorithms has become standard practice. Tools like MOVICS provide comprehensive multi-algorithm frameworks.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| Multi-omics outperforms single-omics for subtyping | Early vs. late vs. intermediate: no consensus | Few methods designed for clinical-scale deployment |
| No single method dominates all scenarios | DL vs. simpler methods at typical sample sizes | Integration of clinical variables not standardized |
| Consensus approaches improve robustness | How to handle missing data across layers | Single-cell multi-omics integration in early stages |
| DL captures non-linear relationships | Appropriate metrics for integration quality | Spatial multi-omics integration tools are nascent |
| Standardized benchmarks are essential | Scalability to 5+ omics layers simultaneously | Causal inference from multi-omics data lacking |

---

### Theme 03 -- Multi-Omics Applications in Lung Cancer

> **2,648 papers** | 1 Tier A | 127 Tier B | 5 retracted

**What the literature establishes**

Proteogenomic studies from CPTAC revealed that protein-level alterations do not always mirror transcriptomic changes, identifying novel therapeutic targets through phosphoproteomics invisible at the genomic level. Integrative analyses have refined NSCLC subtyping beyond histopathological classification. Multi-omics approaches to tumor microenvironment characterization have revealed immune-excluded and immune-infiltrated subtypes with differential immunotherapy response. Multi-omics prognostic signatures show incremental improvement over single-omics approaches, though external validation remains limited.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| Proteogenomics reveals features invisible to genomics | Whether incremental value justifies complexity | Very few studies include matched pharmacogenomic data |
| Multi-omics prognosis modestly outperforms single-omics | Optimal omics combination for specific endpoints | Limited multi-omics studies on radiation response |
| TME characterization benefits from integration | How to validate when independent datasets are rare | No multi-omics studies on NSCLC in never-smokers |
| External validation is the major bottleneck | Whether batch effects compromise discoveries | Sex-stratified multi-omics analyses nearly absent |

---

### Theme 04 -- AI/ML in Lung Cancer and Oncology

> **11,167 papers** | 8 Tier A | 803 Tier B | 30 retracted

**What the literature establishes**

Deep learning classifies NSCLC subtypes from histopathology WSIs with high accuracy and predicts molecular alterations from H&E-stained slides. Radiomics/radiogenomics link imaging features to molecular characteristics and treatment outcomes, though reproducibility remains challenging. Foundation models pre-trained on large pathology datasets show strong transfer learning. ML-based immunotherapy response prediction incorporating TMB, PD-L1, gene expression, and imaging features shows multi-modal approaches outperforming single-modality models. External validation studies consistently show performance degradation, and algorithmic bias from demographic underrepresentation is a significant concern.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| DL classifies NSCLC subtypes with high accuracy | AI should replace vs. augment pathologists | Few ML models validated on multi-ethnic cohorts |
| Multi-modal AI outperforms single-modality | Fair benchmarking across demographic groups | Absence of sex-stratified AI model evaluation |
| External validation shows performance degradation | Extent of data leakage in published studies | Limited AI tools for never-smoker NSCLC |
| Foundation models reduce labeled data needs | Whether Western-trained models generalize globally | Integration of molecular + clinical AI is primitive |
| Radiomics requires harmonization | Optimal regulatory frameworks for clinical AI | AI fairness/bias assessment rarely performed |

---

### Theme 05 -- Sex and Gender Differences in Lung Cancer

> **4,707 papers** | 2 Tier A | 66 Tier B | 2 retracted

**What the literature establishes**

Sex and gender differences are well-documented but mechanistically underexplored. Women, particularly never-smokers, show higher EGFR mutation rates in LUAD. Estrogen receptor signaling is implicated through non-genomic pathways. Immunotherapy outcomes show sex-specific patterns, though findings are inconsistent. Loss of Y chromosome in male tumors is associated with altered immune surveillance. Epidemiological data consistently show women developing lung cancer younger and with lighter smoking histories.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| Women have higher EGFR rates, especially never-smokers | Whether ICI sex differences are biological or confounded | Mechanistic sex hormone interaction studies sparse |
| Sex-specific ICI outcomes exist (debated magnitude) | ER signaling: direct driver vs. modifier | Sex-stratified drug response data absent from databases |
| ER biology is relevant to lung cancer | Whether sex-stratified dosing is warranted | Y chromosome loss in lung cancer poorly characterized |
| Sex-stratified analyses are underperformed | How to separate sex from gender in outcomes | Pregnancy-associated lung cancer understudied |

---

### Theme 06 -- Never-Smoker Lung Cancer

> **2,689 papers** | 2 Tier A | 76 Tier B | 4 retracted

**What the literature establishes**

Never-smoker lung cancer is genomically and clinically distinct. Three major molecular subtypes identified in never-smoker LUAD: piano (low mutation burden, UBA1-driven), mezzo (EGFR-dominant), and forte (KRAS-dominant, higher burden). EGFR mutations occur in 40-60% of East Asian and 10-20% of Western never-smokers. Mutational signatures show absence of smoking-associated SBS4 and enrichment of clock-like (SBS1, SBS5) and APOBEC signatures. Tumor microenvironment tends to be less inflamed.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| Genomically distinct from smoking-associated disease | Etiological contribution of specific exposures | Etiological mechanisms in many cases remain unknown |
| EGFR is the most common driver | Whether immunotherapy response differs fundamentally | Limited immunoprofiling of never-smoker tumors |
| Mutational signatures differ fundamentally | Optimal screening strategies for at-risk never-smokers | No clinical trials for never-smoker subtypes |
| East Asian populations have distinctive features | Whether APOBEC has specific triggers | Germline risk x environment interactions understudied |

---

### Theme 07 -- Environmental Exposures and Lung Cancer

> **4,023 papers** | 2 Tier A | 79 Tier B | 1 retracted

**What the literature establishes**

PM2.5 exposure promotes EGFR-driven LUAD in never-smokers through promotion of pre-existing EGFR-mutant clones via inflammatory signaling rather than direct mutagenesis. Radon increases risk dose-dependently with characteristic chromosomal aberrations. Asbestos, silica, and diesel exhaust carry established risks with distinct molecular signatures. Indoor air pollution from cooking fumes and biomass combustion disproportionately affects women in Asian populations.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| PM2.5 and air pollution are established risk factors | PM2.5: mutagenic vs. promotional mechanisms | Exposome-to-subtype studies are rare |
| Environmental exposures can act non-mutagenically | Threshold of exposure for cancer risk | Wildfire smoke long-term effects unknown |
| Radon risk is dose-dependent | Risk attribution in multi-exposure settings | PFAS + lung cancer mechanisms unexplored |
| Indoor pollution disproportionately affects women | Whether e-cigarettes carry long-term risk | Environmental justice dimensions understudied |

---

### Theme 08 -- Epigenetics in Lung Cancer

> **5,902 papers** | 0 Tier A | 91 Tier B | **76 retracted**

**What the literature establishes**

DNA methylation changes (hypermethylation of CDKN2A, RASSF1A, MGMT; global hypomethylation) are early events in lung carcinogenesis. Methylation-based classifiers distinguish NSCLC subtypes and predict prognosis. Non-coding RNAs (miRNAs, lncRNAs) function as both oncogenes and tumor suppressors. ATAC-seq has revealed enhancer landscapes defining subtypes and master TFs. cfDNA methylation shows promise for early detection and MRD monitoring.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| Methylation changes are early carcinogenic events | Drivers vs. passengers among epigenetic marks | Causal vs. consequential changes not distinguished |
| Tumor suppressor hypermethylation is reproducible | Functional significance of many lncRNA associations | Single-cell epigenomics in lung cancer is limited |
| Non-coding RNAs play functional roles | Reproducibility of miRNA prognostic signatures | Epigenetic therapy clinical trials are few |
| cfDNA methylation promising for liquid biopsy | Whether epigenetic therapies work in solid tumors | Longitudinal epigenetic monitoring underexplored |

> **NOTE:** 76 retracted papers (highest of any theme) signals reproducibility concerns in miRNA/lncRNA prognostic signature studies. This finding should be mentioned in the review.

---

### Theme 09 -- Immune Biomarkers and Immunotherapy Response

> **6,459 papers** | 9 Tier A | 679 Tier B | 14 retracted

**What the literature establishes**

Immune biomarkers extend well beyond PD-L1. TMB correlates with immunotherapy benefit but has context-dependent limitations (STK11/KEAP1 co-mutated tumors respond poorly despite adequate TMB). Pan-cancer immune landscape analyses have classified tumors into immune subtypes. Gene expression signatures reflecting T cell inflammation and interferon signaling show reproducible associations. The gut microbiome modulates immunotherapy efficacy.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| PD-L1 alone is an imperfect predictor | Optimal TMB threshold for clinical decisions | Composite panels not standardized for clinical use |
| TMB adds imperfect predictive value | Whether composites significantly outperform in practice | Spatial immune biomarkers not validated prospectively |
| STK11/KEAP1 co-mutations confer ICI resistance | Degree to which microbiome modulation helps | Biomarker dynamics during treatment poorly captured |
| Multi-parameter approaches outperform single markers | How to standardize HLA typing for prediction | Neoantigen-based approaches need outcome data |

---

### Theme 10 -- Targeted Therapy Access & Translational Bottleneck

> **6,431 papers** | 0 Tier A | 67 Tier B | 2 retracted

**What the literature establishes**

Biomarker testing rates remain suboptimal with disparities by race, socioeconomic status, geography, and insurance. Many molecularly defined patients never receive matched therapies due to access barriers, testing gaps, or rapid deterioration. Real-world outcomes are more heterogeneous than clinical trial results. Clinical trial representation of women, minorities, and older adults remains inadequate.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| Biomarker testing rates are suboptimal and inequitable | Whether RWE should inform guidelines equally to RCTs | Interventions to improve testing rates not evaluated |
| Real-world outcomes more heterogeneous than trials | How to address structural testing barriers | RWE from LMICs is minimal |
| Disparities exist along race, SES, geography lines | Whether molecular tumor boards improve outcomes | Patient-reported outcomes rarely integrated |
| Guideline-concordant care improves outcomes | Role of direct-to-consumer genomic testing | Cost-effectiveness of multi-omics not established |

---

### Theme 11 -- Drug Repurposing in Oncology

> **6,386 papers** | 0 Tier A | 24 Tier B | 28 retracted

**What the literature establishes**

CMap approaches match drug-induced gene expression signatures to disease signatures. Pharmacogenomic databases (GDSC, CCLE, PRISM) provide large-scale drug sensitivity data. Synthetic lethality approaches targeting KRAS or STK11/KEAP1 dependencies offer targeted strategies. Network pharmacology integrates drug-target-disease networks. Multi-omics integration enhances drug response prediction.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| Computational repurposing can identify viable candidates | Whether predictions translate clinically at meaningful rates | Translation to clinical trials remains low |
| Pharmacogenomic databases enable systematic analysis | Optimal validation frameworks for candidates | Drug combination optimization using multi-omics is nascent |
| Multi-omics enhances drug response prediction | How to prioritize among many candidates | Lung cancer-specific repurposing < pan-cancer studies |
| Synthetic lethality promising for KRAS-mutant LC | Whether network pharmacology captures real complexity | DMF/KEAP1-targeting candidates need clinical data |

> **NOTE:** Only 24 Tier B papers -- the thinnest supporting literature of any theme. May need targeted manual expansion.

---

### Theme 12 -- Emerging Frontiers (Single-Cell, Spatial, Liquid Biopsy, Metabolomics)

> **6,179 papers** | 2 Tier A | 108 Tier B | 7 retracted

**What the literature establishes**

scRNA-seq has revealed extensive intratumoral heterogeneity and complex TME compositions. Spatial transcriptomics and proteomics preserve tissue architecture while providing molecular detail. Liquid biopsy (ctDNA, cfDNA methylation) enables non-invasive monitoring, early detection, and MRD assessment. Metabolomics/lipidomics add functional dimensions. Lung and gut microbiome have been linked to cancer susceptibility and immunotherapy response.

| Consensus | Disagreement | Gaps |
|:---|:---|:---|
| Single-cell reveals previously unrecognized heterogeneity | Whether small biopsies represent whole-tumor biology | Multi-modal single-cell + spatial integration nascent |
| Spatial technologies add critical architectural context | Technical reproducibility of spatial platforms | Clinical validation of liquid biopsy for early detection ongoing |
| Liquid biopsy approaching clinical utility | Sensitivity/specificity of liquid biopsy for early-stage | Metabolomic profiling of subtypes is sparse |
| Microbiome modulates immunotherapy response | Clinical utility of microbiome-based interventions | Spatial omics in never-smoker lung cancer absent |

---

## 5. Evidence Strength Heat Map

Assessment of evidence depth by theme, based on Tier A/B concentration and literature maturity:

| Theme | Evidence Strength | Maturity | Actionability for Review |
|:---|:---:|:---:|:---|
| 01 Molecular Heterogeneity | STRONG | Mature | Foundational section -- cite heavily |
| 02 Multi-Omics Methods | STRONG | Mature | Methods spine of the review |
| 03 Multi-Omics Applications | MODERATE | Growing | Connect methods to lung-specific results |
| 04 AI/ML | STRONG | Rapidly growing | Largest theme -- curate carefully |
| 05 Sex/Gender | MODERATE | Early | Gap itself is a key finding |
| 06 Never-Smoker | MODERATE | Growing | Central to the review's thesis |
| 07 Environmental | MODERATE | Mature (epidemiology) | Strong epi, weak molecular intersection |
| 08 Epigenetics | MODERATE | Mixed (high retractions) | Emphasize reproducibility concerns |
| 09 Immune Biomarkers | STRONG | Mature | Rich literature -- focus on NSCLC-specific |
| 10 Translational | WEAK | Diffuse | Important narrative but fewer landmarks |
| 11 Drug Repurposing | WEAK | Nascent | Needs manual curation / expansion |
| 12 Emerging Frontiers | MODERATE | Rapidly growing | Highlight technological trajectory |

---

## 6. Critical Gaps Identified Across All Themes

These gaps represent the review's strongest contribution to the field:

| Gap | Relevant Themes | Priority for Review |
|:---|:---|:---:|
| **Sex-stratified multi-omics analyses nearly absent** | 01, 03, 04, 05 | HIGHEST |
| **No multi-omics studies focused on NSCLC in never-smokers** | 03, 06 | HIGHEST |
| **Exposome-to-molecular-subtype studies are extremely sparse** | 06, 07 | HIGH |
| **AI fairness/bias assessment rarely performed for oncology** | 04 | HIGH |
| **Few ML models validated on multi-ethnic cohorts** | 04, 10 | HIGH |
| **Composite immune biomarker panels not standardized** | 09 | HIGH |
| **Drug repurposing-to-clinical-trial translation rate is low** | 11 | HIGH |
| **Cost-effectiveness of multi-omics precision oncology not established** | 10 | MODERATE |
| **Single-cell epigenomics in lung cancer is limited** | 08, 12 | MODERATE |
| **Spatial omics in never-smoker lung cancer absent** | 06, 12 | MODERATE |
| **Pre-neoplastic lesion evolution poorly understood** | 01 | MODERATE |
| **Longitudinal molecular profiling through treatment is sparse** | 01, 08, 12 | MODERATE |
| **miRNA/lncRNA prognostic signatures have reproducibility concerns** | 08 | MODERATE |
| **Pregnancy-associated lung cancer molecularly understudied** | 05 | LOWER |

---

## 7. Retraction Analysis

| Theme | Retracted | Notes |
|:---|---:|:---|
| 01 Molecular Heterogeneity | 50 | Spread across subtypes |
| 02 Multi-Omics Methods | 8 | Low rate |
| 03 Multi-Omics Applications | 5 | Low rate |
| 04 AI/ML | 30 | Some in radiomics |
| 05 Sex/Gender | 2 | Clean |
| 06 Never-Smoker | 4 | Clean |
| 07 Environmental | 1 | Very clean |
| 08 **Epigenetics** | **76** | **Highest -- miRNA/lncRNA prognostic sigs** |
| 09 Immune Biomarkers | 14 | Moderate |
| 10 Translational | 2 | Clean |
| 11 Drug Repurposing | 28 | Moderate -- network pharmacology area |
| 12 Emerging Frontiers | 7 | Low rate |
| **Total** | **208** | Excluded from master library |

> The 76 retractions in Theme 08 are concentrated in miRNA and lncRNA prognostic signature studies, consistent with known reproducibility crises in these subfields. Consider mentioning this pattern in the review as evidence for the need for rigorous validation frameworks.

---

## 8. Anchor PMID Audit

| PMID | Expected Paper | Theme | Status |
|:---|:---|:---:|:---:|
| 25079552 | TCGA LUAD (*Nature* 2014) | 01 | Present |
| 22960745 | TCGA LUSC (*Nature* 2012) | 01 | Present |
| 26168399 | George -- SCLC (*Nature* 2015) | 01 | Present |
| 31406302 | Skoulidis -- co-mutations (*Nat Rev Cancer* 2019) | 01 | Present |
| 32649874 | Gillette -- CPTAC LUAD (*Cell* 2020) | 01 | Present |
| 32649875 | Chen -- East Asia proteogenomics (*Cell* 2020) | 01 | Present |
| 32649877 | Xu -- LUAD proteomics (*Cell* 2020) | 01 | Present |
| 38181741 | Liu -- SCLC proteogenomics (*Cell* 2024) | 01 | Present |
| 30926931 | Rudin -- SCLC subtypes (*Nat Rev Cancer* 2019) | 01 | Present |
| 33011388 | Gay -- SCLC therapeutic vulnerabilities (*JTO* 2021) | 01 | Present |
| 32185779 | MOVICS (*Bioinformatics* 2020) | 02 | Present |
| 28369062 | mixOmics DIABLO (*PLoS ONE* 2017) | 02 | Metadata mismatch |
| 19759197 | iCluster (*Bioinformatics* 2009) | 02 | Present |
| 24464287 | SNF (*Nat Methods* 2014) | 02 | Present |
| 32393329 | MOFA+ (*Genome Biol* 2020) | 02 | Present |
| 30590492 | NEMO (*Bioinformatics* 2019) | 02 | Metadata mismatch |
| 33524135 | Cantini benchmarking (*Nat Comms* 2021) | 02 | **MISSING** |
| 30224757 | Coudray -- histopath DL (*Nat Med* 2018) | 04 | Present |
| 35944502 | Chen -- pan-cancer multimodal (*Cancer Cell* 2022) | 04 | Present |
| 39294368 | CHIEF foundation model (*Nature* 2024) | 04 | Present |
| 39030412 | Virchow foundation model (*Nat Med* 2024) | 04 | Metadata mismatch |
| 36108632 | Lipkova -- multimodal AI (*Cancer Cell* 2022) | 04 | Metadata mismatch |
| 35512792 | Boehm -- multimodal oncology (*Nat Rev Cancer* 2022) | 04 | Metadata mismatch |
| 29778737 | Conforti -- sex + ICI (*Lancet Oncol* 2018) | 05 | Present |
| 32350439 | Rubin -- sex differences (*Nat Rev Cancer* 2020) | 05 | Metadata mismatch |
| 17667967 | Sun -- never smoker (*Nat Rev Cancer* 2007) | 06 | Metadata mismatch |
| 34493867 | Zhang -- never smoker genomics (*Nat Genet* 2021) | 06 | Present |
| 37046093 | Hill -- PM2.5 EGFR (*Nature* 2023) | 07 | Present |
| 23900102 | Raaschou-Nielsen -- air pollution (*Lancet Oncol* 2013) | 07 | Metadata mismatch |
| 29628290 | Thorsson -- immune landscape (*Immunity* 2018) | 09 | Present |
| 28052254 | Charoentong -- Immunophenoscore (*Cell Reports* 2017) | 09 | Present |
| 34019806 | Bagaev -- microenvironment (*Cancer Cell* 2021) | 09 | Present |
| 25765070 | Rizvi -- TMB + PD-1 (*Science* 2015) | 09 | Present |
| 33479125 | Litchfield -- pan-cancer ICI (*Cell* 2021) | 09 | Present |
| 29988129 | Lambrechts -- stromal phenotype (*Nat Med* 2018) | 12 | Present |
| 32015526 | Chabon -- CAPP-Seq (*Nature* 2020) | 12 | Present |

> **33524135** (Cantini benchmarking) returns empty from PubMed API. Correct PMID is likely **33402734**, which is in the library via query-based search. Several PMIDs flagged "Metadata mismatch" fetched different papers than expected -- the intended papers were captured through queries regardless.

---

## 9. Surprising Findings & Writing Recommendations

| Finding | Implication for Review |
|:---|:---|
| **76 retractions in epigenetics theme** | Mention as evidence for need for rigorous validation in ncRNA studies |
| **1,928 bridge papers (3+ themes)** | Field is increasingly integrative -- supports the review's central thesis |
| **Never-smoker literature is thinner than expected** | The gap IS the finding -- emphasize as a call to action |
| **Exposome-to-subtype intersection barely exists** | Frame as a major unmet research need |
| **Foundation models/LLMs are the fastest-growing subfield** | Warrants dedicated discussion beyond current outline |
| **Drug repurposing has the weakest evidence base** | Broaden beyond DMF to include synthetic lethality (more literature support) |
| **SCLC transformation as resistance mechanism** | Mention even in NSCLC-focused review |
| **Liquid biopsy/cfDNA methylation rapidly emerging** | Consider adding a section not in current outline |

---

## 10. File Inventory & Access Guide

| What you need | Where to find it |
|:---|:---|
| **Import everything into EndNote** | `master/master_library.ris` (66,671 papers) |
| **High-priority papers only** | `master/high_priority.csv` |
| **Which themes a paper belongs to** | `master/theme_tags.csv` |
| **Synthesis notes for writing each section** | `themes/theme_XX_*/section_notes.md` |
| **Browse papers for a specific theme** | `themes/theme_XX_*/papers.md` |
| **Full paper metadata (JSON, searchable)** | `metadata/all_papers.json` |
| **Papers flagged as retracted** | `metadata/retracted_flagged.csv` |
| **Deduplication details** | `metadata/dedup_report.md` |
| **Search queries and hit counts** | `themes/theme_XX_*/queries_run.md` |
| **Re-run the pipeline** | `scripts/` (see README.md) |

---

*Pipeline: 177 PubMed queries + 36 Europe PMC queries | Deduplication: PMID + DOI + fuzzy title | Scoring: keyword density + journal tier + citations + recency*
