# Cryo-EM and Cryo-ET

**Cryo-electron microscopy (cryo-EM)** freezes purified molecules in thin ice and averages thousands of noisy pictures of
them into a 3D structure. **Cryo-electron tomography (cryo-ET)** tilts a thin slice of a frozen cell in the microscope and
reconstructs a 3D image (a tomogram) of molecules where they work. Both depend on computation:

- the images are extremely noisy, with signal-to-noise ratios of about 0.01–0.1;
- the microscope's contrast transfer function (CTF) blurs them;
- in tomography, a wedge of information is never measured;
- every particle points in a different direction.

This folder holds two notebook courses on the computational methods of the field. They approach it from opposite sides.

---

## Choose a course

| | [From Biology to Research](tutorial/BiologyToResearch/README.md) | [Cryo-EM for Computer Scientists](tutorial/foundation/readme.md) |
|---|---|---|
| **Written for** | First-year biology majors, and anyone who wants to read and understand cryo-ET and cryo-EM analysis research | Computer-science and engineering students, and researchers new to structural biology |
| **Assumes** | High-school algebra and introductory cell biology; no programming, calculus or physics | NumPy, SciPy and Matplotlib fluency; Fourier transforms ([sci_img Phase 01, Module 02](../sci_img/tutorial/foundation/ComputationalSignalBase/FrequencyFiltering/)) |
| **Size** | 35 notebooks (00–34) in seven parts; ≈ 75 h plus a 6–10 h capstone (two semesters) | 13 modules: 17 notebooks and one hands-on practical with IMOD |
| **Approach** | Each notebook turns one paper's central idea into a small experiment. Biology, Python, statistics and deep learning are taught along the way | Each module builds one step of the processing pipeline from first principles, then applies it to public data |
| **Data** | Real atomic models from the Protein Data Bank, downloaded at run time; every image and tomogram is simulated | Simulated data and public samples downloaded at run time (EMPIAR, the CZ cryoET Data Portal); the IMOD practical uses EMPIAR-10164 |
| **Runs on** | A free Google Colab CPU | Google Colab (a T4 GPU helps for modules 06, 07 and 11); module 04 needs IMOD on Linux or macOS |
| **Start here** | [00 · Welcome: from a crowded cell to molecular structures](tutorial/BiologyToResearch/notebooks/00_welcome_cells_to_structures.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/BiologyToResearch/notebooks/00_welcome_cells_to_structures.ipynb) | [01 · Low-SNR image processing](tutorial/foundation/LowSNRNoiseProcessing/cryoem_low_snr_tutorial.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/LowSNRNoiseProcessing/cryoem_low_snr_tutorial.ipynb) |

**Which one?**

- If you are a biologist, or new to programming, take **From Biology to Research**.
- If you already program and want to implement the processing pipeline, take **Cryo-EM for Computer Scientists**.
- Students who finish the first course can use the second as a hands-on follow-up with real data and production
  software.

---

## Course 1 · From Biology to Research

A two-semester course that takes a first-year biology major from "what is a ribosome?" to reading, running and understanding
a number of cryo-ET and cryo-EM papers. Every notebook runs alone on a free Colab CPU and ends with
checkpoint questions, a "paper connection" box and a lab note.

| Part | Modules | What you learn |
|---|---|---|
| A · Foundations | 00–05 | cells and molecules, Python and NumPy, rotations and symmetry, Fourier transforms, noise and statistics, PyTorch |
| B · Imaging physics | 06–10 | image formation and the CTF, tomography and the missing wedge, 4D-STEM, simulated crowded cells, resolution (FSC) |
| C · Classical computational cryo-ET | 11–15 | particle picking, fast and precise subtomogram alignment, averaging and maximum-likelihood classification, template-free discovery |
| D · Deep learning on subtomograms | 16–20 | 3D CNNs, interpretability and segmentation, CNN annotation of tomograms, learning with few labels, simulation to reality |
| E · Unsupervised and geometric deep learning | 21–24 | deep alignment (Gum-Net), deep clustering (DISCA), separating identity from pose (Harmony), denoising without clean data |
| F · Conformational heterogeneity | 25–30 | Gaussian mixture models, e2gmm, cryoDRGN, tomoDRGN, GMM-based focused refinement, atomic model series |
| G · Frontiers and biology | 31–34 | picking with sparse labels, foundation-model segmentation, from maps to biology, and an end-to-end capstone |

