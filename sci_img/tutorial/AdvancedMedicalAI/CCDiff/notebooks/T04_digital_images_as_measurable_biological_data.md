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
