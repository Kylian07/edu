# 🔎 Guided paper study: Fungal plasma membrane biology (2025)

**Publication crosswalk ID:** `S10` | **Prerequisites:** modules 01,05,09,26 | **Format:** 2 × 90-minute seminars + 1 analysis lab.

> Read the full original paper, especially methods and supplementary material. This is a structured *reading and critique tutorial*, not a claim to reproduce the exact authors' experiments.

## 1. Start from biology

**Research question:** How do spatial arrangements of complexes within a membrane bear on antifungal action?

Draw the specimen, observation method, pixel/voxel representation and the biologically relevant inferred variable. Clearly mark whether that variable is observed directly, estimated statistically, or imported as a prior.

## 2. Reconstruction of the algorithm

Map sample preparation, acquisition, reconstruction, classification, observed arrangement and biological inference as reported.

For every model component, create a table of inputs, outputs, supervision, mathematics, and estimated compute complexity. Label each assumption, and identify which mathematical terms come directly from the paper rather than your approximation.

## 3. Minimal independent numerical experiment

Run modules 01,05,09,26, then implement one *small controlled ablation* changing exactly one of: noise level, tilt range, angular heterogeneity, prompt density, training labels, representation dimensionality or domain shift. Use independent synthetic seeds for development and test.

Required figure: baseline and changed-condition plots with identical scales, plus an appropriate quantitative score.

## 4. Evaluate with the right metrics

**Evaluation target:** Independent specimen replicates and spatial quantitative uncertainty.

Draw train / validation / test and biological specimen split diagram. Identify the unit of independence (particle, tomogram, sample, imaging session). Explain how leakage could inflate the published metric.

## 5. Paper critique and failure mode

**Key issue to investigate:** Selection biases, protein identity attribution and treatment confounds.

Write a paragraph explaining what empirical test would falsify one central method claim, and a second paragraph evaluating what evidence is *not* established by the paper alone.

## 6. Biological cross-validation

Distinguish structural observation from causal effect of antifungal perturbation.

Distinguish direct biological evidence from algorithm-dependent interpretation.

## 7. Journal-club deliverables and scoring

1. Annotated forward-model diagram (20 points).
2. Equation-by-equation explanation of the paper's central objective (20 points).
3. Replicable toy experiment or method ablation with at least two random seeds (25 points).
4. Metric and leakage critique (20 points).
5. Biology-grounded next experiment (15 points).

**Paper metadata and source:** see [`../PAPER_TO_TUTORIAL_MAP.md`](../PAPER_TO_TUTORIAL_MAP.md) and locate the original manuscript from the title and the Xu Lab publication list. Verify paper version, publication year, data/code releases and supplemental methods before claiming reproduction.
