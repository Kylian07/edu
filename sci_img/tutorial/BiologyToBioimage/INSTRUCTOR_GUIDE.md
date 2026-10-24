# 🧑‍🏫 Instructor guide

For faculty, TAs and mentors who use **BiologyToBioimage** alongside CMU 02-740 *Bioimage
Informatics*, as a bridge course for first-year biology majors entering computational imaging, or
as structured self-study for undergraduate researchers joining a bioimage-analysis lab. Students
should start from the [README](README.md). This guide covers formats, learning outcomes, how the
course's thematic organisation relates to a lecture-based syllabus, per-module teaching notes,
assessment ideas, and maintenance.

**Design principles.** (1) *Self-contained:* the notebooks teach the course's content themselves —
definitions, pipelines, worked examples, figures (drawn by code) and the "what to remember" points
— so students never need the lecture slides; 📘 *Lecture notes* boxes summarise each part of the
content. (2) *Synthetic data with a known truth:* the repository stores no data or pictures; every
data set is simulated (see [`DATA.md`](DATA.md)), which lets every method be checked against the
truth (🧪 boxes). (3) *Implement, then use:* classical and deep algorithms are both implemented
from scratch (or in a few dozen lines of NumPy/PyTorch) before any production tool is named.
(4) *Organised by theme, not by lecture number:* because a course's lecture order and slide
numbering are revised from year to year, this course groups material into thematic Parts (A–K)
instead of mirroring any one semester's deck order — a deliberate choice so the course does not
need to be renumbered every time the lectures are reorganised.

---

## 1 · Formats that work

| Format | Plan | Notes |
|---|---|---|
| Companion to 02-740 | Part A before the semester (or in week 1), then the remaining Parts in the thematic order of §3 below, paced to roughly follow the semester's topic order | recitations can run a module's key section live; ✏️ exercises make good warm-up problems; 📘 boxes are ready-made revision sheets |
| Second course / lab-onboarding elective (Level 2) | Part J (20–27) over 6–8 weeks, then the capstone (28) | assumes Level 1; each module is roughly 1.5–2.5 h of guided work plus exercises |
| Bridge for incoming students | Modules 00–19 over a summer or a semester (≈ 5–7 h/week), Level 2 and the capstone during a research rotation | front-loads the material most students find hardest to pick up quickly from lecture alone |
| Lab onboarding / rotations | Part A, the Level 1 Part matching the student's project, then the matching Level 2 track and the capstone | pair with the [`foundation`](../README.md) phases in this same directory for more engineering-heavy follow-up work |

**Before week 1.** Ask students to open Module 00 in Colab and run it top to bottom (≈ 1 minute) to
catch account and browser problems early. No downloads are needed: every data set is generated in
the notebook.

---

## 2 · Learning outcomes by part

