# 🔎 Guided paper study: TopoFuse topology-aware segmentation (2026)

**Publication crosswalk ID:** `S04` | **Prerequisites:** modules 14,21,22 | **Format:** 2 × 90-minute seminars + 1 analysis lab.

> Read the full original paper, especially methods and supplementary material. This is a structured *reading and critique tutorial*, not a claim to reproduce the exact authors' experiments.

## 1. Start from biology

**Research question:** Why can high-Dice 3D segmentations still violate biologically meaningful connectivity?

Draw the specimen, observation method, pixel/voxel representation and the biologically relevant inferred variable. Clearly mark whether that variable is observed directly, estimated statistically, or imported as a prior.

## 2. Reconstruction of the algorithm

Define Betti-0 and Betti-2 for toy examples; examine sparse edit/projection versus soft topology loss from the paper.

For every model component, create a table of inputs, outputs, supervision, mathematics, and estimated compute complexity. Label each assumption, and identify which mathematical terms come directly from the paper rather than your approximation.

## 3. Minimal independent numerical experiment

Run modules 14,21,22, then implement one *small controlled ablation* changing exactly one of: noise level, tilt range, angular heterogeneity, prompt density, training labels, representation dimensionality or domain shift. Use independent synthetic seeds for development and test.

Required figure: baseline and changed-condition plots with identical scales, plus an appropriate quantitative score.

## 4. Evaluate with the right metrics

**Evaluation target:** Dice, Betti-error, topological validity, edit fraction and runtime.

Draw train / validation / test and biological specimen split diagram. Identify the unit of independence (particle, tomogram, sample, imaging session). Explain how leakage could inflate the published metric.

## 5. Paper critique and failure mode

**Key issue to investigate:** Changes to relevant biological holes, downsampled topology approximations, failed repair certificate.

Write a paragraph explaining what empirical test would falsify one central method claim, and a second paragraph evaluating what evidence is *not* established by the paper alone.

## 6. Biological cross-validation

Verify continuous membranes and cavities with expert review.

Distinguish direct biological evidence from algorithm-dependent interpretation.

## 7. Journal-club deliverables and scoring

1. Annotated forward-model diagram (20 points).
2. Equation-by-equation explanation of the paper's central objective (20 points).
3. Replicable toy experiment or method ablation with at least two random seeds (25 points).
4. Metric and leakage critique (20 points).
5. Biology-grounded next experiment (15 points).

**Paper metadata and source:** see [`../PAPER_TO_TUTORIAL_MAP.md`](../PAPER_TO_TUTORIAL_MAP.md) and locate the original manuscript from the title and the Xu Lab publication list. Verify paper version, publication year, data/code releases and supplemental methods before claiming reproduction.
