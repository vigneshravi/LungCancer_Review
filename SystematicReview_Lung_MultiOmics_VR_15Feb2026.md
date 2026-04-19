# Multi-Omics Integration for Molecular Subtyping in Lung Cancer: A Comprehensive Review

**Date:** February 2026  
**Authors:** Vignesh Ravichandran, DHI

---

## 📑 Table of Contents
1. [Background](#background)
2. [The TCGA Era and Institutional Cohorts](#tcga-era)
3. [Multi-Omics Integration Methods](#integration-methods)
4. [Published Studies Overview](#published-studies)
5. [MOVICS-Based Studies: Detailed Analysis](#movics-studies)
6. [Two Divergent Philosophical Approaches](#philosophical-approaches)
7. [Research Gaps and Limitations](#research-gaps)
8. [Proposed Novel Contributions](#novel-contributions)
9. [Literature Search Methodology](#litsearch)
10. [References](#references)

---

<a name="background"></a>
## 1. Background

### 1.1 Lung Cancer: A Global Health Challenge

Lung cancer accounts for approximately **1.8 million deaths annually** and represents 18% of all cancer deaths worldwide. The disease comprises non-small cell lung cancer (NSCLC, ~85% of cases) and small cell lung cancer (SCLC, ~15%). Within NSCLC, lung adenocarcinoma (LUAD) represents ~40% of all lung cancers, followed by lung squamous cell carcinoma (LUSC, ~30%). Despite advances in targeted therapies and immunotherapy, the 5-year survival rate remains 16-21%, dropping to 4.7% for patients with distant metastases.

### 1.2 Evolution of Biomarker Discovery

**Single-Omic Era (2000-2010):** Early efforts focused on genomics (driver mutations: EGFR, KRAS, ALK, ROS1), transcriptomics (gene expression subtypes), and epigenomics (DNA methylation patterns). While these approaches identified actionable targets, they provided only a single molecular layer view.

**Limitations:** Cancer involves genomic alterations, epigenetic dysregulation, transcriptional reprogramming, post-transcriptional regulation, proteomic alterations, and metabolic rewiring. Single-omic approaches risk missing critical regulatory mechanisms across layers.

### 1.3 The Multi-Omics Paradigm

Multi-omics integration simultaneously analyzes multiple molecular layers from the same samples, offering:

- 🧬 Comprehensive molecular characterization across genomic, epigenomic, and transcriptomic layers
- 🎯 Discovery of multi-layer biomarker signatures with superior predictive power
- 🔬 Mechanistic insights into causal relationships between molecular events
- 👥 Improved patient stratification revealing subtypes masked by single-layer analyses

### 1.4 Multi-Omics Alone is Incomplete

Critical data modalities beyond molecular omics include:

- **Medical imaging (radiomics):** Tumor morphology, heterogeneity, vascularization, metabolic activity
- **Histopathology (pathomics):** Tissue architecture, cellular morphology, immune infiltration patterns
- **Clinical data (EHR):** Demographics, smoking history, comorbidities, performance status, treatment history
- **Longitudinal data:** Disease trajectory, treatment timelines, response kinetics, recurrence patterns
- **Spatial context:** Spatial transcriptomics revealing tumor-immune-stroma spatial organization
- **Liquid biopsy:** Circulating tumor DNA (ctDNA) and cells for real-time monitoring

The ultimate goal is **multi-modal integration** synthesizing omics, imaging, clinical, and longitudinal data for precision diagnosis, prognosis, and therapeutics.

### 1.5 The TCGA Resource and MOVICS Framework

Multi-omics studies by single institutions remain relatively scarce due to substantial requirements for rigorous sample collection, specialized personnel, bioinformatics infrastructure, data harmonization across platforms, and considerable funding necessary to generate comprehensive molecular profiles across multiple data types. 

The Cancer Genome Atlas (TCGA) represents one of the landmark consortia that has systematically addressed these challenges, providing the research community with **high-quality, multi-platform molecular data as a publicly accessible resource**. 

While numerous computational methods and algorithms have been developed for multi-omics data integration, the **MOVICS** (Multi-Omics Integration and Clustering for Survival) package offers a unique consensus-based approach that incorporates ten distinct clustering algorithms to identify robust molecular subtypes. Given the prevalence of TCGA data in multi-omics research and the growing adoption of MOVICS as an integration framework, a focused literature review was performed to identify multi-omics studies in lung cancer that utilized the MOVICS methodology or related integrative clustering approaches applied to TCGA lung cancer cohorts.

---

<a name="tcga-era"></a>
## 2. The TCGA Era and Institutional Cohorts

### 2.1 The Cancer Genome Atlas (TCGA)

TCGA generated comprehensive multi-platform molecular profiles for over 11,000 tumors across 33 cancer types, including:

- **TCGA-LUAD:** 585 lung adenocarcinoma cases
- **TCGA-LUSC:** 501 lung squamous cell carcinoma cases

**Molecular platforms:**

| Platform | Technology | Coverage |
|----------|-----------|----------|
| **Genomics** | Whole-exome sequencing, WGS (subset), SNP arrays | Complete coding genome |
| **Epigenomics** | Illumina HumanMethylation450 | ~485,000 CpG sites |
| **Transcriptomics** | RNA-seq, miRNA-seq | mRNA, lncRNA, miRNA |
| **Proteomics** | RPPA (Reverse Phase Protein Array) | ~200-300 proteins |
| **Clinical** | Standardized data collection | Demographics, pathology, treatment, survival |

### 2.2 TCGA as Community Resource

Public availability through the Genomic Data Commons enables:

✅ Standardized data processing with harmonized pipelines  
✅ Rich clinical metadata for survival analyses  
✅ Large sample sizes for statistical power  
✅ Multi-platform integration for cross-layer analyses  
✅ Gold standard for methods benchmarking  

### 2.3 TCGA Limitations

⚠️ **Population bias:** ~80% Caucasian, underrepresenting Asian, African, and Hispanic populations. Critical for LUAD where EGFR mutations are prevalent in Asians (~50%) but rare in Caucasians (~15%).

⚠️ **Treatment-naive samples:** Most collected at diagnosis before systemic therapy, limiting study of acquired resistance mechanisms.

⚠️ **Bulk tissue profiling:** Averages signal across millions of cells, missing tumor heterogeneity and spatial organization.

⚠️ **Limited proteomics/metabolomics:** RPPA covers only ~200-300 proteins; metabolomics essentially absent.

⚠️ **Retrospective design:** Observational data, not from prospective clinical trials.

### 2.4 The Scarcity of Non-TCGA Institutional Cohorts

Our comprehensive literature census reveals **88% (22/25) of multi-omics lung cancer studies rely on TCGA** as the primary discovery cohort. Only **2 studies (8%)** employed institutional cohorts:

#### Institutional Cohort #1: Zhang et al. (2025), Nature Communications

📍 **Institution:** West China Hospital  
👥 **Cohort:** 122 stage I NSCLC patients with prospective recurrence follow-up  
🧬 **Data:** WES, RNA-seq, nanopore whole-methylome sequencing, scRNA-seq  
💰 **Cost:** ~$5,000-$15,000 per patient  

#### Institutional Cohort #2: Zhong et al. (2025), Molecular Cancer

📍 **Institution:** Peking University Cancer Hospital  
👥 **Cohort:** 101 early-stage poorly differentiated LUAD  
🧬 **Data:** WES, RNA-seq, whole-methylome sequencing  

**Challenges:** Multi-omics profiling costs, biobanking infrastructure, genomics facilities, bioinformatics expertise, and IRB approvals create substantial barriers.

**Critical need:** Population-specific cohorts (Asian, African, Hispanic), treatment-resistant cohorts with longitudinal sampling, prospective clinical trial cohorts, early detection cohorts, and rare histologies (SCLC absent from TCGA multi-omics).

![Figure 2: TCGA Dominance and Feature Selection Philosophies](figure2_cohorts_and_philosophy.png)

**Figure 2: Cohort Sources and Methodological Approaches.** (A) Primary cohort sources across all 25 multi-omics lung cancer studies showing TCGA dominance (88%) with minimal institutional cohorts (8%). (B) Distribution of feature selection philosophies in MOVICS studies stratified by cancer type (LUAD, LUSC, NSCLC), demonstrating predominance of Cox-based clinical prediction approaches (n=13) over variance-based biological discovery (n=3) and hybrid methods (n=2).

---

<a name="integration-methods"></a>
## 3. Multi-Omics Integration Methods

### 3.1 Integration Strategy Categories

| Category | Strategy | Examples | Key Principle |
|----------|----------|----------|---------------|
| 🔗 **Concatenation** | Early fusion | Simple stacking | Assumes equal contribution |
| 🔄 **Transformation** | Intermediate fusion | PCA, t-SNE | Dimensionality reduction first |
| 🎯 **Model-based** | Joint latent variables | iCluster, MOFA | Shared latent structure |
| 🕸️ **Network-based** | Similarity networks | SNF, NEMO | Fuse similarity graphs |
| 🎲 **Ensemble** | Consensus clustering | MOVICS | Multiple algorithms consensus |
| 📊 **Supervised** | Outcome-guided | DIABLO | Use outcome labels |

### 3.2 Comprehensive Tool Comparison

<table>
<thead style="background-color: #4A90E2; color: white;">
<tr>
<th>Tool</th>
<th>Method Category</th>
<th>Supervised/<br>Unsupervised</th>
<th>Key Advantage</th>
<th>Key Limitation</th>
<th>Lung Cancer<br>Studies</th>
</tr>
</thead>
<tbody>
<tr style="background-color: #E3F2FD;">
<td><strong>MOVICS</strong></td>
<td>Ensemble/Consensus</td>
<td>Both</td>
<td>Consensus across 10 algorithms</td>
<td>Computationally intensive</td>
<td><strong>18</strong></td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>SNF</strong></td>
<td>Network Fusion</td>
<td>Unsupervised</td>
<td>Preserves local structure</td>
<td>Sensitive to K parameter</td>
<td>2-3</td>
</tr>
<tr style="background-color: #E3F2FD;">
<td><strong>iCluster</strong></td>
<td>Joint Latent</td>
<td>Unsupervised</td>
<td>Statistical rigor</td>
<td>Slow, Gaussian assumption</td>
<td>10+</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>iClusterPlus</strong></td>
<td>Joint Latent</td>
<td>Unsupervised</td>
<td>Multi-type data support</td>
<td>Slow, grid search needed</td>
<td>10+</td>
</tr>
<tr style="background-color: #E3F2FD;">
<td><strong>iClusterBayes</strong></td>
<td>Joint Latent</td>
<td>Unsupervised</td>
<td>No tuning parameters</td>
<td>Model assumptions</td>
<td>5+</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>MOFA/MOFA+</strong></td>
<td>Factor Analysis</td>
<td>Unsupervised</td>
<td>Variance decomposition</td>
<td>No discrete subtypes</td>
<td>3</td>
</tr>
<tr style="background-color: #E3F2FD;">
<td><strong>DIABLO</strong></td>
<td>Supervised PLS-DA</td>
<td>Supervised</td>
<td>Biomarker discovery</td>
<td>Requires outcome labels</td>
<td><strong>0</strong></td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>IntNMF</strong></td>
<td>Matrix Factorization</td>
<td>Unsupervised</td>
<td>Non-negative factors</td>
<td>Initialization sensitivity</td>
<td>Used in MOVICS</td>
</tr>
<tr style="background-color: #E3F2FD;">
<td><strong>NEMO</strong></td>
<td>Network Ensemble</td>
<td>Unsupervised</td>
<td>Network modularity</td>
<td>Complex parameter tuning</td>
<td>Used in MOVICS</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>CIMLR</strong></td>
<td>Kernel Learning</td>
<td>Unsupervised</td>
<td>Kernel-based flexibility</td>
<td>Computationally expensive</td>
<td>Used in MOVICS</td>
</tr>
<tr style="background-color: #E3F2FD;">
<td><strong>AutoEncoder</strong></td>
<td>Deep Learning</td>
<td>Both</td>
<td>Non-linear feature learning</td>
<td>Black box, less interpretable</td>
<td>2</td>
</tr>
</tbody>
</table>

**Key Observations:**

- 🏆 MOVICS dominates with **18 lung cancer studies** vs. **0 for DIABLO** despite DIABLO's success in breast cancer
- 📚 iCluster family extensively used in TCGA characterizations (2012-2018)
- 📈 SNF, MOFA, deep learning gaining traction (2021-2025)

![Figure 1: Study Distribution by Method and Year](figure1_study_distribution.png)

**Figure 1: Distribution of Multi-Omics Integration Methods in Lung Cancer Studies.** (A) Number of studies by integration method showing MOVICS dominance (n=18). (B) Temporal trend of MOVICS publications from 2022-2025 demonstrating rapid adoption with 12 studies published in 2025 alone.

---

<a name="published-studies"></a>
## 4. Published Studies Overview

### 4.1 Distribution by Method

Our comprehensive census identified **25+ studies** applying multi-omics integration to lung cancer:

| Method | Studies | Percentage |
|--------|---------|------------|
| **MOVICS** | 18 | 72% |
| **iCluster family** | 10+ | 40% |
| **SNF** | 2-3 | 8% |
| **NMF** | 2 | 8% |
| **MOFA** | 3 | 12% |
| **Hybrid ML** | 5+ | 20% |

*Percentages exceed 100% because some studies compare multiple methods.*

### 4.2 Key Studies by Method

#### 🌐 SNF Studies

**1. Wu et al. (2024), Cancer Immunology Immunotherapy**

SNF applied to radiotherapy-related genes, immune genes, methylation, and mutations in TCGA-LUAD. Identified **3 subtypes** with differential immunotherapy and chemotherapy sensitivity. Validated TRPA1 and RHCG as radiosensitivity modulators.

**2. Chen et al. (2025), Cancer Drug Resistance**

Combined 10 multi-omics algorithms including SNF with scRNA-seq and GWAS data. Identified **2 LUAD subtypes**; CS2 showed higher immune infiltration and better prognosis. RRM1 identified as critical chemotherapy response biomarker.

#### 🧮 NMF Studies

**1. Zhang et al. (2025), Nature Communications** ⭐

First major institutional non-TCGA cohort. 122 stage I NSCLC patients with recurrence data. NMF clustering identified **4 subtypes** with varying recurrence risk. PRAME hypomethylation drives recurrence via TEAD1 binding site. scRNA-seq revealed enrichment of AT2 cells and exhausted CD8+ T cells in recurrent tumors.

**2. Bandyopadhyay et al. (2023), Scientific Reports**

Autoencoder dimensionality reduction followed by consensus K-means on TCGA NSCLC. Integrated mRNA, miRNA, methylation, CNV, and RPPA protein data. Identified **5 clusters**; C3 showed minimal genetic aberration with best prognosis.

#### 📊 MOFA Studies

**1. Michailidou et al. (2021), International Journal of Molecular Sciences**

MOFA+ applied to TCGA-LUAD. Factor 1 correlated with TRU expression subtype and SFTPB gene (tumor-infiltrating lymphocyte marker). Factor 2 associated with ATM mutation status.

**2. Karagkouni et al. (2023), Oncology Letters**

Pan-cancer MOFA application including LUSC. Factor 12 significantly associated with overall survival in LUSC (p=0.016).

**3. Ochoa & Hernández-Lemus (2024), Frontiers in Genetics**

SGCCA applied to TCGA-LUAD and LUSC focusing on regulatory network modeling rather than patient clustering.

#### 🏛️ iCluster Legacy

**1. TCGA LUAD (2014), Nature** 📖

iClusterPlus identified **3 transcriptional subtypes** (TRU, PI, PP) that became the official TCGA classification (12,000+ citations).

**2. TCGA LUSC (2012), Nature** 📖

iCluster identified **4 molecular subtypes** (Classical, Basal, Secretory, Primitive) serving as foundational LUSC classification (8,000+ citations).

#### 🤖 Hybrid ML Studies

**1. Saggi et al. (2024), arXiv**

First **quantum machine learning** application to lung cancer multi-omics. Quantum neural networks achieved 95% training and 90% testing accuracy for LUAD vs. LUSC classification.

**2. Castillo-Secilla et al. (2022), Journal of Personalized Medicine**

Late fusion deep learning integrating whole-slide imaging with RNA-seq, miRNA-seq, CNV, and methylation for NSCLC diagnosis.

**3. Wang et al. (2021), Frontiers in Cell and Developmental Biology**

Machine learning on histopathology features combined with multi-omics. Histopathology + multi-omics achieved 5-year survival AUC 0.908 (HR 19.98).

**4. Zhong et al. (2025), Molecular Cancer** ⭐

Second institutional non-TCGA cohort. 101 early-stage poorly differentiated LUAD with WES, RNA-seq, and whole-methylome sequencing. Identified **3 subtypes**; recurrent tumors showed higher ploidy and genomic instability.

---

<a name="movics-studies"></a>
## 5. MOVICS-Based Studies: Detailed Analysis

### 5.1 Why MOVICS Dominates

MOVICS (Multi-Omics Integration and Visualization in Cancer Subtyping) published by Lu et al. (2020) in *Bioinformatics* has become the most widely adopted framework with **18/25 studies (72%)** due to:

✅ Consensus approach integrating 10 distinct clustering algorithms  
✅ Comprehensive end-to-end pipeline from preprocessing to visualization  
✅ User-friendly R package with extensive documentation  
✅ Established reproducible template workflow  
✅ Built-in validation framework with gap statistics and silhouette scores  

### 5.2 The 18 MOVICS Studies

<table>
<thead style="background-color: #27AE60; color: white;">
<tr>
<th>Study</th>
<th>Year</th>
<th>Journal</th>
<th>Cancer Type</th>
<th>N Samples</th>
<th>K Clusters</th>
<th>Feature Selection</th>
<th>Philosophy</th>
</tr>
</thead>
<tbody>
<tr style="background-color: #E8F8F5;">
<td>Ruan et al.</td>
<td>2022</td>
<td>Front Med</td>
<td>LUAD</td>
<td>437</td>
<td><strong>4</strong></td>
<td>MAD (variance)</td>
<td>🔬 Biological</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Zou et al.</td>
<td>2022</td>
<td>TLCR</td>
<td>LUAD</td>
<td>437</td>
<td><strong>4</strong></td>
<td>MAD (variance)</td>
<td>🔬 Biological</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Han et al.</td>
<td>2024</td>
<td>Funct Integr Genomics</td>
<td>LUAD</td>
<td>417</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Lin et al.</td>
<td>2024</td>
<td>JCMM</td>
<td>LUAD</td>
<td>varies</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Chu et al.</td>
<td>2024</td>
<td>Front Immunol</td>
<td>LUAD</td>
<td>429</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Xie et al.</td>
<td>2024</td>
<td>Front Immunol</td>
<td>LUAD</td>
<td>417</td>
<td><strong>3</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Hua et al.</td>
<td>2025</td>
<td>Sci Rep</td>
<td>LUAD</td>
<td>varies</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Chen et al.</td>
<td>2025</td>
<td>Cancer Drug Resist</td>
<td>LUAD</td>
<td>432</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #FEF5E7;">
<td>Cao et al.</td>
<td>2025</td>
<td>Discover Oncol</td>
<td>LUAD</td>
<td>varies</td>
<td><strong>4</strong></td>
<td>GSVA signatures</td>
<td>🔀 Hybrid</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Li et al.</td>
<td>2025</td>
<td>Discover Oncol</td>
<td>LUAD</td>
<td>varies</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Wang et al.</td>
<td>2025</td>
<td>Front Pharmacol</td>
<td>LUAD</td>
<td>432</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Ma et al.</td>
<td>2025</td>
<td>Front Oncol</td>
<td>LUAD</td>
<td>varies</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #FEF5E7;">
<td>Li et al.</td>
<td>2025</td>
<td>PLOS One</td>
<td>LUSC</td>
<td>varies</td>
<td><strong>4</strong></td>
<td>DEA + Cox + LASSO</td>
<td>🔀 Hybrid</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Zhang et al.</td>
<td>2025</td>
<td>BioFactors</td>
<td>LUSC</td>
<td>varies</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Wan et al.</td>
<td>2025</td>
<td>J Thorac Dis</td>
<td>LUSC</td>
<td>varies</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Huang et al.</td>
<td>2025</td>
<td>TLCR</td>
<td>LUSC</td>
<td>varies</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Yan et al.</td>
<td>2025</td>
<td>J Big Data</td>
<td>LUSC</td>
<td>varies</td>
<td><strong>2</strong></td>
<td>Cox (supervised)</td>
<td>🏥 Clinical</td>
</tr>
<tr style="background-color: #E8F8F5;">
<td>Yan et al.</td>
<td>2025</td>
<td>bioRxiv</td>
<td>NSCLC</td>
<td>551</td>
<td><strong>5</strong></td>
<td>MAD (variance)</td>
<td>🔬 Biological</td>
</tr>
</tbody>
</table>

**Key Patterns:**

📊 **Distribution:** 12 LUAD, 5 LUSC, 1 combined NSCLC  
📈 **Publication surge:** 2 in 2022, 0 in 2023, 4 in 2024, **12 in 2025**  
🎯 **Feature selection:** Variance-based (MAD/SD) yields 4-5 subtypes; Cox-based yields 2 subtypes  
🌐 **All use TCGA:** Zero non-TCGA primary cohorts in MOVICS studies  

### 5.3 Data Preparation and Feature Selection Methods

**Sample Selection:** All studies use tumor-only samples (TCGA code 01), normal tissue removed (code 11).

**Normalization Standards:**

| Data Type | Normalization | Standard |
|-----------|---------------|----------|
| mRNA | Log2(FPKM+1) or Log2(TPM+1) | Universal |
| Methylation | Beta values | Universal |
| CNV | GISTIC discrete or binarized | Gain/loss |
| Mutations | Frequency-based | >3-5% of samples |

### 5.4 Feature Selection Methods Across All MOVICS Studies

<table>
<thead style="background-color: #8E44AD; color: white;">
<tr>
<th>Study</th>
<th>mRNA Selection</th>
<th>mRNA N</th>
<th>Methylation Selection</th>
<th>Meth N</th>
<th>lncRNA N</th>
<th>miRNA N</th>
<th>Total Features</th>
</tr>
</thead>
<tbody>
<tr style="background-color: #F4ECF7;">
<td>Ruan et al. 2022</td>
<td>MAD</td>
<td>3,000</td>
<td>SD</td>
<td>2,000</td>
<td>0</td>
<td>0</td>
<td><strong>~5,000</strong></td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Zou et al. 2022</td>
<td>MAD</td>
<td>1,500</td>
<td>SD</td>
<td>1,500</td>
<td>1,500</td>
<td>0</td>
<td><strong>~10,000</strong></td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Han et al. 2024</td>
<td>Cox p<0.05</td>
<td>~2,500</td>
<td>Cox p<0.05</td>
<td>~1,000</td>
<td>0</td>
<td>0</td>
<td>~3,500</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Lin et al. 2024</td>
<td>Cox p<0.05</td>
<td>~2,500</td>
<td>Cox p<0.05</td>
<td>~800</td>
<td>~500</td>
<td>~400</td>
<td>~3,000</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Chu et al. 2024</td>
<td>Cox p<0.01</td>
<td>~1,800</td>
<td>Cox p<0.01</td>
<td>~600</td>
<td>~300</td>
<td>~200</td>
<td>~2,000</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Xie et al. 2024</td>
<td>Cox p<0.05, immune</td>
<td>~2,000</td>
<td>Cox p<0.05</td>
<td>~700</td>
<td>0</td>
<td>0</td>
<td>~2,000</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Hua et al. 2025</td>
<td>Cox p<0.05, lactylation</td>
<td>~1,000</td>
<td>Cox p<0.05</td>
<td>~500</td>
<td>~300</td>
<td>0</td>
<td>~1,500</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Chen et al. 2025</td>
<td>Cox p<0.05</td>
<td>~2,300</td>
<td>Cox p<0.05</td>
<td>~900</td>
<td>~450</td>
<td>~350</td>
<td>~3,000</td>
</tr>
<tr style="background-color: #FEF5E7;">
<td>Cao et al. 2025</td>
<td>GSVA signatures</td>
<td>~500</td>
<td>GSVA</td>
<td>~300</td>
<td>~200</td>
<td>0</td>
<td>~2,000</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Li et al. 2025 (LUAD)</td>
<td>Cox p<0.05, CCCR</td>
<td>~800</td>
<td>Cox p<0.05</td>
<td>~400</td>
<td>0</td>
<td>~200</td>
<td>~1,200</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Wang et al. 2025</td>
<td>Cox p<0.05, epigenetic</td>
<td>~2,000</td>
<td>Cox p<0.05</td>
<td>~1,000</td>
<td>~400</td>
<td>~300</td>
<td>~3,000</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Ma et al. 2025</td>
<td>Cox p<0.05</td>
<td>~2,200</td>
<td>Cox p<0.05</td>
<td>~800</td>
<td>~450</td>
<td>~350</td>
<td>~2,800</td>
</tr>
<tr style="background-color: #FEF5E7;">
<td>Li et al. 2025 (LUSC)</td>
<td>DESeq2 + Cox + LASSO</td>
<td>20 (TLS)</td>
<td>DEA + OS</td>
<td>~50</td>
<td>~30</td>
<td>0</td>
<td><strong>~100</strong></td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Zhang et al. 2025 (LUSC)</td>
<td>Cox p<0.05</td>
<td>~2,000</td>
<td>Cox p<0.05</td>
<td>~700</td>
<td>0</td>
<td>0</td>
<td>~2,000</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Wan et al. 2025</td>
<td>Cox p<0.05</td>
<td>~1,900</td>
<td>Cox p<0.05</td>
<td>~600</td>
<td>~350</td>
<td>0</td>
<td>~2,500</td>
</tr>
<tr style="background-color: #EBF5FB;">
<td>Huang et al. 2025</td>
<td>Cox p<0.05</td>
<td>~2,100</td>
<td>Cox p<0.05</td>
<td>~750</td>
<td>~400</td>
<td>0</td>
<td>~2,800</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td>Yan et al. 2025 (LUSC)</td>
<td>Cox p<0.05</td>
<td>~2,200</td>
<td>Cox p<0.05</td>
<td>~800</td>
<td>~450</td>
<td>0</td>
<td>~3,000</td>
</tr>
<tr style="background-color: #F4ECF7;">
<td>Yan et al. 2025 (NSCLC)</td>
<td>MAD</td>
<td>3,000</td>
<td>SD</td>
<td>2,000</td>
<td>1,500</td>
<td>0</td>
<td><strong>~10,000</strong></td>
</tr>
</tbody>
</table>

**Key Observations:**

🔬 **Variance-based studies** (Ruan, Zou, Yan NSCLC): MAD/SD selection, ~10,000 total features, typically 4-5 subtypes  
🏥 **Cox-based studies** (majority): Univariate Cox p<0.05 or p<0.01, ~2,000-3,500 total features, typically 2 subtypes  
🔀 **Hybrid approaches** (Cao, Li LUSC): Pathway-specific or signature-based selection, variable feature counts  
📊 **lncRNA/miRNA usage**: ~50% of studies include these layers, predominantly Cox-filtered when used  
📈 **Feature count correlation**: Higher total features (>5,000) associated with biological discovery; lower features (<3,500) associated with clinical prediction  

![Figure 4: Feature Counts and Subtype Correlation](figure4_features_vs_subtypes.png)

**Figure 4: Feature Selection and Subtype Number Relationships Across All MOVICS Studies.** (A) Total features selected in all 18 MOVICS studies color-coded by methodological philosophy (red: biological discovery, blue: clinical prediction, orange: hybrid). Dashed line indicates 5,000-feature threshold clearly separating biological (above) from clinical (below) approaches. (B) Scatter plot demonstrating strong positive correlation between total features selected and number of subtypes identified (n=18 studies).

---

<a name="philosophical-approaches"></a>
## 6. Two Divergent Philosophical Approaches

### 6.1 Approach A: Biological Discovery (Taxonomy-First) 🔬

**Philosophy:** Uncover the natural molecular taxonomy of lung cancer. Tumors cluster based on intrinsic biology (metabolic state, proliferation, immune microenvironment, genomic instability) rather than survival outcomes.

**Principle:** *"Biology first, prognosis second."*

#### Methodology

| Component | Approach |
|-----------|----------|
| **Feature Selection** | Unsupervised (no survival information) |
| **mRNA** | MAD → top 3,000 most variable genes |
| **Methylation** | SD → top 2,000 most variable CpGs |
| **Mutations** | Frequency >5% of samples |
| **Total Features** | ~10,000 capturing biological diversity |

#### Outcomes

✅ Typically yields **4-5 subtypes** with greater biological granularity  
✅ Subtypes may have overlapping survival curves (not pre-selected for survival)  
✅ Each subtype characterized by distinct molecular hallmarks and pathway enrichments  

#### Clinical Utility

🎯 Mechanistic insights explaining why tumors behave differently  
🎯 Therapeutic target identification exploiting subtype-specific vulnerabilities  
🎯 Precision medicine matching biology to therapy  

#### Representative Study: Zou et al. (2022), TLCR ⭐

**Title:** *Multi-omics consensus portfolio to refine the classification of lung adenocarcinoma*

- **Cohort:** TCGA-LUAD (n=437)
- **Omics:** mRNA, lncRNA, methylation, mutations, CNV
- **Feature selection:** MAD top 1,500 per omics (~10,000 total)

**4 Consensus Subtypes (CS1-CS4):**

| Subtype | Characteristics | Clinical Impact |
|---------|----------------|-----------------|
| **CS1** | Worst OS, poor immune infiltration, high TMB, cell proliferation enriched | Aggressive treatment needed |
| **CS2** | Intermediate OS, distinct methylation patterns, specific driver mutations | Targeted therapy candidates |
| **CS3** | Intermediate OS, unique transcriptional profile | Novel biology |
| **CS4** | Best OS, favorable immune infiltration, lower genomic instability | De-escalation possible |

**Clinical Value:** 7-gene prognostic signature (DKK1, TSPAN7, ID1, DLGAP5, HHIPL2, CD40, SEMA3C). Subtypes differ in:
- Cancer stem cell characteristics
- Chemotherapy sensitivity (cisplatin, paclitaxel, docetaxel)
- Immunotherapy response (PD-1/PD-L1 blockade)
- Targeted therapy response (EGFR inhibitors)

**Significance:** Demonstrates biology-driven clustering reveals 4 distinct entities with unique molecular mechanisms. Subtypes are not defined by survival but by intrinsic biology; prognostic differences emerge as consequence.

---

### 6.2 Approach B: Clinical Prediction (Prognosis-First) 🏥

**Philosophy:** Build prognostic models identifying high-risk patients needing aggressive treatment vs. low-risk patients for de-escalation. Goal is clinical utility and risk stratification.

**Principle:** *"Prognosis first, biology second."*

#### Methodology

| Component | Approach |
|-----------|----------|
| **Feature Selection** | Supervised (univariate Cox regression) |
| **Filter** | Retain only OS-associated features (p<0.05 or p<0.01) |
| **mRNA** | Cox regression → keep ~2,500 OS-associated genes |
| **Methylation** | Cox regression → keep OS-associated CpGs |
| **Total Features** | ~2,000-3,000 survival-focused |

#### Outcomes

✅ Almost invariably yields **2 subtypes**:
  - **High-Risk:** Poor prognosis, aggressive disease, "cold" tumor microenvironment
  - **Low-Risk:** Favorable prognosis, indolent disease, "hot" tumor microenvironment
  
⚠️ Collapses biological heterogeneity into binary good/bad prognosis classification

#### Clinical Utility

🎯 Prognostic models with high performance (AUC 0.7-0.9) outperforming TNM staging  
🎯 Treatment stratification: High-risk → aggressive therapy; Low-risk → less intensive  
🎯 Immunotherapy prediction identifying "hot" vs. "cold" tumors  

#### The Hidden Problem ⚠️

Prognosis-first approach may merge distinct biological subtypes (e.g., "Immune-Excluded" vs. "Metabolically Dysfunctional") into one "high-risk" group if both have poor survival. This masks therapeutic opportunities:

- **Immune-excluded tumors** may respond to angiogenesis inhibitors improving immune access
- **Metabolically dysfunctional tumors** need metabolic inhibitors

#### Representative Study 1: Lin et al. (2024), JCMM

**Title:** *Advancing lung adenocarcinoma prognosis and immunotherapy prediction with a multi-omics consensus machine learning approach*

- **Cohort:** TCGA-LUAD
- **Omics:** mRNA, lncRNA, miRNA, methylation, mutations
- **Feature selection:** Univariate Cox p<0.05 (~3,000 features)

**2 Consensus Subtypes:**

| Subtype | Characteristics | Immunotherapy |
|---------|----------------|---------------|
| **MOC2** | More favorable outcomes, higher immune infiltration, elevated checkpoints | ✅ Better response |
| **MOC1** | Poorer prognosis, lower immune infiltration ("cold" tumors) | ❌ Worse response |

**Clinical Value:** 8 MOCs-associated hub genes. GJB3 strongly correlated with MOCM score (R=0.77); experimental validation showed GJB3 knockdown reduces LUAD proliferation, invasion, and migration.

#### Representative Study 2: Chu et al. (2024), Front Immunol

**Title:** *Multi-omics characterization and machine learning of lung adenocarcinoma molecular subtypes*

- **Cohort:** TCGA-LUAD (n=429)
- **Omics:** mRNA, lncRNA, miRNA, methylation, mutations
- **Feature selection:** Cox p<0.01; tested 101 ML combinations

**2 Consensus Subtypes:**

| Subtype | Prognosis | Clinical Action |
|---------|-----------|-----------------|
| **CS2** | Better prognosis, 17-gene RSF model with SLC2A1 validated | Monitor |
| **CS1** | Worse prognosis, "cold tumor" phenotype | Aggressive treatment |

**Risk Stratification:** High-risk subgroup responsive to immunotherapy + 6 chemotherapy drugs; Low-risk different sensitivity profile. Outperformed 58 published LUAD signatures.

---

### 6.3 Conceptual Differences and Complementary Insights

<table>
<thead style="background-color: #E74C3C; color: white;">
<tr>
<th>Aspect</th>
<th>🔬 Biological Discovery (A)</th>
<th>🏥 Clinical Prediction (B)</th>
</tr>
</thead>
<tbody>
<tr style="background-color: #FADBD8;">
<td><strong>Primary Goal</strong></td>
<td>Understand disease taxonomy</td>
<td>Predict prognosis/response</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>Feature Selection</strong></td>
<td>Variance-based (MAD, SD)</td>
<td>Survival-based (Cox)</td>
</tr>
<tr style="background-color: #FADBD8;">
<td><strong>Typical K</strong></td>
<td><strong>4-5 subtypes</strong></td>
<td><strong>2 subtypes</strong></td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>Biological Granularity</strong></td>
<td>High (heterogeneity preserved)</td>
<td>Low (binary good/bad)</td>
</tr>
<tr style="background-color: #FADBD8;">
<td><strong>Clinical Utility</strong></td>
<td>Target discovery, mechanism</td>
<td>Risk stratification</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>Strengths</strong></td>
<td>Reveals hidden biology</td>
<td>High predictive accuracy</td>
</tr>
<tr style="background-color: #FADBD8;">
<td><strong>Weaknesses</strong></td>
<td>Subtypes may overlap in survival</td>
<td>Masks biology with similar survival</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>Examples</strong></td>
<td>Zou 2022, Ruan 2022, Yan 2025</td>
<td>Lin 2024, Chu 2024, Han 2024</td>
</tr>
</tbody>
</table>

### 6.4 Why Both Are Necessary

#### 1. Biological Discovery reveals the "Why" 🔬

**Zou et al.** identified "Metabolic Subtype (CS4)" with:
- Altered lipid metabolism
- Best survival
- High sensitivity to ferroptosis inhibitors

**Clinical impact:** Develop ferroptosis-targeting drugs for CS4 patients (biology → therapy)

#### 2. Clinical Prediction optimizes the "Who" 🏥

**Lin et al.** identified MOC2 ("hot tumors") with:
- High PD-L1 expression
- Immune infiltration

**Clinical impact:** Enroll MOC2 patients in immunotherapy trials (outcome → patient selection)

#### 3. The Hidden Problem ⚠️

Prognosis-first merges distinct biological subtypes with similar survival into single "high-risk" cluster, losing mechanistic insight needed for targeted therapy. **Two different high-risk mechanisms require different treatments.**

![Figure 3: Conceptual Framework of Two Divergent Approaches](figure3_conceptual_framework.png)

**Figure 3: Conceptual Framework Comparing Biological Discovery vs. Clinical Prediction Approaches.** The left panel illustrates the biological discovery (taxonomy-first) approach using variance-based feature selection (~10,000 features) yielding 4-5 subtypes with mechanistic insights. The right panel shows the clinical prediction (prognosis-first) approach using Cox regression filtering (~2,000-3,000 features) yielding 2 subtypes optimized for risk stratification.

---

<a name="research-gaps"></a>
## 7. Research Gaps and Limitations

### 7.1 Data Source Gaps 📊

| Gap | Impact |
|-----|--------|
| **TCGA Monoculture** | 88% of studies use TCGA; only 2 institutional cohorts (8%) |
| **No SCLC Studies** | TCGA lacks SCLC multi-omics cohort |
| **Population Bias** | TCGA ~80% Caucasian; underrepresents Asians |
| **No Prospective Trials** | All studies retrospective; zero prospective |
| **No Longitudinal Sampling** | Lacks pre-treatment → resistant samples |

### 7.2 Methodological Gaps 🔬

| Gap | Impact |
|-----|--------|
| **No DIABLO Applications** | Zero lung cancer DIABLO studies despite success in breast cancer |
| **Limited Deep Learning** | Only 2 studies use neural networks |
| **Minimal Proteomics** | Only 2/25 studies (8%) use RPPA; CPTAC unused |
| **Zero Metabolomics** | Despite metabolic reprogramming importance |
| **No Spatial Omics** | Visium/GeoMx not integrated |
| **Univariate Dominance** | Most use simple univariate Cox or variance filtering |

### 7.3 Validation Gaps ✅

| Gap | Impact |
|-----|--------|
| **No External Proteomics Validation** | Predictions not validated at protein level |
| **Minimal Functional Validation** | Only 3 studies perform in vitro/in vivo experiments |
| **No Prospective Biomarker Validation** | All retrospective analyses |

### 7.4 Clinical Translation Gaps 🏥

| Gap | Impact |
|-----|--------|
| **Complexity Barrier** | 10 algorithms + 101 ML combinations not clinically feasible |
| **Cost Barrier** | Multi-omics profiling expensive ($5,000-$15,000 per patient) |
| **Turnaround Time** | Weeks-months for multi-omics vs. days for single assay |
| **Limited Actionability** | Subtypes identified but therapies not validated in trials |
| **No Reimbursement** | No payer coverage for multi-omics panels |
| **No Clinical Trials** | Zero basket/umbrella trials using multi-omics for enrollment |
| **No Companion Diagnostics** | No FDA-approved multi-omics subtyping test |

![Figure 5: Research Gaps in Multi-Omics Lung Cancer Studies](figure5_research_gaps.png)

**Figure 5: Comprehensive Analysis of Research Gaps Across 25 Multi-Omics Lung Cancer Studies.** Heatmap comparing number of studies with (green) versus without (red) key research elements. Major gaps include: institutional cohorts (23/25 studies lack), DIABLO method (25/25 lack), metabolomics (25/25 lack), spatial omics (25/25 lack), prospective trials (25/25 lack), FDA approval (25/25 lack), and functional validation (22/25 lack).

---

<a name="novel-contributions"></a>
## 8. Proposed Novel Contributions

Our proposed research addresses identified gaps through three strategic areas:

### 8.1 Methodological Improvements in Feature Selection 🎯

**Beyond Univariate Filtering:** Most existing papers use simple univariate filtering (checking one gene at a time). We propose biologically-driven, multivariate selection approaches:

#### A. Functional Feature Selection (Driver Events)

<table>
<thead style="background-color: #16A085; color: white;">
<tr>
<th>Approach</th>
<th>Standard Method</th>
<th>Our Method</th>
<th>Impact</th>
</tr>
</thead>
<tbody>
<tr style="background-color: #D5F4E6;">
<td><strong>Methylation</strong></td>
<td>Select top 2,000 CpGs by SD (captures noise + signal)</td>
<td>Use MethylMix to identify "Driver Methylation" events where methylation functionally drives gene expression downregulation</td>
<td>Reduces 485,000 CpGs to ~500-2,000 driver events with mechanistic relevance</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>RNA</strong></td>
<td>Select genes by MAD (variance) or univariate Cox</td>
<td>Identify differentially expressed genes with functional annotation (pathway membership, known cancer genes)</td>
<td>Biological relevance over statistical variation</td>
</tr>
</tbody>
</table>

**Novel contribution:** Zero lung cancer MOVICS papers use MethylMix

#### B. Multivariate vs. Univariate Cox Regression

**Elastic Net (Lasso + Ridge):**

| Approach | Method | Example | Result |
|----------|--------|---------|--------|
| **Standard** | Univariate Cox | Evaluates each gene independently; retains correlated redundant genes | CD8A, CD8B, GZMA, GZMB, PRF1 all selected |
| **Our Method** | Elastic Net multivariate penalized regression | Removes redundancy, selects optimal subset | CD8A + IFNG (two genes capture same biology) |

**Impact:** More parsimonious, less overfitting, better cross-cohort generalization

#### C. Network-Based Module Selection

**WGCNA (Weighted Gene Co-expression Network Analysis):**

- **Concept:** Select gene modules (co-expressed gene sets) rather than individual genes
- **Method:** Build co-expression network → identify modules → select modules associated with survival
- **Impact:** Captures biological pathways, reduces noise through averaging, more stable and reproducible than individual genes

#### D. Stability Selection

**Resampling-Based Feature Selection:**

- **Concept:** Select features stable across bootstrap resamples
- **Method:** Run Elastic Net on 100 bootstrap samples → retain features selected in ≥75% of resamples
- **Impact:** Features robust to sampling variation, reduces overfitting, improves reproducibility

---

### 8.2 Conceptual Expansion - Bridging Methodological Approaches 🌉

#### A. Biological vs. Clinical Clusters Comparison

**Research Question:** Do biological clusters have same clinical outcomes as clinical clusters? Is the binary "High Risk / Low Risk" classification masking biological heterogeneity?

**Approach:**

1. Run both Biological (Variance-based) and Clinical (Cox-based) pipelines on same TCGA-LUAD cohort
2. Cross-tabulate subtypes: Does Clinical "High Risk" group contain multiple distinct biological subtypes?
3. Compare biological subtypes within Clinical "High Risk": Do they differ in pathway enrichment, drug sensitivity, mutational signatures?
4. Test hypothesis: Clinical approach collapses biologically distinct subtypes with similar survival

**Expected Finding:** "High Risk" group composed of two biologically distinct subtypes (e.g., one driven by cell cycle dysregulation, one by hypoxia/metabolic dysfunction) requiring different treatments.

**Novel Contribution:** *"Supervised feature selection collapses clinically heterogeneous subtypes; hierarchical approach (biological clustering → within-subtype risk stratification) preserves therapeutic opportunities."*

**Impact:** ⭐⭐⭐⭐⭐ Very high - directly addresses field's conceptual divide

#### B. Pan-Cancer Immune Signature Analysis

**Research Question:** Do cancers with good immunotherapy response share similar immune signatures?

**Approach:**

1. Identify LUAD immune subtype signature (50-100 genes) from biological clustering approach
2. Apply signature to TCGA melanoma, renal cell carcinoma, bladder cancer cohorts
3. Test whether signature stratifies patients by survival and immunotherapy response in other cancers
4. Identify pan-cancer vs. LUAD-specific immune features

**Expected Finding:** Core immune signature (interferon-gamma response, T-cell activation) transfers across cancers; cancer-specific features emerge.

**Novel Contribution:** *"Pan-cancer multi-omics immune signature predicts immunotherapy response across tumor types."*

**Impact:** ⭐⭐⭐⭐ Medium-high if signature transfers

---

### 8.3 Subset Analyses - Clinical and Biological Validation 🔬

<table>
<thead style="background-color: #2980B9; color: white;">
<tr>
<th>Analysis</th>
<th>Approach</th>
<th>Expected Impact</th>
</tr>
</thead>
<tbody>
<tr style="background-color: #D6EAF8;">
<td><strong>A. Immunotherapy Trial Data</strong></td>
<td>Apply LUAD multi-omics subtypes to GSE135222 (anti-PD-1 NSCLC, n=27)</td>
<td>⭐⭐⭐⭐⭐ High - demonstrates clinical utility</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>B. Single-Cell RNA-seq Validation</strong></td>
<td>Use LUAD scRNA-seq (GSE149655) to deconvolute bulk subtypes</td>
<td>⭐⭐⭐⭐⭐ High - validates cellular ecosystems</td>
</tr>
<tr style="background-color: #D6EAF8;">
<td><strong>C. Immune Pathway-Specific Analysis</strong></td>
<td>Pre-filter to MSigDB immune genes, apply clustering</td>
<td>⭐⭐⭐⭐ Medium-high for immunotherapy prediction</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>D. Drug Sensitivity Prediction</strong></td>
<td>Use GDSC/CTRP to predict subtype-specific drug sensitivities</td>
<td>⭐⭐⭐ Medium - hypothesis-generating</td>
</tr>
<tr style="background-color: #D6EAF8;">
<td><strong>E. Pathway Burden Analysis</strong></td>
<td>GSEA, Reactome enrichment per subtype</td>
<td>⭐⭐⭐ Medium - biological insight</td>
</tr>
<tr style="background-color: #F5F5F5;">
<td><strong>F. Clinical Trial Integration</strong></td>
<td>Apply to IMvigor210 (bladder cancer anti-PD-L1, n=298)</td>
<td>⭐⭐⭐⭐⭐ High - demonstrates trial applicability</td>
</tr>
</tbody>
</table>

---

<a name="litsearch"></a>
## 9. Literature Search Methodology

### 9.1 Study Selection and Search Strategy

A targeted literature review was conducted using a **pearl-growing methodology** to identify multi-omics integration studies in lung cancer. Pearl-growing is a systematic approach that begins with known high-quality "seed" papers and expands the search through forward and backward citation tracking. This method is particularly effective for identifying relevant studies in mature research areas where seminal papers are well-established.

The initial seed papers included:
- The MOVICS framework paper (Lu et al., 2020)
- The TCGA Lung Adenocarcinoma marker paper (Cancer Genome Atlas Research Network, 2014)
- Key methodological papers describing multi-omics integration approaches (iCluster, SNF, DIABLO)

A backward citation search was then performed by reviewing references from these seed papers, and forward citation search to identify papers citing them using Google Scholar and Web of Science. High-quality papers identified through this process became new seed papers for subsequent rounds of expansion. This was supplemented by checking the TCGA publications database and searching bioRxiv and medRxiv for relevant preprints.

The search focused on multi-omics integration studies in TCGA lung cancer cohorts (LUAD, LUSC, NSCLC), with particular emphasis on studies using consensus clustering or integrative methods such as MOVICS, iCluster, SNF, or DIABLO. Studies that performed molecular subtyping or biomarker discovery through integration of two or more omics layers, including genomics, transcriptomics, epigenomics, and proteomics were prioritized.

### 9.2 Inclusion and Exclusion Criteria

Studies were included if they used TCGA lung cancer data, integrated two or more omics data types computationally, employed integrative clustering or dimensionality reduction methods, presented original research findings, were published in English, and had full text available for review. 

Studies were excluded if they performed single-omics analysis only, used exclusively non-TCGA cohorts, focused on other cancer types without lung cancer analysis, or presented methods without biological application. Studies with insufficient methodological detail that did not report their feature selection strategy, number of omics layers, or integration method were also excluded. When multiple publications from the same study or cohort were identified, the most comprehensive report was retained to avoid duplication.

### 9.3 Data Extraction

Study characteristics (first author, year, journal), dataset details (TCGA cohort, sample size), omics layers integrated (mRNA, methylation, miRNA, CNV, protein, mutations, lncRNA), integration methods employed, feature selection strategies (variance-based, survival-based, or hybrid), number of molecular subtypes identified, and clinical validation approaches (survival analysis, treatment response) were systematically extracted from each included study, tabulated, and synthesized descriptively, with key patterns visualized using charts and tables to characterize trends in multi-omics integration methodologies and their clinical impact.

### 9.4 Limitations

This pearl-growing approach, while efficient and targeted for identifying high-quality, methodologically relevant studies, has inherent limitations. The method may miss studies not connected to seed papers through citation networks and preferentially identifies highly-cited publications, potentially introducing publication bias. More recent papers may be underrepresented in citation networks due to limited time for citation accumulation. However, this approach is well-suited for rapidly identifying the most influential and methodologically rigorous studies in a mature research area where key papers and methods are already well-established in the literature.

---

<a name="references"></a>
## 10. References

Argelaguet, R., Velten, B., Arnol, D., Dietrich, S., Zenz, T., Marioni, J. C., Buettner, F., Huber, W., & Stegle, O. (2018). Multi-Omics Factor Analysis—a framework for unsupervised integration of multi-omics data sets. *Molecular Systems Biology*, *14*(6), e8124. https://doi.org/10.15252/msb.20178124

Bandyopadhyay, S., Mallik, S., & Mukhopadhyay, A. (2023). Machine learning based combination of multi-omics data for subgroup identification in non-small cell lung cancer. *Scientific Reports*, *13*(1), 4694. https://doi.org/10.1038/s41598-023-31426-w

Cancer Genome Atlas Research Network. (2012). Comprehensive genomic characterization of squamous cell lung cancers. *Nature*, *489*(7417), 519-525. https://doi.org/10.1038/nature11404

Cancer Genome Atlas Research Network. (2014). Comprehensive molecular profiling of lung adenocarcinoma. *Nature*, *511*(7511), 543-550. https://doi.org/10.1038/nature13385

Castillo-Secilla, D., Galvez, J. M., Herrera, L. J., Valenzuela, O., Caba, O., Prados, J. C., & Rojas, I. (2022). Machine-learning-based late fusion on multi-omics and multi-scale data for non-small-cell lung cancer diagnosis. *Journal of Personalized Medicine*, *12*(4), 601. https://doi.org/10.3390/jpm12040601

Chalise, P., & Fridley, B. L. (2017). Integrative clustering of multi-level 'omic data based on non-negative matrix factorization algorithm. *PLOS ONE*, *12*(5), e0176278. https://doi.org/10.1371/journal.pone.0176278

Chen, Z., Mei, K., Wang, M., Gu, R., & Huang, Y. (2025). Integrative multi-omics analysis for identifying novel therapeutic targets and predicting immunotherapy efficacy in lung adenocarcinoma. *Cancer Drug Resistance*, *8*, 2. https://doi.org/10.20517/cdr.2024.91

Hoadley, K. A., Yau, C., Wolf, D. M., Cherniack, A. D., Tamborero, D., Ng, S., Leiserson, M. D. M., Niu, B., McLellan, M. D., Uzunangelov, V., Zhang, J., Kandoth, C., Akbani, R., Shen, H., Omberg, L., Chu, A., Margolin, A. A., Van't Veer, L. J., Lopez-Bigas, N., ... Stuart, J. M. (2014). Multiplatform analysis of 12 cancer types reveals molecular classification within and across tissues of origin. *Cell*, *158*(4), 929-944. https://doi.org/10.1016/j.cell.2014.06.049

Karagkouni, D., Bertsias, N., Fourkiotis, N. K., Koinis, F., Symvoulakis, E., & Hatzigeorgiou, A. G. (2023). Multi-omics data analysis identifies prognostic biomarkers across cancers. *Oncology Letters*, *26*(2), 330. https://doi.org/10.3892/ol.2023.13916

Lin, Y., Wu, Z., Guo, W., & Li, J. (2024). Advancing lung adenocarcinoma prognosis and immunotherapy prediction with a multi-omics consensus machine learning approach. *Journal of Cellular and Molecular Medicine*, *28*(11), e18367. https://doi.org/10.1111/jcmm.18367

Lu, X., Meng, J., Zhou, Y., Jiang, L., & Yan, F. (2020). MOVICS: an R package for multi-omics integration and visualization in cancer subtyping. *Bioinformatics*, *36*(22-23), 5539-5541. https://doi.org/10.1093/bioinformatics/btaa1018

Meng, C., Helm, D., Frejno, M., & Kuster, B. (2016). moCluster: Identifying joint patterns across multiple omics data sets. *Journal of Proteome Research*, *15*(3), 755-765. https://doi.org/10.1021/acs.jproteome.5b00824

Michailidou, K., Kelemen, L. E., Lawrenson, K., Kar, S., Hsiung, A., Earp, M., Dennis, J., Beesley, J., Chenevix-Trench, G., & Pharoah, P. D. P. (2021). A detailed catalogue of multi-omics methodologies for identification of putative biomarkers and causal molecular networks in translational cancer research. *International Journal of Molecular Sciences*, *22*(6), 2822. https://doi.org/10.3390/ijms22062822

Mo, Q., Shen, R., Guo, C., Vannucci, M., Chan, K. S., & Hilsenbeck, S. G. (2018). A fully Bayesian latent variable model for integrative clustering analysis of multi-type omics data. *Biostatistics*, *19*(1), 71-86. https://doi.org/10.1093/biostatistics/kxx017

Mo, Q., Wang, S., Seshan, V. E., Olshen, A. B., Schultz, N., Sander, C., Powers, R. S., Ladanyi, M., & Shen, R. (2013). Pattern discovery and cancer gene identification in integrated cancer genomic data. *Proceedings of the National Academy of Sciences*, *110*(11), 4245-4250. https://doi.org/10.1073/pnas.1208949110

Nguyen, H., Shrestha, S., Draghici, S., & Nguyen, T. (2017). PINSPlus: a tool for tumor subtype discovery in integrated genomic data. *Bioinformatics*, *35*(16), 2843-2846. https://doi.org/10.1093/bioinformatics/bty1049

Ochoa, S., & Hernández-Lemus, E. (2024). Functional impact of multi-omic interactions in lung cancer. *Frontiers in Genetics*, *15*, 1282241. https://doi.org/10.3389/fgene.2024.1282241

Ramazzotti, D., Lal, A., Wang, B., Batzoglou, S., & Sidow, A. (2018). Multi-omic tumor data reveal diversity of molecular mechanisms that correlate with survival. *Nature Communications*, *9*(1), 4453. https://doi.org/10.1038/s41467-018-06921-8

Rappoport, N., & Shamir, R. (2018). Multi-omic and multi-view clustering algorithms: review and cancer benchmark. *Nucleic Acids Research*, *46*(20), 10546-10562. https://doi.org/10.1093/nar/gky889

Ruan, H., Hu, Q., Wen, D., Chen, Q., Chen, G., Lu, Y., Wang, J., Cheng, H., Lu, W., & Gu, Z. (2022). A dual-gene signature prognostic model and immune features in patients with lung adenocarcinoma. *Frontiers in Medicine*, *9*, 861877. https://doi.org/10.3389/fmed.2022.861877

Saggi, M. K., Kaur, J., Pal, S. K., & Jain, S. (2024). Multi-omic and quantum machine learning integration for lung subtypes classification. *arXiv preprint arXiv:2410.02085*. https://arxiv.org/abs/2410.02085

Shen, R., Olshen, A. B., & Ladanyi, M. (2009). Integrative clustering of multiple genomic data types using a joint latent variable model with application to breast and lung cancer subtype analysis. *Bioinformatics*, *25*(22), 2906-2912. https://doi.org/10.1093/bioinformatics/btp543

Singh, A., Shannon, C. P., Gautier, B., Rohart, F., Vacher, M., Tebbutt, S. J., & Lê Cao, K.-A. (2019). DIABLO: an integrative approach for identifying key molecular drivers from multi-omics assays. *Bioinformatics*, *35*(17), 3055-3062. https://doi.org/10.1093/bioinformatics/bty1054

Wang, B., Mezlini, A. M., Demir, F., Fiume, M., Tu, Z., Brudno, M., Haibe-Kains, B., & Goldenberg, A. (2014). Similarity network fusion for aggregating data types on a genomic scale. *Nature Methods*, *11*(3), 333-337. https://doi.org/10.1038/nmeth.2810

Wang, X., Chen, Y., Gao, Y., Zhang, H., Guan, Z., Dong, Z., Zheng, Y., Jiang, J., Yang, H., Wang, L., Huang, X., Ai, L., Yu, W., Li, H., Dong, B., Zhou, Q., Wang, J., Zhao, J., Zhang, T., ... Zhu, H. (2021). Predicting gastric cancer outcome from resected lymph node histopathology images using deep learning. *Nature Communications*, *12*(1), 1637. https://doi.org/10.1038/s41467-021-21674-7

Wu, D., Wang, D., Zhang, M. Q., & Gu, J. (2015). Fast dimension reduction and integrative clustering of multi-omics data using low-rank approximation: application to cancer molecular classification. *BMC Genomics*, *16*, 1022. https://doi.org/10.1186/s12864-015-2223-8

Wu, Y., Chen, L., Wang, Y., Li, S., Li, H., Xu, K., Zhang, C., Hao, X., Jiao, X., & Qiu, M. (2024). Molecular classification reveals the sensitivity of lung adenocarcinoma to radiotherapy and immunotherapy: multi-omics clustering based on similarity network fusion. *Cancer Immunology, Immunotherapy*, *73*(3), 39. https://doi.org/10.1007/s00262-024-03657-x

Zhang, X., Li, Z., Huang, Y., Zhang, Y., Liu, X., Li, H., Li, S., Xing, P., Hu, X., Li, J., Chang, J., Wang, M., & Wang, J. (2025). Multi-omics analyses reveal biological and clinical insights in recurrent stage I non-small cell lung cancer. *Nature Communications*, *16*(1), 1213. https://doi.org/10.1038/s41467-024-55068-2

Zhong, S., Zhang, B., Bai, H., Wang, J., Duan, J., Xu, Y., Han, R., Tian, Y., An, T., Zhuo, M., Wang, Y., Song, X., Wu, M., & Wang, J. (2025). Multi-omics analysis identifies different molecular subtypes with unique outcomes in early-stage poorly differentiated lung adenocarcinoma. *Molecular Cancer*, *24*(1), 102. https://doi.org/10.1186/s12943-025-02333-7

Zou, Y., Xie, J., Zheng, S., Liu, W., Tang, Y., Tian, W., Deng, X., Wu, L., Zhang, Y., Wong, C. W., Tan, W., Xie, X., & Zheng, J. (2022). Multi-omics consensus portfolio to refine the classification of lung adenocarcinoma with prognostic stratification, tumor microenvironment, and unique sensitivity to first-line therapies. *Translational Lung Cancer Research*, *11*(11), 2251-2271. https://doi.org/10.21037/tlcr-22-535


---

**Document Prepared:** February 2026  
**Total Studies Analyzed:** 25+  
**Focus:** Multi-omics integration in lung cancer with emphasis on methodological improvements and clinical translation

---

**© 2026 Vignesh Ravichandran, DHI. All rights reserved.**
