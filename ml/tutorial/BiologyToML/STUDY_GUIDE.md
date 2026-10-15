# Study guide: learning 02-620 on your own with BiologyToML

This guide is for the student working alone. It explains how to study a module, how to use the
notebooks next to the 02-620 slides, which derivations you must be able to reproduce, how the
notation changes from deck to deck, and how to prepare for the two midterms and the project.

---

## 1. The study loop (for every module)

1. **Skim the slides first** (10–15 min). Open [`SLIDE_MAP.md`](SLIDE_MAP.md), find the deck and
   flip through the slides the module covers. Do not try to understand everything — note the
   questions the slides raise.
2. **Run the notebook once, top to bottom** (Runtime → Run all on Colab). Read the 🧫 biological
   question, the 🎯 objectives and the 🗺️ contents. The goal of this pass is the big picture.
3. **Work section by section.** For each section: read the 📍 where-we-are box, read the theory
   and say every "*In words:*" sentence back in your own words, run the cells, then read 🔍 *What
   just happened?* and check it against what you see. Do every ✏️ *Your turn* — they are where the
   learning happens.
4. **Pen and paper.** Re-derive every displayed equation on paper before moving on. If a step
   feels like magic, the 🧮 refresher or the earlier module named in the 📍 box has the missing
   piece.
5. **Return to the slides** with the 📑 slide-connection boxes. You should now be able to explain
   every slide of the range — including the ones that are only an equation.
6. **Self-test** with ✅ *Checkpoint*: answer before opening the hidden answer. Then try one
   🧠 discussion question and one 🚀 bonus item.
7. **Write the 📝 lab note.** Five minutes; it is your revision sheet for the exams.

A module takes 2–3 hours this way. It is better to do one module properly than three quickly.

## 2. Reading a 02-620 deck with a notebook open

- **Equations on slides are pictures.** The notebooks re-type them, define every symbol and
  check them numerically. If a notebook and a slide disagree, the notebook explains why (often
  a typo on the slide or a different but equivalent convention; see §4).
- **Worked examples are reproduced exactly**: the six-person genotype table (Module 08), the
  PlayTennis information gains (10), the five-object distance matrix (12), the alarm network's
  0.005355 (15, 17), the 14 d-separation examples (16), the two-dice forward variables
  0.14 / 0.03 / 0.0236 / 0.0052 (19), the three labelled dice sequences (20), the prostate
  coefficients of ESL Table 3.2 (06). Re-compute them by hand once.
- **Slide numbers** in the notebooks are PowerPoint numbers. Some PDF exports drop hidden slides,
  so the PDF page can be one or two lower (details at the top of `SLIDE_MAP.md`).

## 3. The derivations to master

These are the "can you derive it on a blank page?" results of the course. Tick them off.

