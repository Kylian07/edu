# T21 · Benchmark metrics, baselines, and reproducibility

**Suggested week(s):** 27  
**Prerequisite:** T05, T09, T20  
**Primary goal:** Define Acc@1/Acc@5, evaluate rank lists, read paper result tables, and compare efficiency honestly.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

A research paper is evaluated by whether its numerical evidence supports its claims. CCDiff reports performance on VisDiffBench, MetaShift, and MIMIC-CXR, plus runtime and token costs. A biological scientist should read accuracy tables critically and ask: What is a successful result? How was the ground truth defined? How does evaluation differ from real clinical correctness?

## 2. What you need to know

The paper uses an automated GPT-4 judge to assign match scores of 0, 0.5, or 1 between predicted natural-language descriptions and benchmark answers. Thus its Acc@k depends on a semantic evaluator, not on exact string equality. Our offline exercise uses a deliberately simpler exact-label Acc@k to demonstrate the metric; it is **not identical to the paper's reported evaluation**.

Table 1 reports linear CCDiff Acc@1 as .96 (easy), .76 (medium), .70 (hard). Table 2 reports mean 48.6 s and zero LLM tokens for CCDiff's core discovery versus 108.2 s and 3,369 tokens for VisDiff in the reported setting. The GPT-4 benchmark evaluator and certain model-dependent data-preparation steps remain separate from that token claim.

### Source map
Tables 1–2 pp. 7–8; Section 4.1 evaluation; Appendix E stability results.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import acc_at_k,bootstrap_ci
predictions=[['elongated','bright','round'],['round','large'],
             ['bright','elongated'],['large','round']]
answers=['elongated','round','elongated','round']
for k in [1,2,3]:
    print(f'Exact-label toy Acc@{k}: {acc_at_k(predictions,answers,k):.2f}')
flags=[truth in picks[:1] for picks,truth in zip(predictions,answers)]
print('Bootstrap 95% CI:',bootstrap_ci(flags,n_boot=400))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import numpy as np
reported={'difficulty':['Easy','Medium','Hard'],
          'CCDiff Acc@1':[.96,.76,.70],
          'Best VisDiff Acc@1':[.95,.75,.61]}
for dif,ours,base in zip(*reported.values()):
    print(f'{dif}: CCDiff {ours:.2f} vs benchmark baseline {base:.2f}; difference {ours-base:+.2f}')
print('Reported wall-time ratio: ',round(108.2/48.6,2),'x')
```

## 5. Independent experiment

Write a metric adapter specification for scores in {0, .5, 1}; do not implement a fake GPT-4 evaluator. Recompute Table 1 performance gaps and discuss why point-estimate differences may not demonstrate statistical significance. Compare exact-label and meaning-based matching on five synonym examples.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Is toy exact-string Acc@1 numerically equivalent to the paper's evaluator?
2. Does zero LLM tokens in core ranking imply no language model was used anywhere?
3. Why are confidence intervals useful for method comparisons?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Tables 1–2 pp. 7–8; Section 4.1 evaluation; Appendix E stability results.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Define Acc@1/Acc@5, evaluate rank lists, read paper result tables, and compare efficiency honestly.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T22.
