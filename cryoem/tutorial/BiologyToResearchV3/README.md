# From Biology to Research: Cryo-ET and Cryo-EM with the Xu Lab (V3)

A two-semester, notebook-based course that takes a **first-year biology major** from "what is a ribosome?" to reading,
running and critiquing **every cryo-electron tomography (cryo-ET) and cryo-electron microscopy (cryo-EM) paper of the
Xu lab**. The course has 27 modules (00–26). Each one is an executable Jupyter notebook that runs on a free Google Colab
CPU and turns one paper's core idea into a small experiment you can change and break.

> **V3 supersedes [`BiologyToResearchV1`](../BiologyToResearchV1/) and [`BiologyToResearchV2`](../BiologyToResearchV2/).**
> Those folders are kept unchanged for reference. V3 merges their strengths into one deeper, self-contained sequence:
> every notebook was executed end to end before release, every lab paper has a home (see the
> [paper atlas](PAPER_ATLAS.md)), and every claim about a paper is marked as verified, partial or unverified.

**Start here:** [00 · Welcome: from a crowded cell to molecular structures](notebooks/00_welcome_cells_to_structures.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/BiologyToResearchV3/notebooks/00_welcome_cells_to_structures.ipynb)

---

## Who it is for and what you will be able to do

**Assumed background:** high-school algebra and introductory cell biology. No programming, calculus or physics is assumed;
each is introduced when it is first needed, with plain-language "in words" readings of every equation.

**By the end you will be able to:**

1. Explain how a cryo-electron microscope turns a frozen cell into a 3D tomogram, and why the result is noisy, blurred by
   the contrast transfer function and missing a wedge of information.
2. Run — and modify — Python implementations of the core methods of the field: picking, wedge-aware alignment, averaging,
   maximum-likelihood and template-free classification, resolution estimation, 3D CNNs, few-label and unsupervised
   learning, deep alignment, disentanglement, self-supervised denoising, foundation-model segmentation.
3. For **any** Xu-lab cryo paper: state its biological question, data, core algorithm and key equation, evidence,
   baselines and limitations — and reproduce its central idea in a toy.
4. Turn particles and maps into biological claims with proper null models, units of replication and validation.
5. Plan a first real analysis with the lab's [AITom](https://github.com/xulabs/aitom) toolkit and public data (EMPIAR, EMDB,
   CZ cryoET Data Portal).

---

## Roadmap

