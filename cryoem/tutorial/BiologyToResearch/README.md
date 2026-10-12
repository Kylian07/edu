# 🧬 Biology-to-CryoEM Research Curriculum

**Xu Lab Education Portal — 26 self-contained Jupyter tutorials.**

**Intended learner:** first-year undergraduate biology major with no previous programming or physics. The complete route is approximately **2–3 semesters / 28–36 teaching weeks**, followed by mentored paper reproduction. A proficient learner can use an accelerated route.

**Aim:** read the lab's cryo-ET and cryo-EM literature critically, explain its mathematics and biological significance, reproduce a *controlled approximation* of core concepts, and then transition to official research code/datasets for authentic reproduction.

**This is an additive folder** under `cryoem/tutorial/` and should not replace existing tutorial notebooks. Research concept notebooks use tiny synthetic data and mostly CPU, so all run on free-tier Colab. None is claimed to implement an official Xu Lab paper.

## Start here

1. Open `notebooks/01_molecules_to_voxels.ipynb` in Google Colab or Jupyter.
2. Run all cells once. Rerun and alter one parameter.
3. For each notebook, submit a figure, a quantitative comparison and a 150-word note.
4. Consult [`PAPER_TO_TUTORIAL_MAP.md`](PAPER_TO_TUTORIAL_MAP.md) to trace each publication to prerequisite notebooks.
5. After Module 08, cross over to the existing [`cryoem/readme.md`](../../readme.md) tutorials, then return to these research-specific modules.

**Environment:** Colab preinstalled numpy/scipy/matplotlib/scikit-learn/PyTorch usually suffice. Locally: `python -m pip install -r requirements.txt`. Most modules need < 2 GB RAM. Real-tomogram production analysis requires separate datasets, GPU resources, and appropriate software.

**Repository-compatible format:** title+emoji, learning objectives, CPU/free T4 target, seeded imports, reproducible synthetic dataset, math and code interwoven, guided exercises, and paper references. Follows the repository’s [`guide/Tutorial_Creation.md`](../../../guide/Tutorial_Creation.md).

## Scaffolded syllabus

| Phase | Approx. weeks | Modules | Mastery checkpoint |
|---|---:|---|---|
| A. Biology and computational language | 1–5 | 01–04 | Explain density maps, voxel units, 3D rotations and Fourier content |
| B. Physics of imaging | 6–10 | 05–08 | Explain tilt series, CTF, missing wedge and half-map FSC |
| C. Classical discovery and alignment | 11–15 | 09–12 | Implement picking, align synthetic data and reject confounded averaging |
| D. Deep methods under limited supervision | 16–22 | 13–17 | Evaluate a 3D model with correct splits and domain-shift tests |
| E. Denoising, simulation, and geometry | 23–27 | 18–20 | Derive J-invariance, test simulator shift and verify equivariance |
| F. Current research frontiers | 28–33 | 21–25 | Assess prompts, topology, disentanglement, semi-supervised clustering and inverse priors |
| G. Independent research | 34–36 | 26 + paper study | Produce a rigorous mini-reproduction plan and critique |

### Existing tutorials to use, not duplicate

- [`sci_img/tutorial/`](../../../sci_img/tutorial/): image arrays, frequency filtering, image registration, segmentation and self-supervision.
- [`cryoem/tutorial/LowSNRNoiseProcessing/`](../LowSNRNoiseProcessing/): advanced CTF, noise, particle-picking and class-averaging tutorials.
- [`cryoem/tutorial/3DCryoEMReconstruction/`](../3DCryoEMReconstruction/): computational reconstruction and Fourier slice theorem.
- [`cryoem/tutorial/TomogramDiagnosisBuild/`](../TomogramDiagnosisBuild/): real tilt-series processing (IMOD/Etomo).
- [`cryoem/readme.md`](../../readme.md): descriptions of additional STA and segmentation modules; paths should be verified at merge time because the live folder view is not identical to its README.

## Module index

