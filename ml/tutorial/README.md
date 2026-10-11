# Machine Learning for Scientists — Tutorial Series

**Course:** Carnegie Mellon University 02-620 *Machine Learning for Scientists*  
**Prerequisites:** Python, NumPy, linear algebra (vectors/matrices), basic calculus (gradients), and probability fundamentals.

This tutorial series covers the foundational mathematical and computational frameworks of machine learning tailored for scientific and biomedical applications. Rather than treating models as black-box predictors, these modules develop learning theory from first principles, connect loss functions to probabilistic priors, apply regularized algorithms to high-dimensional biological data, and establish rigorous distribution-free uncertainty quantification.

---

## Curriculum Overview

| # | Topic / Subfolder | Core Focus | Notebooks |
|---|-------------------|------------|-----------|
| 01 | [`FundamentalsLearningUncertainty`](FundamentalsLearningUncertainty/) | Supervised vs. unsupervised paradigms, Gaussian noise modeling, MLE vs. MAP parameter estimation, objective landscapes, and asymptotic convergence | `fundamentals of Learning & Uncertainty.ipynb` |
| 02 | [`RegularizedLinearRegression`](RegularizedLinearRegression/) | High-dimensional regression ($p \gg n$), OLS rank deficiency, Ridge ($L_2$/Gaussian prior), Lasso ($L_1$/Laplace prior/coordinate descent), regularization paths, and genomic prediction | `Linear regression methods.ipynb`<br>`Ridge_and_Lasso_for_High_Dimensional_Genomics.ipynb`<br>`ridge_lasso_genomic_prediction_tutorial.ipynb` |
| 03 | [`GenerativeDiscriminativeClassification`](GenerativeDiscriminativeClassification/) | Non-parametric $k$-NN, generative Gaussian Naive Bayes ($P(X \mid Y)$ with conditional independence), discriminative Logistic Regression ($P(Y \mid X)$ via cross-entropy loss), decision boundaries, and probability calibration under correlated features | `8. ML classification KNN & NB.ipynb`<br>`naive_bayes_vs_logreg_tutorial.ipynb` |
| 04 | [`DecisionTreesRandomForests`](DecisionTreesRandomForests/) | Non-linear tree architectures (CART, Gini impurity), variance reduction via bagging and random feature subspace sampling (Random Forests), feature importance (MDI vs. permutation), and TCGA cancer driver mutation classification | `random_forest_driver_mutation_tutorial.ipynb` |
| 05 | [`ConformalPrediction`](ConformalPrediction/) | Distribution-free predictive uncertainty quantification, finite-sample split conformal regression intervals, locally adaptive prediction bands, conformal classification prediction sets, and clinical distribution-shift auditing | `Conformal_Prediction_for_Trustworthy_Biomedical_Models.ipynb` |

---

## Module Summaries

### Module 01 — Fundamentals of Learning & Uncertainty

Scientific datasets present unique statistical challenges: measurements are expensive, sensor noise can be substantial, and sample sizes are often small. This module establishes the mathematical grounding for machine learning in science:
- **Task Categorization:** Formulating supervised conditional prediction $P(Y \mid X)$ vs. unsupervised latent distribution modeling $P(X)$.
- **Parameter Estimation:** Deriving Maximum Likelihood Estimation (MLE) and Maximum A Posteriori (MAP) estimation under Gaussian assumptions.
- **Prior Beliefs as Regularizers:** Demonstrating how prior distributions prevent severe overfitting when sample size $N$ is small, and visualizing objective landscapes.
- **Asymptotic Convergence:** Simulating convergence across sample sizes from $N=1$ to $N=150$, showing empirical evidence dominating the prior as $N \to \infty$.

### Module 02 — Regularized Linear Regression

