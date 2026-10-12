# T08 · Standardization, PCA, and singular value decomposition

**Suggested week(s):** 10  
**Prerequisite:** T06–T07  
**Primary goal:** Understand mean-centering, feature scaling, PCA, numerical rank, and SVD.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Cell area could be around 100 while fluorescence intensity is around 0.5. If we use raw Euclidean distances, area may dominate comparisons solely due to measurement units. Feature-wise standardization addresses this issue, but can amplify noise in low-variance dimensions.

## 2. What you need to know

For an observation $x_{ij}$ and feature $j$, a standardized value is $z_{ij}=(x_{ij}-\mu_j)/\sigma_j$. PCA finds orthogonal directions capturing maximal variance within one matrix. CCA instead finds paired directions across *two* matrices that maximize their correlation. SVD factors a matrix $X=U\Sigma V^\top$ and provides a useful lens for covariance structure, rank, and noisy data.

In high dimensions, sample covariance can be singular or poorly estimated. This matters in CCDiff because embedding dimensions can be large relative to the number of distinct candidate concepts. Students should inspect numerical rank and not equate a successful software fit with reliable inference.

### Source map
Appendix A.1 CCA; Section 3.5 standardization.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_cell_table
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
cells=make_cell_table(n=50,seed=8)
features=['elongation','area','nuclear_area','intensity']
X=cells[features].to_numpy()
Z=StandardScaler().fit_transform(X)
pca=PCA(n_components=2)
Q=pca.fit_transform(Z)
print('Feature means after standardization:',Z.mean(0).round(6))
print('Explained variance fractions:',pca.explained_variance_ratio_)
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(5,4))
for group in ['A','B']:
    mask=(cells.condition==group).to_numpy()
    ax.scatter(Q[mask,0],Q[mask,1],s=15,alpha=.65,label=group)
ax.set(xlabel='PC1',ylabel='PC2',title='PCA of simulated biological features')
ax.legend();plt.show()
print('Singular values of centered X:',np.linalg.svd(Z,full_matrices=False)[1])
```

## 5. Independent experiment

Add a feature column containing the constant value 1. How does a standard scaler handle it? Examine the singular values and numerical rank. Explain why PCA is not the same as CCDiff's inverse CCA.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What does PCA maximize?
2. What does CCA maximize?
3. Why can low-variance coordinates cause numerical problems?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Appendix A.1 CCA; Section 3.5 standardization.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Understand mean-centering, feature scaling, PCA, numerical rank, and SVD.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T09.
