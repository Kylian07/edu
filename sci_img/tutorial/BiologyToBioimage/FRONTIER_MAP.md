# Frontier map: research areas → Level 2 modules

Level 2 of BiologyToBioimage (Modules 20–27) carries the ideas of the course core (Modules 00–19)
to current bioimage-analysis research. Use this map in both directions: when you meet a research
area or a method in a paper, find the module that teaches its foundations; when you finish a
module, find where its ideas are used and what to read and try next.

Every Level 2 module (i) explains the biology and the imaging/assay context, (ii) implements a toy
version of the field's core method on simulated data with a known truth, (iii) checks the method
against that truth (🧪 boxes), (iv) is honest about where the toy demo and the real method diverge,
and (v) ends with a 🧭 *From toy to real data* section and 📄 *Research connection* boxes naming
landmark papers, production tools and open questions. Statements about the state of a field are as
of late 2026.

---

## 1 · How Level 2 builds on Level 1

| Level 1 idea (module) | becomes, in Level 2 … (module) |
|---|---|
| A trained CNN classifier (08) and a U-Net segmenter (11) | pretrained, promptable, zero-shot segmentation foundation models; evaluating them honestly against a specialist baseline (20) |
| CNN-based deep learning (08); generative models — VAEs/GANs (13); denoising (16); restoration as an inverse problem (17) | paired image-to-image regression for virtual/label-free staining, and the hallucination risk of trusting a generated channel (21) |
| Classical features — GLCM, shape, Mahalanobis distance (07); learned features (08); dimensionality reduction (09); colocalization/spatial statistics (18) | per-cell morphological profiling, batch-effect correction, and hit-calling for high-content screens (22) |
| Colocalization and spatial-point-pattern statistics (18); dimensionality reduction / clustering ideas (09); segmentation as the source of per-cell data (10, 11) | multiplexed per-cell marker profiles, spatial neighbourhood enrichment, and a first graph neural network over a spatial graph (23) |
| A trained classifier's point predictions (08); a trained segmenter's point predictions (11) | calibration, aleatoric vs. epistemic uncertainty, ensembles/MC-dropout, and active learning (24) |
| A 2-D U-Net (11); a foundation-model segmenter (20) | 3-D convolutions, patch-based training and stitching, and chunked, multiscale storage for volumes too large to hold in memory (25) |
| A trained CNN classifier/segmenter (08, 11) | saliency/attribution, out-of-distribution failure, data leakage, and p-hacking by threshold-tuning (26) |
| Foundation models (20); image-based profiling (22); spatial omics (23); trustworthy-AI auditing (26) | a model-zoo registry, a scripted tool-orchestrating agent with a verification step, and multimodal (imaging + omics/clinical) fusion (27) |

## 2 · Research areas

### 🔬 Imaging foundation models, restoration and scale

| Area | Module | Landmark ideas and methods | Production tools · what to try next |
|---|---|---|---|
| Promptable, zero-shot segmentation | [20](notebooks/20_foundation_models_for_microscopy.ipynb) | Segment Anything (Kirillov et al. 2023); Cellpose's generalist, diameter-agnostic segmentation (Stringer et al. 2021; Pachitariu & Stringer 2022); micro-SAM (Archit et al. 2025) | Cellpose, micro-SAM · the BioImage Model Zoo (bioimage.io) |
| Virtual / label-free staining | [21](notebooks/21_virtual_staining_label_free_imaging.ipynb) | in-silico labeling (Christiansen et al. 2018); label-free prediction of fluorescence (Ounkomol et al. 2018); virtual histological staining (Rivenson et al. 2019) | paired-image models in the BioImage Model Zoo |
| Content-aware restoration, denoising, super-resolution | [16](notebooks/16_denoising_and_super_resolution.ipynb), [17](notebooks/17_restoration_and_inverse_problems.ipynb) | CARE (Weigert et al. 2018); classic Richardson–Lucy and Wiener deconvolution; SRCNN-style learned super-resolution; PALM/STORM single-molecule localisation super-resolution | CSBDeep/CARE, DeepImageJ |
| Volumetric and large-scale imaging | [25](notebooks/25_volumetric_and_large_scale_imaging.ipynb) | 3D U-Net (Çiçek et al. 2016); the OME-Zarr / NGFF chunked storage specification (Moore et al. 2021); large-scale light-sheet pipelines | napari, BigDataViewer/Fiji, OME-Zarr tooling |

