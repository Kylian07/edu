# T03 · NumPy, matrices, and visualization

**Suggested week(s):** 3  
**Prerequisite:** T01–T02  
**Primary goal:** Convert features to an array; understand rows versus columns; compute group statistics with vectorized code.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Consider a laboratory table in which each row is a cell and the columns are measurements. Algorithms consume numeric arrays, not human-readable spreadsheet labels. Correct dimensions are a recurring theme in CCDiff: its image embeddings are arranged as number-of-images by embedding-dimension matrices.

## 2. What you need to know

If $X\in\mathbb{R}^{N\times d}$, then $N$ is the number of images and $d$ the features per image. The column mean $\mu\in\mathbb{R}^{d}$ describes the average sample in the measured feature space. Before calculating a matrix product, always annotate shapes.

Vectorization with NumPy applies the same operation to many samples at once. That is not just faster; it often makes the mathematics visible in the code. Conversely, a transposed matrix or confusing column names with rows can silently change the meaning of an analysis. Use plots to corroborate numeric summaries rather than treating visualization as decoration.

### Source map
Section 3.4, p. 5 (matrix shapes and similarity); arrays are prerequisite skills.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
from ccdiff_edu import make_cell_table
cells=make_cell_table(n=35,seed=3)
features=['elongation','area','nuclear_area','intensity']
X=cells[features].to_numpy()
print('X shape:',X.shape)
print('Feature names:',features)
print('Column means:',dict(zip(features,np.round(X.mean(axis=0),2))))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(5,4))
for cond in ['A','B']:
    subset=cells.loc[cells.condition==cond]
    ax.scatter(subset['area'],subset['nuclear_area'],s=15,alpha=.65,label=cond)
ax.set(xlabel='Simulated cell area',ylabel='Simulated nuclear area',title='Two correlated measurements')
ax.legend();plt.show()
print('Row 0:', X[0])
print('Feature 0 across all rows:',X[:,0][:5])
```

## 5. Independent experiment

Compute means by condition without `.groupby` (use boolean masks on NumPy arrays). Introduce one intentionally missing value and explain why a naïve mean could fail. Create a plot in which axis labels report the physical quantity and unit (if known).

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What does `X.shape[1]` represent?
2. Why can standardization matter when area and intensity use different numerical scales?
3. In matrix $X\in\mathbb{R}^{N\times d}$, what is $X[:,j]$?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Section 3.4, p. 5 (matrix shapes and similarity); arrays are prerequisite skills.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Convert features to an array; understand rows versus columns; compute group statistics with vectorized code.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T04.
