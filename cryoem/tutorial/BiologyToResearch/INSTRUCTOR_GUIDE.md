# Instructor guide and answer keys

**Delivery:** 75-minute lab + 20-minute discussion per module. Allow 15 minutes to debug data shapes, units and random seeds. Suggest one weekly biology journal-club session for paper integration. Do not present synthetic outcomes as evidence of biological efficacy.

## Formative assessment rubric (each notebook, 10 points)

- Correctly explains biological measurement and input/output (2)
- Correctly interprets a key physical or statistical assumption (2)
- Re-runs and modifies code with controlled parameter study (2)
- Reports suitable metrics and failure case (2)
- Connects the result to a cited paper, distinguishing illustration from reproduction (2)

## Answer guidance for challenges

### M01 — From molecular complexes to voxels

**Challenge:** Change the radius or positions of the blobs. Which representation preserves depth? How would a hollow vesicle differ from a solid protein complex?

**Expected reasoning:** A single projection loses depth: many distinct volumes can have similar projections.

### M02 — Python, images, units, and reproducibility

**Challenge:** Double voxel size without changing the array; what physically changes, and what stays constant?

**Expected reasoning:** Array shape is unchanged; physical field of view doubles. Display scaling changes appearance but not data.

### M03 — Vectors, 3D rotations, and coordinate systems

**Challenge:** Create a 90° rotation and determine which axes are permuted. Why is it invalid to align particles by translations alone?

**Expected reasoning:** Rotations change orientation but preserve pairwise distances; translation-only correction leaves rotational mismatch.

### M04 — Fourier transforms and spatial frequency

**Challenge:** Increase blur sigma to 4; identify which spectral components shrink most and explain why.

**Expected reasoning:** High spatial frequencies shrink most because Gaussian convolution multiplies the spectrum by a low-pass Gaussian.

### M05 — From electron projections to a tilt series

**Challenge:** Try ±30° instead of ±60°. Which orientations become unsampled? Why are tilts rarely a full 180°?

**Expected reasoning:** Restricted tilt coverage leaves missing angular information; thickness, stage geometry and dose constrain sampling.

### M06 — Low-dose imaging and contrast transfer

**Challenge:** Increase noise standard deviation. Which detail is lost? Why are CTF zeros fundamentally difficult to invert?

**Expected reasoning:** CTF zeros remove particular frequency information; no amount of naïve division can recover information absent at a zero.

### M07 — Missing wedge and inverse reconstruction

**Challenge:** Vary angular coverage and quantify mean-squared error. Why can a learned prior improve appearance without ensuring truth?

**Expected reasoning:** Fewer observed frequencies increase ambiguity; hallucinated features can fit the prior while disagreeing with specimen.

### M08 — Fourier-shell correlation and validation

**Challenge:** Regenerate noisy maps with half the noise. What changes? Explain why half-map independence and masking matter.

**Expected reasoning:** Lower noise usually increases FSC. Correlated training/masking artifacts may inflate a reported resolution.

### M09 — Particle picking and object detection

**Challenge:** Sweep detection threshold; count false positives and false negatives within 3 pixels. Why is accuracy a poor metric for sparse particles?

**Expected reasoning:** Background voxels dominate accuracy. Report object-level precision/recall, localization tolerance and errors per volume.

### M10 — Alignment with similarity and optimization

**Challenge:** Add a 15° rotation before translation. Explain why pure correlation may then fail and why a missing-wedge-aware distance is useful.

**Expected reasoning:** Rigid alignment requires 3 rotations and 3 translations in 3D; missing-wedge support should be accounted for in similarity.

### M11 — Template-free structural pattern mining

**Challenge:** Run K=2,3,4 and vary PCA dimensions. Why does clustering agreement not prove a novel biological complex?

**Expected reasoning:** Cluster stability, controls, structural evidence, and external validation are required for biological discovery.

### M12 — Averaging, classification, and conformations

**Challenge:** Plot log RMSE against log N. Explain why systematic alignment bias does not disappear with more samples.

**Expected reasoning:** Random independent noise decays as 1/sqrt(N), but conformational mixing creates persistent structural bias.

### M13 — 3D convolutional features and classification

**Challenge:** Compare max pooling vs global average pooling and write down what spatial detail is lost. What would an unlabeled validation split test?

**Expected reasoning:** Global pooling discards precise location. Biological conclusions need held-out tomograms and specimens, not just patch splits.

### M14 — Semantic segmentation and 3D U-Net

**Challenge:** Choose thresholds by validation rather than testing data; compare boundary quality when two objects touch.

