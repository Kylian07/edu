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
from ccdiff_edu import make_shared_toy_embeddings, select_concepts
from ccdiff_edu.pipeline import inverse_cca_candidates

A, B, text, labels = make_shared_toy_embeddings(n=90, seed=18)
sel = select_concepts(A, text, labels, top_k=8)
proposed = inverse_cca_candidates(B, sel, n_components=4)
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
