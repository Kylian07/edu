# Study guide: learning bioimage analysis on your own with BiologyToBioimage

This guide is for the student working alone. It explains how to study a module, which equations
and procedures you should be able to reproduce, the notation traps, how to prepare for a project,
and how to move from Level 1 (the course core) to Level 2 (the research frontier) and to reading
research papers. Everything you need is in the notebooks: they teach the content themselves.

---

## 1. The study loop (for every module)

1. **Run the notebook once, top to bottom** (Runtime → Run all on Colab). Read the 🧫 biological
   question, the 🎯 objectives and the 🗺️ contents. The goal of this pass is the big picture.
2. **Work section by section.** For each section: read the theory and say every "*In words:*"
   sentence back in your own words, run the cells, then read 🔍 *What just happened?* and check it
   against what you see. Do every ✏️ *Your turn* — that is where the learning happens.
3. **Pen and paper.** Re-derive or re-draw every displayed equation, kernel or diagram before
   moving on. If a step feels like magic, the earlier module named in the key-information table's
   *Prerequisites* row usually has the missing piece.
4. **Consolidate with the summary boxes.** In Level 1, the 📘 *Lecture notes* boxes summarise a
   part of the course's content: definitions, key equations and a worked example. In Level 2, the
   📄 *Research connection* boxes say what the field does and where it is going. You should be able
   to explain every box without looking at the code.
5. **Self-test** with ✅ *Checkpoint*: answer before opening the hidden answer. Then try one
   🧠 discussion question and one 🚀 bonus item.
6. **Write the 📝 lab note.** Five minutes; it is your revision sheet.

A module takes about 1.5–2.5 hours this way. It is better to do one module properly than three
quickly.

## 2. Worked examples to recompute by hand

- The Sobel/Roberts/Prewitt/Kirsch kernels applied to a tiny hand-drawn 5×5 patch, and the Canny
  pipeline's non-maximum suppression and hysteresis thresholds on it (Module 06).
- A 3×3 Hough accumulator vote for three points known to lie on one line (Module 06).
- The GLCM of a tiny 4-level, 4×4 synthetic patch and its contrast/homogeneity Haralick features
  (Module 07).
- A 2×2 Mahalanobis-distance calculation between one point and a two-class Gaussian cluster with a
  non-diagonal covariance (Module 07).
- One EM update (E-step responsibilities, M-step mean/variance/weight) for a 1-D, two-component
  Gaussian mixture on five numbers (Module 10).
- The Dice and IoU of two small overlapping binary masks you draw by hand (Module 11).
- The cost matrix and the Hungarian assignment for four detections across two frames (Module 14).
- The Kabsch rotation that best superimposes three point pairs (Module 15).
- A Wiener-filter restoration of a 1-D toy signal at two different noise-to-signal ratios, to see
  the bias–variance trade-off directly (Module 17).
- Pearson's and Manders' colocalization coefficients for two tiny synthetic channels (Module 18).
- The query–key–value computation and softmax attention weights for three length-4 toy token
  vectors (Module 19).

## 3. The equations and procedures to master

These are the "can you derive or re-draw it on a blank page?" results of Level 1.