**Expected reasoning:** Overlap alone can hide disconnected membranes, merged instances or topology errors.

### M15 — Autoencoding and self-supervised feature learning

**Challenge:** Compare 3 versus 20 PCA components. How can the masking strategy accidentally leak target information?

**Expected reasoning:** Masked-value prediction yields features without manual class annotation, but task-specific downstream validation is essential.

### M16 — Few-shot, one-shot, active learning

**Challenge:** Simulate five query rounds with labels revealed only after query. Compare random sampling over multiple random seeds.

**Expected reasoning:** A fair active-learning comparison fixes initial labels, labeling budget, evaluation data, and random seeds.

### M17 — Domain shifts, open sets, and calibration

**Challenge:** Vary shift severity; report risk-coverage when rejecting uncertain samples. Why can an unknown particle be classified with high softmax confidence?

**Expected reasoning:** Softmax need not detect out-of-distribution structures; explicitly evaluate unseen class, specimen and site shifts.

### M18 — Self-supervised denoising without clean labels

**Challenge:** Replace independent noise by spatially correlated noise. When can neighbor-based self-supervision fail?

**Expected reasoning:** Pixelwise independence is a crucial assumption; correlated noise leaks information through neighbors.

### M19 — Physics-aware simulation and domain randomization

**Challenge:** Train a simple classifier on low-density scenes and test at high density. Which randomized parameters improve robustness?

**Expected reasoning:** A simulator should document noise model, acquisition geometry, structural templates, and train/test domain split.

### M20 — Equivariance and orientation estimation

**Challenge:** For 90° rotation, derive the transformation of the centroid about the image center. Which quantities should an alignment network predict equivariantly?

**Expected reasoning:** Identity representation should suppress pose; an orientation estimator must retain pose information and respect rotation composition.

### M21 — Promptable and tri-planar segmentation

**Challenge:** Move the prompt to background and quantify precision/recall. When can 2D slice consistency conflict with 3D continuity?

**Expected reasoning:** 2D segmentations can disagree across views; real methods need semantic embeddings and geometric constraints.

### M22 — Topology, Betti numbers, and membranes

**Challenge:** Remove just a few voxels to open an enclosed cavity; record Dice and cavity-count changes. Why is topology-aware validation needed?

**Expected reasoning:** Small local errors can catastrophically alter connectivity or cavities even when voxel Dice remains high.

### M23 — Identity, conformation, and imaging transformation

**Challenge:** Design held-out transformations and test whether a learned identity embedding remains stable. Why can disentanglement be non-identifiable?

**Expected reasoning:** Without assumptions or supervision, many latent factorizations explain the same observations.

### M24 — Semi-supervised and knowledge-guided clustering

**Challenge:** Add a penalty that pulls confirmed pairs together before K-means. Compare with labels randomly swapped to simulate incorrect expert knowledge.

**Expected reasoning:** Prior constraints can improve meaningful grouping, but label errors and biased priors can also suppress novel discoveries.

### M25 — Score/flow priors versus physical measurements

**Challenge:** Compare λ=0 (with numerical clipping) versus λ>0. Explain the role of a learned score prior and why it cannot restore unique unmeasured evidence.

**Expected reasoning:** Regularization trades bias against noise amplification; learned priors also introduce distributional assumptions.

### M26 — Research capstone: from crowded scene to evidence

**Challenge:** Create a one-page research report: define biological question, specimen, simulated acquisition, method, data split, metric, failure modes and which paper you would read next.

**Expected reasoning:** Separate image-level and particle-level metrics; compare external tomograms, conduct ablations, and explicitly avoid claims unsupported by observed data.


## Summative checks

- **After M08:** derivation quiz explaining angular coverage, frequency-domain zeros, independent half-map FSC.
- **After M12:** submit align-average-cluster analysis with one purposely mixed class and discuss bias.
- **After M17:** hold out complete tomograms/acquisitions, not neighboring subtomograms; analyze transfer to new acquisition.
- **After M22:** construct a high-Dice but topologically invalid segmentation and detect it with Betti-based evaluation.
- **After M26:** 6–8 page mini-study and 5-minute viva comparing a baseline with a chosen Xu Lab method.

### Research reproducibility checklist

1. Freeze seeds/environment and archive data/metadata provenance.
2. Ensure no particle-level leakage across train/test tomograms and no shape-model overlap between simulated training and benchmark.
3. Respect wedge geometry, dose, CTF and voxel sizes rather than rely solely on PSNR/SSIM.
4. Include ablations, uncertainty, compute costs, failure cases and biological validation.
5. Separate reimplementation of conceptual components from reproduction of official paper code.
