# 📖 Reading guide — how to read the lab's cryo-ET and cryo-EM papers

This guide turns the course into a reading programme. It has four parts: a **five-pass method** for reading any methods
paper, **reading paths** through the [paper atlas](PAPER_ATLAS.md), the **audit worksheet**, and a list of **red flags**.
Each paper in a path is paired with the module that prepares you for it.

---

## 1 · The five-pass method

Methods papers are not read front to back. Use five short passes, and stop whenever you have what you need.

| Pass | Read | Ask | Time |
|---|---|---|---|
| 1 · Map | title, abstract, figure 1, the last paragraph of the introduction | What biological or technical problem? What is claimed to be new? | 10 min |
| 2 · Evidence | every figure and table with its caption; the results headings | What was measured, on which data, against which baseline? Which numbers carry the claim? | 30 min |
| 3 · Method | the methods overview and the **one** key equation (loss, score, model) | Can I say the equation in words? What are the inputs and outputs? Which module taught this idea? | 30–60 min |
| 4 · Doubt | limitations, supplementary material, data and code availability | Where could it fail? What is the unit of replication? Was anything tuned on the test data? | 20 min |
| 5 · Rebuild | the module's toy, then the released code (often in [AITom](https://github.com/xulabs/aitom)) | Can I reproduce the central effect in a toy? Does the code match the paper? | 1–3 h |

**Translating equations.** Every equation in the course has an *"in words"* reading. Do the same for papers: name each
symbol, say what is summed or maximised over, and say what makes the quantity large or small. If you cannot, find the
module in the atlas index and redo its theory section.

**Reading figures.** For each panel write one sentence: *"This panel shows ___ as a function of ___ for ___; the point is
___."* If the point is not obvious, look for the comparison (baseline, control, ablation) the panel is built around.

---

## 2 · Reading paths

Each path is ordered from foundations to frontier. **Bold** = read in full with the audit worksheet; the others can be read
in passes 1–3. Status marks follow the atlas (✅ verified · 🟡 partial · ⚠️ not verified).

### Path 1 · Alignment and averaging (the core of subtomogram analysis)

| Order | Paper | Prepare with |
|---|---|---|
| 1 | Xu, Zhang & Alber 2009 — rotation-invariant features 🟡 | Module 02 |
| 2 | **Xu, Beck & Alber 2012 — Fourier-space constrained fast alignment** ✅ | Modules 03, 12 |
| 3 | Xu & Alber 2012 — gradient-based precise alignment ✅ | Module 13 |
| 4 | Xu & Alber 2013 — target segmentation in crowded subtomograms ✅ | Module 13 |
| 5 | **Zhao *et al.* 2018 — FAML** ✅ | Modules 04, 14 |
| 6 | Lü *et al.* 2019 — MPI + stochastic average gradient ✅ | Module 13 |
| 7 | **Zeng & Xu 2020 — Gum-Net** ✅ | Module 21 |
| 8 | Jiang *et al.* 2025 — BOE-ViT 🟡 | Module 21 |

### Path 2 · Discovering what is in a cell (template-free and unsupervised)

| Order | Paper | Prepare with |
|---|---|---|
| 1 | Beck *et al.* 2011 — the proteome in space and time (review) ✅ | Modules 00, 33 |
| 2 | Xu, Beck & Alber 2011 — template-free detection 🟡 | Module 15 |
| 3 | **Xu *et al.* 2019 — de novo structural pattern mining (MPP)** ✅ | Module 15 |
| 4 | Zeng, Howe & Xu 2021 — Jim-Net ✅ | Module 22 |
| 5 | **Zeng *et al.* 2023 — DISCA** ✅ | Modules 22, 34 |
| 6 | **Uddin *et al.* 2022 — Harmony** ✅ | Module 23 |
| 7 | Nair *et al.* 2025 — class discovery with semantic prototypes ✅ | Module 22 |
| 8 | Kim *et al.* 2023 — review of unbiased pattern mining 🟡 | Modules 14, 34 |

### Path 3 · Finding particles

