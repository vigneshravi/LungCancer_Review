"""Generate section_notes.md synthesis for each theme from collected papers."""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import THEMES, ANCHOR_PMIDS


def synthesize_theme(theme_id):
    """Generate section_notes.md for a theme based on collected papers."""
    theme = THEMES[theme_id]
    theme_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "themes", theme["dir"])
    papers_json = os.path.join(theme_dir, "papers.json")

    if not os.path.exists(papers_json):
        print(f"No papers.json for {theme_id}")
        return

    with open(papers_json) as f:
        papers = json.load(f)

    # Sort by relevance
    papers.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)

    tier_a = [p for p in papers if p.get("priority_tier") == "A"]
    tier_b = [p for p in papers if p.get("priority_tier") == "B"]

    # Get anchor papers
    anchors = ANCHOR_PMIDS.get(theme_id, [])
    anchor_papers = [p for p in papers if p["pmid"] in anchors]

    # Top papers for citation candidates
    top_papers = (tier_a + tier_b)[:30]

    output_path = os.path.join(theme_dir, "section_notes.md")
    with open(output_path, "w") as f:
        f.write(f"# {theme_id.replace('_', ' ').title()} — Synthesis\n\n")
        f.write(f"*Theme: {theme['name']}*\n")
        f.write(f"*Total papers: {len(papers)} | Tier A: {len(tier_a)} | Tier B: {len(tier_b)}*\n\n")

        # Key anchor papers summary
        if anchor_papers:
            f.write("## Anchor Studies\n\n")
            for p in anchor_papers:
                doi_link = f"[{p['doi']}](https://doi.org/{p['doi']})" if p.get("doi") else ""
                f.write(f"- **{p.get('authors_first', '')} et al. ({p.get('year', '')})** [PMID: {p['pmid']}] {doi_link}\n")
                f.write(f"  *{p.get('journal', '')}* — {p.get('title', '')}\n")
                if p.get("tldr"):
                    f.write(f"  TLDR: {p['tldr']}\n")
                f.write("\n")

        # What the literature establishes
        f.write("## What the literature establishes\n\n")
        f.write(_generate_establishes(theme_id, tier_a, tier_b, anchor_papers))
        f.write("\n\n")

        # Consensus
        f.write("## Where consensus exists\n\n")
        f.write(_generate_consensus(theme_id, tier_a, tier_b))
        f.write("\n\n")

        # Disagreements
        f.write("## Where the field disagrees or is uncertain\n\n")
        f.write(_generate_disagreements(theme_id, tier_a, tier_b))
        f.write("\n\n")

        # Gaps
        f.write("## Gaps and open questions\n\n")
        f.write(_generate_gaps(theme_id, tier_a, tier_b))
        f.write("\n\n")

        # Candidate citations
        f.write("## Candidate citations for the review\n\n")
        for i, p in enumerate(top_papers[:30], 1):
            doi_link = f"[{p['doi']}](https://doi.org/{p['doi']})" if p.get("doi") else ""
            f.write(f"{i}. {p.get('authors_first', '')} et al. ({p.get('year', '')}) — "
                    f"*{p.get('journal', '')}* [PMID: {p['pmid']}] {doi_link} "
                    f"(Score: {p.get('relevance_score', 0):.2f}, Tier: {p.get('priority_tier', 'C')})\n")
        f.write("\n")

        # Notes for writing
        f.write("## Notes for the writing phase\n\n")
        f.write(_generate_writing_notes(theme_id, papers, tier_a, tier_b))

    print(f"  ✓ section_notes.md written for {theme_id}")


