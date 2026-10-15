# From Biology to Machine Learning: a self-study companion to CMU 02-620

A notebook-based course that takes a **first-year biology major** from "what is a genotype
matrix?" to a **deep, working understanding of every lecture of CMU 02-620 *Machine Learning
for Scientists*** — regression and regularisation, classification (k-NN, naïve Bayes,
logistic regression, trees, random forests, SVMs), clustering, mixture models and EM, PCA,
Bayesian networks, Gaussian graphical models, hidden Markov models, Bayesian learning and MCMC,
neural networks and model selection. The course has 25 modules (00–24). Each is an executable
Jupyter notebook that runs on a free Google Colab CPU, follows the storyline, notation and
worked examples of the corresponding 02-620 slides, derives every formula step by step,
implements every algorithm from scratch in NumPy, and applies it to real biological data.

**Start here:** [00 · Welcome: what machine learning does for biology](notebooks/00_welcome_ml_for_biology.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xulabs/edu/blob/main/ml/tutorial/BiologyToML/notebooks/00_welcome_ml_for_biology.ipynb)

---

## Who it is for and what you will be able to do

**Assumed background:** high-school algebra and introductory biology. No programming,
calculus, linear algebra or statistics is assumed. Part A teaches exactly the parts of the
02-620 prerequisites (02-601 *Programming for Scientists*, 02-680 *Essential Mathematics and
Statistics for Scientists*) that the lectures use, at the moment they are needed, and every
equation in the course comes with a plain-language "*In words:*" reading.

**By the end you will be able to:**

1. Formulate a biological question as a learning problem — inputs X, outputs Y, the function
   f, supervised P(Y∣X) or unsupervised P(X) — and choose a method family for it.
2. Derive, by hand, the results the 02-620 slides derive: least squares as maximum likelihood,
   ridge as MAP, the lasso's soft-thresholding, naïve-Bayes counts, the logistic-regression
   gradient, information gain, the SVM margin and dual, k-means and EM updates, PCA as an
   eigenproblem, Bayesian-network factorisations, d-separation, variable elimination, Chow–Liu
   trees, the precision-matrix/conditional-independence identity, the forward–backward and
   Viterbi recursions, Baum–Welch, conjugate posteriors and Gibbs sampling, back-propagation,
   and the bias–variance decomposition.
3. Implement each of these algorithms in a few dozen lines of NumPy, check it against
   scikit-learn/SciPy, and explain every number it prints.
4. Analyse real data honestly: GWAS-style regression, leukaemia classification and class
   discovery (Golub *et al.* 1999), signalling-network learning from single cells (Sachs *et al.*
   2005), with proper train/validation/test splits, cross-validation and uncertainty.
5. Carry out a complete 02-620-style project — one data set, three methods — and write it up.

---

## Roadmap

