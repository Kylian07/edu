# Cryo-EM and cryo-ET for a biology student

A biology-first, research-facing course that begins with cells and molecules and ends with the ability to examine Xu lab cryo-electron microscopy (cryo-EM) and cryo-electron tomography (cryo-ET) publications critically. It replaces the previous specialist-first `cryoem` entry path with a self-contained sequence of 22 small, runnable notebooks, a research bridge, five guided paper studies, and a paper-by-paper atlas. The advanced computational ideas are introduced only after the biological question and the measurement are clear.

**Start here:** [00 — From cells to molecular structures](tutorial/biology_first/00_cell_to_structure.ipynb). A student needs introductory cell biology and arithmetic, but no prior programming, calculus, physics, or structural biology. Use the [getting-started guide](getting_started.md) for Colab and Python basics.

## What the student will learn

By the end, a student should be able to:

- Explain what an electron microscope measures, why samples are vitrified, and how single-particle cryo-EM differs from cellular cryo-ET.
- Track a biological question through raw images, motion/tilt alignment, reconstruction, particle detection, averaging or segmentation, validation, and interpretation.
- Reason about pixel and voxel size, dose and noise, Fourier frequencies, the CTF, the missing wedge, rotations, and alignment.
- Distinguish localization, segmentation, classification, conformation, composition, and molecular identity.
- Evaluate AI methods under scarce labels, simulation-to-real shifts, self-supervision, generative priors, and independent specimen-level testing.
- Read every cryo-related publication in the [paper atlas](paper_atlas.md) with a consistent question–data–method–evidence–limitation framework.

The course builds **research literacy and conceptual computational fluency**. Toy simulations teach mechanisms; they are not reproductions of the cited papers. The [research bridge](research_bridge.md) names the additional mathematics and implementation work needed for full technical mastery.

## Course map

Each notebook uses the same format as the repo's [tutorial specification](https://github.com/xulabs/edu/blob/main/guide/Tutorial_Creation.md): overview, learning goals, prerequisites, setup, theory, runnable experiment, interpretation, a parameter change, and a link to a research paper. The activities run on a free Google Colab CPU session using NumPy and synthetic data, so there are no large downloads, paid services, or required GPU. The hardware and limitations are stated in every notebook.

| Stage | Notebooks | Main question | Exit evidence |
|---|---|---|---|
| I. Biological and measurement foundations | [00](tutorial/biology_first/00_cell_to_structure.ipynb), [01](tutorial/biology_first/01_cryo_microscopy_workflow.ipynb), [02](tutorial/biology_first/02_pixels_voxels_sampling.ipynb), [03](tutorial/biology_first/03_dose_noise_averaging.ipynb) | What structure can be inferred from a low-dose image? | Labeled scale drawing, experiment flowchart, and noise/averaging note. |
| II. Reconstructing and finding structures | [04](tutorial/biology_first/04_fourier_ctf.ipynb), [05](tutorial/biology_first/05_projections_tomography.ipynb), [06](tutorial/biology_first/06_alignment_rotations.ipynb), [07](tutorial/biology_first/07_particle_picking.ipynb), [08](tutorial/biology_first/08_averaging_resolution.ipynb) | Which information is measured, missing, aligned, or averaged? | Forward-model sketch; picking precision/recall; half-map validation critique. |
| III. Learning from annotated and unannotated data | [09](tutorial/biology_first/09_segmentation_and_identity.ipynb), [10](tutorial/biology_first/10_ml_basics.ipynb), [11](tutorial/biology_first/11_limited_labels.ipynb), [12](tutorial/biology_first/12_unsupervised_pattern_mining.ipynb) | How do computational labels become biologically meaningful? | Specimen-level split plan, error analysis, and candidate-cluster validation plan. |
| IV. Modern methods and biological interpretation | [13](tutorial/biology_first/13_simulation_domain_shift.ipynb), [14](tutorial/biology_first/14_self_supervision_denoising.ipynb), [15](tutorial/biology_first/15_equivariance_disentanglement.ipynb), [16](tutorial/biology_first/16_maps_to_biology.ipynb) | What generalizes, what can be hallucinated, and what does a map support? | Domain-shift test, denoising control, and claim–evidence table. |
| V. Research depth | [17](tutorial/biology_first/17_single_particle_reconstruction.ipynb), [18](tutorial/biology_first/18_likelihood_hidden_states.ipynb), [19](tutorial/biology_first/19_volumetric_networks.ipynb), [20](tutorial/biology_first/20_generative_priors.ipynb), [research bridge](research_bridge.md) | How do full reconstruction and modern inference methods work? | Forward-model derivation, hidden-state critique, and raw-data consistency test. |
| VI. Paper mastery | [21](tutorial/biology_first/21_paper_capstone.ipynb), [paper atlas](paper_atlas.md) | How does one audit a full cryo paper? | Two-paper comparison, conceptual reproduction, limitation, and next experiment. |