| Idea | Module |
|---|---|
| The imaging pipeline: acquire → process → measure → decide | [00](notebooks/00_welcome_bioimage_analysis.ipynb) |
| NumPy array/channel conventions; dtype clipping pitfalls | [01](notebooks/01_python_numpy_for_images.ipynb) |
| The Gaussian point-spread function and why blur is a convolution | [02](notebooks/02_what_is_a_digital_image.ipynb) |
| 2-D convolution by hand; Gaussian vs. mean smoothing trade-off; histogram equalization | [03](notebooks/03_filtering_and_histograms.ipynb) |
| The 2-D Fourier transform; low-pass/high-pass filtering; image pyramids | [04](notebooks/04_frequency_domain_and_scale.ipynb) |
| Local-maximum detection; Delaunay correspondence; sub-pixel Gaussian-fit localisation | [05](notebooks/05_keypoints_and_particles.ipynb) |
| Gradient operators; non-maximum suppression; hysteresis thresholding; the Hough accumulator | [06](notebooks/06_edges_lines_and_curves.ipynb) |
| GLCM/Haralick texture; Mahalanobis distance; information gain for a decision tree; the SVM margin | [07](notebooks/07_classical_feature_based_classification.ipynb) |
| Forward propagation; the softmax + cross-entropy loss; backpropagation by the chain rule | [08](notebooks/08_deep_learning_classification.ipynb) |
| PCA as an eigenproblem of the covariance matrix; the autoencoder bottleneck | [09](notebooks/09_dimensionality_reduction_and_reconstruction.ipynb) |
| 1-D EM for a Gaussian mixture; marker-controlled watershed; the Chan–Vese energy | [10](notebooks/10_segmentation_classical.ipynb) |
| Transposed convolution; the U-Net skip connection; the Dice loss | [11](notebooks/11_segmentation_deep.ipynb) |
| IoU; non-maximum suppression; the anchor/RPN idea | [12](notebooks/12_object_detection.ipynb) |
| The VAE's reconstruction + KL (ELBO) loss; the GAN minimax objective | [13](notebooks/13_image_synthesis_and_generative_models.ipynb) |
| The Kalman-filter predict/update step; the Hungarian algorithm's assignment problem | [14](notebooks/14_object_tracking.ipynb) |
| Mutual information between two images; the Kabsch SVD-based rotation | [15](notebooks/15_image_registration.ipynb) |
| PSNR/SSIM; FFT low-pass denoising; the bicubic-to-SRCNN residual-learning idea | [16](notebooks/16_denoising_and_super_resolution.ipynb) |
| The degradation model g = h∗f + n; inverse filtering's instability; the Wiener filter | [17](notebooks/17_restoration_and_inverse_problems.ipynb) |
| Pearson/Manders colocalization; the Clark–Evans index; Ripley's L and its CSR envelope | [18](notebooks/18_colocalization_and_spatial_statistics.ipynb) |
| Scaled dot-product self-attention; the ViT patch-embedding pipeline; the DDPM forward process | [19](notebooks/19_attention_transformers_diffusion.ipynb) |

**Level 2 additions** (understand the idea and the toy implementation once each): evaluating a
zero-shot segmenter honestly against a specialist baseline, in- vs. out-of-distribution (20); the
paired image-to-image training objective and why it can hallucinate (21); per-cell feature
embeddings and batch-effect correction (22); neighbourhood-enrichment permutation testing and
one-layer message passing (23); calibration/reliability diagrams and the active-learning sampling
loop (24); patch-based 3-D training and overlap-add stitching (25); gradient/occlusion attribution
and a leakage-vs-grouped-split comparison (26); the plan → call-tool → observe loop of a verified
agent (27).

## 4. Notation (and the traps)

| Topic | What varies | Course convention |
|---|---|---|
| Image axes | `(x, y)` vs. `(row, col)` vs. `(y, x)` | arrays are indexed `(row, col)` = `(y, x)`; the notebook says so at first use |
| Intensity range | `[0, 255]` uint8 vs. `[0, 1]` float | this course uses float images in `[0, 1]` unless stated otherwise — watch for silent `uint8` overflow when you convert back |
| Boxes | `(x1, y1, x2, y2)` vs. `(ymin, xmin, ymax, xmax)` | this course uses `(ymin, xmin, ymax, xmax)`, matching the toolkit's `iou_boxes` |
| Masks | binary `{0, 1}` vs. label image `{0, 1, 2, …}` | a *mask* is binary; a *label image* (instance segmentation) numbers each object from 1, with 0 = background |
| Convolution vs. correlation | true convolution flips the kernel; most image-processing libraries (and this course) use correlation and call it "convolution" | noted explicitly in Module 03 |
| Frequency | cycles per pixel vs. cycles per image | the notebook always states which axis a frequency-domain plot uses |
| Attention | row-vector vs. column-vector convention for Q, K, V | this course uses row-vectors: one row per token/patch |