| Order | Paper | Prepare with |
|---|---|---|
| 1 | **Pei *et al.* 2016 — crowded-cell simulation and picking assessment** ✅ | Modules 09, 11 |
| 2 | Wang *et al.* 2018 — pseudo-structures for template-matching statistics ✅ | Module 11 |
| 3 | Zhou *et al.* 2018 — feature-decomposition saliency ✅ | Module 11 |
| 4 | Li R *et al.* 2019 — Faster R-CNN for mitochondria ✅ | Module 17 |
| 5 | **Uddin *et al.* 2025 — TomoPicker (sparse labels)** ✅ | Module 31 |
| 6 | **Xu, Zhan & Xu 2025 — CryoMAE** ✅ | Module 31 |
| 7 | RobPicker ⚠️ (read when available) | Module 31 |

### Path 4 · Deep learning with real-world constraints (labels, domains, robustness)

| Order | Paper | Prepare with |
|---|---|---|
| 1 | **Xu *et al.* 2017 — deep subdivision** ✅ | Modules 05, 16 |
| 2 | Che *et al.* 2018 — improved 3D CNNs ✅ | Module 16 |
| 3 | Zhao, Zhou *et al.* 2018 — Respond-CAM ✅ | Module 17 |
| 4 | **Li R *et al.* 2020 — few-shot ProtoNet3D** ✅ | Module 19 |
| 5 | Du *et al.* 2021 — HAL active learning ✅ | Module 19 |
| 6 | **Lin, Zeng *et al.* 2019 — 3D-ADA** ✅ | Module 20 |
| 7 | Bandyopadhyay *et al.* 2022 — Cryo-Shift ✅ | Module 20 |
| 8 | Jain, Li & Xu 2024 — transfer from video models ✅ | Module 16 |

### Path 5 · Images that need cleaning, segmenting and simulating

| Order | Paper | Prepare with |
|---|---|---|
| 1 | Liu S *et al.* 2020 — unified packing for simulation ✅ | Module 09 |
| 2 | Wu *et al.* 2022 — CryoETGAN ✅ | Module 20 |
| 3 | **Liu X *et al.* 2025 — J-invariant volume shuffle** ✅ | Module 24 |
| 4 | Zeng *et al.* 2024 — DUAL ✅ | Module 24 |
| 5 | **Zhao *et al.* 2024 — CryoSAM** ✅ | Module 32 |
| 6 | Uddin *et al.* 2026 — Stable Diffusion segmentation 🟡 | Module 32 |
| 7 | Salla *et al.* 2026 — TopoFuse ✅ | Module 32 |

### Path 6 · Molecules that move: Gaussian mixtures, neural fields and model series

| Order | Paper | Prepare with |
|---|---|---|
| 1 | **Chen & Ludtke 2021 — mixed-dimensional deep GMM (e2gmm)** ✅ | Modules 25, 26 |
| 2 | **Zhong *et al.* 2021 — cryoDRGN** ✅ | Module 27 |
| 3 | Chen, Toader & Lederman 2023 — scalable high-resolution deep GMMs ✅ | Module 26 |
| 4 | **Powell & Davis 2024 — tomoDRGN** ✅ | Module 28 |
| 5 | Chen, Schmid & Chiu 2024 — improving resolution and resolvability with GMMs ✅ | Module 29 |
| 6 | Chen 2025 — molecular model series ✅ | Module 30 |
| 7 | Chen 2026 — GMM-based focused refinement (arXiv) ✅ | Module 29 |

### Path 7 · New ways to image and annotate cells

| Order | Paper | Prepare with |
|---|---|---|
| 1 | **Chen *et al.* 2017 — CNN annotation of cellular tomograms** ✅ | Module 18 |
| 2 | Seifer *et al.* 2024 — optimizing contrast in 4D-STEM cryo-tomography 🟡 | Module 08 |
| 3 | **Seifer, Houben & Elbaum 2026 — shadow montage and cone-beam 4D-STEM tomography** ✅ | Module 08 |
| 4 | Kiriati, Fernández & Elbaum 2026 — *Tomo4D* and *Depth-resolved 4D-STEM by tomo4d* (abstracts) ⚠️ | Module 08 |