## Suggested two-semester pace

The notebooks total about **65 hours** of directed work; with reading, discussion, and the capstone, plan **120–150 hours**. This is a 30-week route at roughly 4–5 hours weekly. Faster students can combine two notebooks in a week, but should not skip the lab notes or paper discussions.

| Weeks | Study plan | Milestone |
|---|---|---|
| 1–4 | 00–03, one notebook per week. Read a cell-biology chapter on proteins, membranes, and ribosomes alongside the notebooks. | Explain the full experiment in a two-minute diagram. |
| 5–9 | 04–08. Use paper-figure discussions to keep the mathematical tools attached to biological questions. | Explain missing information, alignment, and independent validation. |
| 10–13 | 09–12. Compare one supervised and one template-free research paper. | Design an unbiased split and a biological identity check. |
| 14–17 | 13–16. Read one simulation/transfer paper and one modern segmentation or denoising paper. | Show a domain-shift failure and a generative-prior failure. |
| 18–22 | Study notebooks 17–20 and the [research bridge](research_bridge.md): equations, vocabulary, and four quantitative exercises. | Short oral explanation of the forward model and uncertainty. |
| 23–27 | Work through the [five guided paper studies](paper_studies.md), then read one paper from each of atlas sections A–G, first by figures, then by methods. Revisit weak topics in the notebooks. | Seven one-page paper audits. |
| 28–30 | Complete notebook 21 and the final comparison. | Two-paper report plus reproducible toy analysis. |

## A consistent weekly routine

1. **Before:** read the notebook's “why this matters” and predict the result of its experiment in words.
2. **During:** run the notebook, change one parameter, and note what changed. If a cell errors, read the traceback and re-run from the top before editing code.
3. **After:** write four lines: input, output, core assumption, and failure mode. Explain one plotted or printed quantity without looking at the code.
4. **Paper bridge:** open the linked paper, label one figure as measurement, algorithm output, or biological inference, and record the evidence for its claim.

This follows the repository's [learning guide](https://github.com/xulabs/edu/blob/main/guide/learning_guide.md) while making the cryo track accessible at entry level. The existing [`sci_img/tutorial`](https://github.com/xulabs/edu/tree/main/sci_img/tutorial) image and PyTorch notebooks are optional reinforcements when a student needs more practice with arrays, filtering, registration, or neural networks.

## Scientific checkpoints

- **Noise:** under independent additive-noise assumptions, averaging N aligned identical particles reduces noise standard deviation by `√N`. State the SNR convention before stating a scaling law; averaging mixed states can blur biology.
- **Sampling:** the Nyquist period `2 × pixel size` is a theoretical sampling limit, not the achieved structural resolution.
- **CTF and missing wedge:** a transfer-function zero or unsampled tilt direction is missing information, not something that simple sharpening can recover.
- **Resolution:** the familiar 0.143 criterion belongs to gold-standard **3D FSC between independently processed half maps**. Do not call it a universal FRC or half-bit threshold. Inspect local resolution, anisotropy, masks, and data independence.
- **AI outputs:** a plausible density, segmentation, or class label needs validation against measurements, held-out specimens, and biological context.

## Assessment

A notebook is complete when its code runs from top to bottom, its “change one thing” task has a written prediction and result, and its lab note names a failure mode. A paper audit is complete when the student can locate the data source, independent test unit, method comparison, metric, and biological validation in the actual article. The capstone rubric is in [instructor_notes.md](instructor_notes.md).

## Repository layout and adoption

This `cryoem/` directory is ready to replace the existing `cryoem/` track in `xulabs/edu`. Keep the lowercase `readme.md` name used by the current track. The new path is `cryoem/tutorial/biology_first/*.ipynb`; all course links are relative and need no hosting setup. Update the root `README.md` quick link to read **“Cryo-EM and cryo-ET for Biology Students”** and point to `cryoem/readme.md` when integrating. The older specialist notebooks can be kept in a separate advanced archive if desired, but this course has no dependency on them. Before a repository merge, a maintainer should check the latest publication list and decide whether to retain those older notebooks as optional follow-ons.

**Sources used to design the course:** the current [education repository](https://github.com/xulabs/edu), its [tutorial specification](https://github.com/xulabs/edu/blob/main/guide/Tutorial_Creation.md), the [published CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub), the [lab publication page](https://xulabs.github.io/publication/), and the [lab BibTeX bibliography](https://raw.githubusercontent.com/xulabs/xulabs.github.io/master/doc/reference_xulab.bib).
