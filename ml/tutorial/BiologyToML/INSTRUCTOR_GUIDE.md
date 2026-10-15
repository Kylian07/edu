# 🧑‍🏫 Instructor guide

For faculty, TAs and mentors who use **BiologyToML** alongside CMU 02-620 *Machine Learning
for Scientists*, as a bridge course for students entering computational biology, or as
structured self-study for undergraduate researchers. Students should start from the
[README](README.md); this guide covers formats, learning outcomes, per-module teaching notes,
assessment, a list of slide errata found while writing the course, and maintenance.

---

## 1 · Formats that work

| Format | Plan | Notes |
|---|---|---|
| Companion to 02-620 (recommended) | Part A before or in weeks 1–2, then the lecture-aligned schedule in the [README](README.md#following-02-620-week-by-week) | recitations can run the module's key section live; ✏️ exercises make good warm-up problems; 📑 boxes point students from slides to explanations |
| Bridge for incoming students | Modules 00–14 over a summer (≈ 7 h/week for 10 weeks), Parts D–E during the semester | front-loads the mathematics most students struggle with in weeks 2–6 |
| First-year two-semester sequence | the 30-week plan in the [README](README.md#a-two-semester-bridge-for-first-year-students--45-h-per-week) | one 75–90 min session per module: 15 min concept, 50 min guided notebook, 15 min checkpoint discussion |
| Lab onboarding | Part A, the part matching the student's project, then 23–24 | pair with the topic tutorials in [`ml/tutorial`](../README.md) |

**Before week 1.** Ask students to open Module 00 in Colab and run it top to bottom (≈ 1
minute). This catches account, browser and network problems early. If a download fails, the
notebooks print "using a simulated stand-in instead" and keep running on simulated data — the
numbers in the text then no longer match, which is worth telling students up front.

---

## 2 · Learning outcomes by part

| Part | Students can… | Evidence |
|---|---|---|
| A · Foundations (00–05) | write NumPy code on genotype and expression matrices; compute joint/conditional probabilities and apply Bayes' rule; multiply, invert and eigendecompose matrices; differentiate and run gradient descent; derive MLE and MAP estimates | lab notes; checkpoints; a hand derivation of the MLE of an allele frequency and of a Beta-prior MAP |
| B · Supervised learning (06–11) | derive least squares, ridge, lasso, naïve Bayes, logistic regression, information gain and the SVM margin/dual; implement each; evaluate with precision/recall and a held-out set | derivations on paper; a toy GWAS; an ALL/AML classifier with an honest test error |
| C · Unsupervised learning (12–14) | run and interpret k-means, hierarchical clustering, EM for mixtures and PCA; choose K; recognise degenerate EM solutions; read a PCA plot critically | class discovery on the Golub data with an ARI; a PCA "map" with a written caveat |
| D · Graphical models (15–20) | factorise and count parameters; decide d-separation; run enumeration, variable elimination and sampling; learn CPTs, Chow–Liu trees and BIC-scored DAGs; read zeros of a precision matrix; run forward–backward, Viterbi and Baum–Welch | the 14 d-separation examples; P(B∣J,¬M) by hand; a learned Sachs network with precision/recall against the consensus |
| E · Bayesian, neural, model selection (21–24) | derive conjugate posteriors; write a Gibbs sampler and diagnose it; back-propagate by hand; derive the bias–variance decomposition; run nested CV without leakage | the capstone report and peer review |

---

## 3 · Per-module teaching notes

Each line gives the one idea to land, the most common difficulty, and a discussion prompt.

| Module | Idea to land | Typical difficulty | Discussion prompt |
|---|---|---|---|
| 00 | X, Y, f; supervised = P(Y∣X), unsupervised = P(X) | treating "AI" as one technique | For Golub 1999, what were X, Y and f — and what was *class discovery*? |
| 01 | arrays with `axis=`; vectorisation | off-by-one indexing; int8 overflow | Why does a seed make a simulation reproducible but not "true"? |
| 02 | conditional probability and conditional independence | confusing P(A∣B) with P(B∣A) | A carrier test is 99 % sensitive — why can most positives still be false? |
| 03 | Xw as a weighted sum; rank and invertibility | when N < J, why "infinitely many perfect fits" | Two SNPs in perfect LD: what can and can't the data tell us? |
| 04 | gradient = direction of steepest ascent; convexity | step-size intuition; matrix-calculus rules | Why is a concave log-likelihood good news? |
| 05 | likelihood as a function of θ; MAP = imaginary counts | "probability of the data" vs "probability of θ" | When should a prior dominate the data? |
| 06 | MLE under Gaussian noise = least squares | the matrix derivation of the normal equations | Univariate GWAS hits vs joint regression: why do they disagree under LD? |
| 07 | ridge = Gaussian prior; lasso = sparsity via soft-thresholding | why L1 gives exact zeros | Is a lasso-selected SNP causal? What would you need to claim that? |
| 08 | conditional independence turns 3ⁿ into 2n parameters | zero counts; NB probabilities are often over-confident | Why can NB classify well while its probabilities are wrong? |
| 09 | linear log-odds; gradient ascent on a concave likelihood | the two sign conventions on the slides | Generative or discriminative for 30 patients? For 30,000? |
| 10 | information gain; trees have high variance; forests average it away | conditional entropy bookkeeping | Why does a single noisy day (D15) reshape the tree? |
| 11 | margin = 2/‖w‖; support vectors; kernels as dot products | the dual and the meaning of αᵢ | "SVMs have no model selection" — what must still be chosen? |
| 12 | k-means as alternating minimisation; linkage choices | correlation vs Euclidean distance | Did clustering *discover* ALL vs AML, or were the genes chosen to find it? |
| 13 | EM = alternate soft assignment and weighted MLE | why the likelihood can go to infinity | When are soft assignments worth the extra assumptions? |
| 14 | PCs are eigenvectors of the covariance; centring | `eigh` returns ascending order; reading loadings | What can a PCA "map of Europe" not tell you about ancestry? |
| 15 | joint = ∏ P(Xᵢ∣Pa); parameter counting | the chain rule as a complete DAG | What does an arrow in a gene network claim, and what not? |
| 16 | three triples; colliders open when observed | descendants of colliders | Collider bias in case-only studies: give a biological example. |
| 17 | variable elimination reuses work; Chow–Liu; BIC search | factor bookkeeping; Markov equivalence | Why did Sachs *et al.* need perturbation experiments? |
| 18 | Θᵢⱼ = 0 ⟺ conditional independence; graphical lasso | covariance vs precision | A partial correlation between p38 and JNK: regulation, or a shared upstream kinase? |
| 19 | forward recursion = law of total probability + Markov property | underflow; Viterbi vs posterior decoding | Why is the slide-90 path not the most probable one? |
| 20 | Baum–Welch = EM with expected counts | label switching; local optima | How would you choose the number of hidden states for a genome? |
| 21 | posterior ∝ likelihood × prior; Gibbs samples conditionals | burn-in and autocorrelation | When is a full posterior worth more than a MAP estimate? |
| 22 | a neuron = logistic regression; back-propagation = chain rule | gradient shapes; overfitting with few samples | What did the CNN's filter learn, and how would you check it is biology? |
| 23 | bias–variance; CV for selection, a test set for reporting | selection bias (choosing genes before CV) | Why is "100 % CV accuracy" on Golub with pre-selected genes not a result? |
| 24 | one question, an evaluation contract, three methods, honest uncertainty | comparing methods within noise | Which of the three methods would you deploy, and what would you tell a clinician? |

---

## 4 · Assessment

- **Checkpoints** (✅, with hidden answers) work as entry/exit tickets; 6–8 per module.
- **Lab notes** (📝 template at the end of each notebook): ask for one per module; grade for
  correct inputs/outputs/method and a sensible failure mode.
- **Derivation quizzes**: the table in [`STUDY_GUIDE.md` §3](STUDY_GUIDE.md#3-the-derivations-to-master)
  lists the derivations every student should reproduce on a blank page.
- **Hand calculations** that mirror exam questions: forward variables (19), information gains
  (10), naïve-Bayes counts (08), alarm-network queries (17), a k-means step and single-link
  merges (12), the SVM margin (11).
- **Capstone** (Module 24): report + presentation + peer review. Suggested rubric (the notebook
  contains a student-facing version):

| Criterion | Excellent (4) | Adequate (2–3) | Insufficient (0–1) |
|---|---|---|---|
| Question and evaluation contract | biological question, unit of replication, split, metric and baseline stated before analysis | most elements present | metric or split chosen after seeing results |
| Methods | three methods, each justified, tuned within training folds with a fixed budget | three methods, tuning partly ad hoc | test data used for tuning or selection |
| Results and uncertainty | fold spread, paired comparison or bootstrap CI, calibration where relevant | point estimates with some spread | single numbers only |
| Interpretation | stability of selected features, limits of biological claims | some interpretation | causal claims from predictive models |
| Reproducibility and communication | seeded, runs end to end, clear figures and report | minor gaps | cannot be rerun |

---

## 5 · Slide errata and clarifications found while writing the course

The notebooks follow the Spring 2025 decks closely; while reproducing every worked example
the authors found the following slips. Each is flagged where it occurs in the notebook (⚠️ box
or 📑 slide connection). They may be worth fixing in the next revision of the slides.
Slide numbers are PowerPoint numbers.

| Deck | Slide(s) | Issue | Correct statement / how the notebook handles it |
|---|---|---|---|
| `001_intro` | 18 | "ATT gene" for Huntington disease | almost certainly HTT ([00](notebooks/00_welcome_ml_for_biology.ipynb)) |
| `001_intro` | 67 | "∼" used for "proportional to" | written ∝ ([05](notebooks/05_likelihood_mle_map.ipynb)) |
| `002_regression` | 4 vs 5 | slide 4 titled "Lung Cancer GWAS", notes and slide 5 discuss breast cancer | noted ([06](notebooks/06_linear_regression_gwas.ipynb)) |
| `002_regression` | 9 | "genotype at SNP i individual j" contradicts the matrix layout (rows = individuals) | rows = individuals, columns = SNPs |
| `002_regression` | 32 | minus sign inside the square, [−(yⁱ − xⁱᵀw)]², under an argmax | −(yⁱ − xⁱᵀw)² |
| `002_regression` | 35 vs 40/46 | "MLCE" and "MCLE" for the same estimator | maximum conditional likelihood estimate |
| `002_regression` | 45 (notes) | y = Xᵀw + ε | y = Xw + ε |
| `002_regression` | 50–51 | prior density written with σ² instead of σ₀² and (2π)^{1/2} instead of (2π)^{J/2} | final MAP objective on slide 50 is still correct ([07](notebooks/07_ridge_lasso_sparse_regression.ipynb)) |
| `002_regression` | 58 | index typos in the last column of the centred matrix | noted |
| `003_classification-kNN-NB` | 14 vs `002` 9 | AA called "minor-allele homozygous" while coded 0 (i.e. the code counts the major allele) | either coding works; 2 − G carries the same information ([01](notebooks/01_python_numpy_for_biologists.ipynb)) |
| `003_classification-kNN-NB` | 39, 50 | swapped i/j indices, Y = 1 hard-coded; two-outcome (Beta) denominator used for 3-valued genotypes | (count + a)/(N_y + 3a) for three categories ([08](notebooks/08_knn_naive_bayes.ipynb)) |
| `003_classification-kNN-NB` | 49 | stray "=" in argmax_θ = P(D∣θ)P(θ)/P(D) | noted ([05](notebooks/05_likelihood_mle_map.ipynb)) |
| `003_classification-kNN-NB` | 54 | "n features → 4n parameters" omits the class prior | 2nk + (k − 1) for k classes ([08](notebooks/08_knn_naive_bayes.ipynb)) |
| `004_classification-LR` | 8–19, 32 vs 23–31 | two sign conventions for the logistic model (1/(1+exp(w₀+Σwᵢxᵢ)) vs exp(·)/(1+exp(·))) | differ by the sign of every weight; one convention used and explained ([09](notebooks/09_logistic_regression.ipynb)) |
| `004_classification-LR` | 28–29 | step size called η, then λ | notation alert ([04](notebooks/04_calculus_and_optimization.ipynb)) |
| `004_classification-LR` | 31 | with λ = 1/(2σ²) the shrinkage term of the update should be 2ηλwᵢ | derived; scikit-learn's C = 1/(2λ) ([09](notebooks/09_logistic_regression.ipynb)) |
| `005_decision-tree` | 20–21 | information gains computed from rounded intermediate entropies (0.246, 0.151) | exact: 0.247, 0.152, 0.048, 0.029 ([10](notebooks/10_decision_trees_random_forests.ipynb)) |
| `005_decision-tree` | 35 | pruning evaluated on the "test set" | must be a separate validation set; a test set is kept untouched |
| `005_decision-tree` | 62, 64 | "CHSM" | CHASM |
| `006_clustering` | 17 | correlation formula lacks the 1/p factor (or unnormalised σ) | fixed in the text ([12](notebooks/12_clustering_kmeans_hierarchical.ipynb)) |
| `007_SVM` | 46 (notes) | the min/max swap written as "max_x max_α" | weak and strong duality stated and checked ([04](notebooks/04_calculus_and_optimization.ipynb)) |
| `007_SVM` | 48, 51 | Lagrangian box says αᵢ ≤ 0 | αᵢ ≥ 0 ([11](notebooks/11_support_vector_machines.ipynb)) |
| `007_SVM` | 52, extra slide | C > αᵢ ≥ 0 | C ≥ αᵢ ≥ 0 (margin violators have αᵢ = C) |
| `007_SVM` | 56 | support vectors described only as points on the wrong side of the margin | points exactly on the margin (0 < αᵢ < C) are support vectors too |
| `007_SVM` | 1 | reading "Murphy Ch 4.5" | the SVM material is Murphy §14.5 |
| `008_BN_mz_021825` | 81 | Example 8's second path copied from Example 3 | W—Y—X; verdict unchanged ([16](notebooks/16_bayesian_networks_independence.ipynb)) |
| `008_BN_mz_021825` | 61–93 | evidence set written {Z}, clashing with node Z | renamed "evidence" |
| `008_BN_mz_021825` | 107 | P(B, J, ¬M) = 0.00601 from rounded terms | exact 0.0063175 ([17](notebooks/17_bayesian_networks_inference_learning.ipynb)) |
| `008_BN_mz_021825` | 123–126 | the 19 → 14 operation count holds for a fixed value of B | explained ([17](notebooks/17_bayesian_networks_inference_learning.ipynb)) |
| `009_GGM_mz_030925` | 21–22 | the 8 × 8 edge-weighted Θ is not positive definite | shown; 0.7·I added, same graph ([18](notebooks/18_gaussian_graphical_models.ipynb)) |
| `009_GGM_mz_030925` | 46–51 | S defined with 1/(2N) | 1/N, so that Θ̂ = S⁻¹ |
| `009_GGM_mz_030925` | 52 | (Θ⁻¹)ᵢᵢ = Sᵢᵢ + λ holds only if the diagonal is penalised (and in Friedman et al.'s scaling) | both versions verified in code |
| `009_GGM_mz_030925` | 40 | β₀ paired with μ₁ | true only for centred predictors |
| `010_mixture-model_mz_031725` | 60, 66 | EM "guaranteed to increase / converge"; "local minimum" | the likelihood never decreases; convergence to a stationary point (local *maximum*) if bounded; the unconstrained GMM likelihood is unbounded ([13](notebooks/13_mixture_models_em.ipynb)) |
| `010_mixture-model_mz_031725` | 69 | held-out score written with the complete-data formula | observed-data likelihood (sum over clusters) |
| `010_mixture-model_mz_031725` | 72–77 | Bernoulli data written x ∈ ℝᴶ | binary vectors |
| `011_PCA_mz_031825` | 49 | factor 2 dropped in the derivative | harmless; noted ([14](notebooks/14_pca_dimensionality_reduction.ipynb)) |
| `011_PCA_mz_031825` | 52 | strict "<" | "≤" |
| `011_PCA_mz_031825` | 55 | "361 × 261 pixels, 83,781 dimensions" | 361 × 261 = 94,221 (83,781 = 321 × 261) |
| `012_HMM-DBN_mz_032425` | 14, 20, 34 vs 107 | P(qₜ=sᵢ∣qₜ₋₁=sⱼ) vs aᵢⱼ = P(qₜ=sⱼ∣qₜ₋₁=sᵢ) | slide-107 convention used throughout ([19](notebooks/19_hmm_inference.ipynb)) |
| `012_HMM-DBN_mz_032425` | 69 | "Transition" and "Emission" labels swapped | slide 70 is correct |
| `012_HMM-DBN_mz_032425` | 90 | the displayed path A A A B B B B B B A A is not the Viterbi path of 1 2 2 1 1 2 1 1 1 2 2 | under the slide parameters the most probable path is all A (1.75 × 10⁻⁸ vs 2.25 × 10⁻¹²); verified by brute force ([19](notebooks/19_hmm_inference.ipynb)) |
| `012_HMM-DBN_mz_032425` | 94–95 | "path defined by argmax_j δₜ(j)"; δ defined as a conditional | traceback through backpointers is required; δ is a joint probability |
| `012_HMM-DBN_mz_032425` | 108–109 | "moving window of size 2" for emissions | size 1 ([20](notebooks/20_hmm_learning.ipynb)) |
| `012_HMM-DBN_mz_032425` | 113 | "local minima" | local maxima of the likelihood |
| `012_HMM-DBN_mz_032425` | 124 | duration product index range; Poisson duration can be 0 | product over the segment t−l+1…t; 1 + Poisson(λ − 1) used |
| `013_Bayesian-MCMC_mz_032725` | 24 | p(wⱼ ∣ w₋ⱼ, data) called a "marginal" | a full conditional ([21](notebooks/21_bayesian_learning_mcmc.ipynb)) |
| `014_NN_mz_032725` | 16 | sigmoid with the opposite sign to slide 4 | flagged ([22](notebooks/22_neural_networks.ipynb)) |
| `014_NN_mz_032725` | 46–49 | δ rules assume squared error with sigmoid units (Mitchell), while slide 41 says "loss function" | both squared-error and cross-entropy rules derived |
| `015_model-selection_mz_040725` | 3 | "k-NN: number of clusters K"; "SVM: NA" | number of neighbours; SVMs need C, kernel and its parameters, class weights, preprocessing ([11](notebooks/11_support_vector_machines.ipynb), [23](notebooks/23_model_selection.ipynb)) |
| `015_model-selection_mz_040725` | 42–43 | BIC written as "min over θ" | minimise over models, each at its maximum-likelihood fit |
| `015_model-selection_mz_040725` | 55 | E[εf̂] = E[ε]E[f̂] assumes test noise independent of the training data | made explicit ([23](notebooks/23_model_selection.ipynb)) |
| `015_model-selection_mz_040725` | 61 | y-axis label P(cᵢ∣X) | p(x∣cᵢ)P(cᵢ) |

Two clarifications rather than errors are also handled throughout: more CV folds change the cost
and the bias/variance of the *estimate* (independence of samples matters more), and a learned
network edge or a lasso-selected feature is a statistical dependence, not a demonstrated mechanism.

---

## 6 · Technical notes and maintenance

- **Tested with** Python 3.13, NumPy 2.5, SciPy 1.18, pandas 3.0, scikit-learn 1.9, Matplotlib 3.11
  and PyTorch 2.14 (CPU); code avoids arguments that changed across scikit-learn 1.3–1.9 (version
  guards where needed). Every notebook runs in under a minute on a laptop CPU; the whole course in
  about 5 minutes.
- **Structure check:** `python validate_notebooks.py` (schema, required sections, Colab badges,
  stripped outputs, relative links, and that every toolkit copy matches `course_toolkit.py`);
  `--execute` also runs all notebooks.
- **Editing a notebook:** edit in Jupyter, run it top to bottom, check that the narrative still
  matches the outputs, then clear outputs before committing
  (`jupyter nbconvert --clear-output --inplace notebooks/NN_*.ipynb`).
- **Changing a shared helper:** edit `course_toolkit.py`, then paste the new definition into the
  🧰 toolkit cell of every notebook that uses it — the validator lists each stale copy.
- **Data:** `datasets/make_datasets.py` rebuilds the real data from pinned upstream commits
  (see [`datasets/README.md`](datasets/README.md)). The loaders read `../datasets/` inside a clone,
  otherwise download from `raw.githubusercontent.com/xulabs/edu/main/…`; offline they fall back to
  simulated stand-ins.
- **Slide numbering:** notebooks cite PowerPoint slide numbers; several PDF exports drop hidden
  slides (see the note in [`SLIDE_MAP.md`](SLIDE_MAP.md)).
