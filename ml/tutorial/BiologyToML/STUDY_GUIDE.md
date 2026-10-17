# Study guide: learning machine learning for biology on your own with BiologyToML

This guide is for the student working alone. It explains how to study a module, which
derivations you must be able to reproduce, the notation traps, how to prepare for exams and the
project, and how to move from Level 1 (the 02-620 core) to Level 2 (the research frontier) and
to reading research papers. Everything you need is in the notebooks: they teach the lecture
content themselves.

---

## 1. The study loop (for every module)

1. **Run the notebook once, top to bottom** (Runtime → Run all on Colab). Read the 🧫 biological
   question, the 🎯 objectives and the 🗺️ contents. The goal of this pass is the big picture.
2. **Work section by section.** For each section: read the 📍 where-we-are box, read the theory
   and say every "*In words:*" sentence back in your own words, run the cells, then read
   🔍 *What just happened?* and check it against what you see. Do every ✏️ *Your turn* — that is
   where the learning happens.
3. **Pen and paper.** Re-derive every displayed equation before moving on. If a step feels like
   magic, the 🧮 refresher or the earlier module named in the 📍 or 🔗 box has the missing piece.
4. **Consolidate with the summary boxes.** In Level 1, the 📘 *Lecture notes* boxes summarise
   everything the 02-620 lecture teaches on the topic — definitions, key equations, a worked
   example and an 🎓 exam tip. In Level 2, the 📄 *Research connection* boxes say what the field
   does and where it is going. You should be able to explain every box without looking at the
   code.
5. **Self-test** with ✅ *Checkpoint*: answer before opening the hidden answer. Then try one
   🧠 discussion question and one 🚀 bonus item.
6. **Write the 📝 lab note.** Five minutes; it is your revision sheet.

A module takes 2–3 hours this way. It is better to do one module properly than three quickly.

## 2. Worked examples to recompute by hand

