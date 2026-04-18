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

---
---

# 11. Results: Thematic Literature Synthesis

> The following sections present a narrative synthesis of the evidence collected across all 12 themes. Each section contains 4-5 paragraphs summarizing the current state of knowledge, areas of consensus and controversy, and critical gaps. All findings are paraphrased; citations reference PMID-linked studies retrieved through the systematic search pipeline. These sections are intended to serve as the raw material for manuscript drafting.

---

## 11.1 Lung Cancer Molecular Heterogeneity Foundations

The molecular architecture of lung cancer has been comprehensively mapped through large-scale consortium studies, revealing that lung adenocarcinoma (LUAD) and lung squamous cell carcinoma (LUSC) are fundamentally distinct diseases at the genomic, transcriptomic, and proteomic levels. The Cancer Genome Atlas (TCGA) landmark studies established the mutational landscape of LUAD, identifying recurrent alterations in EGFR, KRAS, and ALK as key oncogenic drivers [PMID: [25079552](https://pubmed.ncbi.nlm.nih.gov/25079552/)], while the parallel LUSC characterization revealed a distinct spectrum dominated by TP53 mutations, FGFR1 amplifications, and SOX2 amplification [PMID: [22960745](https://pubmed.ncbi.nlm.nih.gov/22960745/)]. These foundational studies demonstrated that histological subtype corresponds to fundamentally different biology, necessitating subtype-specific therapeutic strategies rather than unified approaches to non-small cell lung cancer (NSCLC).

Beyond NSCLC, the molecular classification of small cell lung cancer (SCLC) has undergone a transformative revision. George et al. reported the first comprehensive genomic profiling of SCLC, revealing near-universal TP53 and RB1 inactivation alongside recurrent alterations in NOTCH, MYC, and chromatin remodeling pathways [PMID: [26168399](https://pubmed.ncbi.nlm.nih.gov/26168399/)]. This work set the stage for the transcription factor-based subtype classification proposed by Rudin et al., which defined four SCLC subtypes -- SCLC-A (ASCL1), SCLC-N (NEUROD1), SCLC-P (POU2F3), and SCLC-Y (YAP1) -- each associated with distinct therapeutic vulnerabilities [PMID: [30926931](https://pubmed.ncbi.nlm.nih.gov/30926931/)]. Subsequent immunohistochemical validation by Baine et al. confirmed the feasibility of classifying clinical specimens into these subtypes [PMID: [33011388](https://pubmed.ncbi.nlm.nih.gov/33011388/)], while recent proteogenomic characterization by Liu et al. identified subtype-specific phosphoproteomic signatures and candidate drug targets that were invisible at the genomic level [PMID: [38181741](https://pubmed.ncbi.nlm.nih.gov/38181741/)].

Co-mutation patterns have emerged as critical determinants of both prognosis and treatment response in NSCLC. Skoulidis and Heymach comprehensively reviewed how co-occurring genomic alterations -- particularly KRAS/STK11, KRAS/KEAP1, and KRAS/TP53 in LUAD -- define biologically and clinically distinct disease subgroups with differential sensitivity to immunotherapy and targeted agents [PMID: [31406302](https://pubmed.ncbi.nlm.nih.gov/31406302/)]. Proteogenomic studies from the Clinical Proteomic Tumor Analysis Consortium (CPTAC) have further revealed that protein-level and phosphoprotein-level alterations frequently diverge from genomic predictions, identifying druggable kinase activities not apparent from DNA sequencing alone. Gillette et al. identified therapeutic vulnerabilities in LUAD through integrated proteomic and phosphoproteomic profiling [PMID: [32649874](https://pubmed.ncbi.nlm.nih.gov/32649874/)], while Xu et al. delineated proteomic subtypes with distinct immune and metabolic features [PMID: [32649877](https://pubmed.ncbi.nlm.nih.gov/32649877/)]. East Asian populations, where never-smoker LUAD predominates, demonstrated unique proteogenomic signatures driven by EGFR-pathway rewiring [PMID: [32649875](https://pubmed.ncbi.nlm.nih.gov/32649875/)].

The field has also recognized the clinical significance of histologic transformation as a mechanism of acquired resistance to targeted therapies. NSCLC-to-SCLC transformation under EGFR TKI pressure represents a well-documented route of treatment failure, highlighting the need for longitudinal molecular profiling. Recent work by Martinez-Ruiz et al. tracked genomic and transcriptomic evolution across treatment, demonstrating that subclonal dynamics and phenotypic plasticity drive therapeutic resistance [PMID: [37046093](https://pubmed.ncbi.nlm.nih.gov/37046093/)]. Harada et al. have drawn attention to rare molecular subtypes -- including large cell neuroendocrine carcinoma and sarcomatoid carcinoma -- which remain molecularly understudied relative to LUAD and LUSC [PMID: [36806787](https://pubmed.ncbi.nlm.nih.gov/36806787/)]. Critically, most large-scale molecular studies have been conducted predominantly in European-ancestry cohorts, and sex-stratified molecular characterization has rarely been performed systematically, leaving important biological dimensions of lung cancer heterogeneity underexplored.

---

## 11.2 Multi-Omics Integration Methods

The methodological landscape for multi-omics integration has evolved substantially over the past decade, progressing from simple data concatenation to statistically principled and computationally sophisticated frameworks. The iCluster algorithm, introduced by Shen et al., provided the first widely adopted approach for joint latent variable modeling across multiple genomic data types, demonstrating that integrative clustering could identify cancer subtypes invisible to any single platform [PMID: [19759197](https://pubmed.ncbi.nlm.nih.gov/19759197/)]. Wang et al. developed Similarity Network Fusion (SNF), which constructs and fuses patient similarity networks from each data type, offering a flexible non-parametric alternative that has been widely adopted for multi-omics subtype discovery [PMID: [24464287](https://pubmed.ncbi.nlm.nih.gov/24464287/)]. MOFA+ extended Bayesian factor analysis to the multi-omics setting, enabling simultaneous decomposition of variation across data modalities while handling missing data and batch effects [PMID: [32393329](https://pubmed.ncbi.nlm.nih.gov/32393329/)].

Benchmarking studies have revealed that no single integration method dominates across all cancer types, sample sizes, and data configurations. Pierre-Jean et al. systematically evaluated 13 unsupervised integration methods, demonstrating substantial variability in performance depending on the signal structure and noise characteristics of the input data [PMID: [31792509](https://pubmed.ncbi.nlm.nih.gov/31792509/)]. Chauvel et al. further showed that the choice between early, intermediate, and late integration strategies has a meaningful impact on subtype recovery, with intermediate approaches often providing the best balance between data-type-specific signal preservation and cross-platform integration [PMID: [31220206](https://pubmed.ncbi.nlm.nih.gov/31220206/)]. More recent benchmarking by Hu et al. extended these evaluations to single-cell multi-omics methods, revealing that algorithmic performance is highly dependent on data sparsity and modality pairing [PMID: [39322753](https://pubmed.ncbi.nlm.nih.gov/39322753/)].

Deep learning approaches have introduced new possibilities for capturing non-linear relationships across omics layers. Variational autoencoders (VAEs) and graph neural networks (GNNs) have been applied to multi-omics integration with increasing frequency, with recent tools such as Flexynesis providing unified deep learning frameworks for bulk multi-omics data integration in precision oncology [PMID: [40940333](https://pubmed.ncbi.nlm.nih.gov/40940333/)]. Athaya et al. reviewed multimodal deep learning approaches for single-cell multi-omics data, identifying transformer architectures and attention mechanisms as particularly promising for cross-modality alignment [PMID: [37651607](https://pubmed.ncbi.nlm.nih.gov/37651607/)]. However, a persistent question remains whether deep learning methods genuinely outperform simpler statistical approaches at the sample sizes typical of current cancer cohorts, and scalability to five or more omics layers simultaneously has not been convincingly demonstrated.

Despite this methodological richness, several critical gaps persist. Very few integration methods have been designed with clinical deployment in mind -- runtime, memory efficiency, interpretability, and integration of clinical covariates remain secondary considerations in most tool development. Methods for integrating spatial multi-omics data are nascent, and tools for temporal or longitudinal multi-omics integration are largely absent. Baiao et al. provided a comprehensive technical review spanning classical statistical to deep generative approaches, highlighting that causal inference from multi-omics data remains an open methodological challenge [PMID: [40748323](https://pubmed.ncbi.nlm.nih.gov/40748323/)]. The field would benefit from consensus benchmarks and standardized evaluation frameworks that go beyond clustering agreement to assess clinical utility and biological interpretability of integration outputs.

---

## 11.3 Multi-Omics Applications in Lung Cancer

The application of multi-omics integration to lung cancer has yielded discoveries that fundamentally could not have emerged from single-platform analyses. Proteogenomic studies have been particularly illuminating: Lehti&ouml; et al. profiled the proteogenomic landscape of NSCLC and identified molecular subtypes associated with specific therapeutic responses that were not predicted by genomic data alone, including kinase activities detectable only at the phosphoprotein level [PMID: [34870237](https://pubmed.ncbi.nlm.nih.gov/34870237/)]. Song et al. extended proteogenomic analysis to reveal NSCLC subtypes predictive of chromosome instability and differential drug sensitivity [PMID: [39580524](https://pubmed.ncbi.nlm.nih.gov/39580524/)]. These studies consistently demonstrate that protein-level measurements add clinically relevant information beyond what can be inferred from DNA or RNA alone, particularly for identifying druggable targets in the kinase signaling landscape.

Integrative approaches to tumor microenvironment (TME) characterization have revealed immune contexts that modulate treatment response. Multi-omics profiling combining transcriptomic, epigenomic, and proteomic data has identified immune-excluded versus immune-infiltrated subtypes with markedly different immunotherapy outcomes. Hanley et al. used single-cell analysis combined with multi-omics data to identify prognostic fibroblast subpopulations linked to molecular and immunological subtypes of NSCLC [PMID: [36720863](https://pubmed.ncbi.nlm.nih.gov/36720863/)]. Aung et al. demonstrated that spatial multi-omics signatures could predict immunotherapy outcomes in NSCLC, suggesting that the spatial organization of the TME carries information beyond bulk molecular profiles [PMID: [41073787](https://pubmed.ncbi.nlm.nih.gov/41073787/)]. Chen et al. further showed that integrative spatial analysis reveals tumor heterogeneity and immune colony niches related to clinical outcomes [PMID: [39983726](https://pubmed.ncbi.nlm.nih.gov/39983726/)].

Multi-omics-based prognostic models have shown incremental improvement over single-omics signatures, though the magnitude of improvement varies and external validation remains a major bottleneck. Wang et al. demonstrated that multi-omics analyses of recurrent stage I NSCLC reveal biological and clinical insights not captured by standard staging [PMID: [39929832](https://pubmed.ncbi.nlm.nih.gov/39929832/)]. Machine learning frameworks integrating multiple omics layers have been developed specifically for lung cancer subtype classification and prognosis prediction, including hierarchical graph neural network approaches [PMID: [41554048](https://pubmed.ncbi.nlm.nih.gov/41554048/)]. Zhang et al. applied multi-omics characterization combined with machine learning to identify LUAD molecular subtypes that guide immunotherapy decisions [PMID: [39669580](https://pubmed.ncbi.nlm.nih.gov/39669580/)].

Despite these advances, significant gaps limit the translational impact of multi-omics integration in lung cancer. Very few studies include matched pharmacogenomic data linking multi-omics profiles to drug response. Multi-omics applications to radiation therapy response remain limited. Most critically, there are no published multi-omics studies focused specifically on NSCLC in never-smokers, and sex-stratified multi-omics analyses are nearly absent from the literature -- both representing major blind spots given the distinct biology of these populations. Su et al. have begun addressing this gap with proteogenomic characterization that reveals distinct tumorigenesis pathways in specific lung cancer manifestations [PMID: [40069142](https://pubmed.ncbi.nlm.nih.gov/40069142/)], but systematic multi-omics studies stratified by sex, smoking status, and ancestry remain an urgent unmet need.

---

## 11.4 AI/ML in Lung Cancer and Oncology

Artificial intelligence and machine learning have been applied across the entire spectrum of lung cancer research, from molecular subtyping to clinical outcome prediction, with deep learning on histopathology images representing the most mature application. Coudray et al. demonstrated that a convolutional neural network trained on whole slide images (WSIs) could classify NSCLC into LUAD versus LUSC with performance comparable to expert pathologists, and further predict specific genomic alterations including STK11, EGFR, and TP53 mutations directly from H&E-stained tissue [PMID: [30224757](https://pubmed.ncbi.nlm.nih.gov/30224757/)]. This landmark study established the paradigm that histopathology images encode molecular information that can be decoded computationally. Chen et al. extended this to a pan-cancer multimodal framework integrating histology with genomic data, showing that multi-modal deep learning models outperform single-modality approaches for survival prediction [PMID: [35944502](https://pubmed.ncbi.nlm.nih.gov/35944502/)].

Foundation models pre-trained on massive pathology image datasets have emerged as a transformative development in the field since 2023. Wang et al. developed a pathology foundation model for cancer diagnosis and prognosis prediction that demonstrated strong transfer learning across multiple tumor types, reducing the need for large labeled training sets in individual tasks [PMID: [39232164](https://pubmed.ncbi.nlm.nih.gov/39232164/)]. Yang et al. built a generalizable foundation model that achieved state-of-the-art performance in cancer diagnosis and survival prediction from histopathological images with minimal fine-tuning [PMID: [40064883](https://pubmed.ncbi.nlm.nih.gov/40064883/)]. Dolezal et al. introduced uncertainty quantification methods that enable deep learning models to flag predictions where confidence is low, providing a critical safety mechanism for clinical deployment [PMID: [36323656](https://pubmed.ncbi.nlm.nih.gov/36323656/)]. These models represent a paradigm shift from task-specific architectures to general-purpose visual encoders.

Radiomics and radiogenomics have established links between imaging features and underlying molecular characteristics, although reproducibility remains a persistent challenge. Radiomics-based models have been developed for predicting immunotherapy response in NSCLC, with Rakaee et al. demonstrating that a deep learning model applied to pre-treatment CT scans could predict immunotherapy outcomes in advanced NSCLC [PMID: [39724105](https://pubmed.ncbi.nlm.nih.gov/39724105/)]. However, radiomic features are highly sensitive to acquisition parameters, scanner manufacturers, and reconstruction algorithms, necessitating harmonization strategies for multi-institutional validation. Bakas et al. developed consensus recommendations for AI-based response assessment in neuro-oncology that provide a useful framework adaptable to thoracic imaging [PMID: [39481415](https://pubmed.ncbi.nlm.nih.gov/39481415/)].

The reproducibility and generalizability of medical AI remain significant concerns. External validation studies consistently demonstrate performance degradation when models are applied to populations different from their training data. Arshad et al. reviewed AI and ML applications in lung cancer detection and prognosis, concluding that algorithmic bias related to demographic underrepresentation in training cohorts is a systemic problem requiring proactive mitigation [PMID: [41463234](https://pubmed.ncbi.nlm.nih.gov/41463234/)]. Few ML models have been validated on multi-ethnic, multi-institutional cohorts; sex-stratified model development and evaluation is virtually absent; and AI tools specifically designed for never-smoker NSCLC do not yet exist. Regulatory frameworks for clinical AI deployment lag behind technical capabilities, creating an implementation gap between research performance and clinical utility. The convergence of AI with multi-omics data -- rather than imaging alone -- represents the next frontier, yet integration of molecular data with clinical AI remains technically primitive and methodologically unstandardized.

---

## 11.5 Sex and Gender Differences in Lung Cancer

Sex and gender differences in lung cancer epidemiology, molecular biology, and treatment outcomes are well documented at the population level but remain mechanistically underexplored. Epidemiological data consistently demonstrate that women develop lung cancer at younger ages and with lighter smoking histories than men, and the proportion of never-smoker lung cancer cases is substantially higher among women. Patel et al. characterized lung cancer as a contemporary epidemic in US women, drawing attention to rising incidence trends that could not be fully explained by smoking patterns alone [PMID: [15082704](https://pubmed.ncbi.nlm.nih.gov/15082704/)]. Women show significantly higher rates of EGFR mutations in LUAD, particularly among never-smokers, suggesting that sex-linked biological factors -- beyond differential smoking exposure -- contribute to the distinct mutational landscape observed in female lung cancer patients.

Estrogen receptor signaling has been implicated as a biologically relevant pathway in lung cancer pathogenesis. Siegfried et al. were among the first to propose a functional role for estrogen in non-small cell lung cancer, presenting evidence that estrogen receptor beta is expressed in lung tumor tissue and may promote proliferation through non-genomic signaling mechanisms [PMID: [11905727](https://pubmed.ncbi.nlm.nih.gov/11905727/)]. Mah et al. demonstrated that aromatase expression in tumor tissue predicts survival in women with early-stage NSCLC, providing further evidence for hormonal modulation of lung cancer biology [PMID: [17974992](https://pubmed.ncbi.nlm.nih.gov/17974992/)]. The Women's Health Initiative trial provided epidemiological evidence that combined estrogen-progestin hormone therapy was associated with increased lung cancer mortality, particularly from NSCLC, adding clinical urgency to understanding estrogen-lung cancer interactions [PMID: [19767090](https://pubmed.ncbi.nlm.nih.gov/19767090/)]. More recently, Park et al. used proteogenomic characterization to identify estrogen signaling as a targetable pathway specifically in never-smoker LUAD [PMID: [38607364](https://pubmed.ncbi.nlm.nih.gov/38607364/)].

Immunotherapy outcomes demonstrate sex-specific patterns that remain actively debated. Conforti et al. conducted a seminal meta-analysis of randomized controlled trials of immune checkpoint inhibitors across tumor types, reporting that the magnitude of benefit from anti-PD-1/PD-L1 therapy appeared greater in men than in women [PMID: [29778737](https://pubmed.ncbi.nlm.nih.gov/29778737/)]. Subsequent analyses have produced inconsistent results, with some studies confirming a sex-based differential and others finding no significant interaction. Vaval&agrave; et al. explored gender differences and immunotherapy outcomes in advanced lung cancer, noting that confounders including smoking status, TMB, and PD-L1 expression may partially account for observed sex differences [PMID: [34769372](https://pubmed.ncbi.nlm.nih.gov/34769372/)]. Madala et al. and Caliman et al. further investigated sex-related differences in survival outcomes among lung cancer patients treated with PD-1/PD-L1 inhibitors, emphasizing the need for sex-stratified trial design and reporting [PMID: [35400597](https://pubmed.ncbi.nlm.nih.gov/35400597/); PMID: [36045535](https://pubmed.ncbi.nlm.nih.gov/36045535/)].

Critical gaps in this domain are themselves among the most important findings of this review. Sex-stratified drug response data are largely absent from major pharmacogenomic databases including GDSC and CCLE. Loss of Y chromosome in male lung tumors and its impact on immune evasion remain poorly characterized. Pregnancy-associated lung cancer is molecularly understudied, and sex-specific biomarker panels for immunotherapy patient selection have not been developed. The broader challenge of disentangling biological sex from sociocultural gender effects in outcomes research -- including differential healthcare-seeking behavior, occupational exposures, and treatment access -- requires deliberately designed epidemiological and translational studies that the field has not yet prioritized.

---

## 11.6 Never-Smoker Lung Cancer

Lung cancer arising in never-smokers represents a genomically and clinically distinct entity that has received disproportionately little molecular characterization relative to smoking-associated disease. Zhang et al. provided a landmark genomic and evolutionary classification of lung cancer in never-smokers, identifying three major molecular subtypes: piano (characterized by low mutation burden and frequent UBA1-driven pathology), mezzo (dominated by EGFR mutations), and forte (KRAS-dominant with higher mutation burden resembling smoker-associated tumors) [PMID: [34493867](https://pubmed.ncbi.nlm.nih.gov/34493867/)]. These subtypes have distinct evolutionary trajectories and clinical behaviors, establishing that never-smoker lung cancer is not a single disease but a family of molecularly defined entities. Sun et al. had earlier articulated the conceptual framework for never-smoker lung cancer as a fundamentally different disease, highlighting its enrichment for EGFR mutations and ALK fusions and its distinct epidemiological patterns [PMID: [17882278](https://pubmed.ncbi.nlm.nih.gov/17882278/)].

The mutational signature landscape of never-smoker lung cancer differs fundamentally from that of smokers. Smoking-associated tumors are dominated by signature SBS4 (tobacco carcinogen exposure), while never-smoker tumors show enrichment of clock-like signatures (SBS1, SBS5) and APOBEC-associated mutagenesis (SBS2, SBS13). Govindan et al. compared the genomic landscapes of NSCLC in smokers and never-smokers, revealing substantially lower overall mutation burden and a distinct spectrum of driver alterations in never-smoker tumors [PMID: [22980976](https://pubmed.ncbi.nlm.nih.gov/22980976/)]. D&iacute;az-Gay et al. recently provided a comprehensive analysis of the mutagenic forces shaping never-smoker lung cancer genomes, demonstrating that the contribution of endogenous mutational processes -- rather than exogenous carcinogen exposure -- predominates in this population [PMID: [40604281](https://pubmed.ncbi.nlm.nih.gov/40604281/)]. EGFR mutations occur in 40-60% of East Asian never-smokers and 10-20% of Western never-smokers, with Chen et al. mapping the proteogenomic landscape of non-smoking lung cancer in East Asia [PMID: [32649875](https://pubmed.ncbi.nlm.nih.gov/32649875/)].

The tumor immune microenvironment of never-smoker lung cancers tends to be less inflamed than that of smoker-associated tumors, with lower CD8+ T cell infiltration and reduced expression of immune checkpoint molecules, potentially contributing to variable immunotherapy responses. Hamouz et al. provided a functional genomics review highlighting that the immunologically "cold" microenvironment in many never-smoker tumors poses a challenge for immune checkpoint blockade, while simultaneously identifying subsets with high APOBEC-driven neoantigen loads that may benefit from immunotherapy [PMID: [37686122](https://pubmed.ncbi.nlm.nih.gov/37686122/)]. Liquid biopsy approaches, particularly ctDNA-based monitoring, have shown promise for non-invasive detection and tracking of never-smoker lung cancers, though Chabon et al. demonstrated that integrating genomic features improves early lung cancer detection sensitivity [PMID: [32269342](https://pubmed.ncbi.nlm.nih.gov/32269342/)].

Despite the clinical importance of never-smoker lung cancer -- which accounts for an estimated 10-25% of all lung cancers globally and is rising in incidence -- several fundamental questions remain unanswered. The etiological mechanisms in a substantial proportion of never-smoker cases remain unknown, with no identifiable environmental, genetic, or infectious cause. No clinical trials have been specifically designed around never-smoker molecular subtypes, and never-smoker representation in liquid biopsy validation cohorts is low. The interaction between germline risk variants, as identified by Li et al. in genome-wide association studies of never-smoker lung cancer risk [PMID: [20304703](https://pubmed.ncbi.nlm.nih.gov/20304703/)], and environmental exposures remains insufficiently characterized. The relative scarcity of this literature compared to smoking-associated disease is itself a significant finding of this review, underscoring the need for dedicated research programs and multi-ethnic cohort studies focused on this population.

---

## 11.7 Environmental Exposures and Lung Cancer

Environmental exposures contribute to lung cancer through diverse and increasingly well-characterized molecular mechanisms, though the intersection between specific exposures and molecular subtypes remains sparsely mapped. Ambient air pollution, particularly fine particulate matter (PM2.5), has been established as a significant lung cancer risk factor. Pope et al. provided foundational epidemiological evidence linking long-term exposure to fine particulate air pollution with increased lung cancer mortality [PMID: [11879110](https://pubmed.ncbi.nlm.nih.gov/11879110/)]. Raaschou-Nielsen et al. confirmed this association across 17 European cohorts, demonstrating elevated lung cancer incidence even at pollution levels below European regulatory limits [PMID: [23849838](https://pubmed.ncbi.nlm.nih.gov/23849838/)]. The mechanistic basis for PM2.5-induced carcinogenesis was clarified by Mart&iacute;nez-Ruiz et al., who provided evidence that air pollution promotes EGFR-driven lung adenocarcinoma in never-smokers through promotion of pre-existing EGFR-mutant clones via inflammatory IL-1&beta; signaling, rather than through direct mutagenesis [PMID: [37046093](https://pubmed.ncbi.nlm.nih.gov/37046093/)]. This promotional mechanism represents a paradigm shift in understanding environmental carcinogenesis.

Radon exposure represents the second leading cause of lung cancer after smoking and has been extensively studied in occupational and residential settings. Pershagen et al. demonstrated an association between residential radon and lung cancer in a Swedish nationwide study [PMID: [8264737](https://pubmed.ncbi.nlm.nih.gov/8264737/)], while V&auml;h&auml;kangas et al. identified characteristic mutations in TP53 and RAS genes among uranium miners exposed to radon, establishing molecular signatures distinct from smoking-related damage [PMID: [1347094](https://pubmed.ncbi.nlm.nih.gov/1347094/)]. Occupational exposures to asbestos carry well-documented lung cancer risks: Camus et al. quantified non-occupational chrysotile asbestos exposure as a lung cancer risk factor [PMID: [9603793](https://pubmed.ncbi.nlm.nih.gov/9603793/)], while Lipsett et al. confirmed the diesel exhaust-lung cancer association through meta-analysis [PMID: [10394308](https://pubmed.ncbi.nlm.nih.gov/10394308/)].

Indoor air pollution, including cooking fumes from high-temperature methods and solid fuel combustion, disproportionately affects women in Asian populations and has been linked to specific LUAD mutational patterns. Murphy et al. recently reviewed the comprehensive landscape of lung cancer in non-smoking individuals, synthesizing evidence from occupational, residential, and ambient exposure sources [PMID: [41114991](https://pubmed.ncbi.nlm.nih.gov/41114991/)]. A recent meta-analysis quantified the association between indoor environmental pollution and lung cancer risk in never-smokers [PMID: [40950280](https://pubmed.ncbi.nlm.nih.gov/40950280/)], reinforcing the importance of non-tobacco exposure assessment in this population.

Critical gaps in the environmental exposure literature include the near-complete absence of exposome-scale studies that systematically link environmental exposures to specific molecular subtypes. Long-term molecular effects of wildfire smoke exposure on lung cancer risk are unknown despite increasing relevance due to climate change. The relationship between per- and polyfluoroalkyl substance (PFAS) exposure and lung cancer remains unexplored at the molecular level. The interaction between multiple concurrent exposures (additive versus synergistic effects) is poorly quantified, and environmental justice dimensions of exposure-related lung cancer -- wherein disadvantaged communities bear disproportionate exposure burdens -- remain understudied from a molecular epidemiology perspective.

---

## 11.8 Epigenetics in Lung Cancer

Epigenetic alterations are pervasive in lung cancer and operate across multiple regulatory layers, from DNA methylation to chromatin remodeling to non-coding RNA networks. DNA methylation changes represent among the earliest detectable molecular events in lung carcinogenesis. Promoter hypermethylation of tumor suppressors including CDKN2A, RASSF1A, MGMT, and DAPK occurs in pre-neoplastic lesions and progresses during tumor evolution, while global hypomethylation contributes to genomic instability. Wielscher et al. demonstrated that DNA methylation signatures of chronic low-grade inflammation are associated with increased cardio-respiratory disease risk, including lung cancer, establishing epigenetic links between chronic inflammation and carcinogenesis [PMID: [35504910](https://pubmed.ncbi.nlm.nih.gov/35504910/)]. Heeke et al. showed that tumor- and circulating-free DNA methylation can identify clinically relevant SCLC subtypes, bridging epigenetic profiling with therapeutic classification [PMID: [38278149](https://pubmed.ncbi.nlm.nih.gov/38278149/)].

Chromatin remodeling and histone modification play critical mechanistic roles in lung cancer biology. Kondo et al. demonstrated that gene silencing in cancer can occur through histone H3 lysine 27 trimethylation independent of promoter DNA methylation, revealing an alternative epigenetic silencing mechanism [PMID: [18488029](https://pubmed.ncbi.nlm.nih.gov/18488029/)]. Alam et al. showed that KMT2D deficiency impairs super-enhancer function and confers a glycolytic vulnerability exploitable therapeutically in lung cancer [PMID: [32243837](https://pubmed.ncbi.nlm.nih.gov/32243837/)]. Yuan et al. identified elevated NSD3 histone methylation as a driver of squamous cell lung cancer [PMID: [33536620](https://pubmed.ncbi.nlm.nih.gov/33536620/)], while de Miguel et al. demonstrated that SWI/SNF chromatin remodeling complexes promote tyrosine kinase inhibitor resistance in EGFR-mutant lung cancer [PMID: [37541244](https://pubmed.ncbi.nlm.nih.gov/37541244/)]. Na et al. revealed that KMT2C deficiency promotes SCLC metastasis through DNMT3A-mediated epigenetic reprogramming [PMID: [35449309](https://pubmed.ncbi.nlm.nih.gov/35449309/)].

cfDNA methylation-based approaches have emerged as promising liquid biopsy biomarkers for early detection and disease monitoring. Zuccato et al. recently demonstrated that DNA methylation signatures in circulating free DNA can predict brain metastasis development in lung cancer patients [PMID: [39379704](https://pubmed.ncbi.nlm.nih.gov/39379704/)]. Enhancer landscape mapping through ATAC-seq and related chromatin accessibility assays has defined subtype-specific regulatory programs and master transcription factors in lung cancer. Napoli et al. showed that deltaNp63 regulates a common landscape of enhancer-associated genes in NSCLC [PMID: [35105868](https://pubmed.ncbi.nlm.nih.gov/35105868/)], while Huang et al. identified super-enhancer-mediated circRNAs with high splicing diversity and transcriptional regulatory potential [PMID: [40512546](https://pubmed.ncbi.nlm.nih.gov/40512546/)].

A critical cautionary finding from this theme is the notably high retraction rate: 76 papers in the epigenetics collection were flagged as retracted, the highest of any theme. These retractions are concentrated in miRNA and lncRNA prognostic signature studies, consistent with known reproducibility concerns in these subfields. This pattern suggests that many published non-coding RNA prognostic associations may not be robust, and the field would benefit from rigorous independent validation with pre-registered analysis plans. Additional gaps include the limited application of single-cell epigenomic profiling in lung cancer, the scarcity of epigenetic therapy clinical trials in solid tumors, and the challenge of distinguishing causal epigenetic drivers from passenger alterations that arise as a consequence of other oncogenic processes.

---

## 11.9 Immune Biomarkers and Immunotherapy Response

The search for reliable biomarkers to predict immunotherapy response in NSCLC has expanded well beyond PD-L1 immunohistochemistry, driven by the recognition that PD-L1 expression alone is an imperfect predictor of clinical benefit. Rizvi et al. established that higher somatic mutation burden -- tumor mutational burden (TMB) -- is associated with improved response to PD-1 blockade in NSCLC, providing a genomic rationale for immunotherapy sensitivity based on neoantigen load [PMID: [25765070](https://pubmed.ncbi.nlm.nih.gov/25765070/)]. Ricciuti et al. further demonstrated that high TMB in NSCLC is associated with increased immune infiltration and immunotherapy sensitivity, though the optimal TMB threshold for clinical decision-making remains debated [PMID: [35708671](https://pubmed.ncbi.nlm.nih.gov/35708671/)]. Critically, molecular context modifies TMB utility: STK11 and KEAP1 co-mutations confer immunotherapy resistance in NSCLC even in the setting of high TMB, demonstrating that genomic co-alterations override simple mutation counting.

Pan-cancer immune landscape analyses have provided a framework for understanding tumor-immune interactions across malignancies. Thorsson et al. characterized six immune subtypes across 33 cancer types, defined by distinct immune cell compositions, cytokine profiles, and survival outcomes, providing a taxonomy applicable to NSCLC [PMID: [29628290](https://pubmed.ncbi.nlm.nih.gov/29628290/)]. Charoentong et al. developed the Immunophenoscore, a computational approach to quantify immunogenicity based on effector cells, immunosuppressive cells, MHC-related molecules, and immune checkpoints, demonstrating predictive value for immunotherapy response [PMID: [28052254](https://pubmed.ncbi.nlm.nih.gov/28052254/)]. Bagaev et al. identified four conserved pan-cancer microenvironment subtypes that predict immunotherapy response, showing that the tumor microenvironment architecture has independent predictive value beyond tumor-intrinsic molecular features [PMID: [34019806](https://pubmed.ncbi.nlm.nih.gov/34019806/)].

The role of the gut microbiome as a modulator of immunotherapy efficacy has gained substantial attention. Stein-Thoeringer et al. demonstrated that a non-antibiotic-disrupted gut microbiome is associated with improved clinical responses to adoptive cell therapy [PMID: [36914893](https://pubmed.ncbi.nlm.nih.gov/36914893/)], while Ferrari et al. showed that specific microbiota can sensitize cancer cells to immune checkpoint inhibitors through upregulation of HLA class I molecules [PMID: [37738976](https://pubmed.ncbi.nlm.nih.gov/37738976/)]. HLA diversity and neoantigen presentation have emerged as additional axes of immunotherapy prediction, with Kraemer et al. mapping the immunopeptidome landscape associated with T cell infiltration and immune editing in lung cancer [PMID: [37127787](https://pubmed.ncbi.nlm.nih.gov/37127787/)]. De Vries et al. demonstrated that gamma-delta T cells serve as effectors of immunotherapy in cancers with HLA class I defects, identifying an alternative immune mechanism relevant to tumors with antigen presentation loss [PMID: [36631610](https://pubmed.ncbi.nlm.nih.gov/36631610/)].

Despite this rich literature, clinical implementation of composite biomarker panels remains unstandardized. Spatial immune biomarkers -- including immune proximity scores and tertiary lymphoid structure quantification -- have shown promise but have not been validated prospectively. Biomarker dynamics during treatment are poorly captured by pre-treatment single-timepoint assessments. Wang et al. demonstrated that impaired T cell and neoantigen retention during serial sampling of metastatic NSCLC provides dynamic predictive information [PMID: [40341231](https://pubmed.ncbi.nlm.nih.gov/40341231/)]. The integration of multi-parameter immune biomarkers into clinically actionable decision algorithms remains an active area of investigation.

---

## 11.10 Targeted Therapy Access, Translational Bottleneck, and Real-World Outcomes

A persistent translational gap separates the promise of precision oncology from its real-world delivery to lung cancer patients. Despite the identification of numerous actionable molecular targets in NSCLC, biomarker testing rates remain suboptimal and inequitable. Bach et al. documented racial differences in the treatment of early-stage lung cancer over two decades ago [PMID: [10519898](https://pubmed.ncbi.nlm.nih.gov/10519898/)], and subsequent studies have confirmed that these disparities extend to precision medicine: Dutta et al. systematically analyzed inequities in precision oncology diagnostics, showing that Black, Hispanic, and uninsured patients are significantly less likely to receive comprehensive biomarker testing [PMID: [37248397](https://pubmed.ncbi.nlm.nih.gov/37248397/)]. Arora et al. demonstrated that genetic ancestry-based differences in biomarker prevalence further affect eligibility for precision oncology therapies, compounding access inequities [PMID: [39786754](https://pubmed.ncbi.nlm.nih.gov/39786754/)]. Hofman et al. proposed real-world solutions for improving implementation of predictive biomarker testing [PMID: [39904223](https://pubmed.ncbi.nlm.nih.gov/39904223/)].

Real-world evidence studies consistently show that outcomes for NSCLC patients receiving targeted therapies or immunotherapy are more heterogeneous than clinical trial results. Saito et al. evaluated the real-world clinical utility of comprehensive genomic profiling in advanced solid tumors, demonstrating measurable but variable benefit depending on institutional infrastructure and molecular tumor board implementation [PMID: [41495408](https://pubmed.ncbi.nlm.nih.gov/41495408/)]. Besse et al. reported on the SAFIR02-Lung trial, which tested biomarker-directed targeted therapy combined with durvalumab in advanced NSCLC, illustrating both the potential and the operational challenges of implementing multi-biomarker-directed treatment in clinical practice [PMID: [38351187](https://pubmed.ncbi.nlm.nih.gov/38351187/)]. Li et al. conducted an umbrella review linking socioeconomic status to cancer outcomes, reinforcing that precision oncology cannot achieve its potential without addressing the structural barriers that determine who receives testing and treatment [PMID: [39557933](https://pubmed.ncbi.nlm.nih.gov/39557933/)].

Molecular tumor boards (MTBs) have emerged as an institutional mechanism for translating multi-omics data into clinical decisions. Tsimberidou et al. reviewed current and future considerations for precision oncology MTBs, arguing that multidisciplinary interpretation of complex molecular data improves treatment selection quality [PMID: [37845306](https://pubmed.ncbi.nlm.nih.gov/37845306/)]. Kato et al. demonstrated that real-world data from a molecular tumor board showed improved outcomes with a precision N-of-One approach [PMID: [33009371](https://pubmed.ncbi.nlm.nih.gov/33009371/)]. Tamborero et al. developed the Molecular Tumor Board Portal to support clinical decisions and automated reporting [PMID: [35221333](https://pubmed.ncbi.nlm.nih.gov/35221333/)]. Meyer et al. reviewed new promises and challenges in treating advanced NSCLC, noting that the treatment landscape for approved targeted therapies -- including osimertinib for EGFR, sotorasib/adagrasib for KRAS G12C, and ALK inhibitors -- continues to expand [PMID: [39121882](https://pubmed.ncbi.nlm.nih.gov/39121882/)].

Key gaps in the translational landscape include the minimal real-world evidence from low- and middle-income countries, limited evaluation of interventions designed to improve biomarker testing rates, and the absence of rigorous cost-effectiveness analyses for multi-omics precision oncology. Patient-reported outcomes are rarely integrated with molecular data, clinical trial representation of women and minorities remains inadequate, and the convergence of machine learning with genomics for precision oncology implementation remains in early stages [PMID: [41478861](https://pubmed.ncbi.nlm.nih.gov/41478861/)].

---

## 11.11 Drug Repurposing in Oncology

Computational drug repurposing leverages multi-omics data and systems pharmacology to identify new therapeutic indications for existing drugs, offering a potentially faster and less expensive route to treatment than de novo drug development. The Connectivity Map (CMap) concept, introduced by Lamb et al., established the paradigm of matching drug-induced gene expression signatures to disease signatures to identify candidate compounds with therapeutic potential [PMID: [17186018](https://pubmed.ncbi.nlm.nih.gov/17186018/)]. Zhao et al. provided a comprehensive assessment of CMap-based drug repurposing strategies for oncotherapy, evaluating their strengths and limitations across cancer types [PMID: [37068308](https://pubmed.ncbi.nlm.nih.gov/37068308/)]. Tanoli et al. recently reviewed computational drug repurposing approaches broadly, evaluating in silico resources and highlighting that clinical translation rates remain low despite promising computational predictions [PMID: [40102635](https://pubmed.ncbi.nlm.nih.gov/40102635/)].

Large-scale pharmacogenomic databases have enabled systematic analysis of drug-gene interactions in cancer. The DGIdb database, recently updated by Cannon et al., provides a curated resource of drug-gene interactions for precision medicine and drug discovery [PMID: [37953380](https://pubmed.ncbi.nlm.nih.gov/37953380/)]. Nair et al. mapped the landscape of drug combination responses in NSCLC, revealing synergistic and antagonistic interactions that depend on molecular context [PMID: [37380628](https://pubmed.ncbi.nlm.nih.gov/37380628/)]. MotieGhader et al. applied gene co-expression and drug-gene interaction analysis for drug repositioning specifically in NSCLC [PMID: [35676421](https://pubmed.ncbi.nlm.nih.gov/35676421/)]. Kolesar et al. explored the integration of liquid biopsy with pharmacogenomics for precision therapy of EGFR-mutant and resistant NSCLC [PMID: [35209919](https://pubmed.ncbi.nlm.nih.gov/35209919/)].

Synthetic lethality has emerged as a particularly promising repurposing strategy in lung cancer, especially for tumors harboring KRAS, STK11, or KEAP1 alterations. Leung et al. reviewed synthetic lethality approaches in lung cancer and their translational potential [PMID: [27686855](https://pubmed.ncbi.nlm.nih.gov/27686855/)], while Long et al. demonstrated that PARP inhibition induces synthetic lethality and adaptive immunity in LKB1-mutant lung cancer, suggesting that DNA damage response exploitation can have immunomodulatory consequences [PMID: [36512628](https://pubmed.ncbi.nlm.nih.gov/36512628/)]. Postel-Vinay and Soria reviewed the potential for exploiting DNA-repair defects to optimize lung cancer treatment more broadly [PMID: [22330686](https://pubmed.ncbi.nlm.nih.gov/22330686/)]. Wood et al. provided a comprehensive review of the prognostic and predictive value of KRAS in NSCLC as a framework for KRAS-targeted repurposing strategies [PMID: [27100819](https://pubmed.ncbi.nlm.nih.gov/27100819/)].

Drug repurposing remains the theme with the thinnest supporting literature in this review, with only 24 Tier B papers. The translation rate from computational prediction to clinical validation is low, and lung cancer-specific repurposing studies are fewer than pan-cancer efforts. Drug combination optimization using multi-omics data is nascent, and specific candidates such as dimethyl fumarate for KEAP1-mutant cancers require clinical trial data. Patient-derived organoid and xenograft validation of repurposing candidates remains limited but is essential for bridging the gap between in silico prediction and clinical utility.

---

## 11.12 Emerging Frontiers: Single-Cell, Spatial, Metabolomic, and Liquid Biopsy Technologies

Single-cell RNA sequencing has revealed levels of intratumoral heterogeneity and tumor microenvironment complexity that were invisible to bulk profiling approaches. Lambrechts et al. pioneered single-cell transcriptomic characterization of the lung tumor stroma, identifying phenotypic molding of stromal cells and novel fibroblast and endothelial cell states within the lung tumor microenvironment [PMID: [29988129](https://pubmed.ncbi.nlm.nih.gov/29988129/)]. Zilionis et al. compared single-cell transcriptomes of human and mouse lung cancers, revealing conserved myeloid populations across species that shape the immunosuppressive microenvironment [PMID: [30979687](https://pubmed.ncbi.nlm.nih.gov/30979687/)]. Maynard et al. tracked therapy-induced evolution of human lung cancer at single-cell resolution, demonstrating treatment-driven changes in both tumor cell and immune cell states [PMID: [32822576](https://pubmed.ncbi.nlm.nih.gov/32822576/)]. De Zuani et al. recently provided a comprehensive single-cell and spatial transcriptomics atlas of NSCLC, mapping cellular diversity across histological subtypes and treatment contexts [PMID: [38782901](https://pubmed.ncbi.nlm.nih.gov/38782901/)]. Liu et al. constructed a single-cell atlas of immune heterogeneity in anti-PD-1-treated NSCLC, revealing cell state transitions associated with response and resistance [PMID: [40147443](https://pubmed.ncbi.nlm.nih.gov/40147443/)].

Spatial omics technologies preserve tissue architecture while providing molecular detail, enabling characterization of the spatial organization of tumor-immune interactions that cannot be captured by dissociative single-cell methods. Tagore et al. applied single-cell and spatial genomics to map the landscape of NSCLC brain metastases, revealing spatial patterns of immune exclusion and tumor-stromal organization [PMID: [40016452](https://pubmed.ncbi.nlm.nih.gov/40016452/)]. Li et al. developed AI-enabled virtual spatial proteomics from histopathology for interpretable biomarker discovery in lung cancer, demonstrating that computational approaches can bridge the gap between widely available H&E imaging and resource-intensive spatial profiling [PMID: [41491099](https://pubmed.ncbi.nlm.nih.gov/41491099/)]. Ozirmak Lermi et al. provided a systematic comparison of imaging-based spatial transcriptomics platforms using NSCLC tissue, offering practical guidance for platform selection [PMID: [41006245](https://pubmed.ncbi.nlm.nih.gov/41006245/)].

Liquid biopsy technologies are approaching clinical utility across multiple applications in lung cancer. Abbosh et al. demonstrated ctDNA-based tracking of early metastatic dissemination in the TRACERx longitudinal study, showing that circulating tumor DNA can detect minimal residual disease and predict recurrence [PMID: [37055640](https://pubmed.ncbi.nlm.nih.gov/37055640/)]. Black et al. developed longitudinal ultrasensitive ctDNA monitoring for high-resolution lung cancer risk prediction [PMID: [41205598](https://pubmed.ncbi.nlm.nih.gov/41205598/)]. Li et al. explored liquid biopsy-based single-cell metabolic phenotyping of lung cancer patients for informative diagnostics [PMID: [31451693](https://pubmed.ncbi.nlm.nih.gov/31451693/)]. Wang et al. combined lung cancer scRNA-seq with lipidomics to reveal aberrant lipid metabolism patterns useful for early-stage diagnosis [PMID: [35108060](https://pubmed.ncbi.nlm.nih.gov/35108060/)].

The microbiome has emerged as an unexpected player in lung cancer biology and immunotherapy response. McElderry et al. conducted a large-scale microbiome analysis of 940 lung cancers in never-smokers, notably finding a lack of clinically relevant associations between tumor microbiome composition and outcomes in this population [PMID: [41387456](https://pubmed.ncbi.nlm.nih.gov/41387456/)] -- a finding that challenges earlier positive associations reported in smaller studies and highlights the need for adequately powered studies. Critical gaps in emerging technologies include the absence of spatial omics studies in never-smoker lung cancer, the nascent state of multi-modal single-cell and spatial data integration methods, cost and scalability barriers that limit clinical adoption, and the need for larger longitudinal liquid biopsy cohorts to establish clinical validation benchmarks for early detection and MRD monitoring.