def _generate_establishes(theme_id, tier_a, tier_b, anchors):
    """Generate 'what the literature establishes' based on theme."""
    texts = {
        "theme_01": (
            "The molecular landscape of lung cancer has been extensively characterized through large-scale consortium "
            "efforts. TCGA and CPTAC studies have delineated the genomic, transcriptomic, and proteomic architecture "
            "of lung adenocarcinoma (LUAD) and lung squamous cell carcinoma (LUSC), revealing distinct driver mutation "
            "profiles. LUAD is dominated by activating mutations in EGFR, KRAS, and ALK fusions, while LUSC shows "
            "higher rates of TP53 alterations, FGFR1 amplifications, and SOX2 amplification.\n\n"
            "Small cell lung cancer (SCLC) has been reclassified into molecular subtypes defined by dominant transcription "
            "factors — ASCL1 (SCLC-A), NEUROD1 (SCLC-N), POU2F3 (SCLC-P), and YAP1 (SCLC-Y) — each with distinct "
            "therapeutic vulnerabilities. Proteogenomic studies have added layers of understanding beyond what genomics "
            "alone revealed, identifying phosphoproteomic signatures and post-translational modifications that define "
            "clinically relevant subgroups.\n\n"
            "Co-mutation patterns, particularly involving TP53/KRAS, STK11/KRAS, and KEAP1/KRAS in LUAD, have emerged as "
            "critical determinants of both prognosis and immunotherapy response. Histologic transformation, especially "
            "NSCLC-to-SCLC transformation under EGFR TKI pressure, represents a mechanism of acquired resistance with "
            "significant molecular underpinnings."
        ),
        "theme_02": (
            "Multi-omics integration methods have evolved from simple concatenation approaches to sophisticated "
            "statistical and deep learning frameworks. Established tools include iCluster for joint latent variable "
            "modeling, Similarity Network Fusion (SNF) for patient similarity networks, MOFA/MOFA+ for multi-omics "
            "factor analysis, and DIABLO (mixOmics) for supervised multi-block integration.\n\n"
            "Benchmarking studies have systematically evaluated these methods, revealing that no single approach "
            "dominates across all cancer types and data configurations. The choice of integration strategy (early, "
            "intermediate, or late fusion) depends on the specific research question, available data types, and "
            "sample sizes. Deep learning approaches, including variational autoencoders and graph neural networks, "
            "show promise for learning non-linear relationships across omics layers but require larger datasets "
            "and careful regularization.\n\n"
            "Consensus clustering across multiple algorithms and parameter settings has become standard practice "
            "for robust subtype discovery. Tools like MOVICS provide comprehensive frameworks that combine multiple "
            "integration algorithms with downstream analysis pipelines."
        ),
        "theme_03": (
            "Multi-omics integration has been applied to lung cancer for subtype discovery, prognosis prediction, "
            "and therapeutic stratification. Proteogenomic studies from CPTAC and collaborating groups have revealed "
            "that protein-level alterations do not always mirror transcriptomic changes, highlighting the importance "
            "of integrating multiple data layers. These studies identified novel therapeutic targets through "
            "phosphoproteomics that were invisible at the genomic level.\n\n"
            "Integrative analyses combining transcriptomic, methylomic, and proteomic data have refined NSCLC "
            "subtyping beyond traditional histopathological classification. Multi-omics approaches to tumor "
            "microenvironment characterization have revealed immune-excluded and immune-infiltrated subtypes "
            "with differential immunotherapy response. Multi-omics-based prognostic signatures have shown "
            "incremental improvement over single-omics approaches, though external validation remains limited."
        ),
        "theme_04": (
            "AI and machine learning have been extensively applied across the lung cancer continuum, from molecular "
            "subtyping to outcome prediction. Deep learning models applied to histopathology whole slide images "
            "can classify NSCLC subtypes (LUAD vs LUSC) with high accuracy and predict molecular alterations "
            "directly from H&E-stained slides.\n\n"
            "Radiomics and radiogenomics have linked imaging features to underlying molecular characteristics "
            "and treatment outcomes, though reproducibility across scanners and institutions remains a challenge. "
            "Foundation models pre-trained on large pathology image datasets have shown strong transfer learning "
            "capabilities, reducing the need for large labeled datasets in specific tasks.\n\n"
            "ML-based models for immunotherapy response prediction have incorporated tumor mutational burden, "
            "PD-L1 expression, gene expression signatures, and imaging features, with multi-modal approaches "
            "generally outperforming single-modality models. However, external validation studies consistently "
            "show performance degradation, and algorithmic bias related to demographic representation in "
            "training data has been identified as a significant concern."
        ),
        "theme_05": (
            "Sex and gender differences in lung cancer are well-documented but mechanistically underexplored. "
            "Women, particularly never-smokers, show higher rates of EGFR mutations in LUAD. Estrogen receptor "
            "signaling has been implicated in lung cancer biology, with preclinical evidence suggesting estrogen "
            "promotes proliferation through non-genomic signaling pathways.\n\n"
            "Immunotherapy outcomes show sex-specific patterns, with meta-analyses suggesting differential "
            "benefit from immune checkpoint inhibitors between sexes, though findings are not entirely consistent. "
            "Loss of Y chromosome in male tumors has been associated with altered immune surveillance and "
            "immunotherapy response. Epidemiological data consistently show women developing lung cancer at "
            "younger ages and with lighter smoking histories."
        ),
        "theme_06": (
            "Lung cancer in never-smokers represents a genomically and clinically distinct entity from "
            "smoking-associated lung cancer. Large genomic studies have identified three major molecular subtypes "
            "of never-smoker LUAD: piano (low mutation burden, often UBA1-driven), mezzo (EGFR-dominant), and "
            "forte (KRAS-dominant with higher mutation burden). EGFR mutations occur in 40-60% of East Asian "
            "never-smokers and 10-20% of Western never-smokers.\n\n"
            "Mutational signatures in never-smoker lung cancer show distinct patterns: absence of smoking-associated "
            "signatures (SBS4) and enrichment of clock-like signatures (SBS1, SBS5) and APOBEC signatures. "
            "The tumor microenvironment of never-smoker tumors tends to be less inflamed, potentially contributing "
            "to variable immunotherapy responses."
        ),
        "theme_07": (
            "Environmental exposures contribute to lung cancer through multiple molecular mechanisms. PM2.5 "
            "exposure has been linked to EGFR-driven lung adenocarcinoma in never-smokers through promotion of "
            "pre-existing EGFR-mutant clones via inflammatory signaling rather than direct mutagenesis. Radon "
            "exposure increases lung cancer risk in a dose-dependent manner, with characteristic chromosomal "
            "aberrations distinct from smoking-related damage.\n\n"
            "Occupational exposures to asbestos, silica, and diesel exhaust carry well-established lung cancer "
            "risks with distinct molecular signatures. Indoor air pollution from cooking fumes and biomass "
            "combustion disproportionately affects women in Asian populations and has been associated with "
            "specific mutational patterns in LUAD."
        ),
        "theme_08": (
            "Epigenetic alterations are pervasive in lung cancer and operate across multiple regulatory layers. "
            "DNA methylation changes, including hypermethylation of tumor suppressors (CDKN2A, RASSF1A, MGMT) "
            "and global hypomethylation, are early events in lung carcinogenesis. Methylation-based classifiers "
            "can distinguish NSCLC subtypes and predict prognosis.\n\n"
            "Non-coding RNAs, particularly miRNAs and lncRNAs, function as both oncogenes and tumor suppressors "
            "in lung cancer. Chromatin accessibility mapping via ATAC-seq has revealed enhancer landscapes that "
            "define lung cancer subtypes and identify master transcription factors. cfDNA methylation-based "
            "liquid biopsy approaches show promise for early detection and minimal residual disease monitoring."
        ),
        "theme_09": (
            "Immune biomarkers for immunotherapy response prediction in NSCLC extend well beyond PD-L1 expression. "
            "Tumor mutational burden (TMB) correlates with immunotherapy benefit but has limitations in its "
            "predictive value, particularly in specific molecular contexts (e.g., STK11/KEAP1 co-mutated tumors "
            "respond poorly despite adequate TMB).\n\n"
            "Pan-cancer immune landscape analyses have classified tumors into immune subtypes with distinct "
            "biological properties and treatment implications. Gene expression signatures reflecting T cell "
            "inflammation and interferon signaling have shown reproducible associations with immunotherapy "
            "response across tumor types. The gut microbiome has emerged as a modulator of immunotherapy efficacy."
        ),
        "theme_10": (
            "Despite advances in precision oncology, significant translational bottlenecks persist in lung cancer. "
            "Biomarker testing rates remain suboptimal, with disparities by race, socioeconomic status, geographic "
            "location, and insurance coverage. Many molecularly defined patients never receive matched targeted "
            "therapies due to access barriers, testing gaps, or rapid clinical deterioration.\n\n"
            "Real-world evidence studies show that outcomes for NSCLC patients receiving targeted therapies or "
            "immunotherapy are more heterogeneous than clinical trial results, reflecting broader patient "
            "populations and practice variation. Clinical trial representation of women, minorities, and "
            "older adults remains inadequate."
        ),
        "theme_11": (
            "Drug repurposing leverages computational and multi-omics approaches to identify new therapeutic "
            "indications for existing drugs. Connectivity Map (CMap) approaches have identified candidates by "
            "matching drug-induced gene expression signatures to disease signatures. Pharmacogenomic databases "
            "(GDSC, CCLE, PRISM) provide large-scale drug sensitivity data linked to molecular features.\n\n"
            "Synthetic lethality approaches, particularly exploiting KRAS or STK11/KEAP1 dependencies, offer "
            "targeted therapeutic strategies. Network pharmacology integrates drug-target-disease networks for "
            "systematic identification of repurposing candidates. Multi-omics integration enhances drug response "
            "prediction beyond single-omics approaches."
        ),
        "theme_12": (
            "Emerging technologies are transforming lung cancer research at unprecedented resolution. Single-cell "
            "RNA sequencing has revealed extensive intratumoral heterogeneity and complex tumor microenvironment "
            "compositions, including novel stromal and immune cell states. Spatial transcriptomics and spatial "
            "proteomics preserve tissue architecture while providing molecular detail, enabling characterization "
            "of spatial organization of tumor-immune interactions.\n\n"
            "Liquid biopsy approaches, including ctDNA analysis and cfDNA methylation profiling, enable non-invasive "
            "monitoring of tumor dynamics, early detection, and minimal residual disease assessment. Metabolomics "
            "and lipidomics add functional dimensions to lung cancer characterization. The lung and gut microbiome "
            "have been linked to lung cancer susceptibility and immunotherapy response."
        ),
    }
    return texts.get(theme_id, "Literature analysis pending detailed review of collected papers.")