Modern scientific studies frequently operate in the high-dimensional regime ($p \gg n$), such as whole-genome sequencing panels or transcriptomic profiles measured across limited patient cohorts. In this regime, ordinary least squares fails because $X^\top X$ is singular and non-invertible:
- **Theory & Mathematics:** Establishing the rank deficiency of OLS, the closed-form $L_2$ shrinkage of Ridge regression, and the sparsity-inducing $L_1$ geometry of Lasso regression.
- **Algorithms from Scratch:** Implementing closed-form Ridge solvers and cyclic coordinate descent with soft-thresholding without external libraries.
- **Regularization Paths:** Tracking coefficient trajectories as penalty hyperparameter $\lambda$ sweeps from zero to infinity.
- **Genomic Application:** Predicting quantitative phenotypes from molecular markers using both controlled pathway simulations and real published CIMMYT wheat genotype data.

### Module 03 — Generative vs. Discriminative Classification

In biomedical diagnostics, classifiers predict categorical outcomes (e.g., tumor malignancy) from continuous measurements. This module explores the foundational theoretical and practical trade-offs between generative and discriminative models:
- **Instance-Based Non-Parametric Learning:** Using $k$-Nearest Neighbors ($k$-NN) to capture flexible non-linear decision boundaries and evaluating the bias-variance impact of hyperparameter $k$.
- **Generative Classification (Naive Bayes):** Modeling class-conditional feature distributions $P(X \mid Y)$ and prior probabilities $P(Y)$, relying on conditional feature independence for fast, closed-form estimation.
- **Discriminative Classification (Logistic Regression):** Directly optimizing class boundaries $P(Y \mid X)$ via convex cross-entropy loss and gradient descent without distributional assumptions on inputs.
- **Correlated Feature Violations:** Demonstrating on real diagnostic breast cancer data how strong physical feature correlations (radius, perimeter, area) distort Naive Bayes probabilities while logistic regression adjusts weights seamlessly.
- **Probability Calibration:** Benchmarking Brier scores and reliability curves to ensure predicted diagnostic probabilities reflect true clinical risk.

### Module 04 — Decision Trees & Random Forests

Biological systems frequently exhibit non-linear interactions and threshold dynamics. While individual decision trees recursively partition data, they suffer from high variance and instability. Random Forests overcome this through ensemble learning:
- **Tree Theory (CART):** Recursively partitioning feature space using Gini impurity reduction to identify optimal split thresholds.
- **Variance Reduction (Bagging):** Training diverse trees on bootstrap samples of the training data and averaging predictions to reduce estimator variance.
- **Feature Subspace Decorrelation:** Restricting split candidates to random subsets ($m \approx \sqrt{p}$) to decorrelate individual trees and prevent dominant features from homogenizing the ensemble.
- **Feature Importance Diagnostics:** Quantifying variable contributions via Mean Decrease Impurity (MDI) versus permutation importance.
- **Cancer Mutation Classification:** Replicating the philosophy of the landmark bioinformatics tool CHASM to classify cancer driver versus passenger mutations in TCGA breast cancer sequencing data and testing cross-cancer generalization on melanoma.

### Module 05 — Conformal Prediction for Trustworthy Biomedical Models

Point predictions and raw softmax probabilities fail to quantify whether a biomedical model is confident or guessing, especially when deploying across different clinical sites. Conformal prediction provides distribution-free, finite-sample guarantees:
- **Split Conformal Regression:** Deriving prediction intervals from calibration residuals with mathematically guaranteed marginal coverage $1-\alpha$, regardless of sample size or data distribution.
- **Locally Adaptive Bands:** Normalizing nonconformity scores by local dispersion estimators to expand intervals in heteroscedastic regions and tighten them where confidence is high.
- **Calibrated Prediction Sets:** Replacing forced single-class diagnosis with Adaptive Prediction Sets (APS) of plausible disease classes.
- **Subgroup & Distribution-Shift Auditing:** Auditing demographic subgroups for hidden undercoverage and stress-testing models against covariate and concept shifts when transferring across clinical sites.
- **Responsible Translation:** Translating statistical coverage into safe clinical decision support without conflating prediction intervals with confidence or causal intervals.

---

## Setup & Dependencies

```bash
pip install numpy scipy matplotlib pandas scikit-learn
```