| Part | Students can… | Evidence |
|---|---|---|
| A · Foundations (00–01) | explain the acquire → process → measure → decide pipeline; write NumPy code that indexes, crops and composites multichannel images | a lab note on a toy multichannel composite |
| B · Seeing like a microscope (02–04) | explain why different microscopy contrast modes exist; implement convolution-based filtering and histogram equalization; compute and read a 2-D FFT | a side-by-side simulated bright-field/phase/fluorescence comparison; a before/after FFT low-pass denoise |
| C · Finding structure (05–06) | implement sub-pixel particle localisation and the Canny edge-detection pipeline; run a from-scratch Hough transform | a point-detection pipeline recovering a known particle count and position; a Hough-detected line set checked against ground truth |
| D · Classifying bioimages (07–08) | extract GLCM/shape/Mahalanobis features and train a classical classifier; train and evaluate a small CNN; recognise class imbalance | a classical-vs-CNN accuracy comparison on the same simulated cells |
| E · Latent structure (09) | derive PCA as an eigenproblem; compare PCA, MDS, Isomap and t-SNE; train a small autoencoder | an eigenimage visualisation and a reconstruction-error comparison across methods |
| F · Segmenting, detecting, synthesizing (10–13) | run thresholding, watershed, active contours and normalized cut; train a U-Net; build a sliding-window detector; train a VAE and a small GAN | Dice/IoU scores against simulated ground truth; a detector precision/recall curve; a VAE latent-space interpolation |
| G · Across time and space (14–15) | implement Kalman-filter and Hungarian-algorithm tracking; register two images by points and by mutual information | a recovered lineage checked against the simulator's true tracks; a recovered transform checked against the true one |
| H · Restoring signal (16–17) | denoise with FFT, wavelet and learned methods; restore a degraded image with a Wiener filter; explain PALM/STORM | PSNR/SSIM before/after; a Wiener-filter bias–variance sweep |
| I · Quantifying and modern architectures (18–19) | run a colocalization and spatial-statistics analysis with an appropriate null model; implement self-attention and a toy diffusion model from scratch | a Ripley's-L-vs-CSR-envelope plot on simulated clustered/dispersed/random patterns; a working ViT patch-classification demo |
| J · Research frontier (20–27) | evaluate a foundation-model segmenter honestly against a specialist baseline; explain virtual-staining hallucination risk; correct a batch effect; run a neighbourhood-enrichment test; quantify and act on model uncertainty; explain volumetric-imaging scale challenges; audit a model for leakage/shift; describe a verified agent loop | ground-truth checks throughout each module; a short written audit of one trained model's failure modes |
| K · Capstone (28) | run a complete simulate→restore→segment→classify→track→quantify pipeline end to end and report results against a known truth | the capstone report and one pursued project-studio extension |

---

## 3 · How this course's Parts relate to a lecture-based syllabus

The notebooks never point to slides or lecture numbers, and this guide deliberately does not give a
"lecture N → module M" table, because a specific semester's lecture order and numbering can and
does change. Instead, the table below gives the **topic correspondence** — the broad subject area
each Part covers — so an instructor can align recitations with whatever that semester's lecture
order happens to be, without the mapping going stale when the lectures are reorganised.

| This course's Part | Broad topic area it corresponds to |
|---|---|
| A · Foundations | course introduction; programming prerequisite |
| B · Seeing like a microscope | optics and microscopy contrast; image formation, sampling and filtering |
| C · Finding structure | point/particle and edge/line feature detection |
| D · Classifying bioimages | classical and deep-learning image classification |
| E · Latent structure | dimensionality reduction |
| F · Segmenting, detecting, synthesizing | classical and deep segmentation; object detection; generative models |
| G · Across time and space | object tracking; image registration |
| H · Restoring signal | denoising, super-resolution and restoration |
| I · Quantifying and modern architectures | colocalization and spatial statistics; attention/transformer and diffusion architectures |
| J · Research frontier | topics beyond a typical lecture syllabus: foundation models, virtual staining, image-based profiling, spatial omics, uncertainty, volumetric scale, trustworthy AI, AI agents |
| K · Capstone | an integrative project |

If your own course materials are reorganised in a future semester, this table (and the course
itself) does not need to change: match the broad topic area in the right-hand column to wherever it
now sits in your updated syllabus.

---

## 4 · Per-module teaching notes

Each line gives the one idea to land, a typical difficulty, and a discussion prompt.

