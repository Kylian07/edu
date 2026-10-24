# T06 · Vectors, dot products, and projections

**Suggested week(s):** 7  
**Prerequisite:** T03, T05  
**Primary goal:** Represent image/text embeddings as vectors and calculate norms, dot products, and projections.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

CLIP turns an image into a vector, such as a point with hundreds or thousands of coordinates. A coordinate need not correspond directly to an interpretable property. Yet vector mathematics allows us to compare representations. Begin with three deliberately interpretable axes: cell elongation, brightness, and nucleus size.

## 2. What you need to know

For vectors $x,y\in\mathbb{R}^d$, $x^\top y=\sum_j x_jy_j$ is their dot product and $\|x\|_2=\sqrt{x^\top x}$ is their Euclidean length. The scalar projection of $x$ onto a unit vector $u$ equals $x^\top u$.

This is the first geometric prerequisite for CCA, which searches for useful *projection directions*, and for CLIP similarity, which compares the angle between embeddings. Keep the semantic meaning distinct from the geometry: a large positive dot product does not automatically mean a scientifically valid concept is present.

### Source map
Sections 3.4–3.5 and Appendix A.1: all use projections and matrix notation.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
cell=np.array([1.7,.55,.30])
concept=np.array([1.,0.,0.])
print('dot product:',cell @ concept)
print('norm cell:',np.linalg.norm(cell))
print('projection of cell onto elongation:',cell @ (concept/np.linalg.norm(concept)))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
X=np.array([[1.5,.5,.3],[1.8,.6,.28],[1.2,.7,.4]])
W=np.array([[1.,0.],[0.,1.],[0.,0.]])
projected=X @ W
print('Input matrix shape:',X.shape,'Projector shape:',W.shape)
print('Projected shape:',projected.shape)
print(projected)
```

## 5. Independent experiment

Draw a two-dimensional scatterplot and project every point onto a chosen unit direction. Compare projection [1,0] versus [1/sqrt(2),1/sqrt(2)]. Predict the matrix shapes before running the code.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What is a projection direction?
2. What numerical condition makes two vectors orthogonal?
3. Why is embedding dimension not equal to the number of images?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Sections 3.4–3.5 and Appendix A.1: all use projections and matrix notation.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Represent image/text embeddings as vectors and calculate norms, dot products, and projections.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T07.