| Part | Module | Time | 02-620 deck(s) |
|---|---|---|---|
| **A · Foundations** | [00 · 🧬 Welcome: what machine learning does for biology](notebooks/00_welcome_ml_for_biology.ipynb) | 1.25 h | `001_intro` 12–60 |
| | [01 · 🐍 Python & NumPy for biologists](notebooks/01_python_numpy_for_biologists.ipynb) | 2 h | prerequisite (02-601) |
| | [02 · 🎲 Probability: the language of uncertainty](notebooks/02_probability_for_biologists.ipynb) | 2.5 h | prerequisite (02-680) |
| | [03 · 📐 Vectors and matrices: the shape of biological data](notebooks/03_linear_algebra_for_data.ipynb) | 2.5 h | prerequisite (02-680) |
| | [04 · ⛰️ Calculus and optimization: how machines learn](notebooks/04_calculus_and_optimization.ipynb) | 2.5 h | prerequisite |
| | [05 · 🪙 Learning from data: likelihood, MLE and MAP](notebooks/05_likelihood_mle_map.ipynb) | 2.5 h | `001_intro` 38–69 |
| **B · Supervised learning** | [06 · 📈 Linear regression and genome-wide association](notebooks/06_linear_regression_gwas.ipynb) | 2.5 h | `002_regression` 1–46 |
| | [07 · 🪢 Regularization: ridge, lasso and sparse genetic effects](notebooks/07_ridge_lasso_sparse_regression.ipynb) | 2.5 h | `002_regression` 45–70 |
| | [08 · 🧮 Classification I: k-nearest neighbours and naïve Bayes](notebooks/08_knn_naive_bayes.ipynb) | 2.5 h | `003_classification-kNN-NB` |
| | [09 · 📉 Classification II: logistic regression, generative vs discriminative](notebooks/09_logistic_regression.ipynb) | 2.5 h | `004_classification-LR` |
| | [10 · 🌳 Decision trees, random forests and cancer driver mutations](notebooks/10_decision_trees_random_forests.ipynb) | 2.75 h | `005_decision-tree` |
| | [11 · ⚔️ Support vector machines: margins, support vectors and kernels](notebooks/11_support_vector_machines.ipynb) | 2.75 h | `007_SVM` |
| **C · Unsupervised learning** | [12 · 🧩 Clustering: k-means, hierarchical clustering and co-expressed genes](notebooks/12_clustering_kmeans_hierarchical.ipynb) | 2.5 h | `006_clustering` |
| | [13 · 🫧 Mixture models and the EM algorithm](notebooks/13_mixture_models_em.ipynb) | 3 h | `010_mixture-model` |
| | [14 · 🗺️ Principal component analysis: genes mirror geography](notebooks/14_pca_dimensionality_reduction.ipynb) | 2.5 h | `011_PCA` |
| **D · Probabilistic graphical models** | [15 · 🕸️ Bayesian networks I: graphs that factorize probability](notebooks/15_bayesian_networks_representation.ipynb) | 2.25 h | `008_BN` 1–37 |
| | [16 · 🚦 Bayesian networks II: reading independence from the graph](notebooks/16_bayesian_networks_independence.ipynb) | 2.5 h | `008_BN` 38–96 |
| | [17 · 🔎 Bayesian networks III: inference and learning a signalling network](notebooks/17_bayesian_networks_inference_learning.ipynb) | 3 h | `008_BN` 97–174 |
| | [18 · 🔗 Gaussian graphical models: networks from correlations](notebooks/18_gaussian_graphical_models.ipynb) | 2.5 h | `009_GGM` |
| | [19 · 🎲 Hidden Markov models I: decoding hidden states in sequences](notebooks/19_hmm_inference.ipynb) | 3 h | `012_HMM-DBN` 1–95 |
| | [20 · 🔁 Hidden Markov models II: learning, Baum–Welch and beyond](notebooks/20_hmm_learning.ipynb) | 2.75 h | `012_HMM-DBN` 96–134 |
| **E · Bayesian learning, neural networks, model selection** | [21 · 🎰 Bayesian learning and MCMC](notebooks/21_bayesian_learning_mcmc.ipynb) | 2.5 h | `013_Bayesian-MCMC` |
| | [22 · 🧠 Neural networks: from logistic regression to deep learning on DNA](notebooks/22_neural_networks.ipynb) | 3 h | `014_NN` |
| | [23 · ⚖️ Model selection: bias, variance, cross-validation and the limits of prediction](notebooks/23_model_selection.ipynb) | 3 h | `015_model-selection` |
| | [24 · 🏁 Capstone: one dataset, three methods — a complete 02-620-style project](notebooks/24_capstone_project.ipynb) | 6–10 h | project (`001_intro` 10), all decks |

Total: about **61 hours** of notebook work for Modules 00–23 plus **6–10 hours** for the
capstone; with slide reading, textbook sections and the exercises, plan for **120–150 hours**.
The slide-by-slide correspondence is in [`SLIDE_MAP.md`](SLIDE_MAP.md).

```text
 Part A  Foundations ───────────► Part B  Supervised learning ─────────► Part C  Unsupervised learning
 (Python, probability, linear       (regression & GWAS, ridge/lasso,        (k-means & hierarchical clustering,
  algebra, calculus, MLE/MAP)        k-NN, naïve Bayes, logistic            mixtures & EM, PCA)
                                     regression, trees, SVMs)                        │
                                                                                     ▼
 Part E  Bayesian learning, neural ◄──────────────────────────── Part D  Probabilistic graphical models
 networks, model selection, CAPSTONE                             (Bayesian networks, GGMs, HMMs & DBNs)
```

The order follows the dependencies of the ideas rather than the calendar of the lecture:
mixtures and PCA (Part C) come before graphical models (Part D) because mixtures are the
simplest latent-variable models and HMMs are "mixtures threaded over time". Students taking
02-620 can follow the lecture order instead — see below.

---

## Three ways to use the course

### Following 02-620 week by week

If you are taking 02-620 now, work through Part A in the two weeks before the semester (or
alongside weeks 1–2), then study each module in the week of its lecture:

| 02-620 week | Lecture (slide 59 of `001_intro`) | Modules |
|---|---|---|
| before / 1 | Introduction; supervised vs unsupervised; MLE, MAP | 00–05 |
| 2 | Linear regression, regularisation | 06, 07 |
| 3 | k-NN, naïve Bayes, logistic regression | 08, 09 |
| 4 | Generative vs discriminative; decision trees, random forests | 09 §8, 10 |
| 5 | Hierarchical clustering, k-means | 12 |
| 6 | SVM | 11 |
| 7 | Probabilistic graphical models · Midterm I | 15, 16, 17 |
| 8 | Spring break | catch up; redo the ✅ checkpoints of 06–17 |
| 9 | Dynamic Bayesian networks, Gaussian graphical models | 18, 20 §6 |
| 10 | Mixture models, EM; PCA | 13, 14 |
| 11–12 | Hidden Markov models: forward–backward, Viterbi, Baum–Welch | 19, 20 |
| 13 | Bayesian estimation, MCMC; neural networks | 21, 22 |
| 14 | Model selection · Midterm II | 23 |
| 15 | Project presentations | 24 |

