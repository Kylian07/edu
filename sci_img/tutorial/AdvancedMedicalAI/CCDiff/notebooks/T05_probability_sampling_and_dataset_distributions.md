# T05 · Probability, sampling, and dataset distributions

**Suggested week(s):** 5–6  
**Prerequisite:** T01–T04  
**Primary goal:** Explain sampling variability, empirical distributions, overlap, and bootstrap uncertainty.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Biologists often compare populations from a limited sample. A histogram helps us see more than a single mean. The apparent difference between sample A and sample B may fluctuate when new cells are drawn. This is the first step toward understanding *distribution shift*.

## 2. What you need to know

For observations $x_1,\ldots,x_n$, the empirical mean is $\bar x =\sum_i x_i/n$. A bootstrap repeatedly samples observations with replacement and recomputes a statistic. Its quantiles approximate how that statistic would vary under resampling assumptions. This elementary procedure will later help compare benchmark accuracy estimates and assess sensitivity to sample size.

The bootstrap is not a substitute for experimental design: if images from the same patient are correlated, independent image-level resampling can give confidence intervals that are too narrow. Biological replicates may need to be resampled as groups.

### Source map
Introduction on distribution shift; Sections 4 and 4.5; statistical background beyond paper equations.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
import numpy as np
from ccdiff_edu import make_cell_table, bootstrap_ci
cells=make_cell_table(n=60,seed=5)
a=cells.query("condition=='A'")['elongation'].to_numpy()
b=cells.query("condition=='B'")['elongation'].to_numpy()
print('Observed mean difference A - B:',round(float(a.mean()-b.mean()),3))
print('Bootstrap 95% interval A mean:',bootstrap_ci(a,n_boot=500,seed=5))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
rng=np.random.default_rng(5)
boot_diffs=[]
for _ in range(500):
    sa=rng.choice(a,len(a),replace=True)
    sb=rng.choice(b,len(b),replace=True)
    boot_diffs.append(sa.mean()-sb.mean())
print('Bootstrap 95% interval of mean difference:',np.quantile(boot_diffs,[.025,.975]))
import matplotlib.pyplot as plt
plt.hist(boot_diffs,bins=22);plt.xlabel('Resampled mean difference');plt.ylabel('Count');plt.show()
```

## 5. Independent experiment

Repeat with only 10 cells per group. Compare intervals to those from 60. Then artificially duplicate each observation ten times and re-bootstrap as if all 600 rows were independent: explain why the resulting precision is misleading.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. What does a bootstrap interval quantify?
2. Does a narrow interval prove causal significance?
3. Why can dataset construction change what differences can be found?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Introduction on distribution shift; Sections 4 and 4.5; statistical background beyond paper equations.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Explain sampling variability, empirical distributions, overlap, and bootstrap uncertainty.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T06.