| Derivation | Slides | Module |
|---|---|---|
| MLE of a Bernoulli / binomial probability (4/7 for H,H,T,T,H,H,T) | `003` 40 | [05 §2](notebooks/05_likelihood_mle_map.ipynb) |
| MAP with a Beta prior = "imaginary counts" | `003` 49–50 | [05 §4](notebooks/05_likelihood_mle_map.ipynb), [08 §8](notebooks/08_knn_naive_bayes.ipynb) |
| Gaussian likelihood ⇒ least squares; normal equations w = (XᵀX)⁻¹Xᵀy | `002` 18–24, 32–39 | [06 §4, §6](notebooks/06_linear_regression_gwas.ipynb), [04 §6](notebooks/04_calculus_and_optimization.ipynb) |
| Gaussian prior ⇒ ridge, λ = σ²/σ₀²; centring and the intercept | `002` 47–59 | [07 §2–4](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| Soft-thresholding solution of the one-dimensional lasso | `002` 67–69 | [07 §7](notebooks/07_ridge_lasso_sparse_regression.ipynb) |
| Naïve-Bayes parameter counts 3ⁿ, (3ⁿ−1)·2, 2·n·2 (+1); MLE = counts | `003` 18–23, 34–46 | [08 §3–6](notebooks/08_knn_naive_bayes.ipynb) |
| Logistic-regression log-likelihood and gradient Σ xᵢ(y − P̂) | `004` 22–28 | [09 §5](notebooks/09_logistic_regression.ipynb) |
| Entropy, conditional entropy, information gain | `005` 13–25 | [10 §2–3](notebooks/10_decision_trees_random_forests.ipynb) |
| SVM margin M = 2/‖w‖; hard/soft-margin QP; w = Σαᵢyᵢxᵢ; (xᵀz)² = φ(x)ᵀφ(z) | `007` 22–29, 38–52, 62–66 | [11 §3–6](notebooks/11_support_vector_machines.ipynb) |
| k-means never increases its objective | `006` 20–28 | [12 §4](notebooks/12_clustering_kmeans_hierarchical.ipynb) |
| GMM responsibilities (Bayes' rule) and the EM updates | `010` 28–31, 58–64 | [13 §3–5](notebooks/13_mixture_models_em.ipynb) |
| PCA: maximise uᵀSu s.t. uᵀu = 1 ⇒ Su = λu | `011` 47–51 | [14 §6](notebooks/14_pca_dimensionality_reduction.ipynb), [04 §7](notebooks/04_calculus_and_optimization.ipynb) |
| Bayesian-network factorisation and parameter counting (31 vs 10) | `008` 18–28 | [15 §3–4](notebooks/15_bayesian_networks_representation.ipynb) |
| d-separation on the three triples; Markov blankets | `008` 50–93 | [16 §2–5](notebooks/16_bayesian_networks_independence.ipynb) |
| Enumeration and variable elimination for P(B∣J,¬M) | `008` 108–127 | [17 §1–3](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| Chow–Liu: maximum spanning tree on mutual information | `008` 158–162 | [17 §7](notebooks/17_bayesian_networks_inference_learning.ipynb) |
| Θᵢⱼ = 0 ⟺ conditional independence; the conditional is a regression | `009` 29–42 | [18 §5–7](notebooks/18_gaussian_graphical_models.ipynb) |
| Forward and backward recursions; Viterbi | `012` 39–72, 91–95 | [19 §5–9](notebooks/19_hmm_inference.ipynb) |
| HMM MLE by counting; Baum–Welch E- and M-steps | `012` 99–119 | [20 §1–4](notebooks/20_hmm_learning.ipynb) |
| Posterior of Bayesian linear regression; a Gibbs step | `013` 15, 23–35 | [21 §3, §6](notebooks/21_bayesian_learning_mcmc.ipynb) |
| Back-propagation for a two-layer network | `014` 41–49 | [22 §4](notebooks/22_neural_networks.ipynb) |
| Bias–variance decomposition of the squared error | `015` 45–58 | [23 §4](notebooks/23_model_selection.ipynb) |

## 4. Notation across the decks (and the traps)

The lectures were written at different times and by different people, so notation drifts.
The notebooks always say which convention they use.

| Topic | What changes | Course convention |
|---|---|---|
| Number of features | J (`002`, `010`), n (`003`, `004`), K (`009`, `011`), p (`002` slides 66–67, `015`) | J; the notebook names the slide's letter |
| Number of samples | N (most decks), L (`003`, `004`), n (`015`) | N |
| Regression weights | w (`002`), β (`002` slides 62–69, `015`) | w, intercept w₀ |
| Prior variance of weights | σ₀² (`002`), σ_w² (`013`) | as on the slide being discussed |
| Logistic function | 1/(1+exp(w₀+Σwᵢxᵢ)) on `004` slides 8–19, 32 and `014` slide 16 vs exp(·)/(1+exp(·)) on `004` slides 23–31 — they differ by the sign of every weight | P(Y=1∣x) = 1/(1+exp(−(w₀+wᵀx))) |
| λ | step size (`004` slide 29), ridge/lasso strength (`002`, `015`), Lagrange multiplier and eigenvalue (`011`) | the notebook says which |
| HMM transitions | P(qₜ=sᵢ∣qₜ₋₁=sⱼ) (`012` slides 14, 20, 34) vs aᵢⱼ = P(qₜ=sⱼ∣qₜ₋₁=sᵢ) (slide 107) | aᵢⱼ = P(next = j ∣ current = i) |
| Genotype coding | AA = 0, AT = 1, TT = 2 (`002` slide 9); `003` slide 14 calls AA "minor-allele homozygous" | 0/1/2 copies of one chosen allele; 2 − G carries the same information |
| SVM margin | full band width 2/‖w‖ (slides) vs half-width 1/‖w‖ (ESL, Murphy) | the slides' full width |
| Conditional ML estimate | "MLCE" and "MCLE" both appear (`002`) | maximum conditional likelihood |

## 5. The three ideas that recur in every lecture

1. **The two-step template** — choose a probability model (Step 1), estimate its parameters
   by MLE, MAP or full Bayes (Step 2). Seen in 05, 06, 07, 08, 09, 13, 15–21. The
   non-probabilistic exceptions — trees (10), k-means (12), SVM (11) — each have a probabilistic
   cousin (random forests ↔ averaging, k-means ↔ GMM, SVM ↔ logistic regression).
2. **Conditional independence buys tractability** — 3ⁿ → 2n (naïve Bayes, 08), 31 → 10 (alarm
   network, 15), a chain over time (HMM, 19), a sparse precision matrix (GGM, 18). Markov
   blankets and d-separation (16) read these assumptions off a picture.
3. **Latent variables ⇒ EM** — MLE is easy if the hidden labels were known; the labels are easy
   to infer if the parameters were known; so alternate. The same algorithm appears in mixtures
   (13), HMMs (Baum–Welch, 20), k-means as its hard-assignment limit (12–13), and Gibbs sampling
   is its sampling sibling (21).

The capstone (24 §11) puts all methods on one page.

## 6. Preparing for the midterms and the project

- **Midterm I** has covered the material up to SVMs (the `007_midterm` slide: "the exam will
  cover up to SVM"), i.e. decks `001`–`007`: Modules 05–12, with Part A as the mathematical
  background. **Midterm II** is not cumulative and covers the rest (`008`–`015`): Modules 13–23.
  Check the current semester's announcement. The midterms allow one hand-written page of notes —
  build it from your 📝 lab notes and the 📌 key takeaways.
- For each module: redo the ✅ checkpoint without looking; re-derive the table in §3 for that
  lecture; explain each 📑 slide box's *exam tip* to someone else.
- Work the numerical examples by hand with a calculator (forward variables, information gains,
  naïve-Bayes counts, the alarm-network queries, a k-means iteration, a single-link merge), then
  check them in the notebook.
- **The project** (one data set, three methods, as a team): Module 24 is a complete worked
  example with an evaluation contract, nested cross-validation, uncertainty, a report template
  and a peer-review rubric.

## 7. When you are stuck

| Symptom | What to do |
|---|---|
| `NameError` for a function or variable | run the notebook from the top (setup and toolkit cells first); after a kernel restart everything must be re-run |
| "Could not obtain … using a simulated stand-in" | you are offline or the download failed; the notebook still runs but on simulated data — numbers will differ from the text |
| Numbers slightly different from the text | library versions differ; the conclusion should not change. If it does, re-run from the top (the seeds assume top-to-bottom order) |
| A derivation step makes no sense | go to the module named in the 📍 box; the 🧮 refreshers of Modules 02–04 cover every tool used later |
| A slide and a notebook disagree | read the ⚠️ box near the slide connection; the [`INSTRUCTOR_GUIDE.md`](INSTRUCTOR_GUIDE.md) lists known slide errata |

## 8. Lab-note template

```text
Module:                         date:
Input (data, its source, real or simulated):
Output (what the code produced):
Method (one sentence):
Key equation (and its reading in words):
Key parameters (and what changed when I modified one):
One failure mode / assumption that can break:
Connection to the 02-620 slides (deck, slides):
One question I still have:
```
