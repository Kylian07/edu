# Topic 04 — Decision Trees & Random Forests

## Overview

Complex biological mechanisms frequently involve non-linear dependencies, combinatorial regulation, and switch-like threshold behaviors that linear models cannot easily capture. Tree-based methods partition feature space into axis-aligned rectangular subsets using hierarchical decision rules. While individual decision trees provide intuitive interpretations, they suffer from high variance and severe susceptibility to overfitting.

**Random Forests** resolve this instability through ensemble learning, combining two foundational statistical mechanisms:

1. **Classification and Regression Trees (CART):** Recursively partitioning observations by greedily selecting the split $(j, t)$ that maximizes Gini impurity reduction:
   $$\text{Gini}(S) = 1 - \sum_{c=1}^C p_c^2, \qquad \Delta\text{Gini} = \text{Gini}(S) - \left(\frac{|S_L|}{|S|}\text{Gini}(S_L) + \frac{|S_R|}{|S|}\text{Gini}(S_R)\right)$$
2. **Bootstrap Aggregation (Bagging):** Training $B$ individual trees on bootstrap samples of the training set (sampling $N$ observations uniformly with replacement). Averaging reduces estimator variance toward zero as $B \to \infty$ for perfectly uncorrelated estimators.
3. **Random Feature Subspace Decorrelation:** At each split node, considering only a small random subset of features ($m \approx \sqrt{p}$). This prevents strong predictor variables from dominating every tree, ensuring diversity across the ensemble and maximizing the variance-reduction benefit of averaging.
4. **Feature Importance Estimation:** Identifying biologically critical features using two distinct strategies:
   - **Mean Decrease Impurity (MDI):** Accumulated Gini gain attributed to each feature across all trees in the forest.
   - **Permutation Feature Importance:** Measuring empirical performance drop on held-out samples when values of a specific feature are randomly permuted.
5. **Application to Cancer Genomics:** Distinguishing pathological cancer **driver mutations** from harmless passenger hitchhikers—a foundational problem in cancer biology. This implementation replicates the core philosophy of **CHASM** (Carter et al., 2009) using real curated somatic mutations from the TCGA breast cancer (BRCA) cohort and evaluating generalization on melanoma (SKCM).

---

## What you will learn

- **Tree Architecture & Splitting:** How CART constructs decision trees via recursive binary partitioning and Gini impurity optimization.
- **Ensemble Theory:** The mathematical principles of variance reduction via bagging and random feature subspace sampling.
- **From-Scratch Implementation:** Building complete `DecisionTreeScratch` and `RandomForestScratch` estimators in Python without external machine learning libraries.
- **Ensemble Gain:** Benchmarking how ensembling stabilizes decision boundaries, improves test accuracy, and boosts ROC AUC / PR curves compared to individual trees.
- **Feature Importance Diagnostics:** Comparing MDI versus permutation importance and diagnosing potential biases in impurity metrics.
- **Real Genomic Discovery:** Training on curated TCGA breast cancer mutations with sequence-context odds-ratio features and testing generalization to an unseen cancer type (TCGA melanoma).

---

## Notebooks

| File | Description |
|------|-------------|
| [`random_forest_driver_mutation_tutorial.ipynb`](random_forest_driver_mutation_tutorial.ipynb) | Complete from-scratch tutorial implementing CART decision trees and Random Forests to predict cancer driver versus passenger mutations using real TCGA genomic data, comparing ensemble gains, feature importances, and cross-cancer generalization. |

---

## Key References

- Breiman, L. (2001). Random forests. *Machine Learning* 45(1), 5–32.
- Breiman, L., Friedman, J., Stone, C. J. & Olshen, R. A. (1984). *Classification and Regression Trees*. Wadsworth & Brooks/Cole.
- Carter, H. et al. (2009). Cancer-specific high-throughput annotation of somatic mutations (CHASM). *Cancer Research* 69(16), 6664–6672.
- Hastie, T., Tibshirani, R. & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer, Chapters 9 & 15.
- Strobl, C., Boulesteix, A.-L., Zeileis, A. & Hothorn, T. (2007). Bias in random forest variable importance measures: Illustrations, sources and a solution. *BMC Bioinformatics* 8, 25.
- 02-620 *Machine Learning for Scientists* course materials, Topic on Decision Trees & Random Forests.
