# T22 · Ablations, pairing stability, and scientifically meaningful controls

**Suggested week(s):** 28  
**Prerequisite:** T05, T15–T21  
**Primary goal:** Run controlled variations of alpha, top-k, pairing, and null datasets; assess variability instead of cherry-picking.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Research-level understanding comes from changing one methodological choice at a time and asking whether the conclusions survive. CCDiff's paper includes ablations of kernels, candidate caption quality, inverse-CCA ranking, and modulo-pairing stability. Students should add null experiments that the paper's summary tables alone cannot replace.

## 2. What you need to know

A useful ablation compares configurations while holding all other variables fixed. When ranking depends on multiple stochastic or underdetermined operations, repeat runs, report uncertainty, and store seeds. The manuscript's Appendix E reports small variations across five random modulo-pairings, but this empirical observation does not prove the pairing has a statistically meaningful correspondence.

An especially informative null control sets A=B, or generates them independently from the same distribution. Any strong output under this control is evidence that the pipeline can produce apparently distinctive language without true group separation. Use direct mean image-text similarity differences as a baseline to test whether CCA adds information.

### Source map
Appendix D candidate captioner sensitivity; Appendix E kernel, ranker, and pairing ablations.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,ccdiff_bidirectional
A,B,text,labels=make_shared_toy_embeddings(n=90,seed=22)
for k in [5,8,10]:
    for alpha in [0.,.3,.7]:
        o=ccdiff_bidirectional(A,B,text,labels,top_k=k,n_components=3,alpha=alpha)
        top=o['A_vs_B']['ranked'][0]['label']
        print('k=',k,'alpha=',alpha,'top A description=',top)
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
for seed in range(8):
    out=ccdiff_bidirectional(A,B,text,labels,top_k=8,n_components=3,
                             seed=seed,shuffle=True)
    print(seed,[item['label'] for item in out['A_vs_B']['ranked'][:2]])
identical=ccdiff_bidirectional(A,A,text,labels,top_k=8,n_components=3)
print('Identical-set control top result:',identical['A_vs_B']['ranked'][0]['label'])
```

## 5. Independent experiment

Create a CSV experiment log with seed, top-k, alpha, candidate bank quality, and top-1 phrase. Calculate the fraction of trials that rank the known morphological difference first. Distinguish 'same output under random pairings' from 'demonstrated statistical validity' and propose one better paired- or unpaired-view test.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What changes in a proper one-variable ablation?
2. Why is the identical-set control important?
3. Does consistency across random modulo pairings imply semantic correctness?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Appendix D candidate captioner sensitivity; Appendix E kernel, ranker, and pairing ablations.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Run controlled variations of alpha, top-k, pairing, and null datasets; assess variability instead of cherry-picking.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T23.