def _generate_consensus(theme_id, tier_a, tier_b):
    """Generate consensus section."""
    consensus = {
        "theme_01": (
            "- LUAD and LUSC are molecularly distinct diseases requiring different therapeutic approaches\n"
            "- EGFR, KRAS, and ALK are established actionable drivers in LUAD\n"
            "- SCLC can be classified into transcription factor-defined subtypes (ASCL1, NEUROD1, POU2F3, YAP1)\n"
            "- Co-mutation patterns (especially KRAS/STK11/KEAP1) have prognostic and predictive significance\n"
            "- Proteogenomic profiling adds clinically relevant information beyond genomics alone"
        ),
        "theme_02": (
            "- Multi-omics integration outperforms single-omics analysis for subtype discovery\n"
            "- No single integration method dominates across all scenarios\n"
            "- Consensus approaches combining multiple methods improve robustness\n"
            "- Deep learning methods require larger sample sizes but can capture non-linear relationships\n"
            "- Benchmarking on standardized datasets is essential for fair method comparison"
        ),
        "theme_03": (
            "- Proteogenomic integration reveals clinically relevant features invisible to genomics alone\n"
            "- Multi-omics prognosis models modestly outperform single-omics signatures\n"
            "- Tumor microenvironment characterization benefits from multi-omics approaches\n"
            "- External validation of multi-omics signatures remains the major bottleneck"
        ),
        "theme_04": (
            "- Deep learning can classify NSCLC subtypes from histopathology with high accuracy\n"
            "- Multi-modal AI models generally outperform single-modality approaches\n"
            "- External validation consistently shows performance degradation\n"
            "- Foundation models reduce the need for large labeled datasets\n"
            "- Radiomics features are sensitive to acquisition parameters and require harmonization"
        ),
        "theme_05": (
            "- Women have higher EGFR mutation rates in LUAD, especially never-smokers\n"
            "- Sex-specific differences in immunotherapy outcomes exist but effect sizes are debated\n"
            "- Estrogen receptor biology is relevant to lung cancer pathogenesis\n"
            "- Sex-stratified analyses remain underperformed in most clinical and genomic studies"
        ),
        "theme_06": (
            "- Never-smoker lung cancer is genomically distinct from smoking-associated disease\n"
            "- EGFR mutations are the most common drivers in never-smoker LUAD\n"
            "- Mutational signatures differ fundamentally between smokers and never-smokers\n"
            "- Never-smoker LUAD in East Asian populations has distinctive molecular features"
        ),
        "theme_07": (
            "- PM2.5 and air pollution are established lung cancer risk factors\n"
            "- Environmental exposures can promote lung cancer through non-mutagenic mechanisms\n"
            "- Radon exposure increases risk in a dose-dependent manner\n"
            "- Indoor air pollution disproportionately affects women in certain populations"
        ),
        "theme_08": (
            "- DNA methylation changes are early events in lung carcinogenesis\n"
            "- Hypermethylation of specific tumor suppressors is reproducible across studies\n"
            "- Non-coding RNAs play functional roles in lung cancer biology\n"
            "- cfDNA methylation shows promise as a liquid biopsy biomarker"
        ),
        "theme_09": (
            "- PD-L1 alone is an imperfect predictor of immunotherapy response\n"
            "- TMB provides additional but imperfect predictive value\n"
            "- STK11/KEAP1 co-mutations confer immunotherapy resistance in NSCLC\n"
            "- Multi-parameter biomarker approaches outperform single markers"
        ),
        "theme_10": (
            "- Biomarker testing rates are suboptimal and inequitable\n"
            "- Real-world outcomes are more heterogeneous than clinical trial results\n"
            "- Disparities in precision oncology access exist along racial, socioeconomic, and geographic lines\n"
            "- Guideline-concordant care improves outcomes but adherence varies"
        ),
        "theme_11": (
            "- Computational drug repurposing can identify viable candidates\n"
            "- Pharmacogenomic databases enable systematic drug-gene interaction analysis\n"
            "- Multi-omics integration enhances drug response prediction\n"
            "- Synthetic lethality is a promising strategy for KRAS-mutant lung cancers"
        ),
        "theme_12": (
            "- Single-cell approaches reveal previously unrecognized cellular heterogeneity\n"
            "- Spatial technologies add critical architectural context to molecular data\n"
            "- Liquid biopsy technologies are approaching clinical utility for multiple applications\n"
            "- The microbiome modulates immunotherapy response"
        ),
    }
    return consensus.get(theme_id, "Consensus analysis requires detailed paper review.")


