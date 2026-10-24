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
from ccdiff_edu import make_shared_toy_embeddings, select_concepts
from ccdiff_edu.pipeline import inverse_cca_candidates, score_candidates

A, B, text, labels = make_shared_toy_embeddings(n=85, seed=19)
sel = select_concepts(A, text, labels, top_k=9)
proposed = inverse_cca_candidates(B, sel, n_components=4)
for alpha in [0.0, .3, .7, 1.0]:
    scored = score_candidates(proposed, sel, alpha=alpha)
    print(alpha, [(x['label'], round(x['score'], 3)) for x in scored[:3]])
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
