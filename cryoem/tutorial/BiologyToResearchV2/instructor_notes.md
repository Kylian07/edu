# Instructor and mentor notes

The intended learner is a first-year biology major. Teach from a biological question toward measurement, then computation. Each 2–3 hour notebook can be paired with a short group discussion; the code is deliberately small and synthetic so the student can change one variable without a GPU or large data transfer. For mathematical topics, require explanation of what a quantity measures before manipulating its formula.

## Required work products

| Stage | Submission | Feedback focus |
|---|---|---|
| I | Scale drawing, single-particle vs tomography workflow, averaging note. | Does the student distinguish image, map, and biological identity? |
| II | Forward-model sketch, missing-wedge drawing, picking precision/recall, FSC critique. | Are missing data and validation treated honestly? |
| III | Train/validation/test split by specimen, two-class error table, proposed molecular validation of a cluster. | Are labels and biological claims kept separate? |
| IV | Simulation-to-real test, denoising artifact control, claim–evidence table. | Can the student expose a plausible failure? |
| V–VI | Two-paper comparison and oral explanation. | Can the student connect a newer paper to the specific limitation of an older one? |

## Capstone rubric (18 points)

Score each dimension 0–3: **biological question**, **forward-model assumptions**, **reproducible computation**, **independent evaluation**, **alternative explanation**, and **next experiment**. A score of 3 requires precise evidence from a paper figure, table, methods paragraph, or executable result. A score of 2 has a correct explanation with a minor gap. A score of 1 is largely descriptive. A score of 0 is absent or incorrect. A defensible completion is at least 14/18 with no zero in independent evaluation or alternative explanation.

The capstone should compare two papers in one lineage, for example 2011 template-free detection with 2023 PNAS clustering, 2012 fast alignment with 2025 BOE-ViT, or 2018 coarse segmentation with 2024 CryoSAM. Students need not reproduce a full research model. They should reproduce a **central concept** on the synthetic data in this course or on a small public sample, then state exactly what that reproduction does and does not test.

## Common misconceptions to correct

1. A large smooth feature is not automatically biological; filtering, missing views, and averaging can make artifacts coherent.
2. “0.143 FSC” is not interchangeable with FRC or a half-bit threshold. Require a description of independent half maps, mask, local variation, and anisotropy.
3. A low pixel size does not certify high resolution. Ask for sampling and achieved-resolution evidence separately.
4. A cluster is not a protein identity. Ask what independent molecular evidence would justify naming it.
5. Accuracy from particle-level random splits can be inflated by shared specimen conditions. Require specimen-level or at least tomogram-level testing.
6. Denoising and generative completion may create plausible structures. Ask for comparison with raw data and perturbation of model settings.

## Optional advanced practical

A mentor with computing resources may add a real-data cryo-ET practical using a public tilt series and [IMOD/Etomo](https://bio3d.colorado.edu/imod/doc/etomoTutorial.html), or reuse the repository's prior specialist tomogram tutorial. Keep it optional: public tilt series can require substantial storage and local installation, while the core lessons are designed for free Colab. Give students a known-good processed example and recorded provenance if the acquisition/reconstruction step cannot be run locally.

## Maintenance

Review the [paper atlas](paper_atlas.md) once per teaching cycle against the [published CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) and [lab publication page](https://xulabs.github.io/publication/). Some 2026 entries are currently title-level and should gain direct paper links and figure-specific reading tasks when manuscripts are available. If a DOI or venue changes between preprint and publication, retain one canonical published citation and note the preprint separately.
