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
| 2 | **Xu, Beck & Alber 2012 — Fourier-space constrained fast alignment** ✅ | Modules 03, 11 |
| 3 | Xu & Alber 2012 — gradient-based precise alignment ✅ | Module 12 |
| 4 | Xu & Alber 2013 — target segmentation in crowded subtomograms ✅ | Module 12 |
| 5 | **Zhao *et al.* 2018 — FAML** ✅ | Modules 04, 13 |
| 6 | Lü *et al.* 2019 — MPI + stochastic average gradient ✅ | Module 12 |
| 7 | **Zeng & Xu 2020 — Gum-Net** ✅ | Module 19 |
| 8 | Jiang *et al.* 2025 — BOE-ViT 🟡 | Module 19 |

### Path 2 · Discovering what is in a cell (template-free and unsupervised)

| Order | Paper | Prepare with |
|---|---|---|
| 1 | Beck *et al.* 2011 — the proteome in space and time (review) ✅ | Modules 00, 25 |
| 2 | Xu, Beck & Alber 2011 — template-free detection 🟡 | Module 14 |
| 3 | **Xu *et al.* 2019 — de novo structural pattern mining (MPP)** ✅ | Module 14 |
| 4 | Zeng, Howe & Xu 2021 — Jim-Net ✅ | Module 20 |
| 5 | **Zeng *et al.* 2023 — DISCA** ✅ | Modules 20, 26 |
| 6 | **Uddin *et al.* 2022 — Harmony** ✅ | Module 21 |
| 7 | Nair *et al.* 2025 — class discovery with semantic prototypes ✅ | Module 20 |
| 8 | Kim *et al.* 2023 — review of unbiased pattern mining 🟡 | Modules 13, 26 |

### Path 3 · Finding particles

| Order | Paper | Prepare with |
|---|---|---|
| 1 | **Pei *et al.* 2016 — crowded-cell simulation and picking assessment** ✅ | Modules 08, 10 |
| 2 | Wang *et al.* 2018 — pseudo-structures for template-matching statistics ✅ | Module 10 |
| 3 | Zhou *et al.* 2018 — feature-decomposition saliency ✅ | Module 10 |
| 4 | Li R *et al.* 2019 — Faster R-CNN for mitochondria ✅ | Module 16 |
| 5 | **Uddin *et al.* 2025 — TomoPicker (sparse labels)** ✅ | Module 23 |
| 6 | **Xu, Zhan & Xu 2025 — CryoMAE** ✅ | Module 23 |
| 7 | RobPicker ⚠️ (read when available) | Module 23 |

### Path 4 · Deep learning with real-world constraints (labels, domains, robustness)

| Order | Paper | Prepare with |
|---|---|---|
| 1 | **Xu *et al.* 2017 — deep subdivision** ✅ | Modules 05, 15 |
| 2 | Che *et al.* 2018 — improved 3D CNNs ✅ | Module 15 |
| 3 | Zhao, Zhou *et al.* 2018 — Respond-CAM ✅ | Module 16 |
| 4 | **Li R *et al.* 2020 — few-shot ProtoNet3D** ✅ | Module 17 |
| 5 | Du *et al.* 2021 — HAL active learning ✅ | Module 17 |
| 6 | **Lin, Zeng *et al.* 2019 — 3D-ADA** ✅ | Module 18 |
| 7 | Bandyopadhyay *et al.* 2022 — Cryo-Shift ✅ | Module 18 |
| 8 | Jain, Li & Xu 2024 — transfer from video models ✅ | Module 15 |

### Path 5 · Images that need cleaning, segmenting and simulating

| Order | Paper | Prepare with |
|---|---|---|
| 1 | Liu S *et al.* 2020 — unified packing for simulation ✅ | Module 08 |
| 2 | Wu *et al.* 2022 — CryoETGAN ✅ | Module 18 |
| 3 | **Liu X *et al.* 2025 — J-invariant volume shuffle** ✅ | Module 22 |
| 4 | Zeng *et al.* 2024 — DUAL ✅ | Module 22 |
| 5 | **Zhao *et al.* 2024 — CryoSAM** ✅ | Module 24 |
| 6 | Uddin *et al.* 2026 — Stable Diffusion segmentation 🟡 | Module 24 |
| 7 | Salla *et al.* 2026 — TopoFuse ✅ | Module 24 |

### Path 6 · From structures to biology

| Order | Paper | Prepare with |
|---|---|---|
| 1 | **Zhang *et al.* 2010 — simultaneous fitting by mathematical programming** ✅ | Module 25 |
| 2 | Thalassinos *et al.* 2013 — conformational states (perspective) 🟡 | Modules 13, 25 |
| 3 | **Jiang *et al.* 2025 — the fungal plasma membrane and caspofungin** ✅ | Module 25 |
| 4 | DISCA's biological findings (Zeng *et al.* 2023) ✅ | Modules 20, 25 |

**Minimum set for the course goal.** If time is short, read the bold papers of paths 1–3 and 6 with the worksheet; for
everything else, passes 1–3 plus the module's paper-connection box.

---

## 3 · The audit worksheet

Copy this table for every paper you read in full. A filled-in example for DISCA is in
[Module 26](notebooks/26_capstone_visual_proteomics.ipynb), Section 12.

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
| Thresholds or hyper-parameters chosen on the test data | performance is over-estimated (data leakage) | 05, 26 |
| Particles, not tomograms or cells, treated as independent replicates | p-values become meaningless (pseudo-replication) | 04, 25 |
| Half-maps refined against a shared reference; no mask or criterion reported | FSC resolution is inflated | 09, 26 |
| A structure recovered from noise by aligning to a template | reference bias / "Einstein from noise" | 13 |
| Clusters that track orientation or the missing wedge, not structure | classification by artefact | 13, 20 |
| Only simulated data, or simulated train and test from the same simulator | simulation-to-real gap unknown | 08, 18 |
| A spatial "pattern" tested against a null model without excluded volume or the right region | inhomogeneity mistaken for clustering | 25, 26 |
| Identity claimed from a low-resolution blob | similar-sized complexes look alike (e.g. RuBisCO and ClpB merge) | 20, 26 |
| Paper and released code disagree (loss, architecture, data) | results may not be reproducible as described | atlas corrections |
| "Up to" numbers in the abstract | the best case, not the typical case (e.g. CryoMAE's 22.4 % vs ≈ 11 % average) | 23 |

---

## 5 · Where to find the papers

Start from the DOI links in the [atlas](PAPER_ATLAS.md). Many lab papers are open access (PMC author manuscripts, arXiv,
CVF open access, bioRxiv, BMC, Frontiers, PLOS). Released code is usually in [AITom](https://github.com/xulabs/aitom) — the
atlas and each module's paper box give the folder. For papers marked ⚠️, ask the lab or your instructor for a copy before
drawing conclusions about their content.
