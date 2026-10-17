# From Biology to Research: Cryo-ET and Cryo-EM with the Xu Lab

A two-semester, notebook-based course that takes a **first-year biology major** from "what is a ribosome?" to reading,
running and critiquing **the cryo-electron tomography (cryo-ET) and cryo-electron microscopy (cryo-EM) papers of the Xu
lab** — and a set of closely related papers on conformational heterogeneity (Gaussian mixture models, cryoDRGN,
tomoDRGN), automated annotation of cellular tomograms, and 4D-STEM tomography. The course has **35 modules (00–34)**.
Each one is an executable Jupyter notebook that runs on a free Google Colab CPU and turns one paper's core idea into a
small experiment you can change and break.

**Nothing is stored in the repository.** The molecules are real atomic models from the Protein Data Bank, downloaded
the first time a notebook needs them and cached on your computer, outside the repository; maps, cells, tomograms and
every figure are computed from them when the notebook runs. No pictures, maps or datasets are kept in the repository
(offline, code-built stand-ins of the same size and symmetry replace the PDB models, so every notebook still runs).

**Start here:** [00 · Welcome: from a crowded cell to molecular structures](notebooks/00_welcome_cells_to_structures.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/BiologyToResearch/notebooks/00_welcome_cells_to_structures.ipynb)

---

## Who it is for and what you will be able to do

**Assumed background:** high-school algebra and introductory cell biology. No programming, calculus or physics is assumed;
each is introduced when it is first needed, with plain-language "in words" readings of every equation.

**By the end you will be able to:**

1. Explain how a cryo-electron microscope turns a frozen cell into a 3D tomogram, and why the result is noisy, blurred by
   the contrast transfer function and missing a wedge of information; explain how scanning (4D-STEM) instruments record
   the same specimen differently.
2. Run — and modify — Python implementations of the core methods of the field: picking, wedge-aware alignment, averaging,
   maximum-likelihood and template-free classification, resolution estimation, 3D CNNs and tomogram annotation,
   few-label and unsupervised learning, deep alignment, disentanglement, self-supervised denoising, foundation-model
   segmentation.
3. Describe a molecule that moves: single-particle reconstruction, Gaussian mixture models, per-particle heterogeneity
   (e2gmm, cryoDRGN, tomoDRGN), focused refinement of flexible regions and series of atomic models.
4. For **any** paper in the [atlas](PAPER_ATLAS.md): state its biological question, data, core algorithm and key
   equation, evidence, baselines and limitations — and reproduce its central idea in a toy.
5. Turn particles and maps into biological claims with proper null models, units of replication and validation.
6. Plan a first real analysis with the lab's [AITom](https://github.com/xulabs/aitom) toolkit and public data (EMPIAR, EMDB,
   CZ cryoET Data Portal).

---

## Roadmap

