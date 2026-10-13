# Research bridge: the mathematics and reasoning behind Xu lab cryo papers

The [22 notebooks](readme.md) provide an intuitive first pass. This guide is the second pass: it connects the same ideas to the equations, assumptions, and validation questions used in research papers. Work through it after notebook 16, then return to it while reading the [paper atlas](paper_atlas.md). A first-year biology student can start with the conceptual paragraphs and worked numbers. Derivations marked **deep dive** can be revisited after calculus, linear algebra, and probability courses.

## 1. One language for the whole field: a forward model

A forward model predicts measured images from a proposed structure. An inverse method works backward from measured images to structure. Let `V(r)` be a three-dimensional molecular density or electrostatic-potential representation; `R` a rotation; `P_R` the projection at that orientation; `H` the microscope's contrast transfer operator; `D` the detector/sampling operator; and `ε` noise. A useful schematic is

```text
observed image y = D[ H * P_R(V) ] + ε .
```

For a tilt series, `R` is partly known from the stage angle but must be refined because the specimen can move or deform. For single-particle cryo-EM, each particle's orientation is initially unknown. For subtomogram analysis, a reconstructed volume is cropped around each candidate and its 3D pose is estimated. The formula is intentionally schematic: realistic models include dose, motion, defocus variation, thickness, inelastic scattering, detector response, and noise correlations.

**Worked question.** Suppose a reconstruction looks elongated. Is that a feature of `V`, a bias in `R`, a gap in projection directions, or a segmentation artifact? Draw one test for each possibility. This is how to turn a visual impression into an evidence plan.

