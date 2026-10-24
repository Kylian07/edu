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