### A two-semester bridge for first-year students (≈ 4–5 h per week)

| Weeks | Semester 1 | Milestone |
|---|---|---|
| 1–2 | 00, 01 | run notebooks; write small Python functions on DNA and genotype matrices |
| 3–4 | 02 | Bayes' rule for a genetic test; conditional independence by simulation |
| 5–6 | 03, 04 | solve a linear system; run gradient descent; explain why XᵀX can be singular |
| 7–8 | 05, 06 | derive least squares from a Gaussian likelihood; run a toy GWAS |
| 9–10 | 07, 08 | ridge as MAP, lasso by coordinate descent; naïve Bayes by counting |
| 11–12 | 09, 10 | logistic-regression gradient; ID3 on PlayTennis; a random forest |
| 13–14 | 11 | SVM margin, dual and kernels |
| 15 | review | redo all ✅ checkpoints of Parts A–B |

| Weeks | Semester 2 | Milestone |
|---|---|---|
| 1–2 | 12, 13 | k-means, dendrograms, EM for a Gaussian mixture |
| 3 | 14 | PCA from an eigendecomposition; the simulated "map" of genetic variation |
| 4–6 | 15, 16, 17 | factorise, read d-separation, infer and learn a Bayesian network |
| 7 | 18 | precision matrix and graphical lasso on single-cell signalling data |
| 8–9 | 19, 20 | forward, backward, Viterbi, Baum–Welch |
| 10 | 21 | conjugate posteriors and a Gibbs sampler |
| 11 | 22 | back-propagation by hand; a CNN that finds a DNA motif |
| 12 | 23 | bias–variance, nested cross-validation |
| 13–15 | 24 | capstone project, report and peer review |

### A summer bridge before 02-620 (≈ 10 weeks × 7 h)

Modules 00–14 over the summer (Parts A–C), then Parts D–E during the semester alongside the
lectures. This front-loads the material most students find hardest to pick up quickly (the
mathematics of Part A and the derivations of Part B).

---

## How every notebook works

All notebooks follow the repository's [tutorial specification](../../../guide/Tutorial_Creation.md)
and share one structure, so you always know where to look:

| Part of the notebook | What it gives you |
|---|---|
| Title, Colab badge, key-information table | hardware, frameworks, prerequisites, time, the 02-620 slides covered |
| ⚠️ Important notes, 🎯 objectives, 🗺️ contents | what is real data and what is simulated; what you will be able to do |
| 🧫 The biological question | why a biologist should care |
| Setup cells | hardware check, dependency check, seeds, and the 🧰 **course toolkit** |
| Numbered sections | 📍 where we are, 🧮 math refreshers, theory with equations **and** their "*In words:*" reading, runnable experiments |
| 🔍 What just happened? / ✏️ Your turn | interpretation of each result, then a change for you to make |
| 📑 Slide connection | the exact 02-620 slides covered, what they show, what the notebook adds, an exam tip |
| ⚠️ boxes | pitfalls, common misconceptions, and places where a slide is ambiguous or contains a typo |
| 📌 Key takeaways · ✅ Checkpoint · 🧠 Questions · 🚀 Bonus · 📝 Lab note | summary, self-test with hidden answers, discussion, extensions, a lab-notebook template |
| 📚 References · ➡️ Next | full citations; the next module |

**Honesty policy.** Toys illustrate mechanisms and are labelled SIMULATED. Real data are used
wherever they exist and are small enough for a free CPU. When a slide's displayed result does
not follow from its own numbers (for example, the Viterbi path on `012_HMM-DBN` slide 90),
the notebook shows the computation and says so.

---

## Shared conventions (used by all 25 notebooks)