### 🧪 Quantitative and spatial biology

| Area | Module | Landmark ideas and methods | Production tools · what to try next |
|---|---|---|---|
| Colocalization and spatial-point-pattern statistics | [18](notebooks/18_colocalization_and_spatial_statistics.ipynb) | Manders et al. (1993); Costes et al. (2004) automatic thresholding; Ripley (1977, 1981); Clark & Evans (1954) | Fiji/ImageJ colocalization and spatial-statistics plugins |
| Image-based phenotypic profiling | [22](notebooks/22_image_based_profiling_and_perturbation_biology.ipynb) | Cell Painting (Bray et al. 2016); data-analysis strategies for morphological profiling (Caicedo et al. 2017); the JUMP Cell Painting Consortium (Chandrasekaran et al. 2023) | CellProfiler, the JUMP data set |
| Spatial omics and multiplexed imaging | [23](notebooks/23_spatial_omics_and_multiplexed_imaging.ipynb) | CODEX (Goltsev et al. 2018); MERFISH (Chen et al. 2015); histoCAT (Schapiro et al. 2017) | Squidpy, 10x Genomics Xenium data |

### 🛡️ Trustworthy, data-efficient AI and systems

| Area | Module | Landmark ideas and methods | Production tools · what to try next |
|---|---|---|---|
| Uncertainty and active learning | [24](notebooks/24_uncertainty_and_active_learning.ipynb) | MC-dropout (Gal & Ghahramani 2016); deep ensembles (Lakshminarayanan et al. 2017); modern-network calibration (Guo et al. 2017); active-learning surveys (Settles 2009) | napari, ilastik (Berg et al. 2019) for human-in-the-loop annotation |
| Explainability and trustworthy ML | [26](notebooks/26_explainability_and_trustworthy_ai.ipynb) | Grad-CAM (Selvaraju et al. 2017); saliency maps (Simonyan et al. 2014); a well-known shortcut-learning failure in medical imaging (Zech et al. 2018); the DOME reporting recommendations (Walsh et al. 2021) | model cards; the DOME checklist |
| AI agents and multimodal pipelines | [27](notebooks/27_ai_agents_and_multimodal_pipelines.ipynb) | ReAct agents (Yao et al. 2023); AI systems for science (Boiko et al. 2023; Bran et al. 2024); the BioImage Model Zoo as a tool registry (Ouyang et al. 2022) | LLM APIs with tool use — always with verification |
| Integrative capstone | [28](notebooks/28_capstone_pipeline.ipynb) | a full simulate → restore → segment → classify → track → quantify pipeline, checked end to end against simulated truth | — |

## 3 · Open questions you will meet

- Do foundation segmentation models beat a well-tuned specialist U-Net on the data that actually
  matters to your lab, or only on broad benchmarks? (20)
- How do you decide, in practice, whether a virtual stain is trustworthy enough to base a
  biological conclusion on? (21)
- Can batch-effect correction remove technical variation without also removing the real treatment
  effect you are trying to measure? (22)
- Does a cell-type "niche" reflect a causal spatial interaction, or just a shared microenvironment?
  (23)
- How should a lab decide how many images to label next, and when an uncertainty estimate itself
  can be trusted? (24)
- What is lost by processing a large volume patch by patch rather than all at once, and when does
  it matter? (25)
- How much of a published bioimage-analysis benchmark result survives a leakage and
  distribution-shift audit? (26)
- What must a human always verify before acting on an AI agent's bioimage-analysis pipeline output?
  (27)
