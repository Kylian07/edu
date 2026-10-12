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