- [01 — From molecular complexes to voxels](notebooks/01_molecules_to_voxels.ipynb) — A: Biology + computation.
- [02 — Python, images, units, and reproducibility](notebooks/02_python_images_units.ipynb) — A: Biology + computation.
- [03 — Vectors, 3D rotations, and coordinate systems](notebooks/03_rotations_linear_algebra.ipynb) — A: Biology + computation.
- [04 — Fourier transforms and spatial frequency](notebooks/04_fourier_signal_basics.ipynb) — A: Biology + computation.
- [05 — From electron projections to a tilt series](notebooks/05_projection_tilt_geometry.ipynb) — B: Imaging physics.
- [06 — Low-dose imaging and contrast transfer](notebooks/06_electron_dose_ctf.ipynb) — B: Imaging physics.
- [07 — Missing wedge and inverse reconstruction](notebooks/07_missing_wedge_reconstruction.ipynb) — B: Imaging physics.
- [08 — Fourier-shell correlation and validation](notebooks/08_fsc_resolution_validation.ipynb) — B: Imaging physics.
- [09 — Particle picking and object detection](notebooks/09_particle_picking.ipynb) — C: Classical cryo-ET discovery.
- [10 — Alignment with similarity and optimization](notebooks/10_subtomogram_alignment.ipynb) — C: Classical cryo-ET discovery.
- [11 — Template-free structural pattern mining](notebooks/11_template_free_discovery.ipynb) — C: Classical cryo-ET discovery.
- [12 — Averaging, classification, and conformations](notebooks/12_averaging_heterogeneity.ipynb) — C: Classical cryo-ET discovery.
- [13 — 3D convolutional features and classification](notebooks/13_cnn_3d_features.ipynb) — D: Learning from tomograms.
- [14 — Semantic segmentation and 3D U-Net](notebooks/14_unet_segmentation.ipynb) — D: Learning from tomograms.
- [15 — Autoencoding and self-supervised feature learning](notebooks/15_self_supervised_representations.ipynb) — D: Learning from tomograms.
- [16 — Few-shot, one-shot, active learning](notebooks/16_limited_labels_learning.ipynb) — D: Learning from tomograms.
- [17 — Domain shifts, open sets, and calibration](notebooks/17_domain_shift_open_set.ipynb) — D: Learning from tomograms.
- [18 — Self-supervised denoising without clean labels](notebooks/18_j_invariant_denoising.ipynb) — E: Generative + invariance.
- [19 — Physics-aware simulation and domain randomization](notebooks/19_simulation_domain_randomization.ipynb) — E: Generative + invariance.
- [20 — Equivariance and orientation estimation](notebooks/20_equivariant_orientation.ipynb) — E: Generative + invariance.
- [21 — Promptable and tri-planar segmentation](notebooks/21_promptable_triplanar_segmentation.ipynb) — F: Research frontiers.
- [22 — Topology, Betti numbers, and membranes](notebooks/22_topology_preserving_masks.ipynb) — F: Research frontiers.
- [23 — Identity, conformation, and imaging transformation](notebooks/23_disentangle_content_transformation.ipynb) — F: Research frontiers.
- [24 — Semi-supervised and knowledge-guided clustering](notebooks/24_knowledge_guided_clustering.ipynb) — F: Research frontiers.
- [25 — Score/flow priors versus physical measurements](notebooks/25_inverse_generative_priors.ipynb) — F: Research frontiers.
- [26 — Research capstone: from crowded scene to evidence](notebooks/26_end_to_end_research_capstone.ipynb) — G: Integrative research.

## What “deep understanding” means

For **every paper**, students must (a) draw the data-generation pipeline; (b) derive one central objective/algorithm; (c) separate supervision types; (d) implement a toy instance and at least one failure case; (e) identify datasets/splits/metrics; (f) reproduce one result using official source or explicitly report why that is infeasible; and (g) propose a biology-relevant ablation. **Do not confuse these notebooks with paper reproduction.**

## Assessment

- Short quizzes and exit tickets: 20%; notebooks and parameter studies: 35%; paper reconstruction diagrams/reviews: 20%; integrative capstone: 25%.
- Report object-level precision/recall for picking, voxel Dice/topology for segmentation, pose error for alignment, and half-map criteria for averaging where appropriate.
- For real data, split by tomogram, specimen, and acquisition session where possible; report uncertainty, failure modes and biological relevance.

## Resources

- [Xu Lab AITom](https://github.com/xulabs/aitom)
- [CryoET Data Portal](https://cryoetdataportal.czscience.com/)
- [EMPIAR](https://www.ebi.ac.uk/empiar/)
- [EMDB](https://www.ebi.ac.uk/emdb/)
- [PDB](https://www.rcsb.org/)

## Sources and scope note

Paper titles are indexed primarily from [Min Xu's published academic CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) as read in October 2026, with cross-checks against publicly available venues. Google Scholar may rate-limit automated enumeration, so this is a systematic CV-based mapping, not a claim of an exhaustive live Scholar API export. The CV has a few duplicate/out-of-order entries and research papers outside microscopy, which have been excluded here. Related optical-microscopy work is explicitly marked adjacent, not cryo-EM.

## Deep paper-reading seminars

Beyond the 26 executable notebooks, use the [14 guided research-paper seminars](paper_studies/README.md), then the [80-entry crosswalk](PAPER_TO_TUTORIAL_MAP.md) to cover the complete CV-listed cryo literature.
