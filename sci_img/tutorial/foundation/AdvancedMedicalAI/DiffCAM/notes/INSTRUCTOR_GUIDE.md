# Instructor guide — DiffCAM for biology students

## Course design

This is an **experiment-first, concept-before-formalism** curriculum for first-year undergraduate biology students. Use a cycle of prediction → execution → interpretation → limitation → written response. Plan about 6–8 hours weekly (guided coding: 2–3, independent work: 2–3, reading/reflection: 1–2).

Instructors should *not* use students' ability to produce attractive heatmaps as the primary evidence of understanding. Ask: which reference set, which representation, which operation, which uncertainty, and which validity claim?

## Week-by-week assessment anchors

- **Orientation, weeks 1–2:** student explains why saliency requires a defined comparison question; can distinguish a generated lesion mask from an explanation map.
- **Foundations, weeks 3–14:** independently computes data means, covariance, projections, and regularized linear solves; explains effects of scaling and covariance singularity.
- **Learning, weeks 15–23:** avoids patient leakage; trains a tiny CNN; identifies `[N,C,H,W]` feature maps and GAP embeddings `[N,C]`.
- **XAI, weeks 24–27:** implements CAM and Grad-CAM; notices they are proportional for our GAP + linear classifier architecture and predicts when this breaks.
- **DiffCAM, weeks 28–31:** derives `w ∝ (S_v + λI)^−1(z−μ)` from the Rayleigh quotient, solves numerically, and produces a reference-relative map.
- **Research practice, weeks 32–40:** independently changes cohort composition, varies reference size/ridge, and reports limitations and a falsifiable experiment.

## Five misconceptions to diagnose

1. **“A heatmap shows exactly why the AI classified an image.”** Not necessarily. DiffCAM is based on *feature differences against a reference group*; localization or plausibility does not establish causal decision faithfulness.
2. **“The reference data are merely examples for visualization.”** They mathematically determine the mean, scatter, and thus weights. Change them and the research question and result can change.
3. **“The scatter matrix is always invertible.”** Rank ≤ `N−1`; ridge is important with high-dimensional embeddings, especially small reference groups.
4. **“CAM and Grad-CAM are unrelated.”** For a linear classifier over global-average-pooled features, their normalized positive maps coincide under matching conventions; other classifiers need not satisfy this.
5. **“The synthetic medical-like images validate clinical saliency.”** Absolutely not. They check educational implementations against generated region masks, with no patient-level validity.

## Exercise coaching suggestions

### Weeks 1–6
- Ask students to change one image processing variable at a time; have them record expected/observed outcomes.
- Evaluate explanations for possible measurement artifacts and why different biological tissues need different imaging protocols.

### Weeks 7–14
- Have students sketch the feature cloud, ellipse, target-minus-mean vector, and covariance-aware direction on graph paper.
- Require a verbal explanation before equations and a matrix equation check `A @ w ≈ b` after the solve.

### Weeks 15–23
- Teach group-wise splitting of related observations as standard scientific practice, not a bonus.
- Ask why high training accuracy on synthetic morphology proves only task learning on this synthetic distribution.

### Weeks 24–34
- Clarify three claims: region overlap, sensitivity to a classifier, and reference-difference attribution. Record exactly which each evaluation supports.
- Encourage sensitivity plots with independent reference subsets, uncertainty summaries, and reproducible random seeds.

### Weeks 35–40
- Require explicit notation when reference embeddings are unnormalized scatter vs mean covariance.
- Do not replace proper external patient data governance with the generated phantom exercise.

## Mini-project grading rubric (100 points)

- Correct and reproducible code: **25**
- Question, target, reference group, and controls clearly defined: **20**
- Appropriate quantitative measurements and uncertainty: **20**
- Accurate mathematical interpretation: **20**
- Limitations, visualization choices, and scientific writing: **15**

## Capstone grading guidance

Required: a fixed training/test split, model information, reference selection criteria, exact statistic used in covariance/scatter, ridge choice, saliency post-processing convention, quantitative results, a negative control, and a failure-case discussion. Prefer a narrow result with defensible methodology over a broad but unverifiable superiority claim.

### Suggested next research questions

- How stable are maps when reference examples are sampled across experimental batches?
- Does stain normalization alter DiffCAM's target-reference direction?
- Does a reference set matched on imaging device change whether acquisition artifacts are highlighted?
- Are high-overlap heatmaps also faithful to actual model predictions?
- What is the effect of reference sample size relative to embedding dimensionality?

## Helpful external reading

Original paper: https://openaccess.thecvf.com/content/CVPR2025/html/Li_DiffCAM_Data-Driven_Saliency_Maps_by_Capturing_Feature_Differences_CVPR_2025_paper.html

Original Grad-CAM paper: https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html
