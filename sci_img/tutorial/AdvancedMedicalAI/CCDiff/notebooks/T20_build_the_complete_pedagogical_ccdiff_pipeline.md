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