The classic worked examples of the course are typed into the notebooks with their numbers.
Recompute each once with a calculator, then check it in the notebook: the six-person genotype
table for naïve Bayes (Module 08), the PlayTennis information gains (10), the five-object distance
matrix (12), the alarm network's P(B, J, ¬M) = 0.0063175 (15, 17), the 14 d-separation examples
(16), the two-dice forward variables and the Viterbi table for O = (2, 3, 6) (19), the labelled
dice sequences (20), and the least-squares fit of the prostate-cancer study (06; the notebook
shows the original study's coefficients next to the synthetic fit).

## 3. The derivations to master

These are the "can you derive it on a blank page?" results of Level 1. Tick them off.

| Derivation | Module |
|---|---|
| MLE of a Bernoulli / binomial probability (4/7 for H,H,T,T,H,H,T) | [05](notebooks/05_likelihood_mle_map.ipynb) |
| MAP with a Beta prior = "imaginary counts" | [05](notebooks/05_likelihood_mle_map.ipynb), [08](notebooks/08_knn_naive_bayes.ipynb) |
| Gaussian likelihood ⇒ least squares; normal equations w = (XᵀX)⁻¹Xᵀy | [06](notebooks/06_linear_regression_gwas.ipynb), [04](notebooks/04_calculus_and_optimization.ipynb) |
| Gaussian prior ⇒ ridge, λ = σ²/σ₀²; centring and the intercept | [07](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| Soft-thresholding solution of the one-dimensional lasso | [07](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| Naïve-Bayes parameter counts 3ⁿ, (3ⁿ−1)·2, 2·n·2 (+1); MLE = counts | [08](notebooks/08_knn_naive_bayes.ipynb) |
| Logistic-regression log-likelihood and gradient Σ xᵢ(y − P̂) | [09](notebooks/09_logistic_regression.ipynb) |
| Entropy, conditional entropy, information gain | [10](notebooks/10_decision_trees_random_forests.ipynb) |
| SVM margin M = 2/‖w‖; hard/soft-margin QP; w = Σαᵢyᵢxᵢ; (xᵀz)² = φ(x)ᵀφ(z) | [11](notebooks/11_support_vector_machines.ipynb) |
| k-means never increases its objective | [12](notebooks/12_clustering_kmeans_hierarchical.ipynb) |
| GMM responsibilities (Bayes' rule) and the EM updates | [13](notebooks/13_mixture_models_em.ipynb) |
| PCA: maximise uᵀSu s.t. uᵀu = 1 ⇒ Su = λu | [14](notebooks/14_pca_dimensionality_reduction.ipynb), [04](notebooks/04_calculus_and_optimization.ipynb) |
| Bayesian-network factorisation and parameter counting (31 vs 10) | [15](notebooks/15_bayesian_networks_representation.ipynb) |
| d-separation on the three triples; Markov blankets | [16](notebooks/16_bayesian_networks_independence.ipynb) |
| Enumeration and variable elimination for P(B∣J,¬M) | [17](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| Chow–Liu: maximum spanning tree on mutual information | [17](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| Θᵢⱼ = 0 ⟺ conditional independence; the conditional is a regression | [18](notebooks/18_gaussian_graphical_models.ipynb) |
| Forward and backward recursions; Viterbi | [19](notebooks/19_hmm_inference.ipynb) |
| HMM MLE by counting; Baum–Welch E- and M-steps | [20](notebooks/20_hmm_learning.ipynb) |
| Posterior of Bayesian linear regression; a Gibbs step | [21](notebooks/21_bayesian_learning_mcmc.ipynb) |
| Back-propagation for a two-layer network | [22](notebooks/22_neural_networks.ipynb) |
| Bias–variance decomposition of the squared error | [23](notebooks/23_model_selection.ipynb) |

**Level 2 additions** (derive them once each): the negative-binomial log-likelihood and the IRLS
update (24); the ELBO and the reparameterisation gradient (25); scaled dot-product attention (26);
the closed form of q(x_t∣x₀) and the flow-matching target (27); one GCN layer (28); the GP
posterior and expected improvement (29); the steady-state RNA-velocity relation u = (γ/β)s and the
Sinkhorn iteration (32); Moran's I (33); CCA by SVD (34); the LMM likelihood after rotation by
the eigenvectors of K and a single-effect regression (35); the Kabsch rotation (38); the
backdoor adjustment formula and inverse-probability weighting (41); the split-conformal interval
(42); perplexity (43).

## 4. Notation (and the traps)

Textbooks and lectures use different letters for the same thing. The notebooks always say which
convention they use.

| Topic | What varies | Course convention |
|---|---|---|
| Number of features | J, n, K or p | J |
| Number of samples | N, L or n | N |
| Regression weights | w or β | w, intercept w₀ |
| Logistic function | 1/(1+exp(w₀+Σwᵢxᵢ)) or exp(·)/(1+exp(·)) — they differ by the sign of every weight | P(Y=1∣x) = 1/(1+exp(−(w₀+wᵀx))) |
| λ | a step size, a ridge/lasso strength, a Lagrange multiplier or an eigenvalue | the notebook says which |
| HMM transitions | P(qₜ=sᵢ∣qₜ₋₁=sⱼ) or aᵢⱼ = P(qₜ=sⱼ∣qₜ₋₁=sᵢ) | aᵢⱼ = P(next = j ∣ current = i) |
| Genotype coding | count of the minor or of the major allele | 0/1/2 copies of one chosen allele; 2 − G carries the same information |
| SVM margin | full band width 2/‖w‖ or half-width 1/‖w‖ | full width 2/‖w‖ |
| Negative binomial | dispersion α = 1/θ or inverse dispersion θ | Var = μ + μ²/θ (Modules 24, 30) |
| Labels | 0/1 or −1/+1; scikit-learn's breast-cancer coding has 0 = malignant | 1 = disease/positive throughout |

## 5. The ideas that recur everywhere

1. **The two-step template** — choose a probability model, then estimate its parameters by MLE,
   MAP or full Bayes. Seen in 05–09, 13, 15–21 and again in 24, 25, 29, 35, 37. The
   non-probabilistic exceptions — trees (10), k-means (12), SVMs (11) — each have a probabilistic
   cousin.
2. **Conditional independence buys tractability** — 3ⁿ → 2n (naïve Bayes, 08), 31 → 10 (alarm
   network, 15), a chain over time (HMM, 19), a sparse precision matrix (GGM, 18); later the Potts
   model on a contact map (37) and message passing on graphs (28).
3. **Latent variables ⇒ EM, and its relatives** — mixtures (13), HMMs (20), k-means as the hard
   limit (12); Gibbs sampling as the sampling sibling (21); variational inference and VAEs as the
   approximate version (25), used for single cells (25, 31, 34).
4. **Evaluation is part of the method** — held-out data, cross-validation, selection bias (23),
   and in Level 2 grouped splits, leakage, shift, calibration and conformal intervals (42), plus
   the habit of checking every method against a known truth (every 🧪 box).

The capstone (44, Part 1 §11) puts all Level 1 methods on one page; [`FRONTIER_MAP.md`](FRONTIER_MAP.md)
shows how each Level 1 idea grows into a Level 2 method.

## 6. Preparing for exams and the project

- In 02-620, the first midterm has covered material up to support vector machines (Modules 05–12,
  with Part A as background) and the second the rest (Modules 13–23). Check the current
  semester's announcement. If one hand-written page of notes is allowed, build it from your
  📝 lab notes, the 📘 lecture boxes and the 📌 key takeaways.
- For each module: redo the ✅ checkpoint without looking; re-derive that module's rows of the
  table in §3; explain each 🎓 exam tip to someone else.
- Work the numerical examples of §2 by hand, then check them in the notebook.
- **The project** (one data set, several methods, as a team): Module 44 is a complete worked
  example with an evaluation contract, nested cross-validation, uncertainty, a report template, a
  peer-review rubric — and six research tracks with starter code if you want a frontier project.

## 7. From Level 1 to research

- **Finish Level 1 first.** Every Level 2 module names the core modules it builds on (🔗 boxes).
- **Pick a track** (README): single-cell and spatial, genomics and genetics, proteins and drug
  discovery, or AI for science.
- **Use the ground truth.** In every Level 2 module, predict the result of a 🧪 check before
  running it, then change a simulator parameter (fewer cells, stronger batch effect, weaker
  coupling, more noise) and see which methods break first. This is how researchers stress-test
  methods.
- **Then go to real data.** The 🧭 *From toy to real data* section of each module names public
  data sets and production tools. Reproduce one result of the module on real data with the
  production tool, and compare.
- **Reading a research paper** (the capstone, Part 3, has a checklist): What is the biological
  question and the unit of replication? What is the baseline? How were the data split, and could
  information leak? What is the evidence that the method found something true (a ground truth,
  an experiment, a replication)? What would change your mind? Write a five-line summary in your
  lab notebook.

## 8. When you are stuck

| Symptom | What to do |
|---|---|
| `NameError` for a function or variable | run the notebook from the top (setup and toolkit cells first); after a kernel restart everything must be re-run |
| Numbers slightly different from the text | library versions differ; the conclusion should not change. If it does, re-run from the top (the seeds assume top-to-bottom order) |
| A PyTorch cell is slow | it should take seconds to a minute on Colab's CPU; close other heavy notebooks, or reduce the number of training steps (the exercise often asks you to) |
| A derivation step makes no sense | go to the module named in the 📍 or 🔗 box; the 🧮 refreshers of Modules 02–04 cover every tool used later |
| A result contradicts what a paper reports | the data are simulated and often cleaner than real data; the notebook explains what the simulation can and cannot show |

## 9. Lab-note template

```text
Module:                         date:
Biological question:
Data (simulated: which simulator, and what the hidden truth is):
Output (what the code produced):
Method (one sentence):
Key equation (and its reading in words):
Key parameters (and what changed when I modified one):
Ground-truth check (what the method recovered vs the truth):
One failure mode / assumption that can break:
Connection to the 02-620 topics or to research (paper, tool):
One question I still have:
```
