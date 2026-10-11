# Machine Learning for Scientists

Welcome to the **Machine Learning for Scientists** educational track (CMU 02-620). This curriculum explores the statistical, probabilistic, and mathematical foundations of machine learning tailored for scientific and biomedical discovery.

For the complete syllabus, roadmap, and module details, see the **[Tutorial Series Guide](tutorial/README.md)**.

---

## Contents

| Topic / Subfolder | Core Description | Notebooks |
|-------------------|------------------|-----------|
| [`FundamentalsLearningUncertainty`](tutorial/FundamentalsLearningUncertainty/) | Supervised vs. unsupervised learning paradigms, probabilistic modeling, Maximum Likelihood Estimation (MLE) vs. Maximum A Posteriori (MAP), objective landscapes, and sample size asymptotic behavior | `fundamentals of Learning & Uncertainty.ipynb` |
| [`RegularizedLinearRegression`](tutorial/RegularizedLinearRegression/) | High-dimensional regression ($p \gg n$), OLS rank deficiency, Ridge regression ($L_2$ / Gaussian prior), Lasso regression ($L_1$ / Laplace prior / coordinate descent), regularization paths, and genomic phenotype prediction | `Linear regression methods.ipynb`<br>`Ridge_and_Lasso_for_High_Dimensional_Genomics.ipynb`<br>`ridge_lasso_genomic_prediction_tutorial.ipynb` |
| [`GenerativeDiscriminativeClassification`](tutorial/GenerativeDiscriminativeClassification/) | Non-parametric $k$-NN, generative Gaussian Naive Bayes, discriminative Logistic Regression from scratch, decision boundaries, ROC/AUC, and calibration curves on diagnostic breast cancer data | `8. ML classification KNN & NB.ipynb`<br>`naive_bayes_vs_logreg_tutorial.ipynb` |
| [`DecisionTreesRandomForests`](tutorial/DecisionTreesRandomForests/) | Recursive binary splitting (CART, Gini impurity), ensemble bagging and feature decorrelation in Random Forests, MDI vs. permutation feature importance, and cross-cancer generalization on TCGA somatic mutations | `random_forest_driver_mutation_tutorial.ipynb` |
| [`ConformalPrediction`](tutorial/ConformalPrediction/) | Distribution-free uncertainty quantification, finite-sample prediction intervals, adaptive heteroscedastic intervals, multiclass prediction sets, subgroup reliability audits, and biomedical distribution-shift stress testing | `Conformal_Prediction_for_Trustworthy_Biomedical_Models.ipynb` |

---

## Further Reading

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Hastie, T., Tibshirani, R. & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.
- Murphy, K. P. (2012). *Machine Learning: A Probabilistic Perspective*. MIT Press.
- Crossa, J. et al. (2010). Prediction of genetic values of quantitative traits in plant breeding using genomic markers. *Genetics* 186(2), 713–724.
- Breiman, L. (2001). Random forests. *Machine Learning* 45(1), 5–32.
- Carter, H. et al. (2009). Cancer-specific high-throughput annotation of somatic mutations (CHASM). *Cancer Research* 69(16), 6664–6672.
- Angelopoulos, A. N. & Bates, S. (2022). A gentle introduction to conformal prediction and distribution-free uncertainty quantification. *arXiv:2107.07511*.
- Shafer, G. & Vovk, V. (2008). A tutorial on conformal prediction. *Journal of Machine Learning Research* 9, 371–421.
