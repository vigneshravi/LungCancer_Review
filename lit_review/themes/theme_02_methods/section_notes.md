# Theme 02 — Synthesis

*Theme: Multi-omics integration methods*
*Total papers: 5289 | Tier A: 6 | Tier B: 196*

## Anchor Studies

- **Shen et al. (2009)** [PMID: 19759197] [10.1093/bioinformatics/btp543](https://doi.org/10.1093/bioinformatics/btp543)
  *Bioinformatics (Oxford, England)* — Integrative clustering of multiple genomic data types using a joint latent variable model with application to breast and lung cancer subtype analysis.
  TLDR: The resulting methodology iCluster incorporates flexible modeling of the associations between different data types and the variance-covariance structure within data types in a single framework, while simultaneously reducing the dimensionality of the datasets.

- **Wang et al. (2014)** [PMID: 24464287] [10.1038/nmeth.2810](https://doi.org/10.1038/nmeth.2810)
  *Nature methods* — Similarity network fusion for aggregating data types on a genomic scale.
  TLDR: Similarity network fusion substantially outperforms single data type analysis and established integrative approaches when identifying cancer subtypes and is effective for predicting survival.

- **Lehmann et al. (2017)** [PMID: 28369062] [10.1371/journal.pone.0174718](https://doi.org/10.1371/journal.pone.0174718)
  *PloS one* — T cell subtypes and reciprocal inflammatory mediator expression differentiate P. falciparum memory recall responses in asymptomatic and symptomatic malaria patients in southeastern Haiti.
  TLDR: This is the first comprehensive investigation of immune responses to P. falciparum in Haiti, and describes unique cell-mediated immune repertoires that delineate individuals into asymptomatic and symptomatic phenotypes.

- **González-Pacheco et al. (2019)** [PMID: 30590492] [10.1093/ehjci/jey213](https://doi.org/10.1093/ehjci/jey213)
  *European heart journal. Cardiovascular Imaging* — A mechanical prosthesis in a porcelain box.

- **Aslan et al. (2020)** [PMID: 32185779] [10.14744/tjtes.2020.94490](https://doi.org/10.14744/tjtes.2020.94490)
  *Ulusal travma ve acil cerrahi dergisi = Turkish journal of trauma & emergency surgery : TJTES* — Is electromagnetic guidance system superior to a free-hand technique for distal locking in intramedullary nailing of tibial fractures? A prospective comparative study.
  TLDR: Both the FHT distal screwing technique and the EMGS distal Screwing technique are highly effective methods for distal locking in patients who underwent osteosynthesis of tibia fractures with IMN.

- **Argelaguet et al. (2020)** [PMID: 32393329] [10.1186/s13059-020-02015-1](https://doi.org/10.1186/s13059-020-02015-1)
  *Genome biology* — MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data.
  TLDR: This work presents Multi-Omics Factor Analysis v2 (MOFA+), a statistical framework for the comprehensive and scalable integration of single-cell multi-modal data that reconstructs a low-dimensional representation of the data using computationally efficient variational inference and supports flexible sparsity constraints.

## What the literature establishes

Multi-omics integration methods have evolved from simple concatenation approaches to sophisticated statistical and deep learning frameworks. Established tools include iCluster for joint latent variable modeling, Similarity Network Fusion (SNF) for patient similarity networks, MOFA/MOFA+ for multi-omics factor analysis, and DIABLO (mixOmics) for supervised multi-block integration.

Benchmarking studies have systematically evaluated these methods, revealing that no single approach dominates across all cancer types and data configurations. The choice of integration strategy (early, intermediate, or late fusion) depends on the specific research question, available data types, and sample sizes. Deep learning approaches, including variational autoencoders and graph neural networks, show promise for learning non-linear relationships across omics layers but require larger datasets and careful regularization.

Consensus clustering across multiple algorithms and parameter settings has become standard practice for robust subtype discovery. Tools like MOVICS provide comprehensive frameworks that combine multiple integration algorithms with downstream analysis pipelines.

## Where consensus exists

- Multi-omics integration outperforms single-omics analysis for subtype discovery
- No single integration method dominates across all scenarios
- Consensus approaches combining multiple methods improve robustness
- Deep learning methods require larger sample sizes but can capture non-linear relationships
- Benchmarking on standardized datasets is essential for fair method comparison

## Where the field disagrees or is uncertain

- Early vs. late vs. intermediate integration: no consensus on optimal strategy
- Whether deep learning methods genuinely outperform simpler statistical methods at typical sample sizes
- How to handle missing data across omics layers
- Appropriate metrics for evaluating integration quality
- Scalability of current methods to 5+ omics layers simultaneously

## Gaps and open questions

- Few methods designed for clinical-scale deployment (runtime, interpretability)
- Integration of clinical variables with omics data not well standardized
- Methods for integrating single-cell multi-omics are in early stages
- Spatial multi-omics integration tools are nascent
- Handling of temporal/longitudinal multi-omics data
- Methods for causal inference from multi-omics data

## Candidate citations for the review

1. Shen et al. (2009) — *Bioinformatics (Oxford, England)* [PMID: 19759197] [10.1093/bioinformatics/btp543](https://doi.org/10.1093/bioinformatics/btp543) (Score: 1.00, Tier: A)
2. Wang et al. (2014) — *Nature methods* [PMID: 24464287] [10.1038/nmeth.2810](https://doi.org/10.1038/nmeth.2810) (Score: 1.00, Tier: A)
3. Lehmann et al. (2017) — *PloS one* [PMID: 28369062] [10.1371/journal.pone.0174718](https://doi.org/10.1371/journal.pone.0174718) (Score: 1.00, Tier: A)
4. González-Pacheco et al. (2019) — *European heart journal. Cardiovascular Imaging* [PMID: 30590492] [10.1093/ehjci/jey213](https://doi.org/10.1093/ehjci/jey213) (Score: 1.00, Tier: A)
5. Aslan et al. (2020) — *Ulusal travma ve acil cerrahi dergisi = Turkish journal of trauma & emergency surgery : TJTES* [PMID: 32185779] [10.14744/tjtes.2020.94490](https://doi.org/10.14744/tjtes.2020.94490) (Score: 1.00, Tier: A)
6. Argelaguet et al. (2020) — *Genome biology* [PMID: 32393329] [10.1186/s13059-020-02015-1](https://doi.org/10.1186/s13059-020-02015-1) (Score: 1.00, Tier: A)
7. Hu et al. (2024) — *Nature methods* [PMID: 39322753] [10.1038/s41592-024-02429-w](https://doi.org/10.1038/s41592-024-02429-w) (Score: 0.68, Tier: B)
8. Uyar et al. (2025) — *Nature communications* [PMID: 40940333] [10.1038/s41467-025-63688-5](https://doi.org/10.1038/s41467-025-63688-5) (Score: 0.68, Tier: B)
9. Liu et al. (2025) — *Nature methods* [PMID: 41083898] [10.1038/s41592-025-02856-3](https://doi.org/10.1038/s41592-025-02856-3) (Score: 0.68, Tier: B)
10. Pierre-Jean et al. (2020) — *Briefings in bioinformatics* [PMID: 31792509] [10.1093/bib/bbz138](https://doi.org/10.1093/bib/bbz138) (Score: 0.65, Tier: B)
11. Athaya et al. (2023) — *Briefings in bioinformatics* [PMID: 37651607] [10.1093/bib/bbad313](https://doi.org/10.1093/bib/bbad313) (Score: 0.63, Tier: B)
12. Baião et al. (2025) — *Briefings in bioinformatics* [PMID: 40748323] [10.1093/bib/bbaf355](https://doi.org/10.1093/bib/bbaf355) (Score: 0.63, Tier: B)
13. Huizing et al. (2023) — *Nature communications* [PMID: 38001063] [10.1038/s41467-023-43019-2](https://doi.org/10.1038/s41467-023-43019-2) (Score: 0.60, Tier: B)
14. Wang et al. (2025) — *Briefings in bioinformatics* [PMID: 40211981] [10.1093/bib/bbaf157](https://doi.org/10.1093/bib/bbaf157) (Score: 0.60, Tier: B)
15. Zhao et al. (2026) — *Genome biology* [PMID: 41975483] [10.1186/s13059-026-04070-6](https://doi.org/10.1186/s13059-026-04070-6) (Score: 0.60, Tier: B)
16. Chauvel et al. (2020) — *Briefings in bioinformatics* [PMID: 31220206] [10.1093/bib/bbz015](https://doi.org/10.1093/bib/bbz015) (Score: 0.58, Tier: B)
17. Kang et al. (2022) — *Briefings in bioinformatics* [PMID: 34791014] [10.1093/bib/bbab454](https://doi.org/10.1093/bib/bbab454) (Score: 0.58, Tier: B)
18. Zhao et al. (2023) — *Briefings in bioinformatics* [PMID: 36702755] [10.1093/bib/bbad025](https://doi.org/10.1093/bib/bbad025) (Score: 0.58, Tier: B)
19. Liu et al. (2023) — *Briefings in bioinformatics* [PMID: 37232375] [10.1093/bib/bbad196](https://doi.org/10.1093/bib/bbad196) (Score: 0.58, Tier: B)
20. Xiao et al. (2024) — *Briefings in bioinformatics* [PMID: 38493343] [10.1093/bib/bbae095](https://doi.org/10.1093/bib/bbae095) (Score: 0.58, Tier: B)
21. Yan et al. (2024) — *Briefings in bioinformatics* [PMID: 38670157] [10.1093/bib/bbae184](https://doi.org/10.1093/bib/bbae184) (Score: 0.58, Tier: B)
22. Yang et al. (2025) — *Nature communications* [PMID: 39893194] [10.1038/s41467-025-56523-4](https://doi.org/10.1038/s41467-025-56523-4) (Score: 0.58, Tier: B)
23. Wang et al. (2025) — *Nature communications* [PMID: 40442129] [10.1038/s41467-025-60333-z](https://doi.org/10.1038/s41467-025-60333-z) (Score: 0.58, Tier: B)
24. Fu et al. (2025) — *Nature methods* [PMID: 40640531] [10.1038/s41592-025-02737-9](https://doi.org/10.1038/s41592-025-02737-9) (Score: 0.58, Tier: B)
25. Cantini et al. (2021) — *Nature communications* [PMID: 33402734] [10.1038/s41467-020-20430-7](https://doi.org/10.1038/s41467-020-20430-7) (Score: 0.57, Tier: B)
26. Herrmann et al. (2021) — *Briefings in bioinformatics* [PMID: 32823283] [10.1093/bib/bbaa167](https://doi.org/10.1093/bib/bbaa167) (Score: 0.56, Tier: B)
27. Cao et al. (2024) — *Nature communications* [PMID: 38582890] [10.1038/s41467-024-47418-x](https://doi.org/10.1038/s41467-024-47418-x) (Score: 0.56, Tier: B)
28. Slobodyanyuk et al. (2024) — *Nature communications* [PMID: 38971800] [10.1038/s41467-024-49986-4](https://doi.org/10.1038/s41467-024-49986-4) (Score: 0.56, Tier: B)
29. Wang et al. (2024) — *Nature communications* [PMID: 39127735] [10.1038/s41467-024-50701-6](https://doi.org/10.1038/s41467-024-50701-6) (Score: 0.56, Tier: B)
30. Zhou et al. (2025) — *Nature communications* [PMID: 39747840] [10.1038/s41467-024-55204-y](https://doi.org/10.1038/s41467-024-55204-y) (Score: 0.56, Tier: B)

## Notes for the writing phase

- **Bridge papers** (spanning multiple themes): 0 papers
- **Recent papers** (2023+): 3658 papers
- **Tier A papers**: 6 — prioritize these for citation
- **Tier B papers**: 196 — use selectively for supporting evidence

- **RETRACTED papers found**: 8 — DO NOT CITE:
  - PMID 40884456: Integration of single cell multiomics data by deep transfer ...
  - PMID 38480676: RETRACTED: Refining molecular subtypes and risk stratificati...
  - PMID 38881051: A novel deep learning framework for accurate melanoma diagno...
  - PMID 39263113: Emerging research trends in artificial intelligence for canc...
  - PMID 38563455: RETRACTED: Development of gene panel for predicting recurren...
  - PMID 19015639: Requirement for chromatin-remodeling complex in novel tumor ...
  - PMID 26542803: MicroRNA-7 Compromises p53 Protein-dependent Apoptosis by Co...
  - PMID 20065354: Histone deacetylase inhibitors activate NF-kappaB in human l...