| Convention | Value |
|---|---|
| Data matrix | `X` has **N rows = samples** (individuals, patients, cells) and **J columns = features** (SNPs, genes, proteins), as in `002_regression`; when a deck uses *n*, *K* or *p* for the number of features the notebook says so |
| Genotypes | 0/1/2 = copies of one allele (the slides' AA = 0, AT = 1, TT = 2) |
| Labels | `y ∈ {0, 1}` (SVM: −1/+1) |
| Regression weights | `w` with intercept `w0`, as on the slides |
| Logarithms | `log` is natural; entropies use `log2` (bits) |
| Randomness | `SEED = 0`, `rng = np.random.default_rng(SEED)` in every notebook; results are reproducible on the same library versions |
| Slide numbers | PowerPoint (pptx) numbering — see the note in [`SLIDE_MAP.md`](SLIDE_MAP.md) |

[`course_toolkit.py`](course_toolkit.py) holds the reference implementation of the shared
helpers (data loaders with offline fallbacks, genotype and trait simulators, the slides' small
tables — the naïve-Bayes genotype table, the alarm network, the two-dice HMM — metrics and
plotting). **Each notebook contains a verbatim copy of the helpers it needs**, so every notebook
runs on its own in Colab.

## Data

| Data set | Source | Modules |
|---|---|---|
| Leukaemia gene expression, 72 patients × 3,571 genes (ALL vs AML) | Golub *et al.* 1999, preprocessed as Dudoit *et al.* 2002 | 00–05, 08, 09, 11–14, 22–24 |
| Single-cell phospho-protein signalling, 11 proteins, consensus network | Sachs *et al.* 2005 | 15–18, 23, 24 |
| Prostate cancer, 97 men × 8 clinical predictors | Stamey *et al.* 1989 (as in ESL and `002_regression`) | 03, 04, 06, 07, 21, 23 |
| PlayTennis; the naïve-Bayes genotype table; alarm-network CPTs; two-dice HMM | the 02-620 slides / Mitchell 1997 | 05, 08, 10, 15–17, 19, 20 |
| Wisconsin breast cancer, iris, handwritten digits | scikit-learn built-ins | 09, 10, 11, 14, 22–24 |
| Genotypes with population structure, polygenic traits, sequences | simulated (clearly labelled) | throughout |

The real files live in [`datasets/`](datasets/README.md) (provenance, preprocessing and pinned
sources are documented there). Inside a clone they are read from disk; on Colab they are
downloaded from this repository and cached in `course_data/` (set `BIO2ML_CACHE` to change it).
Offline, every loader falls back to a simulated stand-in and says so.

---

## Running the notebooks

**Colab (recommended):** click the badge at the top of any notebook. No GPU is needed; every
notebook runs in well under a minute on a CPU.

**Locally:**

```bash
cd ml/tutorial/BiologyToML
python -m pip install -r requirements.txt
jupyter lab notebooks/
```

**Check the whole course** (schema, structure, toolkit copies, links; add `--execute` to run every notebook):

```bash
python validate_notebooks.py            # fast structural check
python validate_notebooks.py --execute  # also executes all 25 notebooks (≈ 5 min on a laptop CPU)
```

The notebooks are stored **without outputs**.

---

## Companion documents

| Document | Use it to… |
|---|---|
| [`SLIDE_MAP.md`](SLIDE_MAP.md) | find, for every 02-620 deck and slide range, the module and section that teaches it |
| [`STUDY_GUIDE.md`](STUDY_GUIDE.md) | study on your own: the study loop, the derivations to master, notation across decks, exam preparation |
| [`GLOSSARY.md`](GLOSSARY.md) | look up a term (biology, mathematics, statistics, machine learning) and the module that introduces it |
| [`INSTRUCTOR_GUIDE.md`](INSTRUCTOR_GUIDE.md) | use the course in teaching: pacing, assessments, common difficulties, a rubric, and a list of slide errata found while writing the course |
| [`datasets/README.md`](datasets/README.md) | provenance and preprocessing of the real data |
| [`course_toolkit.py`](course_toolkit.py) | the shared helper library |

## Going deeper in this repository

The topic tutorials in [`ml/tutorial`](../README.md) are natural next steps after the matching
modules: [`FundamentalsLearningUncertainty`](../FundamentalsLearningUncertainty/) (after 05),
[`RegularizedLinearRegression`](../RegularizedLinearRegression/) — ridge and lasso on real wheat
genomic data (after 07), [`GenerativeDiscriminativeClassification`](../GenerativeDiscriminativeClassification/)
(after 09), [`DecisionTreesRandomForests`](../DecisionTreesRandomForests/) — random forests on real
TCGA driver mutations (after 10), and [`ConformalPrediction`](../ConformalPrediction/) —
distribution-free uncertainty for biomedical models (after 23). For imaging, see
[`sci_img`](../../../sci_img/tutorial/README.md); for structural biology, the sister course
[Cryo-ET and cryo-EM from biology to research](../../../cryoem/tutorial/BiologyToResearch/README.md).

## Credits

Written for the Xu Lab (Computational Biology Department, Carnegie Mellon University) as a
companion to 02-620 *Machine Learning for Scientists* (course design by Prof. Seyoung Kim;
Spring 2025 instructors Min Xu and Martin Zhang). Data: Golub *et al.* (1999) via the
datamicroarray package; Sachs *et al.* (2005) via the sparsebn package; Stamey *et al.* (1989)
via *The Elements of Statistical Learning*. For research and education only, not for clinical use.
