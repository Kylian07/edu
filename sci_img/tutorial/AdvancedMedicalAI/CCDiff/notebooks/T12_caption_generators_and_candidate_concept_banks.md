# T12 · Caption generators and candidate concept banks

**Suggested week(s):** 15  
**Prerequisite:** T11  
**Primary goal:** Construct, filter, and audit a shared text concept pool; explain the candidate-coverage bottleneck.

> **Learning contract.** All biological measurements and images generated here are synthetic unless explicitly stated. A pretrained CLIP model is *not* required for the offline learning sequence.

## 1. Biology-first motivation

CCDiff does not invent completely new phrases during its mathematical ranking step. It ranks descriptions from a *candidate bank*. The paper uses BLIP-2 captions by default for broad image benchmarks, but explicitly allows curated vocabulary lists. For biological scientists, curated descriptions can be more informative and more feasible to audit than unrestricted model captions.

## 2. What you need to know

A candidate bank $K$ is a list of textual descriptions. Deduplication prevents repeated or near-duplicate captions from overwhelming ranking. Domain-specific language should be validated: “high nucleus-to-cell area ratio” may be meaningful, whereas “diseased appearance” may be vague or even impossible to infer reliably from the image.

A central structural limitation is **concept coverage**: if no candidate expresses the actual biological difference, CCDiff cannot produce that wording from its fixed bank. Vocabulary construction is therefore part of experimental design, not a dispensable preprocessing detail.

### Source map
Sections 3.3 and 5 (candidate-bank creation and limitations); Appendix D caption quality.

**Reading note:** The supplied 35-page NeurIPS 2026 CCDiff manuscript is the source for all assertions about the authors' algorithm and reported experiments. Supplementary teaching mathematics and synthetic experiments are labeled as such.

## 3. Guided lab: inspect the numbers\n\nRun the next cell. Before executing, predict one numeric or visual outcome, then explain what the output means in biological or mathematical terms. Code is designed to run offline on a CPU after installing this repository.

```python
from ccdiff_edu import make_shared_toy_embeddings,select_concepts
A,B,text,labels=make_shared_toy_embeddings(n=70,seed=12)
selection=select_concepts(A,text,labels,top_k=5)
print('Shared pool size:',len(labels))
print('Selected A phrases:',selection['labels'])
print('Source relevance:',selection['relevance'].round(3))
```

## 4. Extend the example\n\nModify the prior quantities deliberately. You should always compare your modified result to the original setting and explain any difference.

```python
# Controlled experiment: the correct A descriptor is not allowed in the pool.
keep=[i for i,t in enumerate(labels) if t!='elongated cell']
modified=select_concepts(A,text[keep],[labels[i] for i in keep],top_k=5)
print('Bank without elongated cell:',modified['labels'])
print('Can the ranker output an absent phrase?', 'elongated cell' in modified['labels'])
```

## 5. Independent experiment

Prepare a 20-term bank of cell-morphology descriptions. Mark each as directly observable, ambiguous, or requiring additional clinical/biological evidence. Reproduce the missing-concept experiment and explain why a high-ranking incorrect substitute is still a methodological failure.

**Submit:** one reproducible notebook cell, one plot or small table, a short scientific interpretation, and one limitation. Explain what is known from data versus assumed.

## 6. Check your understanding

1. Why use a single shared concept pool before set-specific filtering?
2. Can inverse CCA discover a missing word sequence that is not in the bank?
3. Why must a clinical vocabulary be validated by domain experts?

Write responses before opening `solutions/ANSWER_KEY.md`.

### Connection to the research paper
Look up **Sections 3.3 and 5 (candidate-bank creation and limitations); Appendix D caption quality.** in the uploaded manuscript. Explain in two sentences how this tutorial equips you to understand or challenge that section.

## 7. What to carry forward

- You can now: Construct, filter, and audit a shared text concept pool; explain the candidate-coverage bottleneck.
- What to be cautious about: synthetic demonstrations are *not* benchmark reproduction, biological evidence, or clinical diagnosis.
- Suggested next step: T13.
