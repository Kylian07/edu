# CCDiff — Complete Undergraduate Tutorial Handbook

**24 tutorials, from introductory biology to the CCDiff algorithm and research critique.**

> All simulation examples are educational. The manuscript is separately supplied and not embedded here.

## Contents

- [T01: From biological observations to datasets](#t01)
- [T02: Python for biological data analysis](#t02)
- [T03: NumPy, matrices, and visualization](#t03)
- [T04: Digital images as measurable biological data](#t04)
- [T05: Probability, sampling, and dataset distributions](#t05)
- [T06: Vectors, dot products, and projections](#t06)
- [T07: Cosine similarity, covariance, and correlation](#t07)
- [T08: Standardization, PCA, and singular value decomposition](#t08)
- [T09: Machine learning, generalization, and distribution shift](#t09)
- [T10: Neural networks and pretrained visual features](#t10)
- [T11: CLIP, contrastive learning, and image–text embeddings](#t11)
- [T12: Caption generators and candidate concept banks](#t12)
- [T13: Paired biological views and cross-covariance](#t13)
- [T14: Canonical correlation analysis: geometry and objective](#t14)
- [T15: CCA computation, rank, regularization, and stability](#t15)
- [T16: Low-correlation components and inverse CCA](#t16)
- [T17: Candidate selection from average image–text similarity](#t17)
- [T18: Cross-set pairing, inverse-CCA components, and concept matching](#t18)
- [T19: Combining inverse correlation and within-set relevance](#t19)
- [T20: Build the complete pedagogical CCDiff pipeline](#t20)
- [T21: Benchmark metrics, baselines, and reproducibility](#t21)
- [T22: Ablations, pairing stability, and scientifically meaningful controls](#t22)
- [T23: Biomedical case study: microscopy and medical claims](#t23)
- [T24: Read, reproduce, and critically defend the paper](#t24)

---


<a id="t01"></a>


# T01 · From biological observations to datasets

**Suggested week(s):** 1  
**Prerequisite:** None  
**Primary goal:** Identify an observation, feature, condition, and confounder; distinguish an individual-image explanation from a dataset-level difference.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

A biologist observes that cells in one dish look elongated and cells in another look round. One dramatic-looking cell does not establish a difference between experimental conditions. We must define a **sampling unit** (for example, an independently imaged cell), a **population**, and a repeatable measurement. Here the measured feature is elongation; the group labels are A and B. Images taken on the same plate may not be independent.

**Vocabulary:** sample, specimen, biological replicate, technical replicate, measurement, label, batch, dataset, population. 

## 2. What you need to know

CCDiff does not answer *why did the model predict a label for this one image?* Its target is a different question: *which text descriptions are more characteristic of image set A than image set B?* Think about this as a statistical claim about groups, not as a factual statement about every individual member.

The simplest non-ML comparator is the difference between two sample means, $\bar{x}_A-\bar{x}_B$. It provides a useful baseline, but it captures only a predefined numerical measurement. CCDiff attempts to recover natural-language descriptions using pretrained image and text embeddings. Throughout the course, separate **measurement** (what data show), **interpretation** (what the difference means), and **causal explanation** (what caused it).

### Source map
Introduction, pp. 1–2; Figures 1–2, p. 3.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_cell_table
import pandas as pd
cells = make_cell_table(n=40, seed=1)
print(cells.head())
print('\nCounts:', cells.groupby('condition').size().to_dict())
print('\nMean elongation:', cells.groupby('condition')['elongation'].mean().round(2).to_dict())
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6,3))
for group in ['A','B']:
    ax.hist(cells.loc[cells.condition==group,'elongation'], bins=12, alpha=.55, label=group)
ax.set(xlabel='Simulated elongation',ylabel='Cell count',title='Distributions can overlap')
ax.legend()
plt.show()
```

## 5. Independent experiment

Before opening the plot, predict which group will have the larger average elongation. Then (a) find one B cell more elongated than an A cell; (b) count specimens in each group; (c) name one real microscopy confounder (magnification, staining, or acquisition batch); (d) propose how you would collect biological replicates.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. If an A cell is round, does it invalidate the observation that A cells are *more often* elongated?
2. What is the difference between an image-level caption and a set-level description?
3. Would 100 images from the same donor necessarily count as 100 independent biological replicates?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Introduction, pp. 1–2; Figures 1–2, p. 3.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Identify an observation, feature, condition, and confounder; distinguish an individual-image explanation from a dataset-level difference.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T02.


---


<a id="t02"></a>


# T02 · Python for biological data analysis

**Suggested week(s):** 2  
**Prerequisite:** T01  
**Primary goal:** Write loops, conditional expressions, functions, and reusable summaries of biological observations.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Python is a tool for replacing repetitive manual calculations with transparent, reproducible instructions. The goal is not to memorize syntax: a scientist should be able to turn a measurement rule into an inspectable computation. We will use synthetic measurements rather than sensitive patient data.

## 2. What you need to know

A good function has clearly specified input, output, and assumptions. For example, to report what fraction of cells show the morphology “elongated,” we must specify the threshold and whether missing measurements are allowed. A choice such as elongation > 1.5 is an operational definition, not a biological law. If the threshold changes, the apparent fraction may change.

A reproducible script should fix random seeds for simulations, annotate units, and avoid changing the raw data in place. Try reading a Python function as if it were a laboratory protocol: what observations enter and what transformation happens?

### Source map
Introduction, pp. 1–2; programming is an instructional prerequisite, not a technique introduced in the paper.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_cell_table
cells=make_cell_table(n=30,seed=2)
values=cells['elongation'].tolist()
def count_above(xs,threshold):
    count=0
    for x in xs:
        if x>threshold:
            count += 1
    return count
print('Fraction above threshold:', count_above(values,1.5)/len(values))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
def summarize_group(df,group,threshold=1.5):
    selected=df.loc[df['condition']==group,'elongation'].dropna().tolist()
    if len(selected)==0:
        raise ValueError('No usable cells')
    return {'group':group,'n':len(selected),
            'mean':sum(selected)/len(selected),
            'fraction_elongated':count_above(selected,threshold)/len(selected)}
for condition in ['A','B']:
    print(summarize_group(cells,condition))
```

## 5. Independent experiment

Implement `fraction_above(xs, threshold)` so it returns a float. Add input validation for empty lists. Compare fractions at thresholds 1.3, 1.5, and 1.7. Explain why reporting a threshold without its definition is scientifically incomplete.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why put analysis logic in a function?
2. What happens when a denominator is zero?
3. What is the value of a fixed seed for a synthetic example?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Introduction, pp. 1–2; programming is an instructional prerequisite, not a technique introduced in the paper.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Write loops, conditional expressions, functions, and reusable summaries of biological observations.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T03.


---


<a id="t03"></a>


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


---


<a id="t04"></a>


# T04 · Digital images as measurable biological data

**Suggested week(s):** 4  
**Prerequisite:** T03  
**Primary goal:** Understand pixels, channels, intensities, masks, and handcrafted morphology features.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

A grayscale microscopy image is a two-dimensional numerical matrix. A fluorescent image may have several channels, each associated with an optical measurement, but raw channel intensities are not automatically comparable between imaging sessions. Dataset-level comparisons should therefore pay attention to acquisition protocols and batch effects.

Here we generate simple simulated ellipses that resemble stylized cell shapes. These are cartoons for learning, not real microscopy or a validated biological model.

## 2. What you need to know

Simple interpretable image features include mean intensity, segmented area, aspect ratio, texture, and edge density. We can create a mask by thresholding image intensity. In a real experiment, the chosen threshold can be affected by staining, focus, photobleaching, illumination, and image normalization.

A segmentation mask $M_{uv}\in\{0,1\}$ indicates pixels believed to belong to the cell. The segmented area is $A=\sum_{u,v}M_{uv}$ measured in pixels, not automatically in $\mu m^2$. Physical area requires calibration. An apparent difference between image sets might therefore reflect acquisition conditions instead of a biological phenotype.

### Source map
Sections 1 and 4.5 (biomedical context); teaching images are simulated and are not from MIMIC-CXR.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_cell_images
import numpy as np
import matplotlib.pyplot as plt
images=make_cell_images(n=12,size=48,seed=4)
fig,axs=plt.subplots(2,4,figsize=(8,4))
for r,condition in enumerate(['A','B']):
    for c in range(4):
        axs[r,c].imshow(images[condition][c],cmap='gray',vmin=0,vmax=1)
        axs[r,c].set_title(f'{condition}: cell {c+1}')
        axs[r,c].axis('off')
plt.tight_layout();plt.show()
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
def basic_image_features(image, threshold=.35):
    mask=image>threshold
    return {'mean_intensity':float(image.mean()),
            'mask_area_pixels':int(mask.sum()),
            'fraction_foreground':float(mask.mean())}
for condition in ['A','B']:
    print(condition,[basic_image_features(im)['mask_area_pixels']
                     for im in images[condition][:4]])
```

## 5. Independent experiment

Alter the threshold to 0.20, 0.35, and 0.55; graph the change in apparent area. Create a third dataset by brightening B images by 10%, while leaving geometry unchanged. What kind of false difference could a caption-based method surface?

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why is area in pixels not the same as area in square micrometers?
2. Is mean intensity necessarily a biological property?
3. How could an image-acquisition difference be mistaken for a phenotype?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Sections 1 and 4.5 (biomedical context); teaching images are simulated and are not from MIMIC-CXR.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Understand pixels, channels, intensities, masks, and handcrafted morphology features.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T05.


---


<a id="t05"></a>


# T05 · Probability, sampling, and dataset distributions

**Suggested week(s):** 5–6  
**Prerequisite:** T01–T04  
**Primary goal:** Explain sampling variability, empirical distributions, overlap, and bootstrap uncertainty.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Biologists often compare populations from a limited sample. A histogram helps us see more than a single mean. The apparent difference between sample A and sample B may fluctuate when new cells are drawn. This is the first step toward understanding *distribution shift*.

## 2. What you need to know

For observations $x_1,\ldots,x_n$, the empirical mean is $\bar x =\sum_i x_i/n$. A bootstrap repeatedly samples observations with replacement and recomputes a statistic. Its quantiles approximate how that statistic would vary under resampling assumptions. This elementary procedure will later help compare benchmark accuracy estimates and assess sensitivity to sample size.

The bootstrap is not a substitute for experimental design: if images from the same patient are correlated, independent image-level resampling can give confidence intervals that are too narrow. Biological replicates may need to be resampled as groups.

### Source map
Introduction on distribution shift; Sections 4 and 4.5; statistical background beyond paper equations.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
from ccdiff_edu import make_cell_table, bootstrap_ci
cells=make_cell_table(n=60,seed=5)
a=cells.query("condition=='A'")['elongation'].to_numpy()
b=cells.query("condition=='B'")['elongation'].to_numpy()
print('Observed mean difference A - B:',round(float(a.mean()-b.mean()),3))
print('Bootstrap 95% interval A mean:',bootstrap_ci(a,n_boot=500,seed=5))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
rng=np.random.default_rng(5)
boot_diffs=[]
for _ in range(500):
    sa=rng.choice(a,len(a),replace=True)
    sb=rng.choice(b,len(b),replace=True)
    boot_diffs.append(sa.mean()-sb.mean())
print('Bootstrap 95% interval of mean difference:',np.quantile(boot_diffs,[.025,.975]))
import matplotlib.pyplot as plt
plt.hist(boot_diffs,bins=22);plt.xlabel('Resampled mean difference');plt.ylabel('Count');plt.show()
```

## 5. Independent experiment

Repeat with only 10 cells per group. Compare intervals to those from 60. Then artificially duplicate each observation ten times and re-bootstrap as if all 600 rows were independent: explain why the resulting precision is misleading.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What does a bootstrap interval quantify?
2. Does a narrow interval prove causal significance?
3. Why can dataset construction change what differences can be found?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Introduction on distribution shift; Sections 4 and 4.5; statistical background beyond paper equations.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Explain sampling variability, empirical distributions, overlap, and bootstrap uncertainty.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T06.


---


<a id="t06"></a>


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


---


<a id="t07"></a>


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


---


<a id="t08"></a>


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


---


<a id="t09"></a>


# T09 · Machine learning, generalization, and distribution shift

**Suggested week(s):** 11  
**Prerequisite:** T01–T08  
**Primary goal:** Train and test a simple classifier, detect leakage, and separate performance shift from explainability.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

A model that classifies cells perfectly in its original laboratory may fail on images taken with different instruments. This is a distribution shift: the statistical properties of the input population, target distribution, or their relationship differ across environments. CCDiff aims to describe such differences at the dataset level; it does not by itself fix the downstream model.

## 2. What you need to know

Supervised learning estimates a map $f(x)\rightarrow y$. A test set should mimic the intended deployment setting while being independent of training data. An evaluation can be misleading if image crops from the same biological specimen occur in both training and test sets.

For a binary phenotype label, accuracy is the fraction of correct predictions. Compare accuracy with precision, recall, and confusion matrices when groups are imbalanced. Model debugging requires distinguishing statistical association from causal explanations: discovering 'bright background' in failure images might indicate an acquisition confound rather than an intrinsic biology problem.

### Source map
Introduction pp. 1–2; Section 4.6.1 analyzes model failure groups.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_cell_table
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
cells=make_cell_table(n=90,seed=9)
X=cells[['elongation','area','nuclear_area','intensity']].to_numpy()
y=(cells.condition=='B').astype(int).to_numpy()
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.3,random_state=9,stratify=y)
model=LogisticRegression(max_iter=2000).fit(Xtr,ytr)
print('Held-out accuracy:',accuracy_score(yte,model.predict(Xte)))
print('Confusion matrix:',confusion_matrix(yte,model.predict(Xte)))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import numpy as np
# A shifted laboratory measures an extra baseline intensity offset.
Xshift=Xte.copy(); Xshift[:,-1]+=.20
print('Original:',accuracy_score(yte,model.predict(Xte)))
print('Shifted intensity:',accuracy_score(yte,model.predict(Xshift)))
print('Most important coefficient magnitudes:',np.abs(model.coef_[0]))
```

## 5. Independent experiment

Repeat after dropping elongation and evaluate the change. Make one train/test split that deliberately duplicates observations between the sets. Write down why leakage creates overly optimistic performance and why feature drift is not always label drift.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Does detecting a shift diagnose its cause?
2. Why do we reserve data for testing?
3. What is wrong with splitting near-duplicate cell crops across train and test?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Introduction pp. 1–2; Section 4.6.1 analyzes model failure groups.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Train and test a simple classifier, detect leakage, and separate performance shift from explainability.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T10.


---


<a id="t10"></a>


# T10 · Neural networks and pretrained visual features

**Suggested week(s):** 12  
**Prerequisite:** T04, T06, T09  
**Primary goal:** Understand convolution as feature extraction, embeddings as intermediate representations, and pretrained models.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Before using CLIP, it helps to understand the basic idea of an image encoder. A convolutional feature detector scans a small pattern across the image. Modern encoders compose many operations to form learned representations whose individual coordinates may not be interpretable on their own. CCDiff uses *pretrained* visual features; students do not need to train a large network from scratch.

## 2. What you need to know

A 2-D convolution (often implemented as cross-correlation) computes a weighted local sum over an image. The output is a feature map that highlights a pattern such as an edge. Pooling and later layers can summarize spatial content. Vision transformers instead divide images into tokens or patches and aggregate information through attention. Both families produce embeddings for downstream analyses.

**Important distinction:** CCDiff's 'training-free' description means the discovery and ranking pipeline does not train a new image–text model. The pretrained CLIP/BLIP components were trained previously using large datasets and compute.

### Source map
Sections 1 and 3.3; Section 4.1 identifies pretrained CLIP backbone.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
from scipy.ndimage import correlate
from ccdiff_edu import make_cell_images
import matplotlib.pyplot as plt
image=make_cell_images(n=1,seed=10)['A'][0]
vertical_edge=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
response=correlate(image,vertical_edge,mode='reflect')
fig,axs=plt.subplots(1,2,figsize=(7,3))
axs[0].imshow(image,cmap='gray');axs[0].set_title('Synthetic image')
axs[1].imshow(response,cmap='coolwarm');axs[1].set_title('Vertical-edge response')
for ax in axs:ax.axis('off')
plt.tight_layout();plt.show()
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
from scipy.ndimage import sobel
images=make_cell_images(n=12,seed=10)
def handcrafted_embedding(im):
    # Three small features for illustration, NOT pretrained neural features.
    return np.array([im.mean(), np.abs(sobel(im,axis=0)).mean(),
                     np.abs(sobel(im,axis=1)).mean()])
for group in ['A','B']:
    encoded=np.array([handcrafted_embedding(im) for im in images[group]])
    print(group,'embedding shape:',encoded.shape,'mean:',encoded.mean(axis=0).round(3))
```

## 5. Independent experiment

Create a horizontal-edge filter and compare its response to the vertical-edge filter. Then imagine how exposure, resizing, and field of view could change a learned representation even without a biological phenotype difference.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What is a feature map?
2. What does a pretrained encoder supply?
3. Does CCDiff train its own visual encoder?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Sections 1 and 3.3; Section 4.1 identifies pretrained CLIP backbone.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Understand convolution as feature extraction, embeddings as intermediate representations, and pretrained models.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T11.


---


<a id="t11"></a>


# T11 · CLIP, contrastive learning, and image–text embeddings

**Suggested week(s):** 13–14  
**Prerequisite:** T06–T10  
**Primary goal:** Compare image and text vectors in a shared space; distinguish illustrative toy embeddings from real CLIP.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

CLIP contains an image encoder and a text encoder. A phrase such as “elongated cell” becomes a numerical vector, as does a cell image. The angle between these vectors can be used as a proxy for semantic alignment. This is what makes CCDiff possible: both images and descriptions can participate in matrix computations.

## 2. What you need to know

Contrastive image–text training usually encourages matched image–caption embeddings to be more similar than mismatched ones. With L2-normalized embeddings, the dot product equals cosine similarity. Given $X\in\mathbb{R}^{N\times d}$ and $Y\in\mathbb{R}^{K\times d}$, the similarity matrix is $S=\tilde X\tilde Y^\top\in\mathbb{R}^{N\times K}$. Each entry compares one image with one text concept.

The code below uses **synthetic vectors already placed in the same feature space**, not a trained CLIP model. This keeps the lesson reproducible on a CPU and separates the mathematical interface from the expensive model. A real-model optional extension is documented in `OPTIONAL_REAL_MODELS.md` at the repository root.

### Source map
Sections 3.3–3.4 and Algorithm 1 lines 1–11.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,normalize_rows
import numpy as np
A,B,text,labels=make_shared_toy_embeddings(n=50,seed=11)
scoreA=normalize_rows(A)@normalize_rows(text).T
scoreB=normalize_rows(B)@normalize_rows(text).T
print('Similarity matrix shape:',scoreA.shape)
print('Top A concept:',labels[np.argmax(scoreA.mean(axis=0))])
print('Top B concept:',labels[np.argmax(scoreB.mean(axis=0))])
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7,3))
ax.bar(np.arange(len(labels))-.17,scoreA.mean(0),width=.34,label='A')
ax.bar(np.arange(len(labels))+.17,scoreB.mean(0),width=.34,label='B')
ax.set_xticks(np.arange(len(labels)),labels,rotation=65,ha='right')
ax.set_ylabel('Mean cosine similarity');ax.legend();plt.tight_layout();plt.show()
```

## 5. Independent experiment

Write `image_text_similarity(X,Y)` with shape validation and row normalization. Compare normalized and raw dot products when all text embeddings are multiplied by 50. Optional real CLIP: after installing `transformers`, `torch`, and an accessible checkpoint, load it explicitly and run one image–text similarity example; this is not required for the offline assignment.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why can images and words be compared numerically?
2. Does a high cosine similarity prove a biological statement is true?
3. How many entries are in a similarity matrix for 100 images and 20 concepts?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Sections 3.3–3.4 and Algorithm 1 lines 1–11.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Compare image and text vectors in a shared space; distinguish illustrative toy embeddings from real CLIP.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T12.


---


<a id="t12"></a>


# T12 · Caption generators and candidate concept banks

**Suggested week(s):** 15  
**Prerequisite:** T11  
**Primary goal:** Construct, filter, and audit a shared text concept pool; explain the candidate-coverage bottleneck.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

CCDiff does not invent completely new phrases during its mathematical ranking step. It ranks descriptions from a *candidate bank*. The paper uses BLIP-2 captions by default for broad image benchmarks, but explicitly allows curated vocabulary lists. For biological scientists, curated descriptions can be more informative and more feasible to audit than unrestricted model captions.

## 2. What you need to know

A candidate bank $K$ is a list of textual descriptions. Deduplication prevents repeated or near-duplicate captions from overwhelming ranking. Domain-specific language should be validated: “high nucleus-to-cell area ratio” may be meaningful, whereas “diseased appearance” may be vague or even impossible to infer reliably from the image.

A central structural limitation is **concept coverage**: if no candidate expresses the actual biological difference, CCDiff cannot produce that wording from its fixed bank. Vocabulary construction is therefore part of experimental design, not a dispensable preprocessing detail.

### Source map
Sections 3.3 and 5 (candidate-bank creation and limitations); Appendix D caption quality.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,select_concepts
A,B,text,labels=make_shared_toy_embeddings(n=70,seed=12)
selection=select_concepts(A,text,labels,top_k=5)
print('Shared pool size:',len(labels))
print('Selected A phrases:',selection['labels'])
print('Source relevance:',selection['relevance'].round(3))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
# Controlled experiment: the correct A descriptor is not allowed in the pool.
keep=[i for i,t in enumerate(labels) if t!='elongated cell']
modified=select_concepts(A,text[keep],[labels[i] for i in keep],top_k=5)
print('Bank without elongated cell:',modified['labels'])
print('Can the ranker output an absent phrase?', 'elongated cell' in modified['labels'])
```

## 5. Independent experiment

Prepare a 20-term bank of cell-morphology descriptions. Mark each as directly observable, ambiguous, or requiring additional clinical/biological evidence. Reproduce the missing-concept experiment and explain why a high-ranking incorrect substitute is still a methodological failure.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why use a single shared concept pool before set-specific filtering?
2. Can inverse CCA discover a missing word sequence that is not in the bank?
3. Why must a clinical vocabulary be validated by domain experts?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Sections 3.3 and 5 (candidate-bank creation and limitations); Appendix D caption quality.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Construct, filter, and audit a shared text concept pool; explain the candidate-coverage bottleneck.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T13.


---


<a id="t13"></a>


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


---


<a id="t14"></a>


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


---


<a id="t15"></a>


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


---


<a id="t16"></a>


# T16 · Low-correlation components and inverse CCA

**Suggested week(s):** 21  
**Prerequisite:** T11–T15  
**Primary goal:** Implement CCDiff-style cross-set pairing and interrogate the low-correlation heuristic.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

CCDiff first selects concepts relevant to one dataset, then pairs those concept embeddings with images from the *opposing* dataset for CCA. After fitting CCA, it sorts canonical components by ascending absolute correlation. Candidate descriptions are mapped from the associated text-space directions. This is a clever and testable hypothesis, not a theorem equating low correlation with biological distinctiveness.

## 2. What you need to know

Suppose $K_A$ contains phrases representative of dataset A. To seek features distinctive to A, CCDiff pairs images $X_B$ with text embeddings $Y_A$ using a modulo rule to obtain equal row counts. It fits CCA and orders components by ascending $|\rho_i|$. A component with $\rho\approx0$ is interpreted as a weak relationship between the opposing image set and a direction of A's candidate-concept space. The direction is mapped back to a nearby textual candidate using cosine similarity.

**Crucial caution:** the pairing is not semantic correspondence. Neither low correlation nor a text-vector match alone proves that a description is more frequent in A than B. Validation needs negative controls, pairing ablations, and a simple direct difference-in-similarity baseline.

### Source map
Section 3.5, p. 6; Algorithm 1; Appendix E pairing ablation.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,select_concepts
from ccdiff_edu.pipeline import inverse_cca_candidates
A,B,text,labels=make_shared_toy_embeddings(n=80,seed=16)
selected_A=select_concepts(A,text,labels,top_k=8)
proposals=inverse_cca_candidates(B,selected_A,n_components=3)
for item in proposals:print(item['label'],'rho=',round(item['rho'],3),
                             'component=',item['component'])
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import numpy as np
for s in [1,2,3,4,5]:
    result=inverse_cca_candidates(B,selected_A,n_components=3,seed=s,shuffle=True)
    print('pairing seed',s,'top low-correlation text:',result[0]['label'],
          'rho',round(result[0]['rho'],3))
# A simpler baseline: direct difference in average CLIP cosine relevance
base_A=select_concepts(A,text,labels,top_k=len(labels))['all_relevance']
base_B=select_concepts(B,text,labels,top_k=len(labels))['all_relevance']
print('Largest direct mean-similarity difference:',labels[np.argmax(base_A-base_B)])
```

## 5. Independent experiment

Test an identical-set negative control by using A for both own and opposing images. Then test a shuffled pairing control on twenty seeds. How stable are the selected directions and concept labels? Discuss what you can and cannot conclude from the observed numerical results.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why does CCDiff sort by ascending $|\rho|$ instead of descending $\rho$?
2. What pairs are used to describe differences characteristic of A?
3. Does a near-zero CCA correlation mathematically prove uniqueness to A?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Section 3.5, p. 6; Algorithm 1; Appendix E pairing ablation.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Implement CCDiff-style cross-set pairing and interrogate the low-correlation heuristic.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T17.


---


<a id="t17"></a>


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


---


<a id="t18"></a>


# T18 · Cross-set pairing, inverse-CCA components, and concept matching

**Suggested week(s):** 23  
**Prerequisite:** T15–T17  
**Primary goal:** Trace every tensor and mapped description through Section 3.5, recording correlations and nearest concepts.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

This tutorial reconstructs the central CCDiff operation. You will select descriptions that characterize A, then compare their text embeddings against **B's** image embeddings. Reverse the roles to describe B relative to A. The row matching is artificial, and you should treat its stability as an empirical question.

## 2. What you need to know

Section 3.5 standardizes each image/text matrix by feature and creates equal-row-length inputs using modulo pairing. Standard CCA is fitted and the resulting canonical correlations $\rho_i$ are sorted by *ascending absolute value*. The text-space weight vector is converted back to raw embedding coordinates by dividing by the original text-feature standard deviations, then normalized. It is matched to the nearest original concept embedding by cosine similarity.

The sign of a canonical direction is not intrinsically identifiable. CCA components may also rotate in poorly determined subspaces; therefore the nearest concept mapping should be tested for robustness. The educational implementation exposes `component`, `rho`, `cosine_to_direction`, and `label` instead of returning only a final answer.

### Source map
Section 3.5, pp. 5–6; Algorithm 1 steps 13–24; Appendix E.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,select_concepts
from ccdiff_edu.pipeline import inverse_cca_candidates
A,B,text,labels=make_shared_toy_embeddings(n=90,seed=18)
sel=select_concepts(A,text,labels,top_k=8)
proposed=inverse_cca_candidates(B,sel,n_components=4)
for p in proposed:
    print(f"component={p['component']:d} rho={p['rho']:+.3f} "
          f"cos(dir,text)={p['cosine_to_direction']:.3f} {p['label']}")
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np
idx=np.arange(len(B))%len(sel['embeddings'])
xz=StandardScaler().fit_transform(B)
yz=StandardScaler().fit_transform(sel['embeddings'])[idx]
print('Image standardized shape:',xz.shape)
print('Repeated text standardized shape:',yz.shape)
print('Distinct rows before / after pairing:',len(sel['embeddings']),len(yz))
print('Text rank after pairing:',np.linalg.matrix_rank(yz))
```

## 5. Independent experiment

Reconstruct `inverse_cca_candidates` from scratch using 2-dimensional examples. Record the canonical correlation before and after changing the modulo pairing order. Then repeat on deliberately **identical image sets**; if a label remains highly ranked, what does that tell you about the assumption that low correlation proves uniqueness?

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Which images are paired with A's text concepts to discover A-vs-B differences?
2. Why map standardized CCA directions back to raw embedding coordinates?
3. Why is repeated text rank a concern?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Section 3.5, pp. 5–6; Algorithm 1 steps 13–24; Appendix E.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Trace every tensor and mapped description through Section 3.5, recording correlations and nearest concepts.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T19.


---


<a id="t19"></a>


# T19 · Combining inverse correlation and within-set relevance

**Suggested week(s):** 24  
**Prerequisite:** T17–T18  
**Primary goal:** Compute CCDiff scores, normalize within-set relevance, deduplicate concepts, and vary alpha.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

An unusual description could be uncorrelated with the opposing set simply because it is irrelevant everywhere. CCDiff's score tries to prevent such candidates from being rewarded. It blends low opposite-set correlation with how well the phrase matches its *own* image set.

## 2. What you need to know

For a candidate text $t$ with originating-set relevance $s_{c,t}$ and CCA component correlation $\rho$, the paper defines $S_{corr}=1-|\rho|$. It min-max normalizes relevance over the set-specific candidate scores to produce $S_{sim}$, then calculates $S_{CCDiff}=\alpha S_{sim}+(1-\alpha)S_{corr}$. The published experiments choose $\alpha=.3$.

This equation is a **ranking heuristic**, not a calibrated probability. A score of 0.8 does not mean a description has an 80% chance of being true. Min-max scaling can also be unstable if all candidate relevance scores are nearly equal. Multiple components can map to the same phrase; Appendix B.2 retains only its highest score.

### Source map
Section 3.6; Algorithm 1 steps 25–32; Appendix B.2.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,select_concepts
from ccdiff_edu.pipeline import inverse_cca_candidates,score_candidates
A,B,text,labels=make_shared_toy_embeddings(n=85,seed=19)
sel=select_concepts(A,text,labels,top_k=9)
proposed=inverse_cca_candidates(B,sel,n_components=4)
for alpha in [0.0,.3,.7,1.0]:
    scored=score_candidates(proposed,sel,alpha=alpha)
    print(alpha,[(x['label'],round(x['score'],3)) for x in scored[:3]])
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
for candidate in proposed[:2]:
    smin,smax=sel['relevance'].min(),sel['relevance'].max()
    sim=(candidate['relevance']-smin)/(smax-smin)
    corr=1-abs(candidate['rho'])
    computed=.3*sim+.7*corr
    print(candidate['label'],'sim',round(sim,3),'inverse',round(corr,3),
          'total',round(computed,3))
```

## 5. Independent experiment

Construct a hand-calculated two-candidate example: candidate X has similarity 1 and inverse score .2; Y has similarity .2 and inverse score 1. Determine for which values of alpha X outranks Y. Then test all-equal similarity values and decide on a safe denominator convention.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why use absolute canonical correlation?
2. Does CCDiff score represent a probability of correctness?
3. What happens at alpha=0 and alpha=1?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Section 3.6; Algorithm 1 steps 25–32; Appendix B.2.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Compute CCDiff scores, normalize within-set relevance, deduplicate concepts, and vary alpha.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T20.


---


<a id="t20"></a>


# T20 · Build the complete pedagogical CCDiff pipeline

**Suggested week(s):** 25–26  
**Prerequisite:** T01–T19  
**Primary goal:** Execute both directional comparisons, log intermediate results, and distinguish toy demonstration from official reproduction.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

We can now combine the previous ingredients into the paper's five computational steps: embed, select concepts, standardize, fit cross-set inverse CCA, and score/rank. The package implements the computation with synthetic shared-space vectors so it runs offline and students can inspect every intermediate matrix.

## 2. What you need to know

Given two image sets $D_A,D_B$ and concept bank $K$, the two directional calls are not redundant. A-vs-B discovers descriptions characteristic of A by pairing **A's selected concepts** with **B images**. B-vs-A reverses this direction. Selection uses one common bank but two independent within-set relevance scores.

The educational helper deliberately exposes details and requires no GPU. It is not the authors' official CCDiff release. A full benchmark reproduction would require verified pretrained model checkpoints, exact preprocessing, datasets, evaluation protocol, and compute. The paper reports top-k=20, alpha=.3 and ViT-bigG-14 CLIP for general images; toy examples below use smaller dimensions and concept pools.

### Source map
Algorithm 1 pp. 5–6; Sections 3.3–3.6; Section 4.1 for experiment settings.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,ccdiff_bidirectional
A,B,text,labels=make_shared_toy_embeddings(n=90,seed=20)
result=ccdiff_bidirectional(A,B,text,labels,top_k=8,n_components=4,alpha=.3)
for direction in ['A_vs_B','B_vs_A']:
    print('\n',direction)
    print('selected:',result[direction]['selection']['labels'])
    for row in result[direction]['ranked'][:4]:
        print(' ',row['label'],'CCDiff score',round(row['score'],3),
              'rho',round(row['rho'],3))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import json
summary={side:[{'label':r['label'],'score':round(r['score'],4),
                'rho':round(r['rho'],4)} for r in result[side]['ranked']]
         for side in result}
print(json.dumps(summary,indent=2))
# Unit check: a phrase cannot be output if not in the given candidate bank.
assert all(item['label'] in labels for side in summary.values() for item in side)
```

## 5. Independent experiment

Implement the five steps without calling the helper functions (you may still use numpy, StandardScaler, and scikit-learn CCA). Create a table listing intermediate array shapes. Change both groups to be identical and document what happens; this is a negative control, not a performance claim.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What is training-free about the algorithm?
2. Does a returned phrase prove that the biological feature is unique to a set?
3. What would be needed to claim faithful benchmark reproduction?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Algorithm 1 pp. 5–6; Sections 3.3–3.6; Section 4.1 for experiment settings.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Execute both directional comparisons, log intermediate results, and distinguish toy demonstration from official reproduction.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T21.


---


<a id="t21"></a>


# T21 · Benchmark metrics, baselines, and reproducibility

**Suggested week(s):** 27  
**Prerequisite:** T05, T09, T20  
**Primary goal:** Define Acc@1/Acc@5, evaluate rank lists, read paper result tables, and compare efficiency honestly.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

A research paper is evaluated by whether its numerical evidence supports its claims. CCDiff reports performance on VisDiffBench, MetaShift, and MIMIC-CXR, plus runtime and token costs. A biological scientist should read accuracy tables critically and ask: What is a successful result? How was the ground truth defined? How does evaluation differ from real clinical correctness?

## 2. What you need to know

The paper uses an automated GPT-4 judge to assign match scores of 0, 0.5, or 1 between predicted natural-language descriptions and benchmark answers. Thus its Acc@k depends on a semantic evaluator, not on exact string equality. Our offline exercise uses a deliberately simpler exact-label Acc@k to demonstrate the metric; it is **not identical to the paper's reported evaluation**.

Table 1 reports linear CCDiff Acc@1 as .96 (easy), .76 (medium), .70 (hard). Table 2 reports mean 48.6 s and zero LLM tokens for CCDiff's core discovery versus 108.2 s and 3,369 tokens for VisDiff in the reported setting. The GPT-4 benchmark evaluator and certain model-dependent data-preparation steps remain separate from that token claim.

### Source map
Tables 1–2 pp. 7–8; Section 4.1 evaluation; Appendix E stability results.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import acc_at_k,bootstrap_ci
predictions=[['elongated','bright','round'],['round','large'],
             ['bright','elongated'],['large','round']]
answers=['elongated','round','elongated','round']
for k in [1,2,3]:
    print(f'Exact-label toy Acc@{k}: {acc_at_k(predictions,answers,k):.2f}')
flags=[truth in picks[:1] for picks,truth in zip(predictions,answers)]
print('Bootstrap 95% CI:',bootstrap_ci(flags,n_boot=400))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import numpy as np
reported={'difficulty':['Easy','Medium','Hard'],
          'CCDiff Acc@1':[.96,.76,.70],
          'Best VisDiff Acc@1':[.95,.75,.61]}
for dif,ours,base in zip(*reported.values()):
    print(f'{dif}: CCDiff {ours:.2f} vs benchmark baseline {base:.2f}; difference {ours-base:+.2f}')
print('Reported wall-time ratio: ',round(108.2/48.6,2),'x')
```

## 5. Independent experiment

Write a metric adapter specification for scores in {0, .5, 1}; do not implement a fake GPT-4 evaluator. Recompute Table 1 performance gaps and discuss why point-estimate differences may not demonstrate statistical significance. Compare exact-label and meaning-based matching on five synonym examples.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Is toy exact-string Acc@1 numerically equivalent to the paper's evaluator?
2. Does zero LLM tokens in core ranking imply no language model was used anywhere?
3. Why are confidence intervals useful for method comparisons?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Tables 1–2 pp. 7–8; Section 4.1 evaluation; Appendix E stability results.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Define Acc@1/Acc@5, evaluate rank lists, read paper result tables, and compare efficiency honestly.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T22.


---


<a id="t22"></a>


# T22 · Ablations, pairing stability, and scientifically meaningful controls

**Suggested week(s):** 28  
**Prerequisite:** T05, T15–T21  
**Primary goal:** Run controlled variations of alpha, top-k, pairing, and null datasets; assess variability instead of cherry-picking.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Research-level understanding comes from changing one methodological choice at a time and asking whether the conclusions survive. CCDiff's paper includes ablations of kernels, candidate caption quality, inverse-CCA ranking, and modulo-pairing stability. Students should add null experiments that the paper's summary tables alone cannot replace.

## 2. What you need to know

A useful ablation compares configurations while holding all other variables fixed. When ranking depends on multiple stochastic or underdetermined operations, repeat runs, report uncertainty, and store seeds. The manuscript's Appendix E reports small variations across five random modulo-pairings, but this empirical observation does not prove the pairing has a statistically meaningful correspondence.

An especially informative null control sets A=B, or generates them independently from the same distribution. Any strong output under this control is evidence that the pipeline can produce apparently distinctive language without true group separation. Use direct mean image-text similarity differences as a baseline to test whether CCA adds information.

### Source map
Appendix D candidate captioner sensitivity; Appendix E kernel, ranker, and pairing ablations.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,ccdiff_bidirectional
A,B,text,labels=make_shared_toy_embeddings(n=90,seed=22)
for k in [5,8,10]:
    for alpha in [0.,.3,.7]:
        o=ccdiff_bidirectional(A,B,text,labels,top_k=k,n_components=3,alpha=alpha)
        top=o['A_vs_B']['ranked'][0]['label']
        print('k=',k,'alpha=',alpha,'top A description=',top)
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
for seed in range(8):
    out=ccdiff_bidirectional(A,B,text,labels,top_k=8,n_components=3,
                             seed=seed,shuffle=True)
    print(seed,[item['label'] for item in out['A_vs_B']['ranked'][:2]])
identical=ccdiff_bidirectional(A,A,text,labels,top_k=8,n_components=3)
print('Identical-set control top result:',identical['A_vs_B']['ranked'][0]['label'])
```

## 5. Independent experiment

Create a CSV experiment log with seed, top-k, alpha, candidate bank quality, and top-1 phrase. Calculate the fraction of trials that rank the known morphological difference first. Distinguish 'same output under random pairings' from 'demonstrated statistical validity' and propose one better paired- or unpaired-view test.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What changes in a proper one-variable ablation?
2. Why is the identical-set control important?
3. Does consistency across random modulo pairings imply semantic correctness?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Appendix D candidate captioner sensitivity; Appendix E kernel, ranker, and pairing ablations.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Run controlled variations of alpha, top-k, pairing, and null datasets; assess variability instead of cherry-picking.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T23.


---


<a id="t23"></a>


# T23 · Biomedical case study: microscopy and medical claims

**Suggested week(s):** 29  
**Prerequisite:** T04, T09, T12, T20–T22  
**Primary goal:** Construct transparent biologically motivated image-feature embeddings and separate clinical validation from model outputs.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

For biologists, the most meaningful capstone is not to repeat a flower-versus-rose benchmark. Instead, compare two collections of simulated microscopy images and ask which measurable morphology differs. We use transparent image features and manually defined concept prototype vectors to illustrate the CCDiff pipeline. Because these are not CLIP features, this is an **instructional adaptation** rather than a reproduction of the reported MIMIC-CXR experiment.

## 2. What you need to know

A biological image analysis must distinguish visible morphology from diagnostic inference. 'Round shape' is an image-level observation; 'malignant cell' is a clinical claim that would require a reference standard and domain expertise. Many biological differences also arise from slide processing, staining, instrument, or population composition.

In the manuscript, MIMIC-CXR involves credentialed radiology data, CXR-CLIP embeddings, and a BLIP captioner fine-tuned to radiology. Its reported Acc@1 values are .73, .68, .42 (easy/medium/hard). We do not provide MIMIC images, clinical instructions, or pre-trained radiology weights here. For any real clinical deployment, external validation and authorized access are necessary.

### Source map
Section 4.5 and Appendix G for clinical evaluation; Section 5 for concept coverage limits; Appendix L for societal risks.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
from ccdiff_edu import make_cell_images
images=make_cell_images(n=48,size=48,seed=23)
def morphology_features(im):
    mask=im>.35
    coords=np.argwhere(mask)
    covariance=np.cov(coords.T)
    eig=np.sort(np.linalg.eigvalsh(covariance))
    ratio=float(np.sqrt((eig[-1]+1e-8)/(eig[0]+1e-8)))
    # axes: elongation, area, intensity, roughness, symmetry, foreground fraction
    return np.array([ratio,mask.sum()/im.size,im.mean(),
                     np.mean(np.abs(np.diff(im,axis=0))),
                     1./max(ratio,1e-8),mask.mean()])
X_A=np.array([morphology_features(im) for im in images['A']])
X_B=np.array([morphology_features(im) for im in images['B']])
print('Mean features A:',X_A.mean(0).round(3))
print('Mean features B:',X_B.mean(0).round(3))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
from ccdiff_edu import ccdiff_bidirectional
from sklearn.preprocessing import StandardScaler
# Turn handcrafted features into a transparent shared coordinate system.
# Text prototypes are human-authored axis directions (NOT actual text encodings).
scaler=StandardScaler().fit(np.vstack([X_A,X_B]))
A=scaler.transform(X_A);B=scaler.transform(X_B)
concepts=['elongated morphology','round morphology','large segmented area',
          'small segmented area','bright image','dim image',
          'rough intensity','smooth intensity','low symmetry','high symmetry']
P=np.array([[1,0,0,0,0,0],[-1,0,0,0,0,0],
            [0,1,0,0,0,0],[0,-1,0,0,0,0],
            [0,0,1,0,0,0],[0,0,-1,0,0,0],
            [0,0,0,1,0,0],[0,0,0,-1,0,0],
            [0,0,0,0,-1,0],[0,0,0,0,1,0]],float)
result=ccdiff_bidirectional(A,B,P,concepts,top_k=7,n_components=3)
for direction in result:
    print(direction,[(x['label'],round(x['score'],2)) for x in result[direction]['ranked']])
```

## 5. Independent experiment

Validate the actual morphological difference with a manual or rule-based measurement (aspect ratio), not merely with the text ranker. Add a third batch with altered exposure but identical cell shapes and identify any spurious description. Design a review protocol for clinical concepts that prevents unsupported diagnostic wording.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Are handwritten text prototypes equivalent to actual CLIP encodings?
2. What additional approvals/access would be needed to use MIMIC-CXR?
3. Why does a discovered radiological difference not equal a confirmed diagnosis?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Section 4.5 and Appendix G for clinical evaluation; Section 5 for concept coverage limits; Appendix L for societal risks.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Construct transparent biologically motivated image-feature embeddings and separate clinical validation from model outputs.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T24.


---


<a id="t24"></a>


# T24 · Read, reproduce, and critically defend the paper

**Suggested week(s):** 30  
**Prerequisite:** All previous tutorials  
**Primary goal:** Explain the whole method, write a critical mini-review, articulate caveats, and design a principled extension.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

You are now at the point where you can read the CCDiff paper from start to finish. A deep understanding is not demonstrated by reciting an abstract. It is demonstrated by tracing data flow, evaluating mathematical assumptions, interpreting experimental evidence, and identifying tests that might falsify an explanation.

## 2. What you need to know

The research claim is: a relatively lightweight combination of pretrained visual–language embeddings, candidate selection, and inverse use of CCA can identify natural-language descriptions distinguishing image sets, with less LLM dependence during core difference discovery. The evidence includes VisDiffBench, MetaShift, a MIMIC-CXR benchmark, and several application studies.

A rigorous paper discussion must also ask what 'training-free' means, whether all concepts in the ranking set were generated fairly, whether arbitrary cross-set pairing induces meaningful correlations, whether reported improvements have uncertainty bounds, and whether the method exceeds simpler direct-similarity baselines. Distinguish the paper's reported point estimates from your own small-scale toy experiments. Do not claim medical correctness from unlabeled image similarity.

### Source map
Full paper, especially Sections 3–5 and Appendices A, D, E, G, L.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,ccdiff_bidirectional
A,B,Y,labels=make_shared_toy_embeddings(n=100,seed=24)
result=ccdiff_bidirectional(A,B,Y,labels,top_k=8,n_components=4,alpha=.3)
for side in result:
    print(side,[(r['label'],round(r['score'],3)) for r in result[side]['ranked'][:3]])
print('Diagnostic: number of concepts in shared bank =',len(labels))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
from ccdiff_edu import select_concepts
import numpy as np
score_A=select_concepts(A,Y,labels,top_k=len(labels))['all_relevance']
score_B=select_concepts(B,Y,labels,top_k=len(labels))['all_relevance']
print('Direct contrast baseline top A:',labels[np.argmax(score_A-score_B)])
print('Direct contrast baseline top B:',labels[np.argmax(score_B-score_A)])
print('Do the top labels match the CCA-based ranker? Judge the results, not the theory.')
```

## 5. Independent experiment

Prepare a 15-minute research-group presentation: (1) task, (2) key mathematical formulation of CCA, (3) Algorithm 1 flowchart with all tensor shapes, (4) principal reported benchmark results and their evaluator, (5) one reproduced toy experiment, (6) identical-set and pairing controls, and (7) an extension. Submit a two-page critique with a falsifiable hypothesis and a proposed experiment. Never invent unrun benchmark figures.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Can a strong result on a curated benchmark prove clinical generalization?
2. What is the paper's main algorithmic innovation?
3. What negative control would you require before trusting a set-specific description?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Full paper, especially Sections 3–5 and Appendices A, D, E, G, L.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Explain the whole method, write a critical mini-review, articulate caveats, and design a principled extension.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: the full manuscript and a research-group presentation.

