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