**Paper connection.** The 2019 [marker-free tilt alignment](https://doi.org/10.1093/bioinformatics/btz323) paper concerns estimating geometry `R`. The 2012 [Fourier-space matching](https://doi.org/10.1016/j.jsb.2012.02.014) paper concerns comparing transformed crops while respecting measurement limitations. The 2025 [AITom toolkit](https://doi.org/10.1016/j.jsb.2025.108207) joins multiple pipeline steps.

## 2. Sampling, noise, and what a “resolution” number means

A voxel spacing of `a` Å places samples `a` Å apart. The Nyquist period is `2a` Å: a pattern that alternates faster cannot be distinguished on that grid. This is a ceiling imposed by sampling. It is not a guarantee that the specimen and microscope produced interpretable information at that scale. If `a = 4 Å`, the Nyquist period is `8 Å`; an actual map may only support 20 Å details.

For aligned observations `x_i = s + ε_i`, with independent, zero-mean errors of variance `σ²`, the mean is `x̄ = s + (1/N)Σ ε_i`. Because independent variances add, `Var(x̄−s)=σ²/N`, hence the noise standard deviation is `σ/√N`. If “SNR” means signal amplitude divided by noise standard deviation, it grows as `√N`; if it means signal power divided by noise power, it grows as `N`. This model fails when particles are misaligned, differ biologically, or share correlated errors.

**Deep dive: independent half-map FSC.** Split particles before refinement into two disjoint groups, reconstruct independent maps `V₁` and `V₂`, Fourier-transform them, and compare coefficients on each 3D frequency shell `S_q`:

```text
FSC(q) = Re[Σ_{k∈S_q} F₁(k) conjugate(F₂(k))]
         / sqrt[(Σ_{k∈S_q}|F₁(k)|²)(Σ_{k∈S_q}|F₂(k)|²)] .
```

A 0.143 crossing is a common convention for *gold-standard* half-map FSC, subject to correct independence and masking. It does not mean every position or direction has that resolution. A local-resolution method asks how evidence varies across the map; directional analysis asks how missing views affect different orientations. Reusing the same reference or mask information across halves can inflate apparent agreement. Ask whether the paper discloses the split, refinement, masking, and uncertainty. The [local FSC paper](https://doi.org/10.1186/s12859-020-03680-6) is a useful companion.

**Practice.** Calculate a 64-voxel box width at 4 Å/voxel (`25.6 nm`), then compare a 2 Å pixel-size Nyquist period with a reported 8 Å FSC resolution. State why the numbers can differ.

## 3. From projections to a tomogram

A projection collapses one direction through a 3D object. Rotate the object and collect more projections, and spatial features that overlap in one view can separate in another. The Fourier slice theorem states that the 2D Fourier transform of a projection equals a central plane in the 3D Fourier transform of the object (under the ideal projection model). Tomography combines many such planes to estimate the 3D object.

Cryo-ET normally cannot collect every tilt. Extreme tilts make the specimen effectively thicker and image quality poorer, while holder geometry limits movement. Unmeasured planes form a **missing wedge** in Fourier space. This creates anisotropic resolution and can elongate density along the poorly sampled direction. No denoising network can prove the missing information was measured; it can only infer a plausible completion using learned assumptions.

Tilt alignment matters before reconstruction. Gold fiducials can provide landmarks; marker-free methods must infer image shifts, rotation, and related geometry from image content. In a crowded cell, successful alignment should be checked by residuals or independent structural consistency, not merely by a smooth-looking tomogram. Weighted back-projection is fast but can show streaks; iterative methods can reduce some artifacts at computational cost. Their apparent smoothness is not equivalent to higher independent resolution.

**Practice.** Draw a circle of views around a sample, shade only angles from −60° to +60°, and mark the absent directions. Predict how a small spherical object will look in orthogonal slices. Use the [IMOD/Etomo tutorial](https://bio3d.colorado.edu/imod/doc/etomoTutorial.html) as a real-workflow reference; this course does not require the large dataset or local installation.

## 4. Particle detection, pose, and averaging are coupled

A candidate subtomogram has location, orientation, and possibly class or conformation as hidden variables. A template-matching detector compares image patches with a known pattern, often using normalized cross-correlation. A learned picker estimates a score from annotated examples or self-supervised features. In both cases a threshold turns scores into picks, and the precision–recall balance changes with threshold. Evaluation must define a localization tolerance and match detections to reference objects without counting duplicates as separate successes.

Rigid 3D pose contains three translations and three rotation parameters. Exhaustive fine search over all possibilities is expensive. A common strategy is coarse candidate search, then local refinement. Similarity should account for the missing wedge, CTF, and background; otherwise the algorithm may align artifacts. Symmetric molecules create equivalent poses, and flexible molecules may have no single rigid alignment that fits every domain.

Averaging can reveal a recurring structure, yet it can also hide heterogeneity. One way to formalize class uncertainty is a latent-variable model. For class `c` and pose `R`, a likelihood `p(y|c,R,V_c)` measures how well class map `V_c` predicts particle `y`. An expectation step estimates a probability for each class/pose; a maximization step updates maps using those probabilities. Multiple initializations and independent validation help because the optimization may converge to a misleading solution. Compare the [2018 fast-alignment plus maximum-likelihood paper](https://doi.org/10.1093/bioinformatics/bty267), [Gum-Net](https://openaccess.thecvf.com/content_CVPR_2020/html/Zeng_Gum-Net_Unsupervised_Geometric_Matching_for_Fast_and_Accurate_3D_Subtomogram_CVPR_2020_paper.html), and the 2025 BOE-ViT entry in the [atlas](paper_atlas.md).

**Deep dive: a useful adversarial control.** Align noise-only crops or simulated non-target structures to the same reference. If their average begins to resemble the reference, the pipeline is susceptible to reference bias. A paper should also test held-out particles, alternative initial models, and biological plausibility.

## 5. Why an unsupervised class is not a protein name

“Unsupervised” means the algorithm can form groups without a named label for every training example. It does not mean the resulting groups are automatically molecular species. A cluster may separate acquisition settings, particle orientations, cell compartments, conformations, or contamination. The central challenge in de novo pattern mining is to make the representation sensitive to stable molecular content and insensitive to nuisance transformations.

Suppose an encoder maps each subtomogram `x_i` to a vector `z_i`. Clustering might minimize `Σ_i ||z_i−μ_{c_i}||²`. This objective only says the vectors are compact around centers. It does not enforce protein identity. Validation can include class averages, reproducibility across tomograms, known structural motifs, spatial localization, perturbations, and independent molecular labels. A rare discovery needs particular care: a small cluster is also where artifacts collect.

The lab's research progression can be read as a sequence of questions: [template-free detection](https://doi.org/10.1093/bioinformatics/btr207) asks how to find candidates; [2019 de novo pattern mining](https://doi.org/10.1016/j.str.2019.01.005) asks how recurring structures can be recovered and interpreted; [2023 deep unsupervised clustering](https://doi.org/10.1073/pnas.2213149120) asks how to scale the process; and recent content–transformation work asks whether composition, conformation, and pose can be separated. After each paper, write **what remained unsolved** that motivated the next.

**Practice.** Build a two-column table for five clusters: “algorithmic evidence” and “biological evidence.” If a cluster is reproducible but has no molecular validation, what conclusion is justified?

## 6. Scarce labels, self-supervision, and transfer

A supervised model learns from explicit examples. A few-shot model uses a small labeled support set; a one-shot model uses one. Weak supervision uses incomplete, coarse, or indirect labels. Active learning chooses which item should be annotated next, often using uncertainty or diversity. Open-set recognition allows “unknown” instead of forcing every object into a training class. These are different responses to the same practical problem: expert labels are costly and new structures exist.

Self-supervision uses structure in the input data as a training signal, such as masked prediction, contrasting related views, or a blind-spot denoising target. Its success depends on the pretext task preserving biologically important content. If two conformations are treated as interchangeable positive pairs, a representation may become invariant to the very state a biologist wants to study. If a denoiser sees its own target through neighboring correlated noise, it can learn noise rather than signal.

**Domain shift** is change between training and use conditions: microscope, defocus, dose, ice, species, cellular context, annotation policy, or class distribution. A model trained on simulated images can perform well on simulations and fail on real cells. Domain randomization, adaptation, and transfer learning can help, but a held-out real test remains necessary. Split at the biological specimen or at least tomogram level when estimating deployment performance; crops from one tomogram are not independent specimens.

**Practice.** Design a fair comparison of [few-shot learning](https://doi.org/10.1371/journal.pcbi.1008227), [active learning](https://doi.org/10.1093/bioinformatics/btab123), and [CryoMAE](https://openaccess.thecvf.com/content/WACV2025/papers/Xu_CryoMAE_Few-Shot_Cryo-EM_Particle_Picking_with_Masked_Autoencoders_WACV_2025_paper.pdf). Fix the same annotation budget and independent test specimens; report class-level error and repeated random draws. Which aspects remain incomparable because the tasks differ?

## 7. Denoising, simulation, segmentation, and generative priors

A simulator needs biological geometry and an imaging forward process. It can create ground-truth coordinates and controlled counterfactuals. It also imports assumptions: if the simulated background is too simple, a detector may learn a shortcut. The lab's simulation and synthesis studies are best read by comparing synthetic and real distributions and asking which details are truly measured. Denoising has a related tension. A cleaner image may be easier for a human or downstream model, but it might erase a rare small object or invent a plausible-looking one.

Segmentation labels voxels; detection localizes objects; classification names crops. A single system can do several tasks, but each needs its own metric and validation. Dice overlap can be high while a membrane has a biologically important gap. A 3D mask assembled from 2D prompts can disagree across orthogonal planes. Topology-aware methods try to preserve connectedness or avoid holes, but should be evaluated on biologically relevant topology, not just a scalar overlap score.

A foundation or generative model contributes a **prior** based on earlier training data. In a reconstruction-like objective `data_misfit(V) + λ prior(V)`, increasing `λ` favors the prior over measured data. The prior can stabilize weak measurements, but it can also push toward a familiar structure. Test raw-data consistency, cross-plane continuity, seed and prompt sensitivity, independent maps, and biological controls. This frame helps compare [CryoSAM](https://arxiv.org/abs/2407.06833), [DUAL](https://doi.org/10.1101/2024.03.02.583135), and the 2026 entries in the [atlas](paper_atlas.md).

**Practice.** For a denoising or segmentation paper, write a three-row table: “raw-data evidence,” “model-prior contribution,” and “independent biological check.” An empty third row identifies a limit of the conclusion.

## 8. How to read a methods section at research depth

Use this audit for each atlas paper:

| Question | What to extract |
|---|---|
| Biological or technical problem | The exact unmet need, and why the earlier method was insufficient. |
| Input and output | Raw movies, tilt series, tomograms, subtomograms, maps, masks, or labels; include units and dimensions. |
| Forward and inverse assumptions | Geometry, noise, CTF, class model, priors, invariances, and data availability. |
| Supervision | Dense labels, sparse labels, support examples, pretraining, or no named labels. |
| Evaluation unit | Particles, tomograms, specimens, cell types, instruments; say what was held out. |
| Baseline and metric | Strongest relevant earlier method, precision/recall, Dice, pose error, FSC, biological endpoint, and compute. |
| Failure and uncertainty | Small/rare structures, anisotropy, domain shift, bad ice, class imbalance, alternate explanations. |
| Biological claim | What is measured directly; what is inferred; what independent evidence supports the inference. |

A good final report draws one figure that connects `specimen → measurement → algorithm → result → claim`, marking every assumption. It compares at least two papers in one research lineage, runs one self-contained computation, and proposes a test that could change the conclusion. The [capstone notebook](tutorial/biology_first/21_paper_capstone.ipynb) provides a short template.

## Answers to the numeric checks

- A 64-voxel box at 4 Å/voxel spans `64×4 = 256 Å = 25.6 nm` per side.
- A 2 Å pixel spacing has a 4 Å Nyquist period, while an 8 Å achieved resolution indicates the measured and processed data support less detail than the sampling grid could represent.
- If four identical, independently noisy particles are aligned and averaged, noise standard deviation halves; with sixteen it falls by a factor of four. This result does not apply unchanged to correlated noise or mixed structures.

These answer sketches check arithmetic and core logic. Most research questions here require argument, figures, and evidence from the specific paper rather than a single numerical answer.