Companion documents:

- [README](tutorial/BiologyToResearch/README.md): roadmap, schedules and conventions.
- [Paper atlas](tutorial/BiologyToResearch/PAPER_ATLAS.md): every paper mapped to the modules that teach it.
- [Reading guide](tutorial/BiologyToResearch/READING_GUIDE.md): reading paths through the papers.
- [Glossary](tutorial/BiologyToResearch/GLOSSARY.md): terms used across the course.
- [Instructor guide](tutorial/BiologyToResearch/INSTRUCTOR_GUIDE.md): teaching plans and known toy behaviours.

---

## Course 2 · Cryo-EM for Computer Scientists

A specialist-level curriculum that builds the processing pipeline step by step: noise and the CTF, reconstruction,
tilt-series alignment, a real tomogram, then averaging, detection, segmentation, resolution and heterogeneity. Follow
modules 01–12 in order ([why](tutorial/foundation/readme.md#suggested-order)). Module 13 is self-contained (it
simulates its own subtomograms) and fits anywhere after module 05.

| # | Module | Topics | Notebooks |
|---|---|---|---|
| 01 | [Low-SNR processing](tutorial/foundation/LowSNRNoiseProcessing/) | SNR, CTF simulation, denoising, particle picking, 2D class averaging, FRC, Noise2Void | [low SNR](tutorial/foundation/LowSNRNoiseProcessing/cryoem_low_snr_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/LowSNRNoiseProcessing/cryoem_low_snr_tutorial.ipynb)) · [low-dose denoising](tutorial/foundation/LowSNRNoiseProcessing/lowdose_em_denoising_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/LowSNRNoiseProcessing/lowdose_em_denoising_tutorial.ipynb)) · [particle picking](tutorial/foundation/LowSNRNoiseProcessing/particle_picking_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/LowSNRNoiseProcessing/particle_picking_tutorial.ipynb)) · [class averaging](tutorial/foundation/LowSNRNoiseProcessing/class_averaging_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/LowSNRNoiseProcessing/class_averaging_tutorial.ipynb)) · [self-supervised denoising](tutorial/foundation/LowSNRNoiseProcessing/self_supervised_denoising_medical.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/LowSNRNoiseProcessing/self_supervised_denoising_medical.ipynb)) |
| 02 | [3D reconstruction](tutorial/foundation/3DCryoEMReconstruction/) | forward model, CTF correction, Fourier slice theorem, back-projection, EM pose estimation, NeRF-style reconstruction | [reconstruction](tutorial/foundation/3DCryoEMReconstruction/cryoem_reconstruction_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/3DCryoEMReconstruction/cryoem_reconstruction_tutorial.ipynb)) |
| 03 | [Tilt-series alignment](tutorial/foundation/TiltSeriesAlignment/) | fiducial-less patch tracking, simulated misalignment, reconstruction quality | [alignment](tutorial/foundation/TiltSeriesAlignment/tilt_series_alignment_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/TiltSeriesAlignment/tilt_series_alignment_tutorial.ipynb)) |
| 04 | [Build and diagnose a tomogram](tutorial/foundation/TomogramDiagnosisBuild/) | IMOD/Etomo on EMPIAR-10164: fiducial alignment, WBP and SIRT, diagnosis | [practical guide](tutorial/foundation/TomogramDiagnosisBuild/build_and_diagnose_tomogram.md) (local) |
| 05 | [Subtomogram averaging](tutorial/foundation/SubtomogramAveraging/) | 3D picking by template matching, missing wedge, alignment, FSC, multi-reference classification | [averaging](tutorial/foundation/SubtomogramAveraging/subtomogram_averaging_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/SubtomogramAveraging/subtomogram_averaging_tutorial.ipynb)) |
| 06 | [Few-shot particle detection](tutorial/foundation/FewShotParticleDetection/) | weak spherical labels, Volume Infill augmentation, 3D CNN detection | [detection](tutorial/foundation/FewShotParticleDetection/few_shot_cryoet_particle_detection_with_weak_labels_and_volume_infill.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/FewShotParticleDetection/few_shot_cryoet_particle_detection_with_weak_labels_and_volume_infill.ipynb)) |
| 07 | [Tomogram segmentation](tutorial/foundation/TomogramSegmentation/) | one-click 3D segmentation with SAM, cross-plane propagation, membranes and mitochondria | [interactive](tutorial/foundation/TomogramSegmentation/interactive_cryoet_tomogram_segmentation.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/TomogramSegmentation/interactive_cryoet_tomogram_segmentation.ipynb)) · [membranes and organelles](tutorial/foundation/TomogramSegmentation/membrane_organelle_segmentation_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/TomogramSegmentation/membrane_organelle_segmentation_tutorial.ipynb)) |
| 08 | [Missing wedge: WBP vs SIRT](tutorial/foundation/MissingWedgeReconstruction/) | full vs limited tilt range, Fourier-slice view of the wedge, WBP and SIRT from scratch | [missing wedge](tutorial/foundation/MissingWedgeReconstruction/missing_wedge_wbp_sirt_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/MissingWedgeReconstruction/missing_wedge_wbp_sirt_tutorial.ipynb)) |
| 09 | [Motion correction](tutorial/foundation/MotionCorrection/) | whole-frame and patch-based drift correction of dose-fractionated movies | [motion correction](tutorial/foundation/MotionCorrection/motion_correction_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/MotionCorrection/motion_correction_tutorial.ipynb)) |
| 10 | [Local resolution](tutorial/foundation/LocalResolution/) | global FSC vs sliding-window local FSC, rigid cores and flexible loops | [local resolution](tutorial/foundation/LocalResolution/local_resolution_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/LocalResolution/local_resolution_tutorial.ipynb)) |
| 11 | [Heterogeneous reconstruction](tutorial/foundation/HeterogeneousReconstruction/) | continuous heterogeneity with cryoDRGN: coordinate network, VAE, latent traversals | [cryoDRGN](tutorial/foundation/HeterogeneousReconstruction/CryoDRGN_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/HeterogeneousReconstruction/CryoDRGN_tutorial.ipynb)) |
| 12 | [CTF estimation](tutorial/foundation/CTFEstimation/) | Thon rings, radial averaging, defocus fitting, phase-flip correction on a real micrograph | [CTF](tutorial/foundation/CTFEstimation/ctf_estimation_tutorial.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/CTFEstimation/ctf_estimation_tutorial.ipynb)) |
| 13 | [Subtomogram classification](tutorial/foundation/SubtomogramClassification/) | simulated subtomograms with a missing wedge, 3D CNN classifiers, class imbalance | [classification](tutorial/foundation/SubtomogramClassification/cryoet_ml_tutorial_PR.ipynb) ([Colab](https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/foundation/SubtomogramClassification/cryoet_ml_tutorial_PR.ipynb)) |

