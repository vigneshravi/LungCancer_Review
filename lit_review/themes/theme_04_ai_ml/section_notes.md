# Theme 04 — Synthesis

*Theme: AI/ML in lung cancer and oncology*
*Total papers: 11167 | Tier A: 8 | Tier B: 803*

## Anchor Studies

- **Coudray et al. (2018)** [PMID: 30224757] [10.1038/s41591-018-0177-5](https://doi.org/10.1038/s41591-018-0177-5)
  *Nature medicine* — Classification and mutation prediction from non-small cell lung cancer histopathology images using deep learning.
  TLDR: This study trained a deep convolutional neural network on whole-slide images obtained from The Cancer Genome Atlas to accurately and automatically classify them into LUAD, LUSC or normal lung tissue and trained the network to predict the ten most commonly mutated genes in LUAD.

- **Linghu et al. (2022)** [PMID: 35512792] [10.1097/CM9.0000000000002147](https://doi.org/10.1097/CM9.0000000000002147)
  *Chinese medical journal* — Obesity and chronic diarrhea: a new syndrome?
  TLDR: The problem of overweight and obesity incidence in children and adolescents has increased at an alarming rate, posing a great threat to society as a whole, and finding an effective means to control the growth of obesity is urgently needed.

- **Chen et al. (2022)** [PMID: 35944502] [10.1016/j.ccell.2022.07.004](https://doi.org/10.1016/j.ccell.2022.07.004)
  *Cancer cell* — Pan-cancer integrative histology-genomic analysis via multimodal deep learning.
  TLDR: This work uses multimodal deep learning to jointly examine pathology whole-slide images and molecular profile data from 14 cancer types to predict outcomes and discover prognostic features that correlate with poor and favorable outcomes.

- **Juan et al. (2022)** [PMID: 36108632] [10.1016/j.molcel.2022.08.021](https://doi.org/10.1016/j.molcel.2022.08.021)
  *Molecular cell* — Tissue-specific Grb10/Ddc insulator drives allelic architecture for cardiac development.
  TLDR: The Grb10-Ddc imprinting domain is redefined by uncovering an unconventional intronic secondary DMR that functions as an insulator to instruct the tissue-specific, monoallelic expression of multiple genes-a feature previously ICR exclusive.

- **Hu et al. (2024)** [PMID: 39030412] [10.1186/s42155-024-00470-6](https://doi.org/10.1186/s42155-024-00470-6)
  *CVIR endovascular* — Transcatheter embolization for duodenal ulcer bleeding originating from cystic artery erosion.
  TLDR: Cystic artery embolization proved to be a minimally invasive technique for achieving hemostasis in these cases, indicating that it may be a safe and effective alternative to surgery for this uncommon cause of upper gastrointestinal bleeding.

- **Bosone et al. (2024)** [PMID: 39294368] [10.1038/s41592-024-02412-5](https://doi.org/10.1038/s41592-024-02412-5)
  *Nature methods* — A polarized FGF8 source specifies frontotemporal signatures in spatially oriented cell populations of cortical assembloids.
  TLDR: Human cortical assembloids are engineer by fusing an organizer-like structure expressing fibroblast growth factor 8 (FGF8) with an elongated organoid to enable the controlled modulation of FGF8 signaling along the longitudinal organoid axis and enables the study of cortical area-relevant alterations underlying human disorders.

## What the literature establishes

AI and machine learning have been extensively applied across the lung cancer continuum, from molecular subtyping to outcome prediction. Deep learning models applied to histopathology whole slide images can classify NSCLC subtypes (LUAD vs LUSC) with high accuracy and predict molecular alterations directly from H&E-stained slides.

Radiomics and radiogenomics have linked imaging features to underlying molecular characteristics and treatment outcomes, though reproducibility across scanners and institutions remains a challenge. Foundation models pre-trained on large pathology image datasets have shown strong transfer learning capabilities, reducing the need for large labeled datasets in specific tasks.

ML-based models for immunotherapy response prediction have incorporated tumor mutational burden, PD-L1 expression, gene expression signatures, and imaging features, with multi-modal approaches generally outperforming single-modality models. However, external validation studies consistently show performance degradation, and algorithmic bias related to demographic representation in training data has been identified as a significant concern.

## Where consensus exists

- Deep learning can classify NSCLC subtypes from histopathology with high accuracy
- Multi-modal AI models generally outperform single-modality approaches
- External validation consistently shows performance degradation
- Foundation models reduce the need for large labeled datasets
- Radiomics features are sensitive to acquisition parameters and require harmonization

## Where the field disagrees or is uncertain

- Whether AI models should replace or augment pathologist assessment
- Fair benchmarking practices for medical AI across demographic groups
- Extent of data leakage in published studies
- Whether foundation models trained primarily on Western cohorts generalize globally
- Optimal regulatory frameworks for clinical AI deployment

## Gaps and open questions

- Few ML models validated on multi-ethnic, multi-institutional cohorts
- Absence of sex-stratified AI model development and evaluation
- Limited AI tools for never-smoker NSCLC specifically
- Integration of molecular data with clinical AI remains primitive
- Regulatory frameworks lag behind technical capabilities
- AI fairness and bias assessment rarely performed for oncology models

## Candidate citations for the review

1. Coudray et al. (2018) — *Nature medicine* [PMID: 30224757] [10.1038/s41591-018-0177-5](https://doi.org/10.1038/s41591-018-0177-5) (Score: 1.00, Tier: A)
2. Linghu et al. (2022) — *Chinese medical journal* [PMID: 35512792] [10.1097/CM9.0000000000002147](https://doi.org/10.1097/CM9.0000000000002147) (Score: 1.00, Tier: A)
3. Chen et al. (2022) — *Cancer cell* [PMID: 35944502] [10.1016/j.ccell.2022.07.004](https://doi.org/10.1016/j.ccell.2022.07.004) (Score: 1.00, Tier: A)
4. Juan et al. (2022) — *Molecular cell* [PMID: 36108632] [10.1016/j.molcel.2022.08.021](https://doi.org/10.1016/j.molcel.2022.08.021) (Score: 1.00, Tier: A)
5. Hu et al. (2024) — *CVIR endovascular* [PMID: 39030412] [10.1186/s42155-024-00470-6](https://doi.org/10.1186/s42155-024-00470-6) (Score: 1.00, Tier: A)
6. Bosone et al. (2024) — *Nature methods* [PMID: 39294368] [10.1038/s41592-024-02412-5](https://doi.org/10.1038/s41592-024-02412-5) (Score: 1.00, Tier: A)
7. Wang et al. (2024) — *Nature* [PMID: 39232164] [10.1038/s41586-024-07894-z](https://doi.org/10.1038/s41586-024-07894-z) (Score: 0.72, Tier: A)
8. Yang et al. (2025) — *Nature communications* [PMID: 40064883] [10.1038/s41467-025-57587-y](https://doi.org/10.1038/s41467-025-57587-y) (Score: 0.72, Tier: A)
9. Courtiol et al. (2019) — *Nature medicine* [PMID: 31591589] [10.1038/s41591-019-0583-3](https://doi.org/10.1038/s41591-019-0583-3) (Score: 0.67, Tier: B)
10. Thiesen et al. (2026) — *Cancer research* [PMID: 41481196] [10.1158/0008-5472.CAN-25-2275](https://doi.org/10.1158/0008-5472.CAN-25-2275) (Score: 0.64, Tier: B)
11. Bakas et al. (2024) — *The Lancet. Oncology* [PMID: 39481415] [10.1016/S1470-2045(24)00315-2](https://doi.org/10.1016/S1470-2045(24)00315-2) (Score: 0.63, Tier: B)
12. Wang et al. (2025) — *Briefings in bioinformatics* [PMID: 40515391] [10.1093/bib/bbaf275](https://doi.org/10.1093/bib/bbaf275) (Score: 0.62, Tier: B)
13. Arshad et al. (2025) — *Cancers* [PMID: 41463234] [10.3390/cancers17243985](https://doi.org/10.3390/cancers17243985) (Score: 0.61, Tier: B)
14. Faa et al. (2026) — *Cancers* [PMID: 41976406] [10.3390/cancers18071184](https://doi.org/10.3390/cancers18071184) (Score: 0.61, Tier: B)
15. Dolezal et al. (2022) — *Nature communications* [PMID: 36323656] [10.1038/s41467-022-34025-x](https://doi.org/10.1038/s41467-022-34025-x) (Score: 0.61, Tier: B)
16. Rakaee et al. (2025) — *JAMA oncology* [PMID: 39724105] [10.1001/jamaoncol.2024.5356](https://doi.org/10.1001/jamaoncol.2024.5356) (Score: 0.60, Tier: B)
17. Hu et al. (2025) — *Briefings in bioinformatics* [PMID: 40116660] [10.1093/bib/bbaf121](https://doi.org/10.1093/bib/bbaf121) (Score: 0.60, Tier: B)
18. Li et al. (2025) — *Nature communications* [PMID: 40624052] [10.1038/s41467-025-61349-1](https://doi.org/10.1038/s41467-025-61349-1) (Score: 0.60, Tier: B)
19. Lin et al. (2026) — *Briefings in bioinformatics* [PMID: 41554048] [10.1093/bib/bbaf735](https://doi.org/10.1093/bib/bbaf735) (Score: 0.60, Tier: B)
20. Pang et al. (2023) — *Briefings in bioinformatics* [PMID: 37594302] [10.1093/bib/bbad304](https://doi.org/10.1093/bib/bbad304) (Score: 0.58, Tier: B)
21. Wagner et al. (2023) — *Cancer cell* [PMID: 37652006] [10.1016/j.ccell.2023.08.002](https://doi.org/10.1016/j.ccell.2023.08.002) (Score: 0.58, Tier: B)
22. Gonzalez et al. (2024) — *Journal of pathology informatics* [PMID: 38089005] [10.1016/j.jpi.2023.100348](https://doi.org/10.1016/j.jpi.2023.100348) (Score: 0.58, Tier: B)
23. Wang et al. (2024) — *Cancer cell* [PMID: 38942025] [10.1016/j.ccell.2024.06.002](https://doi.org/10.1016/j.ccell.2024.06.002) (Score: 0.58, Tier: B)
24. Zhao et al. (2025) — *The Lancet. Oncology* [PMID: 39653054] [10.1016/S1470-2045(24)00599-0](https://doi.org/10.1016/S1470-2045(24)00599-0) (Score: 0.58, Tier: B)
25. Qiu et al. (2025) — *Cancer research* [PMID: 40305075] [10.1158/0008-5472.CAN-24-4190](https://doi.org/10.1158/0008-5472.CAN-24-4190) (Score: 0.58, Tier: B)
26. Sharma et al. (2025) — *Nature communications* [PMID: 40436838] [10.1038/s41467-025-59610-8](https://doi.org/10.1038/s41467-025-59610-8) (Score: 0.58, Tier: B)
27. Alsallal et al. (2026) — *Abdominal radiology (New York)* [PMID: 40932499] [10.1007/s00261-025-05181-7](https://doi.org/10.1007/s00261-025-05181-7) (Score: 0.58, Tier: B)
28. Rakaee et al. (2023) — *JAMA oncology* [PMID: 36394839] [10.1001/jamaoncol.2022.4933](https://doi.org/10.1001/jamaoncol.2022.4933) (Score: 0.56, Tier: B)
29. Chen et al. (2024) — *Nature communications* [PMID: 38395893] [10.1038/s41467-024-46043-y](https://doi.org/10.1038/s41467-024-46043-y) (Score: 0.56, Tier: B)
30. Captier et al. (2025) — *Nature communications* [PMID: 39800784] [10.1038/s41467-025-55847-5](https://doi.org/10.1038/s41467-025-55847-5) (Score: 0.56, Tier: B)

## Notes for the writing phase

- **Bridge papers** (spanning multiple themes): 0 papers
- **Recent papers** (2023+): 7374 papers
- **Tier A papers**: 8 — prioritize these for citation
- **Tier B papers**: 803 — use selectively for supporting evidence

- **RETRACTED papers found**: 30 — DO NOT CITE:
  - PMID 36046454: Lung Cancer Classification and Prediction Using Machine Lear...
  - PMID 36866239: Integrative Nomogram of Computed Tomography Radiomics, Clini...
  - PMID 39299968: Comment on, "Survival prediction of glioblastoma patients-ar...
  - PMID 37181405: 18F-FDG PET/CT Image Deep Learning Predicts Colon Cancer Sur...
  - PMID 39221858: A novel Skin lesion prediction and classification technique:...
  - PMID 35155681: Establishment and External Validation of a Hypoxia-Derived G...
  - PMID 41501145: LungGANDetectAI: a GAN-augmented and attention-guided deep l...
  - PMID 35378943: Models of Artificial Intelligence-Assisted Diagnosis of Lung...
  - PMID 34447527: Evaluation of the Effectiveness of Artificial Intelligence C...
  - PMID 35360550: The Value of Artificial Intelligence Film Reading System Bas...
  - PMID 35937383: Classification and Detection of Mesothelioma Cancer Using Fe...
  - PMID 36193309: Artificial Neural Network Assisted Cancer Risk Prediction of...
  - PMID 33963232: A combined microfluidic deep learning approach for lung canc...
  - PMID 34691378: Adaptive Diagnosis of Lung Cancer by Deep Learning Classific...
  - PMID 36785667: Applications of Neural Network-Based Plan-Cancer Method for ...
  - PMID 38480676: RETRACTED: Refining molecular subtypes and risk stratificati...
  - PMID 40779565: RETRACTED: LGD_Net: Capsule network with extreme learning ma...
  - PMID 38881051: A novel deep learning framework for accurate melanoma diagno...
  - PMID 39441216: Single-cell omics and machine learning integration to develo...
  - PMID 36060648: Clinical and Biological Significances of a Ferroptosis-Relat...
  - PMID 36785839: An Efficient Model for Lungs Nodule Classification Using Sup...
  - PMID 40299923: RETRACTED: Optimizing chemotherapeutic targets in non-small ...
  - PMID 34721825: Deep Learning-Based Computed Tomography Imaging to Diagnose ...
  - PMID 35028122: Application of Deep Learning in Lung Cancer Imaging Diagnosi...
  - PMID 36299828: Bioinformatic Deconstruction of Differentially Expressed Seq...
  - PMID 38563455: RETRACTED: Development of gene panel for predicting recurren...
  - PMID 35770126: A Novel Approach to Predict Brain Cancerous Tumor Using Tran...
  - PMID 24655788: Up-regulated miR-199a-5p in gastric cancer functions as an o...
  - PMID 35202419: Wasp venom peptide improves the proapoptotic activity of ale...
  - PMID 17374986: Mechanistic analysis and comparison of viral fusogenic membr...