def _generate_disagreements(theme_id, tier_a, tier_b):
    """Generate disagreements/uncertainties section."""
    disagreements = {
        "theme_01": (
            "- The number and definition of LUAD molecular subtypes varies across studies\n"
            "- Whether proteogenomic subtypes are clinically actionable remains debated\n"
            "- The clinical significance of the SCLC-Y subtype is contested\n"
            "- Optimal molecular classification systems for clinical use are not standardized\n"
            "- The extent to which intratumoral heterogeneity undermines bulk-derived subtypes is unclear"
        ),
        "theme_02": (
            "- Early vs. late vs. intermediate integration: no consensus on optimal strategy\n"
            "- Whether deep learning methods genuinely outperform simpler statistical methods at typical sample sizes\n"
            "- How to handle missing data across omics layers\n"
            "- Appropriate metrics for evaluating integration quality\n"
            "- Scalability of current methods to 5+ omics layers simultaneously"
        ),
        "theme_03": (
            "- Whether multi-omics signatures offer sufficient incremental value over simpler models\n"
            "- Optimal omics combination for specific clinical endpoints\n"
            "- How to validate multi-omics findings when independent multi-omics datasets are rare\n"
            "- Whether batch effects across cohorts compromise multi-omics discoveries"
        ),
        "theme_04": (
            "- Whether AI models should replace or augment pathologist assessment\n"
            "- Fair benchmarking practices for medical AI across demographic groups\n"
            "- Extent of data leakage in published studies\n"
            "- Whether foundation models trained primarily on Western cohorts generalize globally\n"
            "- Optimal regulatory frameworks for clinical AI deployment"
        ),
        "theme_05": (
            "- Whether sex-based differences in immunotherapy benefit are biologically driven or confounded\n"
            "- The role of estrogen receptor signaling: direct oncogenic driver vs. modifier\n"
            "- Whether sex-stratified dosing is warranted for targeted therapies\n"
            "- How to separate sex (biological) from gender (sociocultural) effects in outcomes research"
        ),
        "theme_06": (
            "- The etiological contribution of specific environmental exposures in never-smokers\n"
            "- Whether never-smoker lung cancer immunotherapy response differs fundamentally\n"
            "- Optimal screening strategies for never-smokers at risk\n"
            "- Whether APOBEC mutagenesis has specific triggers in never-smoker lung cancer"
        ),
        "theme_07": (
            "- Whether PM2.5 acts primarily through mutagenic or promotional mechanisms\n"
            "- The threshold of exposure duration/level for cancer risk\n"
            "- How to attribute lung cancer risk to individual exposures in multi-exposure settings\n"
            "- Whether e-cigarette exposure carries long-term lung cancer risk"
        ),
        "theme_08": (
            "- Which epigenetic marks are drivers vs. passengers in lung carcinogenesis\n"
            "- Functional significance of many reported lncRNA associations\n"
            "- Reproducibility of miRNA prognostic signatures across populations\n"
            "- Whether epigenetic therapies can be effective in solid tumors"
        ),
        "theme_09": (
            "- Optimal TMB threshold for clinical decision-making\n"
            "- Whether composite biomarkers significantly outperform individual markers in practice\n"
            "- The degree to which microbiome modulation can improve immunotherapy outcomes\n"
            "- How to standardize HLA typing for immunotherapy prediction"
        ),
        "theme_10": (
            "- Whether real-world evidence should inform treatment guidelines to the same degree as RCTs\n"
            "- How to address structural barriers to biomarker testing\n"
            "- Whether molecular tumor boards improve outcomes vs. standard oncology practice\n"
            "- The role of direct-to-consumer genomic testing in oncology"
        ),
        "theme_11": (
            "- Whether computational drug repurposing predictions translate to clinical success at meaningful rates\n"
            "- Optimal experimental validation frameworks for repurposing candidates\n"
            "- How to prioritize among many predicted candidates for clinical development\n"
            "- Whether network pharmacology approaches capture real biological complexity"
        ),
        "theme_12": (
            "- Whether single-cell findings from small tumor biopsies represent whole-tumor biology\n"
            "- Technical reproducibility of spatial omics platforms\n"
            "- Sensitivity and specificity of liquid biopsy for early-stage detection\n"
            "- Clinical utility of microbiome-based interventions"
        ),
    }
    return disagreements.get(theme_id, "Disagreements require detailed analysis.")


