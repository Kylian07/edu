# Answer key and instructor notes

These are concise model answers to the three end-of-tutorial checks. The independent experiments are intentionally open-ended: report measured results, not invented outputs.


## T01 — From biological observations to datasets

1. No; distributions can overlap. 2. Image-level concerns an individual image, whereas set-level compares how often descriptions apply across two groups. 3. No; images within a donor can be correlated and would overstate independent replication.

**Instructor note:** Before opening the plot, predict which group will have the larger average elongation. Then (a) find one B cell more elongated than an A cell; (b) count specimens in each group; (c) name one real microscopy confounder (magnification, staining, or acquisition batch); (d) propose how you would collect biological replicates.


## T02 — Python for biological data analysis

1. Reuse, testability, and inspectability. 2. Division fails or yields undefined values; explicitly validate empty data. 3. Allows readers to reproduce the generated examples (not to guarantee real-world results).

**Instructor note:** Implement `fraction_above(xs, threshold)` so it returns a float. Add input validation for empty lists. Compare fractions at thresholds 1.3, 1.5, and 1.7. Explain why reporting a threshold without its definition is scientifically incomplete.


## T03 — NumPy, matrices, and visualization

1. Number of features. 2. Otherwise the larger numerical range can dominate distance or covariance. 3. Measurements for feature j across all samples.

**Instructor note:** Compute means by condition without `.groupby` (use boolean masks on NumPy arrays). Introduce one intentionally missing value and explain why a naïve mean could fail. Create a plot in which axis labels report the physical quantity and unit (if known).


## T04 — Digital images as measurable biological data

1. Calibration supplies the physical pixel size. 2. No; it depends on sensor and imaging procedure. 3. Changes in exposure or illumination can systematically alter data and embeddings.

**Instructor note:** Alter the threshold to 0.20, 0.35, and 0.55; graph the change in apparent area. Create a third dataset by brightening B images by 10%, while leaving geometry unchanged. What kind of false difference could a caption-based method surface?


## T05 — Probability, sampling, and dataset distributions

1. Sampling uncertainty under the resampling model. 2. No. 3. Dataset inclusion, sampling, and batch effects determine observed feature distributions.

**Instructor note:** Repeat with only 10 cells per group. Compare intervals to those from 60. Then artificially duplicate each observation ten times and re-bootstrap as if all 600 rows were independent: explain why the resulting precision is misleading.


## T06 — Vectors, dot products, and projections

1. A vector specifying an axis along which observations are measured. 2. Dot product zero. 3. Embedding width is feature-space dimensionality; the dataset has a separate sample axis.

**Instructor note:** Draw a two-dimensional scatterplot and project every point onto a chosen unit direction. Compare projection [1,0] versus [1/sqrt(2),1/sqrt(2)]. Predict the matrix shapes before running the code.


## T07 — Cosine similarity, covariance, and correlation

1. Yes; the statistics are defined over different objects. 2. Cross-covariance uses paired rows. 3. Near-zero means weak linear association; strong negative means a strong opposite linear association. CCDiff ranks by small absolute |rho|.

**Instructor note:** Calculate correlation before and after random permutation in 20 trials, reporting the mean and range. Also compare cosine similarity of [1,0] and [10,0]. Explain why cosine ignores magnitude while covariance generally does not.


## T08 — Standardization, PCA, and singular value decomposition

1. Within-dataset projected variance. 2. Correlation of paired projections of two views. 3. Scaling and inversion can amplify noise or encounter singular matrices.

**Instructor note:** Add a feature column containing the constant value 1. How does a standard scaler handle it? Examine the singular values and numerical rank. Explain why PCA is not the same as CCDiff's inverse CCA.


## T09 — Machine learning, generalization, and distribution shift

1. No; it describes an association. 2. To estimate generalization to unseen observations. 3. It leaks specimen-level information and inflates test performance.

**Instructor note:** Repeat after dropping elongation and evaluate the change. Make one train/test split that deliberately duplicates observations between the sets. Write down why leakage creates overly optimistic performance and why feature drift is not always label drift.


## T10 — Neural networks and pretrained visual features

1. A spatial map of feature responses. 2. A reusable mapping from images to numerical embeddings. 3. No; it uses frozen/pretrained encoders during core analysis.

**Instructor note:** Create a horizontal-edge filter and compare its response to the vertical-edge filter. Then imagine how exposure, resizing, and field of view could change a learned representation even without a biological phenotype difference.


## T11 — CLIP, contrastive learning, and image–text embeddings

1. Both encoders map modalities to an aligned feature space. 2. No; it is a learned similarity signal subject to bias and domain shift. 3. 2,000 entries (100 by 20).

**Instructor note:** Write `image_text_similarity(X,Y)` with shape validation and row normalization. Compare normalized and raw dot products when all text embeddings are multiplied by 50. Optional real CLIP: after installing `transformers`, `torch`, and an accessible checkpoint, load it explicitly and run one image–text similarity example; this is not required for the offline assignment.


## T12 — Caption generators and candidate concept banks

1. It provides a common candidate space for comparison before selecting representative concepts. 2. Not with this fixed-candidate ranking procedure. 3. Model similarity may not reflect clinically justified statements.

**Instructor note:** Prepare a 20-term bank of cell-morphology descriptions. Mark each as directly observable, ambiguous, or requiring additional clinical/biological evidence. Reproduce the missing-concept experiment and explain why a high-ranking incorrect substitute is still a methodological failure.


## T13 — Paired biological views and cross-covariance

1. A row-to-row pairing. 2. Yes, if the numbers of paired samples are equal. 3. The row-level correspondence between the two measurements.

**Instructor note:** Repeat 100 independent row shuffles. Histogram the Frobenius norm of the resulting cross-covariance matrices. Explain what sample pairing adds that mere knowledge of two distributions does not.


