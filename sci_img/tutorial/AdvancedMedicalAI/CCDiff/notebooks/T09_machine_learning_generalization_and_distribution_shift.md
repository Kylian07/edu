# T09 · Machine learning, generalization, and distribution shift

**Suggested week(s):** 11  
**Prerequisite:** T01–T08  
**Primary goal:** Train and test a simple classifier, detect leakage, and separate performance shift from explainability.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

A model that classifies cells perfectly in its original laboratory may fail on images taken with different instruments. This is a distribution shift: the statistical properties of the input population, target distribution, or their relationship differ across environments. CCDiff aims to describe such differences at the dataset level; it does not by itself fix the downstream model.

## 2. What you need to know

Supervised learning estimates a map $f(x)\rightarrow y$. A test set should mimic the intended deployment setting while being independent of training data. An evaluation can be misleading if image crops from the same biological specimen occur in both training and test sets.

For a binary phenotype label, accuracy is the fraction of correct predictions. Compare accuracy with precision, recall, and confusion matrices when groups are imbalanced. Model debugging requires distinguishing statistical association from causal explanations: discovering 'bright background' in failure images might indicate an acquisition confound rather than an intrinsic biology problem.

### Source map
Introduction pp. 1–2; Section 4.6.1 analyzes model failure groups.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_cell_table
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
cells=make_cell_table(n=90,seed=9)
X=cells[['elongation','area','nuclear_area','intensity']].to_numpy()
y=(cells.condition=='B').astype(int).to_numpy()
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.3,random_state=9,stratify=y)
model=LogisticRegression(max_iter=2000).fit(Xtr,ytr)
print('Held-out accuracy:',accuracy_score(yte,model.predict(Xte)))
print('Confusion matrix:',confusion_matrix(yte,model.predict(Xte)))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
import numpy as np
# A shifted laboratory measures an extra baseline intensity offset.
Xshift=Xte.copy(); Xshift[:,-1]+=.20
print('Original:',accuracy_score(yte,model.predict(Xte)))
print('Shifted intensity:',accuracy_score(yte,model.predict(Xshift)))
print('Most important coefficient magnitudes:',np.abs(model.coef_[0]))
```

## 5. Independent experiment

Repeat after dropping elongation and evaluate the change. Make one train/test split that deliberately duplicates observations between the sets. Write down why leakage creates overly optimistic performance and why feature drift is not always label drift.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Does detecting a shift diagnose its cause?
2. Why do we reserve data for testing?
3. What is wrong with splitting near-duplicate cell crops across train and test?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Introduction pp. 1–2; Section 4.6.1 analyzes model failure groups.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Train and test a simple classifier, detect leakage, and separate performance shift from explainability.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T10.
