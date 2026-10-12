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
