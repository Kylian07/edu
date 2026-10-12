# T13 · Paired biological views and cross-covariance

**Suggested week(s):** 16  
**Prerequisite:** T07–T08, T11  
**Primary goal:** Define properly paired multiview samples and compute within- and cross-view covariance.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

In multiomics studies, a cell can have both gene-expression and protein-expression measurements. When the two assays measure the **same** cell, each gene-expression row has a corresponding protein-expression row. This is an appropriate motivating example for canonical correlation analysis.

CCDiff instead pairs images from one set with captions selected for the other set using modulo sampling. The corresponding rows do not necessarily describe the same item; this is a nonstandard, important assumption to investigate.

## 2. What you need to know

Given mean-centered paired matrices $X\in\mathbb{R}^{n\times p}$ and $Y\in\mathbb{R}^{n\times q}$, their sample cross-covariance is $\Sigma_{XY}=X^\top Y/(n-1)$. The entries describe how one measurement variable covaries with a different variable under **the specified row alignment**. If we permute the rows of $Y$ independently, the cross-covariance generally changes.

An embedding distribution may contain an obvious marginal difference between the sets even while arbitrary row pairing produces little meaningful cross-covariance. This motivates comparing inverse CCA against simpler marginal-distribution baselines.

### Source map
Appendix A.1 mathematical CCA; Section 3.5 and Appendix E use modulo-based pairing.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
rng=np.random.default_rng(13)
n=150
latent=rng.normal(size=(n,2))
X=latent@np.array([[1.,.5,.2],[.1,.7,1.]])+rng.normal(scale=.2,size=(n,3))
Y=latent@np.array([[.8,.4],[.1,1.]])+rng.normal(scale=.2,size=(n,2))
Xc=X-X.mean(0);Yc=Y-Y.mean(0)
cross=Xc.T@Yc/(n-1)
print('Cross-covariance shape:',cross.shape)
print(cross.round(2))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
shuffled=Y[rng.permutation(n)]
Ysh=shuffled-shuffled.mean(0)
print('Paired cross-covariance norm:',np.linalg.norm(cross))
print('Shuffled cross-covariance norm:',np.linalg.norm(Xc.T@Ysh/(n-1)))
print('Within-X covariance shape:',np.cov(X,rowvar=False).shape)
```

## 5. Independent experiment

Repeat 100 independent row shuffles. Histogram the Frobenius norm of the resulting cross-covariance matrices. Explain what sample pairing adds that mere knowledge of two distributions does not.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What does the covariance of `X[:,0]` with `Y[:,1]` require?
2. If X and Y have different feature widths, can CCA still work?
3. What scientific assumption is broken by arbitrary row permutations?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Appendix A.1 mathematical CCA; Section 3.5 and Appendix E use modulo-based pairing.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Define properly paired multiview samples and compute within- and cross-view covariance.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T14.
