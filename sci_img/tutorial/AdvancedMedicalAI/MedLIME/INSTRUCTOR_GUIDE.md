# MedLIME Learning Track — Instructor Guide

## Intended student profile

A first-year undergraduate biology major who has never completed a programming or machine-learning course. These lessons build conceptual intuition first and progressively introduce equations. Each notebook is designed for approximately one guided class meeting plus independent challenge exercises.

## Forty-week sequencing

| Weeks | Units | Suggested focus |
|---|---|---|
| 1–4 | Notebook 01 | biology examples, Python variables, image labels vs lesion annotations |
| 5–8 | Notebook 02 | pixels, array slices, Gaussian image filtering, perturbation masks |
| 9–12 | Notebook 03 first half | supervised labels, train/test splitting, logistic regression |
| 13–16 | Notebook 03 second half | PyTorch, MLPs, optimization, generalization |
| 17–20 | Notebook 04 | LIME, local surrogate, weighted regression, saliency |
| 21–22 | Notebook 05 | distribution shift from masking, counterexamples |
| 23 | Notebook 06 | self-supervised learned reconstruction, reconstruction error |
| 24 | Notebook 07 | generative masking, paired AUPRC tests |
| 25–26 | Notebook 08 | target/source shift and image transforms |
| 27–28 | Notebook 09 | supervised adaptation and label-access audit |
| 29–30 | Notebook 10 | similarity, reference libraries, evidence priors |
| 31–32 | Notebook 11 | proximal optimization, L1 penalty, prior regularization |
| 33–36 | Notebook 12 first half | integrated toy pipeline and ablation design |
| 37–40 | Notebook 12 second half | honest evaluation, paper reading, report, oral defense |

## Repeating five-part teaching pattern

1. **Biological question:** What question would a biologist or physician ask about this image?
2. **Computational experiment:** Change just one variable in the provided code.
3. **Mathematical bridge:** Explain at most one new equation per session before deriving variants.
4. **Scientific interpretation:** Distinguish predictions, local surrogate fit, lesion localization, and causal faithfulness.
5. **Exit ticket:** Write a short evidence-based answer in Markdown, not a copied definition.

## Instructor checkpoints and rubric

| Artifact | Week | What to grade |
|---|---:|---|
| Masked toy image | 8 | 25% correct code; 35% understanding masks; 40% biological interpretation |
| Learned classifier | 16 | 30% proper split; 30% training/test metrics; 40% limitations |
| From-scratch LIME | 20 | 30% correct sampling/regression; 30% local fit; 40% explanation claims |
| Masking comparison | 24 | 40% paired comparison; 30% quantitative evidence; 30% hallucination critique |
| STTA supervision audit | 28 | 40% differentiable optimization; 60% clear supervision and leakage explanation |
| Evidence regularization | 32 | 30% neighbors/prior; 30% hyperparameter ablation; 40% reliability caveats |
| Capstone | 40 | 20% reproducibility; 25% experimental controls; 25% quantitative rigor; 30% critical interpretation |

**Expected outcome:** students should be able to explain what every term in the toy local objective does and identify exactly where the educational setup differs from the paper. Avoid grading on whether the MedLIME-inspired combination always wins on toy data: it does not, and that is an intentional opportunity for scientific critique.

## Common misconceptions to correct

- A heatmap whose hot area overlaps a synthetic lesion is **not proof** that a classifier reasons causally or clinically.
- A reconstruction system can erase or invent pathology. A low missing-region MSE is not sufficient evidence of medical trustworthiness.
- A supervised test-time procedure can access information that will be unavailable for unlabeled deployment. In Notebook 09 and the capstone, the true synthetic test label is exposed deliberately; scores from that arm are not a blind test of deployment performance.
- An image-level positive label does not supply the lesion boundary required for pixel AUPRC.
- Nearest neighbors in image intensity need not be nearest neighbors in disease mechanisms.
- A high local regression R² does not guarantee correct attribution or clinical validation.

## Extensions for mathematically ready students

- Derive the gradient of the weighted quadratic local surrogate; explain the role of the intercept.
- Derive the proximal soft-threshold update for an L1 penalty and inspect the effect of scaling weights.
- Compare cosine kNN with Euclidean distance, normalized pooled features, and a pretrained embedding.
- Replace the tiny convolutional inpainter with a genuine masked autoencoder that predicts masked patch targets.
- Introduce patient-disjoint sampling, bootstrap confidence intervals, and an annotated real biomedical dataset under its proper license.
- Reproduce the **original paper's** hyperparameter and architecture details only after reviewing the paper and supplementary text.

## Suggested paper-club questions

1. Which part of MedLIME addresses unrealistic masking, which addresses adaptation, and which addresses unstable local estimates?
2. What precisely is frozen and trainable in the paper's adaptation phase, and what supervision is available?
3. What are the relevant datasets, model architectures, splits, and lesion annotations?
4. How are similarities computed for evidence support? How are priors combined?
5. What are the differences between a positive localization AUPRC and a direct test of explanation faithfulness?
6. Which ablation or negative-control experiment would most strongly challenge the key conclusion?

## Referencing the original work

- Raghav Magazine, Xingjian Li, Min Xu. *MedLIME: A Distribution-Aligned and Evidence-Supported Framework for Medical Saliency Explanations.* CVPR 2026. See the official [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Magazine_MedLIME_A_Distribution-Aligned_and_Evidence-Supported_Framework_for_Medical_Saliency_Explanations_CVPR_2026_paper.html) and [supplement](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Magazine_MedLIME_A_Distribution-Aligned_CVPR_2026_supplemental.pdf).
- Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin. *"Why Should I Trust You?" Explaining the Predictions of Any Classifier.* KDD 2016.
- Kaiming He et al. *Masked Autoencoders Are Scalable Vision Learners.* CVPR 2022.

## Integrity checklist for publication

- [ ] All notebooks run in numerical sequence in a clean environment.
- [ ] The code and explanation explicitly state all teaching approximations.
- [ ] No data or images representing identifiable patients are bundled.
- [ ] No capstone chart is presented as a MedLIME published result.
- [ ] Class materials do not imply that visually plausible saliency guarantees reliability.