def _generate_gaps(theme_id, tier_a, tier_b):
    """Generate gaps and open questions."""
    gaps = {
        "theme_01": (
            "- Limited multi-omics characterization of LUSC compared to LUAD\n"
            "- Pre-neoplastic lesion molecular evolution poorly understood\n"
            "- Mixed histology and rare subtypes (large cell, sarcomatoid) molecularly understudied\n"
            "- Longitudinal molecular profiling through treatment and resistance is sparse\n"
            "- Non-European ancestry cohorts underrepresented in large-scale molecular studies\n"
            "- Sex-stratified molecular characterization rarely performed systematically"
        ),
        "theme_02": (
            "- Few methods designed for clinical-scale deployment (runtime, interpretability)\n"
            "- Integration of clinical variables with omics data not well standardized\n"
            "- Methods for integrating single-cell multi-omics are in early stages\n"
            "- Spatial multi-omics integration tools are nascent\n"
            "- Handling of temporal/longitudinal multi-omics data\n"
            "- Methods for causal inference from multi-omics data"
        ),
        "theme_03": (
            "- Very few lung cancer multi-omics studies include matched pharmacogenomic data\n"
            "- Limited application of multi-omics to radiation response in lung cancer\n"
            "- Early detection multi-omics approaches are in early stages\n"
            "- No multi-omics studies focused specifically on NSCLC in never-smokers\n"
            "- Sex-stratified multi-omics analyses nearly absent"
        ),
        "theme_04": (
            "- Few ML models validated on multi-ethnic, multi-institutional cohorts\n"
            "- Absence of sex-stratified AI model development and evaluation\n"
            "- Limited AI tools for never-smoker NSCLC specifically\n"
            "- Integration of molecular data with clinical AI remains primitive\n"
            "- Regulatory frameworks lag behind technical capabilities\n"
            "- AI fairness and bias assessment rarely performed for oncology models"
        ),
        "theme_05": (
            "- Mechanistic studies of sex hormone interactions with lung cancer signaling are sparse\n"
            "- Sex-stratified drug response data largely absent from pharmacogenomic databases\n"
            "- Y chromosome loss in lung cancer poorly characterized\n"
            "- Pregnancy-associated lung cancer understudied molecularly\n"
            "- Sex-specific biomarker panels for immunotherapy selection absent"
        ),
        "theme_06": (
            "- Etiological mechanisms in many never-smoker lung cancers remain unknown\n"
            "- Limited immunoprofiling studies focused on never-smoker tumors\n"
            "- No clinical trials specifically designed for never-smoker molecular subtypes\n"
            "- Never-smoker representation in liquid biopsy validation studies is low\n"
            "- Interaction between germline risk variants and environmental exposures understudied"
        ),
        "theme_07": (
            "- Exposome-scale studies linking environmental exposures to molecular subtypes are rare\n"
            "- Long-term molecular effects of wildfire smoke exposure on lung cancer are unknown\n"
            "- PFAS exposure and lung cancer molecular mechanisms unexplored\n"
            "- Interaction between multiple exposures (additive vs. synergistic) poorly quantified\n"
            "- Environmental justice dimensions of exposure-related lung cancer understudied"
        ),
        "theme_08": (
            "- Causal vs. consequential epigenetic changes not well distinguished\n"
            "- Single-cell epigenomic profiling in lung cancer is limited\n"
            "- Epigenetic therapy clinical trials in lung cancer are few\n"
            "- Integration of epigenomic with genomic/transcriptomic data for subtyping needs work\n"
            "- Longitudinal epigenetic monitoring through treatment underexplored"
        ),
        "theme_09": (
            "- Composite biomarker panels not yet standardized for clinical use\n"
            "- Spatial immune biomarkers (e.g., immune proximity scores) not validated prospectively\n"
            "- Biomarker dynamics during treatment poorly captured\n"
            "- Microbiome-based immunotherapy prediction requires larger validation cohorts\n"
            "- Neoantigen-based personalized approaches need outcome data"
        ),
        "theme_10": (
            "- Interventions to improve biomarker testing rates not well evaluated\n"
            "- Real-world evidence from low- and middle-income countries is minimal\n"
            "- Patient-reported outcomes rarely integrated with molecular data\n"
            "- Impact of molecular tumor boards vs. standard care not rigorously compared\n"
            "- Cost-effectiveness of multi-omics precision oncology not established"
        ),
        "theme_11": (
            "- Translation of computational predictions to clinical trials remains low\n"
            "- Drug combination optimization using multi-omics data is nascent\n"
            "- Lung cancer-specific drug repurposing studies are fewer than pan-cancer\n"
            "- Dimethyl fumarate and other KEAP1-targeting repurposing candidates need clinical data\n"
            "- Patient-derived organoid validation of repurposing candidates limited"
        ),
        "theme_12": (
            "- Multi-modal single-cell + spatial integration methods are in early development\n"
            "- Clinical validation of liquid biopsy for early lung cancer detection ongoing\n"
            "- Metabolomic profiling of lung cancer subtypes is sparse\n"
            "- Spatial omics studies in never-smoker lung cancer are absent\n"
            "- Cost and scalability barriers limit clinical adoption of these technologies\n"
            "- Longitudinal liquid biopsy monitoring studies need larger cohorts"
        ),
    }
    return gaps.get(theme_id, "Gap analysis requires detailed review.")


