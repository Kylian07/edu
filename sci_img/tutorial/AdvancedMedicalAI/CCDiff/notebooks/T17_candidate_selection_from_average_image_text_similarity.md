# T17 · Candidate selection from average image–text similarity

**Suggested week(s):** 22  
**Prerequisite:** T11–T12, T16  
**Primary goal:** Implement paper Section 3.4, check matrix dimensions and top-k sensitivity.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

In CCDiff, candidate captions are first embedded in the same space as the images. The algorithm does not hand the full bank to inverse CCA: it retains the descriptions with the greatest *average* cosine similarity for each set. This approximates which descriptions are representative of the dataset as a whole.

## 2. What you need to know

If dataset $D_s$ contains $N_s$ images, concept bank $K$ contains $M$ phrases, and image and text embeddings have width $d$, then $\tilde X_s\tilde Y_K^\top$ has shape $N_s\times M$. The score of candidate $j$ is the mean down column $j$: $a_s[j]=\frac1{N_s}\sum_i \cos(\tilde x_i,\tilde y_j)$. Top-$k$ selection provides $K_s$, $Y_s$ and its relevance scores $s_s$.

Because the two image sets may favor different concepts, their top-$k$ sets can differ even though both originated from the shared pool. A very small $k$ can omit important but rare distinctions; a large $k$ can admit irrelevant descriptions that corrupt later covariance analysis.

### Source map
Section 3.4 and Algorithm 1 steps 4–12.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,normalize_rows,select_concepts
import numpy as np
A,B,Y,labels=make_shared_toy_embeddings(n=60,seed=17)
S=normalize_rows(A)@normalize_rows(Y).T
manual_scores=S.mean(axis=0)
print('Similarity matrix:',S.shape)
print('Manual mean scores:',manual_scores.round(2))
assert np.allclose(manual_scores,select_concepts(A,Y,labels,top_k=5)['all_relevance'])
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
for k in [3,5,8,12]:
    out=select_concepts(A,Y,labels,top_k=k)
    print('top-k=',k,'selected concepts:',out['labels'])
print('A top 5:',select_concepts(A,Y,labels,top_k=5)['labels'])
print('B top 5:',select_concepts(B,Y,labels,top_k=5)['labels'])
```

## 5. Independent experiment

Introduce a new vector representing an irrelevant but always positive/background-like concept. Check whether it appears in both top-$k$ sets. Compare mean similarity with median similarity as an **exploratory alternative**; explain how a rare strongly matching subset could affect each estimator.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why do we normalize vectors before matrix multiplication?
2. What is the shape of S for 60 images, 12 concepts?
3. Does average image–text similarity tell us whether a phrase is *distinctive* relative to the other set?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Section 3.4 and Algorithm 1 steps 4–12.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Implement paper Section 3.4, check matrix dimensions and top-k sensitivity.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T18.