## T14 — Canonical correlation analysis: geometry and objective

1. Correlation between projected paired views. 2. Removes arbitrary scale and yields a bounded correlation objective. 3. No; CCDiff considers components with the smallest absolute correlations.

**Instructor note:** Start from covariance and explain why a constraint is needed for each projection. Compare the correlations of the original first columns with the first canonical correlation; repeat on random, *independent* X and Y to probe spurious in-sample association.


## T15 — CCA computation, rank, regularization, and stability

1. No; overfitting is possible. 2. The repeated text matrix has rank bounded by the number of distinct concepts and by centered feature width. 3. To test whether the learned relationship generalizes.

**Instructor note:** Vary the feature width from 2 to 5 to 15 to 30 at fixed 50 training pairs. Record first training/held-out canonical correlations over at least ten seeds. Why should this result make you cautious about low correlation in the inverse-CCA pipeline?


## T16 — Low-correlation components and inverse CCA

1. It seeks low-magnitude relationships, including near zero, rather than strong positive or negative correlation. 2. A's selected text embeddings with B's images. 3. No; row pairing, finite sample estimation, and coverage all matter.

**Instructor note:** Test an identical-set negative control by using A for both own and opposing images. Then test a shuffled pairing control on twenty seeds. How stable are the selected directions and concept labels? Discuss what you can and cannot conclude from the observed numerical results.


## T17 — Candidate selection from average image–text similarity

1. To make the dot products cosine similarities. 2. 60 by 12. 3. No; it measures representativeness within the selected set. Distinctiveness is considered later.

**Instructor note:** Introduce a new vector representing an irrelevant but always positive/background-like concept. Check whether it appears in both top-$k$ sets. Compare mean similarity with median similarity as an **exploratory alternative**; explain how a rare strongly matching subset could affect each estimator.


## T18 — Cross-set pairing, inverse-CCA components, and concept matching

1. Images from B. 2. To compare the projection direction in coordinates corresponding to original concept embeddings. 3. Repeating concepts creates rows without adding distinct semantic observations, potentially destabilizing covariance estimates.

**Instructor note:** Reconstruct `inverse_cca_candidates` from scratch using 2-dimensional examples. Record the canonical correlation before and after changing the modulo pairing order. Then repeat on deliberately **identical image sets**; if a label remains highly ranked, what does that tell you about the assumption that low correlation proves uniqueness?


## T19 — Combining inverse correlation and within-set relevance

1. Strong negative correlation also has large association magnitude; the method favors weak absolute correlation. 2. No, it is a heuristic. 3. Alpha=0 ranks on inverse correlation alone; alpha=1 ranks on within-set relevance alone.

**Instructor note:** Construct a hand-calculated two-candidate example: candidate X has similarity 1 and inverse score .2; Y has similarity .2 and inverse score 1. Determine for which values of alpha X outranks Y. Then test all-equal similarity values and decide on a safe denominator convention.


## T20 — Build the complete pedagogical CCDiff pipeline

1. The discovery pipeline does not train a new vision-language encoder; pretrained encoders exist already. 2. No; validate separately. 3. Exact preprocessing, checkpoints, dataset construction, metrics, and evaluation, with controlled compute.

**Instructor note:** Implement the five steps without calling the helper functions (you may still use numpy, StandardScaler, and scikit-learn CCA). Create a table listing intermediate array shapes. Change both groups to be identical and document what happens; this is a negative control, not a performance claim.


## T21 — Benchmark metrics, baselines, and reproducibility

1. No; the paper uses an LLM semantic judge with graded scores. 2. No; caption generation and evaluation involve pretrained or external models. 3. Point estimates conceal uncertainty and sampling variability.

**Instructor note:** Write a metric adapter specification for scores in {0, .5, 1}; do not implement a fake GPT-4 evaluator. Recompute Table 1 performance gaps and discuss why point-estimate differences may not demonstrate statistical significance. Compare exact-label and meaning-based matching on five synonym examples.


## T22 — Ablations, pairing stability, and scientifically meaningful controls

1. One chosen factor while others are held fixed. 2. It estimates false discoveries in a no-difference case. 3. No; a stable artifact can still be uninformative.

**Instructor note:** Create a CSV experiment log with seed, top-k, alpha, candidate bank quality, and top-1 phrase. Calculate the fraction of trials that rank the known morphological difference first. Distinguish 'same output under random pairings' from 'demonstrated statistical validity' and propose one better paired- or unpaired-view test.


## T23 — Biomedical case study: microscopy and medical claims

1. No, they are pedagogical vectors on known feature axes. 2. Authorized credentialed dataset access and compliance with dataset/license/privacy terms. 3. Such differences are model-supported descriptions, requiring clinical ground truth and expert validation.

**Instructor note:** Validate the actual morphological difference with a manual or rule-based measurement (aspect ratio), not merely with the text ranker. Add a third batch with altered exposure but identical cell shapes and identify any spurious description. Design a review protocol for clinical concepts that prevents unsupported diagnostic wording.


## T24 — Read, reproduce, and critically defend the paper

1. No; cross-domain validation and expert interpretation remain necessary. 2. Rank directions with weak absolute cross-set CCA correlations and map them to candidate descriptions, combining the result with within-set relevance. 3. Identical or independently sampled same-distribution image sets, together with pairing randomization.

**Instructor note:** Prepare a 15-minute research-group presentation: (1) task, (2) key mathematical formulation of CCA, (3) Algorithm 1 flowchart with all tensor shapes, (4) principal reported benchmark results and their evaluator, (5) one reproduced toy experiment, (6) identical-set and pairing controls, and (7) an extension. Submit a two-page critique with a falsifiable hypothesis and a proposed experiment. Never invent unrun benchmark figures.