Learning goals, hardware notes and setup instructions are in the [course README](tutorial/foundation/readme.md).

---

## How the two courses line up

Both courses teach the same pipeline. Use this table to go deeper on a topic in the other course.

| Topic | From Biology to Research | Cryo-EM for Computer Scientists |
|---|---|---|
| Noise, averaging and denoising | 04, 24 | 01 Low-SNR processing |
| Image formation and the CTF | 06 | 01 Low-SNR processing, 12 CTF estimation |
| Tomography, the missing wedge, WBP and SIRT | 07 | 08 Missing wedge |
| Tilt-series alignment | 07 | 03 Tilt-series alignment, 04 Build and diagnose a tomogram |
| 3D reconstruction from projections | 07, 25 | 02 3D reconstruction |
| Particle picking and detection | 11, 31 | 01 Low-SNR processing, 06 Few-shot particle detection |
| Subtomogram alignment and averaging | 12, 13, 14 | 05 Subtomogram averaging |
| Classification of subtomograms | 14, 16, 22 | 05 Subtomogram averaging, 13 Subtomogram classification |
| Resolution and local resolution | 10 | 10 Local resolution |
| Segmentation of tomograms | 17, 18, 32 | 07 Tomogram segmentation |
| Conformational heterogeneity (cryoDRGN) | 26, 27, 28 | 11 Heterogeneous reconstruction |
| Motion correction | — | 09 Motion correction |
| Working with real data and production software | 34 (plans a first real analysis) | 04 Build and diagnose a tomogram |

