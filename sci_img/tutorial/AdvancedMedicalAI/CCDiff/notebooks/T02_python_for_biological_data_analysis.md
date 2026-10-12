# T02 · Python for biological data analysis

**Suggested week(s):** 2  
**Prerequisite:** T01  
**Primary goal:** Write loops, conditional expressions, functions, and reusable summaries of biological observations.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

Python is a tool for replacing repetitive manual calculations with transparent, reproducible instructions. The goal is not to memorize syntax: a scientist should be able to turn a measurement rule into an inspectable computation. We will use synthetic measurements rather than sensitive patient data.

## 2. What you need to know

A good function has clearly specified input, output, and assumptions. For example, to report what fraction of cells show the morphology “elongated,” we must specify the threshold and whether missing measurements are allowed. A choice such as elongation > 1.5 is an operational definition, not a biological law. If the threshold changes, the apparent fraction may change.

A reproducible script should fix random seeds for simulations, annotate units, and avoid changing the raw data in place. Try reading a Python function as if it were a laboratory protocol: what observations enter and what transformation happens?

### Source map
Introduction, pp. 1–2; programming is an instructional prerequisite, not a technique introduced in the paper.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_cell_table
cells=make_cell_table(n=30,seed=2)
values=cells['elongation'].tolist()
def count_above(xs,threshold):
    count=0
    for x in xs:
        if x>threshold:
            count += 1
    return count
print('Fraction above threshold:', count_above(values,1.5)/len(values))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
def summarize_group(df,group,threshold=1.5):
    selected=df.loc[df['condition']==group,'elongation'].dropna().tolist()
    if len(selected)==0:
        raise ValueError('No usable cells')
    return {'group':group,'n':len(selected),
            'mean':sum(selected)/len(selected),
            'fraction_elongated':count_above(selected,threshold)/len(selected)}
for condition in ['A','B']:
    print(summarize_group(cells,condition))
```

## 5. Independent experiment

Implement `fraction_above(xs, threshold)` so it returns a float. Add input validation for empty lists. Compare fractions at thresholds 1.3, 1.5, and 1.7. Explain why reporting a threshold without its definition is scientifically incomplete.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why put analysis logic in a function?
2. What happens when a denominator is zero?
3. What is the value of a fixed seed for a synthetic example?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Introduction, pp. 1–2; programming is an instructional prerequisite, not a technique introduced in the paper.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Write loops, conditional expressions, functions, and reusable summaries of biological observations.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T03.