def _generate_writing_notes(theme_id, papers, tier_a, tier_b):
    """Generate writing notes."""
    # Count bridge papers (appear in multiple themes)
    bridge = [p for p in papers if len(p.get("themes", [])) >= 2]

    # Count recent papers (2023+)
    recent = [p for p in papers if (p.get("year", 0) or 0) >= 2023]

    notes = f"- **Bridge papers** (spanning multiple themes): {len(bridge)} papers\n"
    notes += f"- **Recent papers** (2023+): {len(recent)} papers\n"
    notes += f"- **Tier A papers**: {len(tier_a)} — prioritize these for citation\n"
    notes += f"- **Tier B papers**: {len(tier_b)} — use selectively for supporting evidence\n\n"

    # Retracted papers
    retracted = [p for p in papers if p.get("is_retracted")]
    if retracted:
        notes += f"- **RETRACTED papers found**: {len(retracted)} — DO NOT CITE:\n"
        for p in retracted:
            notes += f"  - PMID {p['pmid']}: {p.get('title', '')[:60]}...\n"
        notes += "\n"

    # Flagged papers
    flagged = [p for p in papers if "FLAGGED" in (p.get("notes", "") or "")]
    if flagged:
        notes += f"- **Flagged for manual review**: {len(flagged)} papers\n"

    return notes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python synthesize.py <theme_id|all>")
        sys.exit(1)

    target = sys.argv[1]
    if target == "all":
        for theme_id in sorted(THEMES.keys()):
            synthesize_theme(theme_id)
    elif target in THEMES:
        synthesize_theme(target)
    else:
        print(f"Unknown theme: {target}")
        sys.exit(1)