| Part | Module | Time | Main lab papers (see the [atlas](PAPER_ATLAS.md)) |
|---|---|---|---|
| **A · Foundations** | [00 · Welcome: from a crowded cell to molecular structures](notebooks/00_welcome_cells_to_structures.ipynb) | 1–1.5 h | Beck *et al.* 2011; AITom; Kim *et al.* 2023 |
| | [01 · Python & NumPy for biologists: images, volumes and density maps](notebooks/01_python_arrays_density_maps.ipynb) | 1.5–2 h | previews of Zhang 2010, Xu 2009 |
| | [02 · Geometry of molecules: coordinates, rotations, symmetry and invariance](notebooks/02_rotations_geometry.ipynb) | 1.5–2 h | Xu, Zhang & Alber 2009 |
| | [03 · Waves and frequencies: the Fourier transform for biologists](notebooks/03_fourier_frequency.ipynb) | 2–2.5 h | foundations of Xu 2012, Gum-Net |
| | [04 · Noise, statistics and inference](notebooks/04_noise_statistics_inference.ipynb) | 2 h | foundations of FAML, MPP, DISCA |
| | [05 · Deep learning in one afternoon (PyTorch)](notebooks/05_deep_learning_pytorch.ipynb) | 2.5 h | SHREC'19/'20; Xu 2017 |
| **B · Imaging physics** | [06 · How an electron microscope makes an image](notebooks/06_electron_image_formation.ipynb) | 2 h | simulators of the lab; CryoMAE context |
| | [07 · Tomography: tilt series, back-projection and the missing wedge](notebooks/07_tomography_missing_wedge.ipynb) | 2 h | Han 2019; Zeng 2022 (J Comput Biol) |
| | [08 · Build an in silico cell: crowding, membranes and realistic tomograms](notebooks/08_in_silico_cell_simulation.ipynb) | 2 h | Pei 2016; Liu 2020 (×2); Wang 2018 |
| | [09 · How good is a map? FSC, half-maps, local resolution and particle selection](notebooks/09_resolution_validation.ipynb) | 2 h | Lü 2020; Shi 2020 |
| **C · Classical computational cryo-ET** | [10 · Finding particles: template matching, difference-of-Gaussians and their pitfalls](notebooks/10_particle_picking_classical.ipynb) | 2 h | Pei 2016; Wang 2018; Zhou 2018 |
| | [11 · Aligning subtomograms fast: constrained correlation and rotational search](notebooks/11_fast_subtomogram_alignment.ipynb) | 2.5 h | **Xu, Beck & Alber 2012** |
| | [12 · Precise alignment, crowded neighbours and scaling up to millions](notebooks/12_precise_alignment_crowding_scale.ipynb) | 2 h | Xu & Alber 2012, 2013; TomoMiner; Lü 2019 |
| | [13 · Averaging and classification: reference-free iteration and maximum likelihood](notebooks/13_averaging_classification_ml.ipynb) | 2.5 h | FAML 2018 |
| | [14 · Discovering the unknown: template-free detection and de novo pattern mining](notebooks/14_template_free_discovery.ipynb) | 2.5 h | Xu 2011; **MPP 2019** |
| **D · Deep learning on subtomograms** | [15 · 3D convolutional networks for subtomogram classification](notebooks/15_3d_cnn_classification.ipynb) | 2.5 h | Xu 2017; Che 2018; Jain 2024 |
| | [16 · Looking inside networks and segmenting structures voxel by voxel](notebooks/16_interpretability_segmentation.ipynb) | 2.5 h | Respond-CAM; DSM-Net; CIVA-Net; COS-Net |
| | [17 · Learning with few labels: self-supervision, few-shot, active and open-set](notebooks/17_learning_with_few_labels.ipynb) | 2.5 h | ProtoNet; FSCC; HAL; Soft LMCCL |
| | [18 · From simulation to reality: domain shift, adaptation and synthetic data](notebooks/18_simulation_to_reality.ipynb) | 2.5 h | 3D-ADA; Cryo-Shift; CryoETGAN; Vox-UDA |
| **E · Unsupervised & geometric deep learning** | [19 · Learning to align without labels: Gum-Net and BOE-ViT](notebooks/19_deep_alignment.ipynb) | 2.5 h | **Gum-Net**; BOE-ViT |
| | [20 · Sorting a cell's particles without labels: Jim-Net and DISCA](notebooks/20_unsupervised_clustering_disca.ipynb) | 2.5 h | **DISCA**; Jim-Net; Nair 2025 |
| | [21 · Separating *what* a molecule is from *how* it is posed: Harmony and beyond](notebooks/21_disentangling_identity_pose.ipynb) | 2.5 h | **Harmony**; 3D spatial VAE |
| | [22 · Denoising without clean data: J-invariance, cycle consistency and score matching](notebooks/22_denoising_without_clean_data.ipynb) | 2.5 h | J-invariant shuffle; DUAL; TSM |
| **F · Frontiers, biology, research practice** | [23 · Picking particles with almost no labels: PU learning, MAE and meta-learning](notebooks/23_picking_with_sparse_labels.ipynb) | 2.5 h | **TomoPicker**; **CryoMAE**; RobPicker ⚠️ |
| | [24 · Segmenting the cellular world: foundation models, diffusion features and topology](notebooks/24_segmenting_the_cellular_world.ipynb) | 2.5 h | **CryoSAM**; SD segmentation; TopoFuse |
| | [25 · From maps to biology: membranes, drugs, fitting atoms and the proteome in situ](notebooks/25_from_maps_to_biology.ipynb) | 2.5 h | **Fungal membrane 2025**; Zhang 2010; Beck 2011 |
| | [26 · Capstone: an end-to-end visual-proteomics study and a paper audit](notebooks/26_capstone_visual_proteomics.ipynb) | 6–10 h | AITom; TomoMiner; DISCA audit |

Total: about **60 hours** of notebook work plus **6–10 hours** of capstone; with paper reading and discussion, plan for
**120–150 hours** over two semesters.

```text
 Part A  Foundations ─────────► Part B  Imaging physics ─────────► Part C  Classical cryo-ET
 (biology, Python, rotations,     (image formation, tomography,      (picking, alignment, averaging,
  Fourier, statistics, DL)         simulation, resolution)            ML classification, discovery)
                                                                                 │
 Part F  Frontiers & biology ◄──── Part E  Unsupervised & geometric ◄─── Part D  Deep learning
 (sparse-label picking, foundation  (deep alignment, DISCA, Harmony,     (3D CNNs, segmentation, few
  models, maps→biology, CAPSTONE)    self-supervised denoising)           labels, sim-to-real)
```

---

## Suggested two-semester schedule (2 × 15 weeks, ≈ 4–5 h per week)

| Weeks | Semester 1 | Milestone |
|---|---|---|
| 1–2 | 00, 01 | Explain the cryo-ET experiment in a two-minute diagram; load and slice a density map |
| 3–4 | 02, 03 | Rotate a molecule and explain why rotation and translation separate in Fourier space |
| 5–6 | 04, 05 | Run a statistical test and train a small network; explain over-fitting |
| 7–8 | 06, 07 | Simulate a projection with a CTF and a tomogram with a missing wedge |
| 9–10 | 08, 09 | Build a crowded cell; compute a gold-standard FSC |
| 11–12 | 10, 11 | Pick particles and align subtomograms with the constrained correlation |
| 13–14 | 12, 13 | Refine alignments; average and classify without a reference |
| 15 | 14 + review | Mine patterns in a simulated cell; one-page audit of Xu, Beck & Alber 2012 |

| Weeks | Semester 2 | Milestone |
|---|---|---|
| 1–2 | 15, 16 | Train a 3D CNN; explain its decisions with Respond-CAM |
| 3–4 | 17, 18 | Classify from 5 examples; measure and reduce a simulation-to-real gap |
| 5–6 | 19, 20 | Align with Gum-Net-lite; cluster with DISCA-lite and BIC |
| 7–8 | 21, 22 | Disentangle content from pose; denoise without clean data |
| 9–10 | 23, 24 | PU-learning picker from 10 clicks; one-click segmentation |
| 11 | 25 | Turn coordinates into a biological claim with the right null model |
| 12–14 | 26 (capstone) | Full pipeline on a sealed sample + report + audit of one paper |
| 15 | Presentations | Each student presents one paper from the atlas with the audit worksheet |

A **one-semester** variant: 00–04, 06–07, 09–11, 13–15, 19–20, 23, 25–26 (about 45 hours).

---

## How every notebook works

All notebooks follow the repository's [tutorial specification](../../../guide/Tutorial_Creation.md) and share one
structure, so you always know where to look:

| Part of the notebook | What it gives you |
|---|---|
| Title, Colab badge, key-information table | hardware, frameworks, prerequisites, time, the lab papers covered |
| ⚠️ Important notes, 🎯 objectives, 🗺️ contents | what is simulated, what is not; what you will be able to do |
| 🧫 The biological question | why a biologist should care |
| Setup cells | hardware check, dependency install, seeds, and the 🧰 **course toolkit** |
| Numbered sections | theory with equations **and** their plain-language reading, then runnable experiments |
| 🔍 What just happened? / ✏️ Your turn | interpretation of each result, then a change for you to make |
| 📄 Paper connection | question, what the paper does, what our toy keeps and leaves out, reported results, code link |
| ✅ Checkpoint · 🧠 Questions · 🚀 Bonus · 📝 Lab note | self-test with hidden answers, discussion, extensions, a lab-notebook template |
| 📚 References · ➡️ Next | full citations; the next module |

**Honesty policy.** Toys illustrate mechanisms; they never claim to reproduce a paper's numbers. When a toy does not show
the trend a paper reports, the notebook says so and explains why. Papers whose text we could not read are marked ⚠️ and
described only by what was verified (title, venue, released code).

---

## Shared conventions (used by all 27 notebooks)

| Convention | Value |
|---|---|
| Array axes | volumes are `vol[z, y, x]`; images `img[y, x]` |
| Voxel size | 10 Å (1 nm) unless stated; the beam travels along **z**; the tilt axis is **y** |
| Missing wedge | $M(\boldsymbol\xi)=\mathbf 1\big(\lvert\xi_z\rvert\le\lvert\xi_x\rvert\tan\theta_{\max}\big)$, as in Xu, Beck & Alber (2012) |
| Rotations | active rotations of $(x,y,z)$ vectors; Euler angles in the ZYZ convention |
| Signal-to-noise ratio | $\mathrm{SNR}=\operatorname{var}(\text{signal})/\operatorname{var}(\text{noise})$ |
| Molecular "zoo" | PolNet density templates made from real PDB entries: ribosome 4V4R, 20S proteasome 3J9I, capped proteasome 6UTJ, RuBisCO 1BXN, plus guests (ClpB 1QVR, p97 3CF3, …) |
| Seeds | `SEED` set in every notebook; results are reproducible on the same library versions |

[`course_toolkit.py`](course_toolkit.py) holds the reference implementation of these helpers (data loading, rotations,
Fourier tools, CTF, tomography, FSC, metrics, crowded-cell simulation, plotting). **Each notebook contains a verbatim copy
of the helpers it needs**, so every notebook runs on its own in Colab.

**Data.** Templates are downloaded from a pinned commit of [PolNet](https://github.com/anmartinezs/polnet) and real maps
from the [NGL viewer](https://github.com/nglviewer/ngl) test data, and cached in `course_data/` (set `CRYO_COURSE_CACHE` to
change it). Without internet, every notebook falls back to simple procedural stand-in shapes and still runs.

---

## Running the notebooks

**Colab (recommended):** click the badge at the top of any notebook. No GPU is needed; a few deep-learning modules use one
automatically if present.

**Locally:**

```bash
cd cryoem/tutorial/BiologyToResearchV3
python -m pip install -r requirements.txt
jupyter lab notebooks/
```

**Check the whole course** (schema, structure, toolkit copies, links; add `--execute` to run every notebook):

```bash
python validate_notebooks.py            # fast structural check
python validate_notebooks.py --execute  # also executes all 27 notebooks (≈ 35–45 min on a laptop CPU)
```

The notebooks are stored **without outputs**, as the repository specification requires.

---

## Companion documents

| Document | Use it to… |
|---|---|
| [`PAPER_ATLAS.md`](PAPER_ATLAS.md) | find every lab cryo paper (81 entries), its verification status and the module that teaches it |
| [`publication_map.csv`](publication_map.csv) | the same map as a spreadsheet |
| [`READING_GUIDE.md`](READING_GUIDE.md) | read a methods paper in five passes; reading paths through the atlas; the audit worksheet |
| [`GLOSSARY.md`](GLOSSARY.md) | look up a term (biology, physics, mathematics, machine learning) and the module that introduces it |
| [`INSTRUCTOR_GUIDE.md`](INSTRUCTOR_GUIDE.md) | plan a course or reading group: pacing, assessments, common difficulties, grading rubrics |
| [`course_toolkit.py`](course_toolkit.py) | the shared helper library |

## Going deeper in this repository

The specialist tutorials in [`cryoem/tutorial`](../) are natural next steps after the matching V3 modules:
[`CTFEstimation`](../CTFEstimation/) and [`MotionCorrection`](../MotionCorrection/) (after 06) ·
[`MissingWedgeReconstruction`](../MissingWedgeReconstruction/), [`TiltSeriesAlignment`](../TiltSeriesAlignment/) and
[`TomogramDiagnosisBuild`](../TomogramDiagnosisBuild/) (after 07) · [`3DCryoEMReconstruction`](../3DCryoEMReconstruction/) and
[`LowSNRNoiseProcessing`](../LowSNRNoiseProcessing/) (after 06–09) · [`LocalResolution`](../LocalResolution/) (after 09) ·
[`SubtomogramAveraging`](../SubtomogramAveraging/) (after 11–13) · [`SubtomogramClassification`](../SubtomogramClassification/)
(after 15) · [`FewShotParticleDetection`](../FewShotParticleDetection/) (after 23) ·
[`TomogramSegmentation`](../TomogramSegmentation/) (after 24) · [`HeterogeneousReconstruction`](../HeterogeneousReconstruction/)
(after 21). For broader imaging AI see [`sci_img`](../../../sci_img/tutorial/README.md); for statistics,
[`ml`](../../../ml/readme.md).

## Credits

Written for the Xu Lab (Computational Biology Department, Carnegie Mellon University). Density templates: PolNet
(Martinez-Sanchez *et al.*), built from PDB entries; real maps from the NGL viewer test data. The course is for research
and education only, not for clinical use.