| Part | Module | Time | Main papers (see the [atlas](PAPER_ATLAS.md)) |
|---|---|---|---|
| **A · Foundations** | [00 · Welcome: from a crowded cell to molecular structures](notebooks/00_welcome_cells_to_structures.ipynb) | 1–1.5 h | Beck *et al.* 2011; AITom; Kim *et al.* 2023 |
| | [01 · Python & NumPy for biologists: images, volumes and density maps](notebooks/01_python_arrays_density_maps.ipynb) | 1.5–2 h | previews of Zhang 2010, Xu 2009 |
| | [02 · Geometry of molecules: coordinates, rotations, symmetry and invariance](notebooks/02_rotations_geometry.ipynb) | 1.5–2 h | Xu, Zhang & Alber 2009 |
| | [03 · Waves and frequencies: the Fourier transform for biologists](notebooks/03_fourier_frequency.ipynb) | 2–2.5 h | foundations of Xu 2012, Gum-Net |
| | [04 · Noise, statistics and inference](notebooks/04_noise_statistics_inference.ipynb) | 2 h | foundations of FAML, MPP, DISCA |
| | [05 · Deep learning in one afternoon (PyTorch)](notebooks/05_deep_learning_pytorch.ipynb) | 2.5 h | SHREC'19/'20; Xu 2017 |
| **B · Imaging physics** | [06 · How an electron microscope makes an image](notebooks/06_electron_image_formation.ipynb) | 2 h | simulators of the lab; CryoMAE context |
| | [07 · Tomography: tilt series, back-projection and the missing wedge](notebooks/07_tomography_missing_wedge.ipynb) | 2 h | Han 2019; Zeng 2022 (J Comput Biol) |
| | [08 · Scanning the beam: 4D-STEM, shadow images and depth sectioning](notebooks/08_4dstem_shadow_tomography.ipynb) 🆕 | 2 h | **Seifer, Houben & Elbaum 2026**; Seifer *et al.* 2024; tomo4d abstracts 2026 ⚠️ |
| | [09 · Build an in silico cell: crowding, membranes and realistic tomograms](notebooks/09_in_silico_cell_simulation.ipynb) | 2 h | Pei 2016; Liu 2020 (×2); Wang 2018 |
| | [10 · How good is a map? FSC, half-maps, local resolution and particle selection](notebooks/10_resolution_validation.ipynb) | 2 h | Lü 2020; Shi 2020 |
| **C · Classical computational cryo-ET** | [11 · Finding particles: template matching, difference-of-Gaussians and their pitfalls](notebooks/11_particle_picking_classical.ipynb) | 2 h | Pei 2016; Wang 2018; Zhou 2018 |
| | [12 · Aligning subtomograms fast: constrained correlation and rotational search](notebooks/12_fast_subtomogram_alignment.ipynb) | 2.5 h | **Xu, Beck & Alber 2012** |
| | [13 · Precise alignment, crowded neighbours and scaling up to millions](notebooks/13_precise_alignment_crowding_scale.ipynb) | 2 h | Xu & Alber 2012, 2013; TomoMiner; Lü 2019 |
| | [14 · Averaging and classification: reference-free iteration and maximum likelihood](notebooks/14_averaging_classification_ml.ipynb) | 2.5 h | FAML 2018 |
| | [15 · Discovering the unknown: template-free detection and de novo pattern mining](notebooks/15_template_free_discovery.ipynb) | 2.5 h | Xu 2011; **MPP 2019** |
| **D · Deep learning on subtomograms** | [16 · 3D convolutional networks for subtomogram classification](notebooks/16_3d_cnn_classification.ipynb) | 2.5 h | Xu 2017; Che 2018; Jain 2024 |
| | [17 · Looking inside networks and segmenting structures voxel by voxel](notebooks/17_interpretability_segmentation.ipynb) | 2.5 h | Respond-CAM; DSM-Net; CIVA-Net; COS-Net |
| | [18 · Teaching a network to annotate a cell: CNN segmentation of cellular tomograms](notebooks/18_cnn_annotation_cellular_tomograms.ipynb) 🆕 | 1.5–2 h | **Chen *et al.* 2017** (Nat Methods) |
| | [19 · Learning with few labels: self-supervision, few-shot, active and open-set](notebooks/19_learning_with_few_labels.ipynb) | 2.5 h | ProtoNet; FSCC; HAL; Soft LMCCL |
| | [20 · From simulation to reality: domain shift, adaptation and synthetic data](notebooks/20_simulation_to_reality.ipynb) | 2.5 h | 3D-ADA; Cryo-Shift; CryoETGAN; Vox-UDA |
| **E · Unsupervised & geometric deep learning** | [21 · Learning to align without labels: Gum-Net and BOE-ViT](notebooks/21_deep_alignment.ipynb) | 2.5 h | **Gum-Net**; BOE-ViT |
| | [22 · Sorting a cell's particles without labels: Jim-Net and DISCA](notebooks/22_unsupervised_clustering_disca.ipynb) | 2.5 h | **DISCA**; Jim-Net; Nair 2025 |
| | [23 · Separating *what* a molecule is from *how* it is posed: Harmony and beyond](notebooks/23_disentangling_identity_pose.ipynb) | 2.5 h | **Harmony**; 3D spatial VAE |
| | [24 · Denoising without clean data: J-invariance, cycle consistency and score matching](notebooks/24_denoising_without_clean_data.ipynb) | 2.5 h | J-invariant shuffle; DUAL; TSM |
| **F · Conformational heterogeneity: Gaussian mixtures and neural fields** 🆕 | [25 · Molecules as clouds of Gaussians: single-particle reconstruction and GMMs](notebooks/25_gaussian_mixture_molecules.ipynb) | 2 h | Chen & Ludtke 2021; Chen, Schmid & Chiu 2024 (foundations) |
| | [26 · Every particle its own shape: the deep Gaussian mixture model (e2gmm)](notebooks/26_e2gmm_heterogeneity.ipynb) | 2 h | **Chen & Ludtke 2021**; **Chen, Toader & Lederman 2023** |
| | [27 · Neural fields for heterogeneous structures: cryoDRGN](notebooks/27_cryodrgn_neural_fields.ipynb) | 2 h | **Zhong *et al.* 2021** (cryoDRGN) |
| | [28 · Heterogeneity inside cells: tomoDRGN and sub-tilt series](notebooks/28_tomodrgn_subtilts.ipynb) | 1.5–2 h | **Powell & Davis 2024** (tomoDRGN) |
| | [29 · Sharpening the moving parts: GMM-based focused refinement](notebooks/29_gmm_focused_refinement.ipynb) | 2 h | **Chen, Schmid & Chiu 2024**; **Chen 2026** (arXiv) |
| | [30 · From maps to moving atoms: molecular model series with GMMs and neural networks](notebooks/30_atomic_models_model_series.ipynb) | 2 h | **Chen 2025** (Commun Biol) |
| **G · Frontiers, biology, research practice** | [31 · Picking particles with almost no labels: PU learning, MAE and meta-learning](notebooks/31_picking_with_sparse_labels.ipynb) | 2.5 h | **TomoPicker**; **CryoMAE**; RobPicker ⚠️ |
| | [32 · Segmenting the cellular world: foundation models, diffusion features and topology](notebooks/32_segmenting_the_cellular_world.ipynb) | 2.5 h | **CryoSAM**; SD segmentation; TopoFuse |
| | [33 · From maps to biology: membranes, drugs, fitting atoms and the proteome in situ](notebooks/33_from_maps_to_biology.ipynb) | 2.5 h | **Fungal membrane 2025**; Zhang 2010; Beck 2011 |
| | [34 · Capstone: an end-to-end visual-proteomics study and a paper audit](notebooks/34_capstone_visual_proteomics.ipynb) | 6–10 h | AITom; TomoMiner; DISCA audit |

🆕 = added in this edition (modules 08, 18 and 25–30); ⚠️ = a paper whose full text could not be verified (see the atlas).
Total: about **75 hours** of notebook work plus **6–10 hours** of capstone; with paper reading and discussion, plan for
**140–170 hours** over two semesters.

```text
 Part A  Foundations ────────► Part B  Imaging physics ────────► Part C  Classical cryo-ET
 (biology, Python, rotations,    (image formation, tomography,     (picking, alignment, averaging,
  Fourier, statistics, DL)        4D-STEM, simulation, resolution)  ML classification, discovery)
                                                                               │
 Part E  Unsupervised & ◄──────────────────── Part D  Deep learning ◄──────────┘
 geometric DL (deep alignment,                (3D CNNs, segmentation, tomogram
 DISCA, Harmony, denoising)                    annotation, few labels, sim-to-real)
        │
        ▼
 Part F  Conformational heterogeneity ──────► Part G  Frontiers & biology
 (GMMs, e2gmm, cryoDRGN, tomoDRGN,             (sparse-label picking, foundation models,
  focused refinement, atomic model series)      maps→biology, CAPSTONE)
```

---

## Suggested two-semester schedule (2 × 15 weeks, ≈ 5 h per week)

| Weeks | Semester 1 | Milestone |
|---|---|---|
| 1–2 | 00, 01 | Explain the cryo-ET experiment in a two-minute diagram; load and slice a density map |
| 3–4 | 02, 03 | Rotate a molecule and explain why rotation and translation separate in Fourier space |
| 5–6 | 04, 05 | Run a statistical test and train a small network; explain over-fitting |
| 7–8 | 06, 07, 08 | Simulate a projection with a CTF and a tomogram with a missing wedge; build a shadow montage |
| 9–10 | 09, 10 | Build a crowded cell; compute a gold-standard FSC |
| 11–12 | 11, 12 | Pick particles and align subtomograms with the constrained correlation |
| 13–14 | 13, 14 | Refine alignments; average and classify without a reference |
| 15 | 15 + review | Mine patterns in a simulated cell; one-page audit of Xu, Beck & Alber 2012 |

| Weeks | Semester 2 | Milestone |
|---|---|---|
| 1–2 | 16, 17, 18 | Train a 3D CNN; explain its decisions with Respond-CAM; annotate a whole tomogram from ten tiles |
| 3–4 | 19, 20 | Classify from 5 examples; measure and reduce a simulation-to-real gap |
| 5–6 | 21, 22, 23 | Align with Gum-Net-lite; cluster with DISCA-lite and BIC; disentangle content from pose |
| 7 | 24, 25 | Denoise without clean data; reconstruct a map from projections and fit it with Gaussians |
| 8–9 | 26, 27, 28 | Learn per-particle conformations (e2gmm, cryoDRGN) and do the same from sub-tilt series |
| 10 | 29, 30 | Sharpen a flexible domain by focused refinement; build a geometry-respecting model series |
| 11 | 31, 32, 33 | PU-learning picker from 10 clicks; one-click segmentation; a biological claim with the right null model |
| 12–14 | 34 (capstone) | Full pipeline on a sealed sample + report + audit of one paper |
| 15 | Presentations | Each student presents one paper from the atlas with the audit worksheet |

A **one-semester** variant: 00–04, 06–07, 10–12, 14–16, 21–22, 25–27, 31, 33–34 (about 50 hours). A **heterogeneity
track** for students with Part A done: 03, 06, 10, 25–30 (about 20 hours).

---

## How every notebook works

All notebooks follow the repository's [tutorial specification](../../../guide/Tutorial_Creation.md) and share one
structure, so you always know where to look:

| Part of the notebook | What it gives you |
|---|---|
| Title, Colab badge, key-information table | hardware, frameworks, prerequisites, time, the papers covered |
| ⚠️ Important notes, 🎯 objectives, 🗺️ contents | what is simulated, what is not; what you will be able to do |
| 🧫 The biological question | why a biologist should care |
| Setup cells | hardware check, dependency install, seeds, and the 🧰 **course toolkit** |
| Numbered sections | theory with equations **and** their plain-language reading, then runnable experiments |
| 🔍 What just happened? / ✏️ Your turn | interpretation of each result, then a change for you to make |
| 📄 Paper connection | question, what the paper does, what our toy keeps and leaves out, reported results, code link |
| ✅ Checkpoint · 🧠 Questions · 🚀 Bonus · 📝 Lab note | self-test with hidden answers, discussion, extensions, a lab-notebook template |
| 📚 References · ➡️ Next | full citations; the next module |

**Honesty policy.** Toys illustrate mechanisms; they never claim to reproduce a paper's numbers. When a toy does not show
the trend a paper reports — or a simple baseline beats a clever method — the notebook says so and explains why. Papers
whose text we could not read are marked ⚠️ and described only by what was verified (title, venue, released code).

---

## Shared conventions (used by all 35 notebooks)

| Convention | Value |
|---|---|
| Array axes | volumes are `vol[z, y, x]`; images `img[y, x]` |
| Voxel size | 10 Å (1 nm) unless stated; the beam travels along **z**; the tilt axis is **y** |
| Missing wedge | $M(\boldsymbol\xi)=\mathbf 1\big(\lvert\xi_z\rvert\le\lvert\xi_x\rvert\tan\theta_{\max}\big)$, as in Xu, Beck & Alber (2012) |
| Rotations | active rotations of $(x,y,z)$ vectors; Euler angles in the ZYZ convention; projections sum along z |
| Signal-to-noise ratio | $\mathrm{SNR}=\operatorname{var}(\text{signal})/\operatorname{var}(\text{noise})$ |
| Molecular "zoo" | real PDB models, downloaded at run time: ribosome 4V4R, 20S proteasome 3J9I, capped proteasome 6UTJ, RuBisCO 1BXN (the L₄S₄ half), plus guests (ClpB 1QVR, p97 3CF3, TRiC 4V94, …) and β-galactosidase 5A1A; a code-built flexible protein for Part F |
| Seeds | `SEED` set in every notebook; results are reproducible on the same library versions |

[`course_toolkit.py`](course_toolkit.py) holds the reference implementation of these helpers (PDB download and
reading, maps from atoms, rotations, Fourier tools, CTF, tomography, FSC, metrics, crowded-cell simulation, Gaussian-mixture projection and
Fourier reconstruction, plotting). **Each notebook contains a verbatim copy of the helpers it needs**, so every notebook
runs on its own in Colab.

**Data.** The only thing downloaded is atomic models from the Protein Data Bank (≈ 37 MB for all 15 entries, from
RCSB, with the wwPDB and PDBe as mirrors). The toolkit's `fetch_pdb` keeps them in `~/.cache/biology_to_research/pdb`
— set `BIO2RESEARCH_PDB_CACHE` to use another folder — and they are converted to density maps and passed through
simulated microscopes; every image, tomogram and dataset is simulated. To prepare a computer or a classroom in advance,
run `python fetch_structures.py` once; it prints which file (deposited entry or biological assembly) each molecule
comes from. Without a network connection, or with `BIO2RESEARCH_STANDINS=1`, the toolkit builds stand-ins of the same
size, mass and symmetry from ideal secondary structure instead: every notebook still runs, but the numbers differ from a
run on the real models. Files the notebooks write (an MRC map in Module 01, a ground-truth table in Module 09) go to the
system's temporary folder, not into the repository.

---

## Running the notebooks

**Colab (recommended):** click the badge at the top of any notebook. No GPU is needed; a few deep-learning modules use one
automatically if present.

**Locally:**

```bash
cd cryoem/tutorial/BiologyToResearch
python -m pip install -r requirements.txt
jupyter lab notebooks/
```

**Check the whole course** (schema, structure, toolkit copies, links, and the "nothing stored" rule: no data files in
the folder, no downloads except the toolkit's PDB download; add `--execute` to run every notebook):

```bash
python validate_notebooks.py            # fast structural check
python validate_notebooks.py --execute  # also executes all 35 notebooks (≈ 70–90 min on a laptop CPU)
```

The notebooks are stored **without outputs**, as the repository specification requires.

---

## Companion documents

| Document | Use it to… |
|---|---|
| [`PAPER_ATLAS.md`](PAPER_ATLAS.md) | find every paper of the course, its verification status and the module that teaches it |
| [`publication_map.csv`](publication_map.csv) | the same map as a spreadsheet |
| [`READING_GUIDE.md`](READING_GUIDE.md) | read a methods paper in five passes; reading paths through the atlas; the audit worksheet |
| [`GLOSSARY.md`](GLOSSARY.md) | look up a term (biology, physics, mathematics, machine learning) and the module that introduces it |
| [`INSTRUCTOR_GUIDE.md`](INSTRUCTOR_GUIDE.md) | plan a course or reading group: pacing, assessments, common difficulties, grading rubrics |
| [`course_toolkit.py`](course_toolkit.py) | the shared helper library |

## Going deeper in this repository

The specialist tutorials in [`cryoem/tutorial`](../) are natural next steps after the matching modules:
[`CTFEstimation`](../CTFEstimation/) and [`MotionCorrection`](../MotionCorrection/) (after 06) ·
[`MissingWedgeReconstruction`](../MissingWedgeReconstruction/), [`TiltSeriesAlignment`](../TiltSeriesAlignment/) and
[`TomogramDiagnosisBuild`](../TomogramDiagnosisBuild/) (after 07) · [`3DCryoEMReconstruction`](../3DCryoEMReconstruction/) and
[`LowSNRNoiseProcessing`](../LowSNRNoiseProcessing/) (after 06–10 and 25) · [`LocalResolution`](../LocalResolution/) (after 10) ·
[`SubtomogramAveraging`](../SubtomogramAveraging/) (after 12–14) · [`SubtomogramClassification`](../SubtomogramClassification/)
(after 16) · [`TomogramSegmentation`](../TomogramSegmentation/) (after 18 and 32) ·
[`FewShotParticleDetection`](../FewShotParticleDetection/) (after 31) ·
[`HeterogeneousReconstruction`](../HeterogeneousReconstruction/) (after 23 and 26–28). For broader imaging AI see
[`sci_img`](../../../sci_img/tutorial/README.md); for statistics, [`ml`](../../../ml/readme.md).

## Credits

Written for the Xu Lab (Computational Biology Department, Carnegie Mellon University). Atomic models come from the
Protein Data Bank (wwPDB; RCSB PDB, PDBe), downloaded at run time; all specimens, images and figures are generated by the
course's own code.
The course is for research and education only, not for clinical use.