### Path 8 · From structures to biology

| Order | Paper | Prepare with |
|---|---|---|
| 1 | **Zhang *et al.* 2010 — simultaneous fitting by mathematical programming** ✅ | Module 33 |
| 2 | Thalassinos *et al.* 2013 — conformational states (perspective) 🟡 | Modules 14, 33 |
| 3 | **Jiang *et al.* 2025 — the fungal plasma membrane and caspofungin** ✅ | Module 33 |
| 4 | DISCA's biological findings (Zeng *et al.* 2023) ✅ | Modules 22, 33 |

**Minimum set for the course goal.** If time is short, read the bold papers of paths 1–3, 6 and 8 with the worksheet; for
everything else, passes 1–3 plus the module's paper-connection box.

---

## 3 · The audit worksheet

Copy this table for every paper you read in full. A filled-in example for DISCA is in
[Module 34](notebooks/34_capstone_visual_proteomics.ipynb), Section 12.

| Question | Your answer |
|---|---|
| **Biological question** — what would a biologist learn if the method works? | |
| **Data & split unit** — real or simulated? Which datasets (EMPIAR/EMDB IDs)? What is held out, and at which level (particle, tomogram, cell, dataset)? | |
| **Method** — inputs → outputs, in three steps | |
| **Key equation** — written out, and read in words | |
| **Baselines** — what is it compared with, and are the baselines tuned fairly? | |
| **Metrics** — which numbers carry the claim? Are they the right ones for the biological question? | |
| **Reported results** — the two or three numbers that matter, with their uncertainty | |
| **Failure case** — where does the method not work (SNR, size, abundance, domain)? | |
| **Falsification test** — what result would show the main claim is wrong, and was it checked? | |
| **Code & data** — released? Does the code match the paper? (see the atlas' correction notes for known mismatches) | |
| **Toy** — which module reproduces the central effect, and does it? | |

---

## 4 · Red flags (and where the course teaches each)

| Red flag | Why it matters | Module |
|---|---|---|
| Thresholds or hyper-parameters chosen on the test data | performance is over-estimated (data leakage) | 05, 34 |
| Particles, not tomograms or cells, treated as independent replicates | p-values become meaningless (pseudo-replication) | 04, 33 |
| Half-maps refined against a shared reference; no mask or criterion reported | FSC resolution is inflated | 10, 34 |
| A structure recovered from noise by aligning to a template | reference bias / "Einstein from noise" | 14 |
| Clusters that track orientation or the missing wedge, not structure | classification by artefact | 14, 22 |
| Only simulated data, or simulated train and test from the same simulator | simulation-to-real gap unknown | 09, 20 |
| A spatial "pattern" tested against a null model without excluded volume or the right region | inhomogeneity mistaken for clustering | 33, 34 |
| Identity claimed from a low-resolution blob | similar-sized complexes look alike (e.g. RuBisCO and ClpB merge) | 22, 34 |
| Paper and released code disagree (loss, architecture, data) | results may not be reproducible as described | atlas corrections |
| "Up to" numbers in the abstract | the best case, not the typical case (e.g. CryoMAE's 22.4 % vs ≈ 11 % average) | 31 |
| A motion read off a latent space without checking poses, masks or particle quality | misalignment and junk can look like conformational change | 26, 27 |
| A sharper flexible region reported with a *lower* global FSC — or the reverse | global FSC and local quality can disagree; ask for local resolution or map–model metrics | 29 |
| A clever method shown without a simple baseline | the baseline may do as well (e.g. a centred-density mask vs CAM pseudo-labels) | 17 |
| Methods described only in a conference abstract | details cannot be checked; do not build on them | 08 |

---

## 5 · Where to find the papers

Start from the DOI links in the [atlas](PAPER_ATLAS.md). Many lab papers are open access (PMC author manuscripts, arXiv,
CVF open access, bioRxiv, BMC, Frontiers, PLOS). Released code is usually in [AITom](https://github.com/xulabs/aitom) — the
atlas and each module's paper box give the folder. For papers marked ⚠️, ask the lab or your instructor for a copy before
drawing conclusions about their content.
