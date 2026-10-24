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
