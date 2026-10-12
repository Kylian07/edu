# T14 · Canonical correlation analysis: geometry and objective

**Suggested week(s):** 17–18  
**Prerequisite:** T06–T08, T13  
**Primary goal:** Explain and derive CCA constrained optimization; fit CCA on synthetic paired measurements.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Pearson correlation considers one numeric variable from each view. CCA asks a more general question: can we find a linear combination of the features in X and a linear combination of the features in Y that strongly co-vary across *paired observations*? Imagine finding an axis summarizing gene-expression measurements that aligns with an axis summarizing protein abundances.

## 2. What you need to know

Define $u=Xw_x$ and $v=Yw_y$. CCA finds $w_x,w_y$ that maximize $\operatorname{corr}(u,v)$, equivalently maximize $w_x^\top\Sigma_{XY}w_y$ under the constraints $w_x^\top\Sigma_{XX}w_x=1$ and $w_y^\top\Sigma_{YY}w_y=1$. Constraints prevent the projections from increasing without bound.

Additional canonical pairs seek new, appropriately constrained relationships after the first. A high canonical correlation is not a causal discovery, nor does it mean that individual weight coefficients have direct biological meaning. Inverse CCA in the manuscript uses the **low end** of the fitted component-correlation spectrum.

### Source map
Appendix A.1 standard CCA; Section 3.5 inverse-CCA insight.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
from sklearn.cross_decomposition import CCA
rng=np.random.default_rng(14)
z=rng.normal(size=(200,2))
X=z@np.array([[1,.5,.1],[0,.4,1]])+rng.normal(scale=.2,size=(200,3))
Y=z@np.array([[.7,.3],[.2,1.]])+rng.normal(scale=.2,size=(200,2))
cca=CCA(n_components=2,scale=True,max_iter=2000)
U,V=cca.fit_transform(X,Y)
rhos=[np.corrcoef(U[:,j],V[:,j])[0,1] for j in range(2)]
print('Canonical correlations:',np.round(rhos,3))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(5,4))
ax.scatter(U[:,0],V[:,0],s=12,alpha=.6)
ax.set(xlabel='X canonical variate 1',ylabel='Y canonical variate 1',title='CCA discovers a shared axis')
plt.show()
print('X and Y weight shapes:',cca.x_weights_.shape,cca.y_weights_.shape)
```

## 5. Independent experiment

Start from covariance and explain why a constraint is needed for each projection. Compare the correlations of the original first columns with the first canonical correlation; repeat on random, *independent* X and Y to probe spurious in-sample association.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What quantity does standard CCA maximize?
2. Why normalize the variances of the projected variables?
3. Is the first canonical component necessarily the one CCDiff ranks highest?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Appendix A.1 standard CCA; Section 3.5 inverse-CCA insight.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Explain and derive CCA constrained optimization; fit CCA on synthetic paired measurements.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T15.
