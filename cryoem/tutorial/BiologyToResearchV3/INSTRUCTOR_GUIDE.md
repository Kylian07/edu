# 🧑‍🏫 Instructor guide

For faculty, TAs and research mentors who use **BiologyToResearchV3** as a course, a reading group, or onboarding for new
undergraduate researchers. Students should start from the [README](README.md); this guide covers planning, per-module
teaching notes, assessment and maintenance.

---

## 1 · Formats that work

| Format | Plan | Notes |
|---|---|---|
| Two-semester course (recommended) | the 30-week schedule in the [README](README.md#suggested-two-semester-schedule-2--15-weeks--45-h-per-week) | one 90-min session per module: 20 min concept, 50 min guided notebook, 20 min paper discussion |
| One-semester course | 00–04, 06–07, 09–11, 13–15, 19–20, 23, 25–26 | skip 05 only if students already know PyTorch |
| Lab onboarding (summer) | Parts A–C in 3 weeks, then the part matching the student's project, then 26 | pair each student with the paper their project builds on ([atlas](PAPER_ATLAS.md)) |
| Journal club | one reading path per term ([reading guide](READING_GUIDE.md)) | the presenter runs the module's toy live and fills in the audit worksheet |

**Before week 1.** Ask students to open module 00 in Colab and run it top to bottom (≈ 1 minute). This catches account,
browser and network problems early. All notebooks also run offline with stand-in shapes; tell students that the warning
"procedural stand-in (offline fallback)" means the download failed, not that the notebook is broken.

---

## 2 · Learning outcomes by part

| Part | Students can… | Evidence |
|---|---|---|
| A · Foundations (00–05) | load and slice maps; rotate molecules; read a power spectrum; choose and interpret a statistical test; train and validate a small network without leakage | lab notes; checkpoints; a one-page "experiment diagram" |
| B · Imaging physics (06–09) | simulate a projection with a CTF, a tilt series with a missing wedge, a crowded cell; compute and interpret a gold-standard FSC | short written explanation of why tomograms are anisotropic |
| C · Classical cryo-ET (10–14) | pick, align (wedge-aware), average, classify by maximum likelihood, mine patterns without templates | audit of Xu, Beck & Alber 2012 or MPP 2019 |
| D · Deep learning (15–18) | train and interpret 3D CNNs; work with few labels; measure and reduce domain shift | an error analysis of a classifier on shifted data |
| E · Unsupervised & geometric (19–22) | explain and run deep alignment, iterative deep clustering, disentanglement, self-supervised denoising | audit of Gum-Net or DISCA |
| F · Frontiers & biology (23–26) | pick from sparse labels; segment with foundation models; turn coordinates into biological claims; run the full pipeline | capstone report + paper audit |

---

## 3 · Per-module teaching notes

Each line gives the one idea to land, the most common difficulty, and a discussion prompt.

| Module | Land this idea | Students usually struggle with | Discuss |
|---|---|---|---|
| 00 | A tomogram is a noisy 3D photograph of a crowded cell; averaging many copies reveals structure | the scale (nm vs Å vs µm) | Why not just take a sharper picture? |
| 01 | Images and volumes are arrays; `[z, y, x]` indexing | axis order and slicing | What does one voxel of 10 Å "contain"? |
| 02 | Rotations are matrices; invariant features ignore orientation | active vs passive rotations; composition order | Which molecular properties survive rotation? |
| 03 | Every image is a sum of waves; resolution = frequency | phase vs magnitude; `fftshift` | Why does rotating a molecule rotate its spectrum but shifting it does not change the magnitude? |
| 04 | Signal can be detected below the noise by averaging and testing | p-values vs effect sizes; multiple testing | What is the unit of replication in a tomography experiment? |
| 05 | A network is a fitted function; validation must be honest | data leakage (particle vs tomogram splits) | How would you detect leakage in a published table? |
| 06 | The microscope images phase contrast filtered by the CTF | sign flips and zeros of the CTF | Why collect at several defoci? |
| 07 | A ±60° tilt range leaves a missing wedge; objects stretch along z | which axis the wedge lies on | What biological shapes are most distorted? |
| 08 | Simulations with crowding are the benchmark's ground truth | why simple simulators flatter methods | What does a simulator *not* model? |
| 09 | FSC between independent halves measures reproducibility | 0.143 (half-maps) vs 0.5 (map vs truth) | Can a map be reproducible but wrong? |
| 10 | Picking trades precision for recall; template matching has bias | interpreting precision–recall curves | When is a template-free picker preferable? |
| 11 | Wedge-constrained correlation + fast rotational search make alignment practical | Fourier masks and normalisation | Why does ignoring the wedge align particles by their wedges? |
| 12 | Local refinement, masking neighbours, and parallelism scale alignment | local vs global optimisation | Where would a gradient method get stuck? |
| 13 | Reference-free averaging and maximum likelihood; reference bias | "Einstein from noise" | How do you prove an average is not reference bias? |
| 14 | Template-free discovery finds what you did not expect | judging cluster redundancy | How would you name an unknown pattern? |
| 15 | 3D CNNs classify subtomograms; benchmarks are simulated | class imbalance; transfer | What does high SHREC accuracy *not* tell you? |
| 16 | Interpretability and voxel segmentation | reading CAMs critically | Is a heat map evidence of what the network uses? |
| 17 | Few-shot, self-supervised, active and open-set learning cut labels | evaluation with tiny test sets | Which label is most valuable to collect next? |
| 18 | Domain shift is the default; adaptation and randomisation help | measuring shift without target labels | Is a model trained on simulation ever "done"? |
| 19 | Networks can learn alignment without labels; equivariance helps | the toy may not beat classical search — honestly reported | When is deep alignment worth it? |
| 20 | Iterative deep clustering with BIC (DISCA) | similar-sized complexes merge | How do you validate clusters without labels? |
| 21 | Separate content from pose (Harmony) | latent spaces and VAEs | What would a "content" axis mean biologically? |
| 22 | Denoise without clean data (J-invariance, cycles, scores) | denoisers can hallucinate | When must you *not* interpret a denoised tomogram? |
| 23 | Unlabelled ≠ negative (PU learning); exemplars + MAE; meta-learning | ranking vs calibration | Why did the similarity loss hurt with random crops? |
| 24 | Foundation models segment with one click; topology matters | prompts and propagation | Who checks a segmentation nobody labelled? |
| 25 | Biological claims need null models, replication units, orthogonal evidence | pseudo-replication; choice of null | Grade each claim of the fungal paper on the ladder of evidence |
| 26 | Evaluate last; reproducible ≠ correct; audit like a reviewer | patience (≈ 3–4 min runtime); over-splitting | What would convince you a new class is real? |

**Known toy behaviours worth discussing (not bugs).** Module 19: the Gum-Net-lite toy does not beat exhaustive search —
the notebook explains why. Module 20: RuBisCO and ClpB merge at 2 nm resolution, as the text discusses. Module 23: the
CryoMAE similarity loss with random crops *hurts*, and an oracle control shows why (a PU problem). Module 26: BIC may
split one molecule into two classes; both get the same identity, which motivates the merge exercise; the "segregation"
p-values are an artefact of the null model, which the notebook explains.

---

## 4 · Assessment

| Component | Weight | What students hand in |
|---|---|---|
| Lab notes | 20 % | the 📝 template of every module, with one parameter change and its effect |
| Checkpoints | 10 % | answers before opening the hidden solutions (honour system or short quizzes) |
| Paper audits | 30 % | four audits during the year (one per semester half), using the worksheet in the [reading guide](READING_GUIDE.md) |
| Mini-projects | 15 % | two ✏️/🚀 extensions, each with a one-page write-up |
| Capstone | 25 % | Module 26 report (abstract written *before* unsealing), evaluation, audit, 10-min presentation |

### Rubric — paper audit (score each row 0–3)

| Criterion | 3 = excellent |
|---|---|
| Biological question | states the question and why it matters, in the student's own words |
| Data and split unit | names datasets (EMPIAR/EMDB IDs), real vs simulated, and the level of the train/test or replication split |
| Method and key equation | inputs → outputs in three steps; the equation written and read in words |
| Evidence | identifies the numbers that carry the claim, with baselines and uncertainty |
| Limitations | a concrete failure case and a falsification test |
| Reproduction | runs the module's toy and relates its result (agreeing or not) to the paper |

### Rubric — capstone (score each row 0–4)

| Criterion | 4 = excellent |
|---|---|
| Pipeline | every step runs; parameters justified; at least one step improved over the baseline |
| Honest evaluation | abstract written before unsealing; evaluation compares claims with truth and explains discrepancies |
| Biology | claims graded on the ladder of evidence; null models discussed |
| Communication | clear figures, a results table, reproducible seeds and settings |
| Audit | complete worksheet for one atlas paper, with a falsification test |

---

## 5 · Maintaining the course

- **Notebooks are stored without outputs.** After editing, clear outputs and run `python validate_notebooks.py --execute`
  (≈ 35–45 min on a laptop CPU; each notebook takes ≤ ~5 min).
- **The toolkit is copied into every notebook** so each runs alone. If you change a helper in
  [`course_toolkit.py`](course_toolkit.py), update the copies too; `python validate_notebooks.py` reports any notebook whose
  copy differs from the reference.
- **Pinned data.** PolNet and NGL downloads use pinned commits (see `POLNET_COMMIT`, `NGL_COMMIT`), so results stay stable.
  To change the data, update the constants in the toolkit and in the notebooks, then re-execute.
- **The atlas.** When a ⚠️ or 🟡 paper becomes readable, verify it, update its row in [`PAPER_ATLAS.md`](PAPER_ATLAS.md) and
  [`publication_map.csv`](publication_map.csv), and extend the matching module's 📄 box. Never fill gaps from memory.
- **New lab papers.** Add a row to the atlas, choose the module whose idea is closest, add a 📄 box there (question, method,
  toy link, results, code), and, if the idea is new, a short toy section.
- **Versions.** Developed and executed with Python 3.13, NumPy 2.5, SciPy 1.18, scikit-learn 1.9, PyTorch 2.14 and Matplotlib 3.11; [`requirements.txt`](requirements.txt)
  lists minimum versions. Colab's preinstalled stack runs all notebooks.
