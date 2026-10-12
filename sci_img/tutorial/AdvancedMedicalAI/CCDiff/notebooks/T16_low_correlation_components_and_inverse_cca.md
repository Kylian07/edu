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