---

## Running the notebooks

**On Google Colab.** Use the badges above. To open any other notebook from this folder, take its GitHub address and
replace `https://github.com/` with `https://colab.research.google.com/github/`.

**On your own computer.**

```bash
git clone https://github.com/xulabs/edu.git

# From Biology to Research
cd edu/cryoem/tutorial/BiologyToResearch
python -m pip install -r requirements.txt
python fetch_structures.py        # optional: download the PDB models once, before class
jupyter lab notebooks/

# Cryo-EM for Computer Scientists (each notebook also installs what it needs in its first cell)
cd edu/cryoem/tutorial/foundation
python -m pip install numpy scipy matplotlib scikit-image torch torchvision tqdm
jupyter lab
```

Module 04 of *Cryo-EM for Computer Scientists* needs [IMOD](https://bio3d.colorado.edu/imod/) on Linux or macOS (WSL2
on Windows). It also needs the EMPIAR-10164 tilt series (8–12 GB), so start that download early. See the
[practical guide](tutorial/foundation/TomogramDiagnosisBuild/build_and_diagnose_tomogram.md).

---

## Data

This folder stores no maps, micrographs, tomograms or other datasets; the notebooks fetch or simulate what they need.

- **From Biology to Research:**
  - **Models:** the PDB models are downloaded the first time a notebook needs them (≈ 37 MB in total) and cached in
    `~/.cache/biology_to_research/pdb`. Set `BIO2RESEARCH_PDB_CACHE` to use another folder.
  - **Simulation:** every image, tomogram and dataset is simulated from those models.
  - **Offline:** without a network connection, code-built stand-ins of the same size and symmetry are used, so every
    notebook still runs. The numbers then differ from those the notebooks describe.
- **Cryo-EM for Computer Scientists:**
  - **Notebooks:** they simulate most of their data and download small public samples at run time. Examples are
    micrographs from EMPIAR-10146 and a piece of a tomogram from the CZ cryoET Data Portal (dataset 10003, the cells of
    EMPIAR-10499).
  - **Module 04:** the practical uses the full EMPIAR-10164 dataset, downloaded by hand.

---

## Related material in this repository

- [Medical & Biological Imaging AI](../sci_img/tutorial/README.md):
  - Phase 01, Module 02 (frequency filtering) is the prerequisite for *Cryo-EM for Computer Scientists*.
  - Phase 04 of that series is *Cryo-EM for Computer Scientists* itself.
- [From Biology to Machine Learning](../ml/tutorial/BiologyToML/README.md): the statistics and machine learning behind
  many methods here, taught to biology majors.
- [From Biology to Mathematics](../math/tutorial/BiologyToMath/README.md): linear algebra, calculus and probability
  for biology majors.
- [AITom](https://github.com/xulabs/aitom): the Xu Lab's open-source toolkit for cryo-ET analysis, used for real data
  after these courses.

---

Developed by the [Xu Lab](https://xulabs.github.io), Computational Biology Department, Carnegie Mellon University.
For research and education only; not for clinical use.
