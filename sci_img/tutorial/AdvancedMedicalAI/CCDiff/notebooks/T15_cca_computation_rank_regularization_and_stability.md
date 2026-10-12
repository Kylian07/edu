# T15 · CCA computation, rank, regularization, and stability

**Suggested week(s):** 19–20  
**Prerequisite:** T08, T13–T14  
**Primary goal:** Inspect sample-size limits, CCA components, fitted versus held-out correlation, and numerical instability.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

With many features and few paired observations, CCA can find seemingly excellent directions even when no genuine cross-view relationship exists. This is especially relevant to CCDiff because a CLIP embedding can be high-dimensional while the selected concept bank may be small and repeatedly sampled.

## 2. What you need to know

CCA estimates directions from covariance statistics, so finite-sample estimation matters. A matrix with only a handful of distinct text vectors has limited rank, even when repeated many times to match the image count. Beware of reporting near-perfect **training-set** canonical correlations as if they imply generalizable dependence.

In this tutorial we deliberately build independent high-dimensional random matrices and fit CCA. The resulting apparently impressive in-sample correlations can collapse on held-out paired observations. Regularization, dimensionality reduction, lower component counts, and resampling are ways to diagnose this problem, though they do not establish semantic validity by themselves.

### Source map
Appendix A.1; Section 3.5; Appendix E pairing-stability results.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
from sklearn.cross_decomposition import CCA
rng=np.random.default_rng(15)
Xtr=rng.normal(size=(50,18));Ytr=rng.normal(size=(50,18))
Xte=rng.normal(size=(200,18));Yte=rng.normal(size=(200,18))
cca=CCA(n_components=3,max_iter=3000)
Utr,Vtr=cca.fit_transform(Xtr,Ytr)
Ute,Vte=cca.transform(Xte,Yte)
for j in range(3):
    print(j,'train',round(np.corrcoef(Utr[:,j],Vtr[:,j])[0,1],3),
             'held-out',round(np.corrcoef(Ute[:,j],Vte[:,j])[0,1],3))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
from sklearn.decomposition import PCA
# Diagnostic: reduce each view's dimensionality before fitting CCA.
px=PCA(n_components=3).fit(Xtr);py=PCA(n_components=3).fit(Ytr)
cca_small=CCA(n_components=2,max_iter=3000)
u,v=cca_small.fit_transform(px.transform(Xtr),py.transform(Ytr))
u2,v2=cca_small.transform(px.transform(Xte),py.transform(Yte))
print('Reduced train r:',np.corrcoef(u[:,0],v[:,0])[0,1])
print('Reduced test r:',np.corrcoef(u2[:,0],v2[:,0])[0,1])
```

## 5. Independent experiment

Vary the feature width from 2 to 5 to 15 to 30 at fixed 50 training pairs. Record first training/held-out canonical correlations over at least ten seeds. Why should this result make you cautious about low correlation in the inverse-CCA pipeline?

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Does a fitted CCA correlation of 0.99 guarantee that the modalities are related?
2. How can repeating only 8 unique candidate text vectors affect rank?
3. Why compare fitted and held-out correlation?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Appendix A.1; Section 3.5; Appendix E pairing-stability results.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Inspect sample-size limits, CCA components, fitted versus held-out correlation, and numerical instability.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T16.