| Module | Idea to land | Typical difficulty | Discussion prompt |
|---|---|---|---|
| 00 | the acquire → process → measure → decide pipeline | treating "image analysis" as one single technique | What is the biological question behind a given bioimage, and which step of the pipeline answers it? |
| 01 | images are arrays; `axis=` and broadcasting | silent dtype overflow/clipping when converting between float and uint8 | Why does a fixed seed make a simulation reproducible but not "real"? |
| 02 | contrast comes from the imaging mode, not just the sample | confusing resolution with magnification; confusing bit depth with dynamic range | Why might the same specimen look completely different under phase-contrast vs. fluorescence? |
| 03 | convolution as a weighted local average; Gaussian vs. mean smoothing trade-off | kernel-size/sigma intuition; edge effects at image borders | When would you prefer a smaller, noisier kernel over a larger, smoother one? |
| 04 | the FFT re-expresses an image, it does not change what is "in" it | interpreting a 2-D frequency-magnitude plot | Why does removing high frequencies blur an image rather than just "clean" it? |
| 05 | a full classical point-detection pipeline, not just one filter | tuning the local-maximum threshold; over- vs. under-detection | What would happen to this pipeline on a very dense or very sparse field of particles? |
| 06 | the Canny pipeline is several distinct classical ideas chained together | the two hysteresis thresholds; the Hough accumulator as a voting scheme | Why does non-maximum suppression need the gradient direction, not just its magnitude? |
| 07 | features + a classical classifier is still a strong, fast baseline | choosing features that actually separate the classes; the curse of too many weak features | What would you check before trusting a classifier with 50 features and 30 training examples? |
| 08 | a neuron is one logistic unit; a CNN learns its own filters | gradient/shape bugs; overfitting with few labelled images | What does one of your CNN's learned filters look like, and how would you check it is biologically meaningful? |
| 09 | PCA finds the directions of greatest variance; non-linear methods preserve different structure | reading loadings; t-SNE's distances between distant clusters are not meaningful | What could a 2-D PCA "map" of your cells fail to show you? |
| 10 | watershed and active contours solve "touching objects" differently | over-segmentation from noisy markers; snake initialisation sensitivity | Why might watershed and Chan–Vese give different answers on the very same image? |
| 11 | skip connections let a U-Net keep fine spatial detail that a plain FCN loses | the weighted loss needed to separate touching objects; Dice vs. IoU | Why is accuracy a poor metric for a mostly-background segmentation task? |
| 12 | a detector must find both *where* (box) and *what* (class) | choosing an IoU threshold for "correct"; anchor-box tuning | What's the cost of a detector's false negative vs. false positive in a real screening pipeline? |
| 13 | shape-space, VAE and GAN are three different generative strategies | VAE blurriness vs. GAN instability; evaluating "realism" | What would convince you a generated synthetic cell image is useful, not just pretty? |
| 14 | tracking-by-detection reduces to a new assignment problem every frame | choosing a sensible cost function; handling divisions/appearances/disappearances | What cost matrix entries would you use to let the Hungarian algorithm handle a cell division? |
| 15 | correlation assumes a linear intensity relationship; mutual information does not | local optima in the registration search; choosing the right transform family | Why would you need mutual information rather than correlation to register a fluorescence image to a brightfield one? |
| 16 | different noise types need different denoising strategies | PSNR/SSIM disagreeing with visual impression | Why might a learned denoiser fail on a noise type it never saw in training? |
| 17 | inverse filtering is unstable; Wiener filtering trades bias for stability | choosing the noise-to-signal regularisation parameter | What happens to a Wiener-filtered image as you sweep its regularisation parameter from too small to too large? |
| 18 | the choice of spatial null model changes what "significant" means | conflating colocalization with physical interaction | What would (and would not) convince you that two proteins are truly interacting, from imaging alone? |
| 19 | attention is a learned, content-based soft neighbour average | keeping track of tensor shapes through multi-head attention | What does a trained attention map actually tell you about which patches "matter" to each other? |
| 20 | a foundation model must be compared against a real specialist baseline, not just used | unconsciously grading a foundation model on a favourable benchmark | When would you choose a fine-tuned specialist over a generalist foundation model, and why? |
| 21 | virtual staining can look convincing and still be wrong | no obvious way to tell a hallucinated structure from a real one without a check | What decision would you refuse to make from a virtual stain alone, and why? |
| 22 | a batch effect and a treatment effect can look identical in raw features | over- or under-correcting a batch effect | How would you tell whether your batch correction removed noise or removed signal? |
| 23 | spatial statistics plus cell typing answer "who is near whom", not "who causes what" | treating co-location as proof of a causal interaction | What experiment would you need to turn a spatial correlation into a causal claim? |
| 24 | a model can be confident and wrong; calibration and uncertainty are different things | conflating "high accuracy" with "well calibrated" | Given a fixed annotation budget, would you rather label the model's most confident or least confident predictions, and why? |
| 25 | processing in patches changes what is practical, not (ideally) what is correct | forgetting to account for patch-boundary effects | What would silently go wrong if you processed a large volume in patches with no overlap at all? |
| 26 | "it worked on my test set" is not enough to trust a model elsewhere | mistaking a model's own confidence or a nice-looking saliency map for proof of correctness | Find one way this very notebook's own pipeline could be leaking information — can you fix it? |
| 27 | an agent is only as trustworthy as its verification step | treating an agent's plausible output as a verified result | What is the one thing you would always insist a human check before acting on an agent's bioimage pipeline? |
| 28 | a real analysis is a chain of imperfect steps that must be audited end to end | losing track of where error enters the pipeline | If your capstone pipeline's final number were wrong, which step would you suspect first, and how would you check it? |

