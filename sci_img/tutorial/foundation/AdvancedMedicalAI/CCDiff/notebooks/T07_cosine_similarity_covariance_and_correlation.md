# T07 · Cosine similarity, covariance, and correlation

**Suggested week(s):** 8–9  
**Prerequisite:** T05–T06  
**Primary goal:** Distinguish individual-vector similarity from statistical association across paired observations.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

CCDiff combines two concepts that sound similar but answer different questions. Cosine similarity compares the direction of two *individual embeddings*. Pearson correlation measures how two numeric variables vary *across paired observations*. Confusing the two would make the central algorithm incomprehensible.

## 2. What you need to know

Cosine similarity is $\cos(x,y)=x^\top y/(\|x\|\|y\|)$. Sample covariance between variables $a$ and $b$ is $\operatorname{Cov}(a,b)=\sum_i(a_i-\bar a)(b_i-\bar b)/(n-1)$. Pearson correlation normalizes covariance by the product of sample standard deviations.

CCA generalizes correlation to **linear projections of two multivariate views**. It requires a pairing relation across rows so its cross-covariance matrix can be interpreted. CCDiff's modulo-based pairing is therefore a particularly important design decision to investigate carefully in the later tutorials.

### Source map
Sections 3.4–3.6, particularly Algorithm 1 lines 18–19 and the inverse correlation score.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
from ccdiff_edu import normalize_rows
v1=np.array([[1.,0.],[1.,1.],[0.,1.]])
print('Cosine between first and second:',float(normalize_rows(v1)[0]@normalize_rows(v1)[1]))
rng=np.random.default_rng(7)
a=rng.normal(size=100)
b=2*a+rng.normal(scale=.4,size=100)
print('Pearson correlation:',np.corrcoef(a,b)[0,1])
print('Covariance:',np.cov(a,b)[0,1])
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
from matplotlib import pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(8,3))
axs[0].scatter(a,b,s=12);axs[0].set(title='Paired observations',xlabel='a',ylabel='b')
axs[1].scatter(a,np.random.default_rng(71).permutation(b),s=12)
axs[1].set(title='Pairing destroyed',xlabel='a',ylabel='permuted b')
plt.tight_layout();plt.show()
```

## 5. Independent experiment

Calculate correlation before and after random permutation in 20 trials, reporting the mean and range. Also compare cosine similarity of [1,0] and [10,0]. Explain why cosine ignores magnitude while covariance generally does not.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Can two vectors be cosine-similar while there is no meaningful sample correlation?
2. Why must CCA know which rows of its input matrices correspond?
3. What is the difference between near-zero correlation and strong negative correlation?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Sections 3.4–3.6, particularly Algorithm 1 lines 18–19 and the inverse correlation score.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Distinguish individual-vector similarity from statistical association across paired observations.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T08.
