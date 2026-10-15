# Slide map: every 02-620 lecture deck → the BiologyToML modules that teach it

Use this map in both directions: while studying a 02-620 deck, find the notebook section that
explains each group of slides in depth; while working through a notebook, find the slides it
expands. The decks are the Spring 2025 slides of CMU 02-620 *Machine Learning for Scientists*
(course design by Prof. Seyoung Kim; instructors Min Xu and Martin Zhang), latest revision of
each lecture.

> **Slide numbers** are the numbers PowerPoint shows for the `.pptx` files. Several PDF exports
> silently drop hidden slides, so a PDF page number can lag behind: `008_BN` (slides 25 and 173
> hidden; PDF page *p* shows slide *p* + 1 for slides 26–172), `009_GGM` (slide 24),
> `010_mixture-model` (4 slides), `011_PCA` (2 slides; lag of 2 from about slide 40),
> `012_HMM-DBN` (3 slides), `013_Bayesian-MCMC` (several), `015_model-selection` (slides 11 and 20).

Every notebook contains **📑 Slide connection** boxes that quote the exact slide range, say what
the slides show and what the notebook adds, and give an exam tip.

---

## `001_intro` — Introduction: machine learning in science (69 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 1–11 | Logistics, prerequisites (02-601, 02-680), grading, project, academic integrity | [00 §1](notebooks/00_welcome_ml_for_biology.ipynb); prerequisites built in [01](notebooks/01_python_numpy_for_biologists.ipynb)–[04](notebooks/04_calculus_and_optimization.ipynb); project → [24 §1](notebooks/24_capstone_project.ipynb) |
| 12–17 | Machine learning between statistics and computer science; applications | [00 §2](notebooks/00_welcome_ml_for_biology.ipynb) |
| 18–37 | Biology becomes a data science: genome draft (2001) and gene finding; SNPs, HapMap, 1000 Genomes, UK Biobank; ancestry and PCA; microarrays, Golub ALL/AML, gene networks, RNA-seq | [00 §2–3](notebooks/00_welcome_ml_for_biology.ipynb) |
| 38–48 | Supervised learning: f: X → Y, regression vs classification, P(Y∣X) for uncertainty | [00 §4](notebooks/00_welcome_ml_for_biology.ipynb), [05 §1](notebooks/05_likelihood_mle_map.ipynb) |
| 49–51, 56–57 | "What is X, Y, f?" for gene finding, GWAS, Golub, networks, population structure | [00 §6](notebooks/00_welcome_ml_for_biology.ipynb) |
| 52–55, 58, 60 | Unsupervised learning: P(X), patterns, density estimation | [00 §5](notebooks/00_welcome_ml_for_biology.ipynb), [05 §1](notebooks/05_likelihood_mle_map.ipynb) |
| 59, 68 | Course schedule | [00 §7](notebooks/00_welcome_ml_for_biology.ipynb), [README](README.md#following-02-620-week-by-week) |
| 62–63 | Learning a joint distribution, then conditioning | [05 §8](notebooks/05_likelihood_mle_map.ipynb) |
| 64–67 | MLE vs MAP; Bayes' rule in machine learning | [02 §3](notebooks/02_probability_for_biologists.ipynb), [05 §2–7](notebooks/05_likelihood_mle_map.ipynb) |

**Summary slide (69) — what you should know:** supervised vs unsupervised learning (00, 05);
supervised learning as P(Y∣X), unsupervised as P(X) (05 §1); MLE vs MAP (05 §2–7).

## Prerequisites assumed by every deck (02-601 and 02-680)

| What the slides assume | Taught in |
|---|---|
| Python, NumPy, Jupyter, plotting | [01](notebooks/01_python_numpy_for_biologists.ipynb) |
| Random variables, joint/conditional probability, Bayes' rule, independence, Gaussian | [02](notebooks/02_probability_for_biologists.ipynb) |
| Vectors, matrices, inverse, rank, eigendecomposition | [03](notebooks/03_linear_algebra_for_data.ipynb) |
| Derivatives, gradients, convexity, gradient ascent, matrix calculus, Lagrange multipliers | [04](notebooks/04_calculus_and_optimization.ipynb) |

---

## `002_regression` — Regression (70 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 1–8 | Family studies vs GWAS, Manhattan plots, types of phenotypes | [06 §1](notebooks/06_linear_regression_gwas.ipynb) |
| 9–17 | Data matrices; univariate model y = w₀ + wx + ε; terminology; the two-step recipe | [06 §2–3](notebooks/06_linear_regression_gwas.ipynb); data matrices in [03 §3](notebooks/03_linear_algebra_for_data.ipynb) |
| 18–24 | MLE of the univariate model = least squares | [06 §4](notebooks/06_linear_regression_gwas.ipynb) |
| — | (added) genome scan, p-values, Bonferroni, population stratification | [06 §5](notebooks/06_linear_regression_gwas.ipynb) |
| 25–31 | Multivariate regression; augmented intercept column | [06 §6](notebooks/06_linear_regression_gwas.ipynb), [03 §3](notebooks/03_linear_algebra_for_data.ipynb) |
| 32–40 | Matrix derivation of the normal equations, w = (XᵀX)⁻¹Xᵀy | [06 §6](notebooks/06_linear_regression_gwas.ipynb), [04 §6](notebooks/04_calculus_and_optimization.ipynb), [03 §4](notebooks/03_linear_algebra_for_data.ipynb) |
| 41–43 | Prostate cancer example (ESL) | [06 §7](notebooks/06_linear_regression_gwas.ipynb) |
| 44–46 | Limits of MLE: XᵀX singular when N < J | [06 §8](notebooks/06_linear_regression_gwas.ipynb), [03 §5](notebooks/03_linear_algebra_for_data.ipynb) |
| 47–54 | MAP with a Gaussian prior | [07 §1–2](notebooks/07_ridge_lasso_sparse_regression.ipynb), [05 §6](notebooks/05_likelihood_mle_map.ipynb) |
| 55–57 | Ridge regression as regularisation, λ = σ²/σ₀² | [07 §3](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| 58–59 | Ridge in practice: centring, unpenalised intercept | [07 §4](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| — | (added) choosing λ on a validation set | [07 §5](notebooks/07_ridge_lasso_sparse_regression.ipynb), [23 §7](notebooks/23_model_selection.ipynb) |
| 60–68 | Sparsity, L₀, the lasso | [07 §6](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| 69 | Pathwise coordinate descent (glmnet) | [07 §7](notebooks/07_ridge_lasso_sparse_regression.ipynb), [04 §8](notebooks/04_calculus_and_optimization.ipynb) |
| 70 | Summary | [07 §8–10](notebooks/07_ridge_lasso_sparse_regression.ipynb) |

**Summary slide (70):** MLE = least squares (06 §4, §6); MAP = ridge when N < J (07 §2–4);
lasso for sparse estimates (07 §6–9).

## `003_classification-kNN-NB` — k-nearest neighbours and naïve Bayes (55 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–4 | Classification tasks; training vs testing; three classifier types | [08 §1](notebooks/08_knn_naive_bayes.ipynb) |
| 5–12 | k-NN, decision boundaries, choosing K, computation time | [08 §2](notebooks/08_knn_naive_bayes.ipynb) |
| 13–20 | Genotype → cancer table; 3ⁿ parameters; Bayes' rule alone is not enough | [08 §3](notebooks/08_knn_naive_bayes.ipynb), [02 §8](notebooks/02_probability_for_biologists.ipynb) |
| 21–23, 28 | Conditional independence: (3ⁿ−1)×2 → 2·n·2 (+1) parameters | [08 §4](notebooks/08_knn_naive_bayes.ipynb), [02 §4](notebooks/02_probability_for_biologists.ipynb) |
| 24–27, 30–32 | The full model (Bernoulli, multinoulli), classifying a new sample | [08 §5](notebooks/08_knn_naive_bayes.ipynb) |
| 34–46 | MLE = counting; the coin-flip example; training on the 6-individual table | [08 §6](notebooks/08_knn_naive_bayes.ipynb), [05 §2](notebooks/05_likelihood_mle_map.ipynb) |
| 47 | Two binary features → class exercise | [08 §7](notebooks/08_knn_naive_bayes.ipynb) |
| 48–50 | Zero counts and MAP pseudo-counts (Beta/Dirichlet priors) | [08 §8](notebooks/08_knn_naive_bayes.ipynb), [05 §4](notebooks/05_likelihood_mle_map.ipynb) |
| 51 | Violated conditional independence | [08 §9](notebooks/08_knn_naive_bayes.ipynb), [09 §8](notebooks/09_logistic_regression.ipynb) |
| 52–54 | Continuous features: Gaussian naïve Bayes; parameter counts | [08 §10](notebooks/08_knn_naive_bayes.ipynb) |
| 55 | Summary (NB vs LR) | [08](notebooks/08_knn_naive_bayes.ipynb) key takeaways, [09 §8](notebooks/09_logistic_regression.ipynb) |

## `004_classification-LR` — Logistic regression (37 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–5 | Classifier types; why not linear regression for 0/1 labels | [09 §1](notebooks/09_logistic_regression.ipynb) |
| 7–17, 19–20 | Probability model, logistic function, linear decision surface | [09 §2–3](notebooks/09_logistic_regression.ipynb) |
| 18 | More than two classes | [09 §4](notebooks/09_logistic_regression.ipynb) |
| 22–30 | Conditional log-likelihood, gradient, concavity, gradient ascent | [09 §5](notebooks/09_logistic_regression.ipynb), [04 §4–5](notebooks/04_calculus_and_optimization.ipynb) |
| 31–32 | MAP / L2 regularisation; separable data | [09 §6](notebooks/09_logistic_regression.ipynb) |
| 33–35 | Generative vs discriminative classifiers | [09 §8](notebooks/09_logistic_regression.ipynb) |
| 36 | Precision and recall | [09 §7](notebooks/09_logistic_regression.ipynb) |
| 37 | Summary | [09](notebooks/09_logistic_regression.ipynb) key takeaways |

## `005_decision-tree` — Decision trees and random forests (67 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 1–9 | Trees for f: X → Y; PlayTennis; why trees | [10 §1](notebooks/10_decision_trees_random_forests.ipynb) |
| 10–25 | Greedy learning; entropy; conditional entropy; information gain = mutual information | [10 §2–4](notebooks/10_decision_trees_random_forests.ipynb) |
| 26–33 | Noisy sample D15; overfitting | [10 §5](notebooks/10_decision_trees_random_forests.ipynb) |
| 34–36 | Early stopping vs reduced-error pruning | [10 §6](notebooks/10_decision_trees_random_forests.ipynb) |
| 37–49 | Continuous inputs, axis-parallel rectangles (iris), IF-THEN rules | [10 §4, §7](notebooks/10_decision_trees_random_forests.ipynb) |
| 50–54 | Pros and cons; high variance vs logistic regression | [10 §8](notebooks/10_decision_trees_random_forests.ipynb) |
| 55–58, 64 | Random forests | [10 §9](notebooks/10_decision_trees_random_forests.ipynb) |
| 59–66 | CHASM: driver vs passenger mutations | [10 §10](notebooks/10_decision_trees_random_forests.ipynb) |
| 67 | Summary | [10](notebooks/10_decision_trees_random_forests.ipynb) key takeaways |

## `006_clustering` — k-means and hierarchical clustering (57 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–14 | Unsupervised data; clustering genes vs samples; what clustering is | [12 §1](notebooks/12_clustering_kmeans_hierarchical.ipynb) |
| 15–18 | Similarity; Euclidean and correlation distance | [12 §2](notebooks/12_clustering_kmeans_hierarchical.ipynb), [03 §2](notebooks/03_linear_algebra_for_data.ipynb) |
| 19–28 | k-means | [12 §3–4](notebooks/12_clustering_kmeans_hierarchical.ipynb) |
| 29–33 | Choosing K: the elbow | [12 §5](notebooks/12_clustering_kmeans_hierarchical.ipynb) |
| 34–52 | Agglomerative clustering; single, complete, average link; dendrograms | [12 §6](notebooks/12_clustering_kmeans_hierarchical.ipynb) |
| 53–55 | Properties; outliers | [12 §7](notebooks/12_clustering_kmeans_hierarchical.ipynb) |
| 56–57 | Lotus example; what you should know | [12 §8](notebooks/12_clustering_kmeans_hierarchical.ipynb) |

## `007_SVM`, `007_SVM_extra_slides` — Support vector machines (74 + 1 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–13 | Cancer-type prediction; linear classifiers so far; the max-margin idea; support vectors | [11 §1–2](notebooks/11_support_vector_machines.ipynb) |
| 15–31 | Margin geometry, M = 2/‖w‖, the hard-margin quadratic program | [11 §3](notebooks/11_support_vector_machines.ipynb) |
| 32–41, 69–73 | Soft margin, slack variables, C; hinge loss | [11 §4](notebooks/11_support_vector_machines.ipynb) |
| 42–56, extra | Lagrangian duality; support vectors; prediction cost | [11 §5](notebooks/11_support_vector_machines.ipynb), [04 §7](notebooks/04_calculus_and_optimization.ipynb) |
| 57–67 | Feature maps and the kernel trick; why SVMs need not overfit | [11 §6](notebooks/11_support_vector_machines.ipynb) |
| 68 | Multiclass: one vs all | [11 §7](notebooks/11_support_vector_machines.ipynb) |
| — | (added) choosing C, kernel and γ on real data | [11 §8](notebooks/11_support_vector_machines.ipynb), [23 §5](notebooks/23_model_selection.ipynb) |
| `007_midterm` | Midterm-1 logistics | — |

## `008_BN_mz_021825` — Probabilistic graphical models / Bayesian networks (174 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 1–8 | Graph + probability; directed vs undirected; examples | [15 §1](notebooks/15_bayesian_networks_representation.ipynb) |
| 9–12 | DAGs; the alarm network; terminology | [15 §2](notebooks/15_bayesian_networks_representation.ipynb) |
| 13–17 | Joint distribution = ∏ P(Xᵢ∣Pa(Xᵢ)); construction recipe | [15 §3](notebooks/15_bayesian_networks_representation.ipynb) |
| 18–29 | Chain rule vs domain knowledge: 31 vs 10 parameters | [15 §4](notebooks/15_bayesian_networks_representation.ipynb), [02 §8](notebooks/02_probability_for_biologists.ipynb) |
| 30–37 | Movie-preference numerical example; summary | [15 §5–6](notebooks/15_bayesian_networks_representation.ipynb) |
| 38–49 | Conditional independence questions; Markov chain | [16 §1–2](notebooks/16_bayesian_networks_independence.ipynb) |
| 50–59 | Markov blankets (alarm network, TF networks) | [16 §3](notebooks/16_bayesian_networks_independence.ipynb) |
| 61–63 | d-separation: active/inactive paths; the algorithm | [16 §4](notebooks/16_bayesian_networks_independence.ipynb) |
| 64–93 | The 14 worked d-separation examples | [16 §5–6](notebooks/16_bayesian_networks_independence.ipynb) |
| 94–96 | Example 15 (TF/target genes); summary | [16 §7](notebooks/16_bayesian_networks_independence.ipynb) |
| 97–115 | Joint, partial and conditional queries; enumeration | [17 §1–2](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| 116–129 | Operation counts; variable elimination; polytrees | [17 §2–3](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| 130–146 | Stochastic inference: ancestral sampling, rejection estimates | [17 §4](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| 147–156 | Learning CPTs (MLE) with a known graph | [17 §5](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| 157–168 | Structure learning; Chow–Liu; Kruskal | [17 §6–8](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| 169–172 | Hill climbing; local maxima, TABU, annealing | [17 §9–10](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| 173–174 | Naïve Bayes revisited; what you should know | [15 §1](notebooks/15_bayesian_networks_representation.ipynb), [17](notebooks/17_bayesian_networks_inference_learning.ipynb) key takeaways |

**What you should know (174):** representation — DAG + CPDs, Markov blanket, d-separation (15, 16);
inference — NP-hard in general, variable elimination, sampling (17 §2–4); learning — easy for a
known graph with full data, Chow–Liu for trees, hardest when the graph is unknown (17 §5–10).

## `009_GGM_mz_030925` — Gaussian graphical models (58 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–12 | Gene networks; Markov random fields; cliques; discrete vs Gaussian | [18 §1–3](notebooks/18_gaussian_graphical_models.ipynb) |
| 14–22 | Multivariate Gaussian; the GGM; adjacency matrices | [18 §4–5](notebooks/18_gaussian_graphical_models.ipynb), [02 §7](notebooks/02_probability_for_biologists.ipynb) |
| 24–31 | Local, pairwise and global Markov properties; precision vs covariance | [18 §5–6](notebooks/18_gaussian_graphical_models.ipynb) |
| 32–42 | Marginals and conditionals; the conditional is a linear regression | [18 §7](notebooks/18_gaussian_graphical_models.ipynb) |
| 44–48 | Maximum-likelihood estimation | [18 §8](notebooks/18_gaussian_graphical_models.ipynb) |
| 49–57 | Sparsity; graphical lasso; QUIC/BIG&QUIC | [18 §9–10](notebooks/18_gaussian_graphical_models.ipynb), [07 §6–7](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| 58 | Summary | [18 §11](notebooks/18_gaussian_graphical_models.ipynb) |

## `010_mixture-model_mz_031725` — Mixture models and EM (80 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–11 | Hard vs soft clustering | [13 §1](notebooks/13_mixture_models_em.ipynb) |
| 12–24 | The Gaussian mixture model; mixture as a Bayesian network; preview of HMMs | [13 §2](notebooks/13_mixture_models_em.ipynb) |
| 25–33 | Inference: responsibilities by Bayes' rule | [13 §3](notebooks/13_mixture_models_em.ipynb) |
| 34–45 | Learning with observed labels | [13 §4](notebooks/13_mixture_models_em.ipynb) |
| 46–67 | Hidden labels: the EM algorithm; k-means revisited; convergence | [13 §5–6](notebooks/13_mixture_models_em.ipynb) |
| 68 | EM in practice: initialisation, restarts | [13 §7](notebooks/13_mixture_models_em.ipynb) |
| 69–70 | Number of clusters; Dirichlet process | [13 §8](notebooks/13_mixture_models_em.ipynb), [23 §8](notebooks/23_model_selection.ipynb) |
| 71–77 | Other mixtures; Bernoulli mixtures | [13 §9–10](notebooks/13_mixture_models_em.ipynb) |
| 78–80 | Comparison table; evaluating clusterings; summary | [13 §11](notebooks/13_mixture_models_em.ipynb) |

## `011_PCA_mz_031825` — Dimensionality reduction / PCA (59 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–6 | High-dimensional data; Novembre et al. 2008 | [14 §1](notebooks/14_pca_dimensionality_reduction.ipynb) |
| 7–13 | The 2-D → 1-D toy | [14 §2](notebooks/14_pca_dimensionality_reduction.ipynb) |
| 15–16 | Mid-semester survey | — |
| 17–31 | Step 1: eigendecomposition; eigenvalues = variance explained | [14 §3](notebooks/14_pca_dimensionality_reduction.ipynb), [03 §6](notebooks/03_linear_algebra_for_data.ipynb) |
| 32–40 | Step 2: projection; centring; coordinates | [14 §4](notebooks/14_pca_dimensionality_reduction.ipynb), [03 §7](notebooks/03_linear_algebra_for_data.ipynb) |
| 41–44 | How many PCs; summary | [14 §5](notebooks/14_pca_dimensionality_reduction.ipynb) |
| 45 | Population structure in Europe | [14 §7](notebooks/14_pca_dimensionality_reduction.ipynb) |
| 47–54 | PCA as an optimisation (Lagrangian) | [14 §6](notebooks/14_pca_dimensionality_reduction.ipynb), [04 §7](notebooks/04_calculus_and_optimization.ipynb) |
| 55–59 | PCA of images; summary | [14 §9–10](notebooks/14_pca_dimensionality_reduction.ipynb) |

## `012_HMM-DBN_mz_032425` — Hidden Markov models and dynamic Bayesian networks (134 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–8 | Latent-variable models; speech; gene finding; haplotype phasing | [19 §1](notebooks/19_hmm_inference.ipynb) |
| 9–20 | HMM definition; HMM as a Bayesian network; joint probability | [19 §2](notebooks/19_hmm_inference.ipynb) |
| 21–31 | The two-dice example; Markov properties | [19 §3](notebooks/19_hmm_inference.ipynb) |
| 32–38 | Inference tasks | [19 §4](notebooks/19_hmm_inference.ipynb) |
| 39–59 | Forward algorithm; worked example O = {2, 3, 6} | [19 §5](notebooks/19_hmm_inference.ipynb) |
| 60–72 | Backward algorithm | [19 §6](notebooks/19_hmm_inference.ipynb) |
| 73–79 | P(Q∣O) for a path | [19 §7](notebooks/19_hmm_inference.ipynb) |
| 80–85 | Posterior P(qₜ∣O) | [19 §8](notebooks/19_hmm_inference.ipynb) |
| 86–95 | Most probable path: Viterbi | [19 §9–10](notebooks/19_hmm_inference.ipynb) |
| 96–109 | Learning with observed states (counting) | [20 §1](notebooks/20_hmm_learning.ipynb) |
| 110–119 | EM / Baum–Welch | [20 §2–4](notebooks/20_hmm_learning.ipynb) |
| 120 | Number of states | [20 §5](notebooks/20_hmm_learning.ipynb) |
| 121–125 | Dynamic Bayesian networks: factorial, semi-Markov, hierarchical HMMs | [20 §6](notebooks/20_hmm_learning.ipynb) |
| 126–133 | Motifs; profile HMMs; phylo-HMMs | [20 §7](notebooks/20_hmm_learning.ipynb), [19 §11](notebooks/19_hmm_inference.ipynb) |
| 134 | What you should know | [19](notebooks/19_hmm_inference.ipynb), [20](notebooks/20_hmm_learning.ipynb) key takeaways |

## `013_Bayesian-MCMC_mz_032725` — Bayesian learning and MCMC (47 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–6, 13–14 | MLE, MAP and fully Bayesian learning; point estimate vs distribution | [21 §1–2](notebooks/21_bayesian_learning_mcmc.ipynb) |
| 7–15 | Bayesian linear regression | [21 §3](notebooks/21_bayesian_learning_mcmc.ipynb) |
| 16–22 | General recipe; sampling as the numerical approach | [21 §4–5](notebooks/21_bayesian_learning_mcmc.ipynb) |
| 23–35 | Gibbs sampling | [21 §6](notebooks/21_bayesian_learning_mcmc.ipynb) |
| 36–43 | Coordinate-descent intuition; burn-in; number of samples | [21 §7](notebooks/21_bayesian_learning_mcmc.ipynb) |
| 44–45 | MCMC beyond Gibbs: Metropolis–Hastings | [21 §8](notebooks/21_bayesian_learning_mcmc.ipynb) |
| 46–47 | MCMC in biology; summary | [21 §9](notebooks/21_bayesian_learning_mcmc.ipynb) |

## `014_NN_mz_032725` — Neural networks (51 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 3–17 | A neuron = logistic regression; hidden layers; nonlinear boundaries; activations | [22 §1–3](notebooks/22_neural_networks.ipynb) |
| 18–23 | Feed-forward and convolutional networks; CNNs for TF binding sites | [22 §8](notebooks/22_neural_networks.ipynb) |
| 24–26 | Graph convolutional networks; drug interactions | [22 §9](notebooks/22_neural_networks.ipynb) |
| 27–39 | Autoencoders, VAEs, NN vs graphical models, RNNs | [22 §10–11](notebooks/22_neural_networks.ipynb) |
| 40–49 | SGD and back-propagation | [22 §4–7](notebooks/22_neural_networks.ipynb) |
| 50–51 | Summary; further reading | [22 §11](notebooks/22_neural_networks.ipynb) |

## `015_model-selection_mz_040725`, `015_model-selection--extra` — Model selection (62 + 11 slides)

| Slides | Topic | Where to study it |
|---|---|---|
| 2–4 | Parameter estimation vs model selection; knobs per method | [23 §1](notebooks/23_model_selection.ipynb) |
| 5–19 | Training vs test error; bias and variance | [23 §2–3](notebooks/23_model_selection.ipynb) |
| 20–26 | Feature subsets, HMM states, Bayesian-network edges | [23 §3](notebooks/23_model_selection.ipynb) |
| 27–37 | Cross-validation, k-fold, LOOCV; never touch the test set | [23 §5–6](notebooks/23_model_selection.ipynb) |
| 38–41 | Regularisation; bias² + variance for the lasso | [23 §7](notebooks/23_model_selection.ipynb), [07](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| 42–43 | Bayesian information criterion | [23 §8](notebooks/23_model_selection.ipynb), [13 §8](notebooks/13_mixture_models_em.ipynb), [20 §5](notebooks/20_hmm_learning.ipynb) |
| 45–58, extra 8–11 | Bias–variance decomposition and its derivation | [23 §4](notebooks/23_model_selection.ipynb) |
| 59–62 | Bayes error rate; summary | [23 §9](notebooks/23_model_selection.ipynb) |
| extra 1–2 | Sparse regression for GWAS | [07 §9](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| extra 3–6 | Golub case study: kNN, Gaussian classifier, logistic regression | [23 §10](notebooks/23_model_selection.ipynb), [24](notebooks/24_capstone_project.ipynb) |
| extra 7 | Regularisation | [23 §7](notebooks/23_model_selection.ipynb) |

**Summary slide (62):** bias–variance trade-off (23 §2–4); cross-validation, BIC, regularisation
(23 §5–8); Bayes error rate (23 §9).

---

## The course project (`001_intro` slide 10)

"Analyse a dataset with three methods of your choice as a team": proposal → peer review →
presentation → final report → peer review. [Module 24](notebooks/24_capstone_project.ipynb) walks
through a complete example and gives a report template, a peer-review rubric and a
self-assessment checklist linked to every deck's summary slide.
