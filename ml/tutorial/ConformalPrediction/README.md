# Topic 05 — Conformal Prediction for Trustworthy Biomedical Models

## Overview

In high-stakes biomedical applications—such as clinical biomarker forecasting, patient survival analysis, or cancer subtype diagnosis—point predictions are insufficient. A single scalar prediction or forced top-1 classification label fails to convey whether the model is highly confident or entirely guessing. Furthermore, standard model probabilities (such as neural network softmax outputs) are frequently uncalibrated, and classical parametric confidence intervals rely on fragile Gaussian or asymptotic assumptions that fail on real, complex biomedical cohorts.

**Conformal Prediction** provides a mathematically rigorous, distribution-free uncertainty quantification framework that wraps around any arbitrary predictive algorithm (from linear models to deep neural networks) to produce finite-sample prediction guarantees:

1. **Three Data Roles:** Explicitly splitting data into training, calibration ($n$ observations), and evaluation/test cohorts. Calibration observations must remain strictly independent of model training to maintain exchangeability.
2. **Split Conformal Regression:** Deriving nonconformity scores from calibration residuals $s_i = |y_i - \widehat{\mu}(x_i)|$. By computing the finite-sample corrected empirical quantile:
   $$\widehat{q} = \text{Quantile}\left(\{s_i\}_{i=1}^n, \frac{\lceil(n+1)(1-\alpha)\rceil}{n}\right)$$
   the resulting symmetric prediction interval $\widehat{C}(X_{n+1}) = [\widehat{\mu}(X_{n+1}) - \widehat{q}, \;\widehat{\mu}(X_{n+1}) + \widehat{q}]$ provably satisfies the marginal coverage guarantee:
   $$P(Y_{n+1} \in \widehat{C}(X_{n+1})) \ge 1 - \alpha$$
   for any new, exchangeable observation $(X_{n+1}, Y_{n+1})$, regardless of sample size or data distribution.
3. **Locally Adaptive Prediction Intervals:** A constant interval width fails when noise is heteroscedastic (varying across patient age, disease severity, or tissue type). By fitting a secondary model $\widehat{\sigma}(x)$ to predict local dispersion and calibrating normalized residuals $s_i = \frac{|y_i - \widehat{\mu}(x_i)|}{\widehat{\sigma}(x_i)}$, prediction intervals adapt dynamically—expanding in noisy regions and tightening where the model is precise.
4. **Classification Prediction Sets:** Rather than forcing a single, potentially erroneous diagnosis, conformal classification transforms softmax probabilities into calibrated prediction sets of plausible disease classes. Using Adaptive Prediction Sets (APS), the prediction set contains the ground-truth diagnosis with guaranteed probability $\ge 1 - \alpha$.
5. **Subgroup Reliability & Distribution-Shift Auditing:** A global marginal guarantee does not ensure uniform validity across demographic subgroups or clinical cohorts. We perform fine-grained coverage audits across patient demographics and stress-test deployed models against hospital-to-hospital covariate and concept shifts when exchangeability breaks down.

---

## What you will learn

- **Distribution-Free Guarantees:** How conformal prediction establishes finite-sample validity without distributional or parametric assumptions.
- **The Exchangeability Condition:** Why calibration requires exchangeability between calibration and test cohorts, and how to detect when exchangeability is violated.
- **Split Conformal Regression:** Deriving the corrected conformal quantile and constructing guaranteed prediction intervals.
- **Coverage vs. Efficiency:** Balancing nominal coverage against prediction interval width and set cardinality.
- **Locally Adaptive Bands:** Normalizing nonconformity scores by conditional variance or MAD estimators to resolve heteroscedasticity.
- **Calibrated Prediction Sets:** Implementing Adaptive Prediction Sets (APS) for multiclass diagnostic problems.
- **Subgroup Auditing & Shift Stress-Testing:** Diagnosing hidden undercoverage in clinical subpopulations and quantifying coverage collapse when transferring models across hospital sites.
- **Responsible Translation:** Distinguishing prediction intervals from confidence and causal intervals to inform real clinical workflows.

---

## Notebooks

| File | Description |
|------|-------------|
| [`Conformal_Prediction_for_Trustworthy_Biomedical_Models.ipynb`](Conformal_Prediction_for_Trustworthy_Biomedical_Models.ipynb) | Comprehensive tutorial covering distribution-free prediction intervals, locally adaptive conformal regression, classification prediction sets, subgroup reliability audits, and external-site distribution-shift stress testing on simulated biomedical cohorts. |

---

## Key References

- Angelopoulos, A. N. & Bates, S. (2022). A gentle introduction to conformal prediction and distribution-free uncertainty quantification. *arXiv preprint arXiv:2107.07511*.
- Shafer, G. & Vovk, V. (2008). A tutorial on conformal prediction. *Journal of Machine Learning Research* 9, 371–421.
- Romano, Y., Patterson, E. & Candès, E. (2019). Conformalized quantile regression. *Advances in Neural Information Processing Systems (NeurIPS)* 32.
- Romano, Y., Sesia, M. & Candès, E. (2020). Classification with valid and adaptive prediction sets. *NeurIPS* 33, 3582–3592.
- Vovk, V., Gammerman, A. & Shafer, G. (2005). *Algorithmic Learning in a Random World*. Springer.
- Tibshirani, R. J., Foygel Barber, R., Candès, E. & Ramdas, A. (2019). Conformal prediction under covariate shift. *NeurIPS* 32.