## 5. The ideas that recur everywhere

1. **Simulate with a known truth, then check.** Every module's 🧪 box compares a method's output
   against the ground truth the simulator returns — the single habit most worth carrying into real
   research (18, 22, 24, 26 make this explicit as a methodological point, not just a teaching
   device).
2. **Classical methods are baselines, not relics.** Modules 07/10 (classical classification and
   segmentation) and 20 (foundation-model evaluation) all make the same point: a fast, interpretable
   classical method is the bar a fancier method must clear, and sometimes does not.
3. **A pipeline is a chain of imperfect steps.** Restoration (16–17) feeds segmentation (10–11),
   which feeds detection (12) and tracking (14), which feeds quantification (18); an error anywhere
   upstream propagates, which is why the capstone (28) builds and audits a complete chain rather
   than one isolated step.
4. **Generative and learned models need a reality check.** VAEs/GANs (13), virtual staining (21)
   and diffusion (19) can all produce plausible-looking but wrong output; the course returns to this
   point explicitly in 21 and 26.
5. **Evaluation is part of the method.** Held-out, grouped, leakage-free splits; calibration;
   out-of-distribution testing (Module 26) and honest uncertainty (Module 24) are as much a part of
   a bioimage-analysis method as the algorithm itself.

[`FRONTIER_MAP.md`](FRONTIER_MAP.md) shows how each Level 1 idea grows into a Level 2 method.

## 6. Preparing for a project

- For each module: redo the ✅ checkpoint without looking; re-derive or re-draw the row of the
  table in §3; explain the 📘/📄 boxes to someone else.
- Work the numerical examples of §2 by hand, then check them in the notebook.
- **The project** (one simulated or real data set, several methods): Module 28 (the capstone) is a
  complete worked example with an evaluation contract, a report structure, three research-track
  extension ideas and a reproducibility checklist to adapt.

## 7. From Level 1 to research

- **Finish Level 1 first.** Every Level 2 module names the core modules it builds on in its
  key-information table.
- **Pick a track** (see the README): imaging foundation models & restoration, quantitative & spatial
  biology, or trustworthy & data-efficient AI.
- **Use the ground truth.** In every Level 2 module, predict the result of a 🧪 check before running
  it, then change a simulator parameter (fewer cells, a stronger batch effect, more noise, an
  out-of-distribution shape mix) and see which methods break first. This is how researchers
  stress-test methods.
- **Then go to real data.** The 🧭 *From toy to real data* section of each Level 2 module names
  public tools and model zoos to use next. Reproduce one result of the module on a small real data
  set with the production tool, and compare.
- **Reading a research paper:** What is the biological question and the unit of replication? What
  is the baseline? How were the data split, and could information leak between train and test? What
  is the evidence that the method found something true (a ground truth, an experiment, a
  replication)? What would change your mind? Write a five-line summary in your lab notebook.

## 8. When you are stuck

| Symptom | What to do |
|---|---|
| `NameError` for a function or variable | run the notebook from the top (setup and toolkit cells first); after a kernel restart everything must be re-run |
| Numbers slightly different from the text | library versions differ; the conclusion should not change. If it does, re-run from the top (the seeds assume top-to-bottom order) |
| A PyTorch cell is slow | it should take seconds to about two minutes on Colab's CPU; close other heavy notebooks, or reduce the number of training steps (an exercise often asks you to) |
| A step makes no sense | check the *Prerequisites* row of the key-information table; the earlier module it names covers the missing piece |
| A result contradicts what a paper reports | the data are simulated and often cleaner than real microscopy data; the notebook explains what the simulation can and cannot show |

## 9. Lab-note template

```text
Module:                         date:
Biological question:
Data (simulated: which simulator, and what the hidden truth is):
Output (what the code produced):
Method (one sentence):
Key equation or procedure (and its reading in words):
Key parameters (and what changed when I modified one):
Ground-truth check (what the method recovered vs. the truth):
One failure mode / assumption that can break:
Connection to the course's topics or to research (paper, tool):
One question I still have:
```