---

## 5 · Assessment

- **Checkpoints** (✅, with hidden answers) work as entry/exit tickets; a handful per module.
- **Lab notes** (📝 template at the end of each notebook): one per module; grade for correct
  inputs/outputs/method, a sensible failure mode, and (Level 2) the ground-truth check result.
- **Hand calculations** that mirror the worked examples in [`STUDY_GUIDE.md` §2](STUDY_GUIDE.md#2-worked-examples-to-recompute-by-hand):
  a small Canny/Hough example, a GLCM on a tiny patch, one EM update, a Hungarian assignment, a
  Kabsch rotation.
- **Level 2 mini-projects:** change one simulator parameter and report which methods break (e.g. a
  stronger batch effect in 22, more out-of-distribution shapes in 20/26, a lower signal-to-noise
  ratio in 16/17), with the ground-truth metric before and after.
- **Capstone** (Module 28): a report plus one pursued project-studio extension. Suggested rubric
  (the notebook contains a student-facing version):

| Criterion | Excellent (4) | Adequate (2–3) | Insufficient (0–1) |
|---|---|---|---|
| Pipeline and evaluation contract | every stage justified, a stated baseline, a metric fixed before looking at results | most elements present | metric chosen after seeing results |
| Methods | each step correctly implemented and sensibly parameterised | some steps ad hoc | a stage silently skipped or misapplied |
| Results and ground truth | checked against the simulated truth at each relevant stage, honest about limitations | a single end-to-end number only | no ground-truth check at all |
| Interpretation | correctly distinguishes what the simulation shows from what it cannot | some overreach | causal or real-data claims from a toy simulation |
| Reproducibility and communication | seeded, runs end to end, clear figures and report | minor gaps | cannot be rerun |

---

## 6 · Technical notes and maintenance

- **Tested with** Python 3.10+, NumPy, SciPy, scikit-image, scikit-learn, Matplotlib, PyWavelets and
  PyTorch (CPU). Every notebook runs in well under five minutes on a 2-core CPU.
- **Structure check:** `python validate_notebooks.py` checks the schema, required sections and
  header keys, Colab badges, stripped outputs, relative links, that every toolkit copy matches
  `course_toolkit.py`, that no notebook refers to lecture slides, embeds or links a picture, or
  reads/downloads data, and that no data files or files over 400 kB are stored. `--execute` also
  runs every notebook.
- **Editing a notebook:** edit in Jupyter, run it top to bottom, check that the narrative still
  matches the outputs (the simulations are seeded), then clear outputs before committing
  (`jupyter nbconvert --clear-output --inplace notebooks/NN_*.ipynb`).
- **Changing a shared helper:** edit `course_toolkit.py`, then replace the definition in the
  🧰 toolkit cell of every notebook that uses it — the validator lists each stale copy. Changing a
  simulator changes the numbers in every notebook that uses it; re-check their narratives.
- **Reorganising the course:** because Parts (not lecture numbers) carry the thematic structure,
  reordering a future semester's lectures never requires renumbering these notebooks — only this
  guide's §3 topic-correspondence table may need a light touch-up.
- **Data policy:** no data files, no pictures, no downloads (see [`DATA.md`](DATA.md)).
