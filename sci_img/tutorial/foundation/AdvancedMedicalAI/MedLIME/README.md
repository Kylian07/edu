# MedLIME Learning Track — from biology freshman to paper reader

Twelve consecutive, CPU-friendly, beginner-accessible Jupyter notebooks. Proposed destination in `xulabs/edu`:

`edu/sci_img/tutorial/MedLIME/`

**Who it is for:** first-year biology students with no prior ML or Python.

**Outcome:** understand the motivation, key terms, and mathematical ideas behind **MedLIME: A Distribution-Aligned and Evidence-Supported Framework for Medical Saliency Explanations** (Magazine, Li, and Xu, CVPR 2026), and design a careful experiment to test the proposed ideas. This track does **not** claim numerical reproduction of MedLIME or clinical validity.

## Start here

From this folder:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
jupyter notebook notebooks/
```

Open `01_medical_images_and_labels.ipynb` and select **Run All Cells**, then continue in order. Start Jupyter from the `MedLIME/` directory or its `notebooks` subdirectory to let notebooks discover `medlime_tutorials.py` automatically. No GPU, internet, downloads, authentication, or external medical datasets required *after dependencies are installed*.

**For Google Colab:** Upload this folder to your Drive and run notebooks from the directory containing `medlime_tutorials.py`, or clone your own fork of the directory. The notebooks intentionally do not assume the source repository has already been merged upstream. A single `.ipynb` uploaded alone will not find the shared library. Local Jupyter is the easiest option.

## Recommended study sequence

| # | Notebook | Weeks | Main skill | Evidence of understanding |
|---|---|---|---|---|
| 1 | Medical images, labels, and lesion localization | 1–4 | images, masks, diagnostic labels | explain why label ≠ localization |
| 2 | Pixels, filters, and image patches | 5–8 | image arrays, masking | manipulate 4×4 patch masks |
| 3 | Classification, overfitting, and neural networks | 9–16 | logistic regression, small MLP, held-out tests | train a classifier |
| 4 | Implement local interpretable explanations (LIME) | 17–20 | black-box query, local weighted regression | produce and interpret a saliency map |
| 5 | When naive image masking fails | 21–24 | distribution shift under perturbation | compare different masking fills |
| 6 | Learned masked-image reconstruction | 21–24 | self-supervised inpainting | train and audit a toy reconstructor |
| 7 | LIME with learned generative masking | 21–24 | compare GM vs baseline | compute paired AUPRC |
| 8 | Distribution shift and test-time transformations | 25–28 | intensity shifts and transforms | distinguish source and target behavior |
| 9 | Supervised test-time adaptation | 25–28 | freeze predictor, optimize affine image adjustment | audit required supervision |
| 10 | Reference cases, similarity, and evidence priors | 29–32 | kNN, kernel weights, explanation priors | generate a reference-only prior |
| 11 | Evidence-regularized local surrogates | 29–32 | L1 + evidence penalty | sweep hyperparameters |
| 12 | Capstone: integrated explanations | 33–40 | synthetic ablations and research critique | report honest AUPRC + limitations |

The recommended pace is **6–8 hours/week** including supplementary reading, debugging, and reflection. The notebooks themselves are shorter. The exit-ticket questions are intentionally left unanswered so an instructor can assess real comprehension. All exercises can be attempted by modifying the cells directly.

## Major technical and scientific distinctions

- **Generated data are not medical data.** The two-lobe synthetic examples are teaching drawings with known abnormality masks. Do not use these results for clinical conclusions.
- **Explanation vs localization:** local surrogate agreement (R²), lesion-mask overlap (AUPRC), and causal/model faithfulness are distinct properties. The notebooks do not equate them.
- **LIME is black-box:** `predict_proba` is the interface used for perturbation explanations; toy adaptation separately uses gradients through a fixed differentiable model.
- **Generative masking:** the learned model here is a tiny convolutional inpainter, **not** MedLIME's masked autoencoder; its learned reconstructions may remove lesions. Only the basic masking logic is shared.
- **Supervised test-time adaptation (STTA):** the teaching analogue optimizes brightness and contrast on a **single query using its TRUE synthetic label**, which is an optimistic supervision assumption and inappropriate for blind test evaluation. The original paper must be followed to match its supervision and architecture exactly.
- **Evidence-based regularization (EBR):** the teaching analogue uses cosine kNN over pooled intensities, a weighted prior on patch coefficients, and an L1 + L2 penalized regression. It is **not** asserted to match the paper's exact objective or reference-retrieval scheme.
- **Do not cherry-pick:** improvement is not guaranteed. At this small scale a method can be worse than baseline. Compare same query seeds, mask budgets, and properly separated reference/test pools.
- **Metrics:** AUPRC here is pixelwise average precision against synthetically known positive-lesion masks. It is undefined for lesion-negative masks, so the localization evaluations use positive cases. A full study must also handle false positives, confidence, patient-level splits, and meaningful statistical uncertainty.

## Data and environment policy

All default data are created in memory by `synthetic_image` and `dataset` in `medlime_tutorials.py`. No patient imaging data, pretrained weights, or datasets are included. No external service requests are made by the notebooks. CPU is sufficient. Files in this folder may be added to a Git repository without bringing patient data.

**To extend with real images:** use a properly licensed dataset with authentic lesion annotation; read its usage conditions; ensure patient-disjoint splits; never optimize adaptation on ground-truth test labels unless evaluating explicitly label-supervised protocols; and obtain the necessary institutional approval for non-public datasets. Potential follow-on datasets include MedMNIST for *classification* and annotated breast-ultrasound images for *localization*. PneumoniaMNIST is not a lesion-mask benchmark.

## Readings (suggested timing)

1. [PyTorch beginner tutorials](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) — after Notebook 02.
2. [Ribeiro et al. (2016), LIME](https://arxiv.org/abs/1602.04938) — with Notebook 04.
3. [He et al. (2022), Masked Autoencoders](https://arxiv.org/abs/2111.06377) — with Notebook 06.
4. [MedLIME, CVPR 2026 paper](https://openaccess.thecvf.com/content/CVPR2026/html/Magazine_MedLIME_A_Distribution-Aligned_and_Evidence-Supported_Framework_for_Medical_Saliency_Explanations_CVPR_2026_paper.html) — during Notebooks 09–12.
5. [MedLIME supplementary material](https://openaccess.thecvf.com/content/CVPR2026/supplemental/Magazine_MedLIME_A_Distribution-Aligned_CVPR_2026_supplemental.pdf) — during Notebook 12.

The source article describes **Generative Masking (GM)**, **Supervised Test-Time Adaptation (STTA)**, and **Evidence-Based Regularization (EBR)** as the three main components. To verify exact experimental configurations, read the primary paper and supplement rather than extrapolating from simplified notebook code.

## Map to the existing Xu Lab repository

Recommended connections into the existing `../../..` curriculum:
- `ComputationalSignalBase/PyTorchTensorBasic/` and `FrequencyFiltering/`: parallel references for Notebooks 01–03.
- `SpatialPerceptionAnalysis/DimensionReductionLatentSpace/` and `BioimageDenoising/`: optional prerequisites for Notebooks 05–06 and 10.
- `AdvancedMedicalAI/MedicalImageClassification/`: optional real-image classification extension.
- `../../../../../ml`: linear regression and regularization reading for Notebooks 04 and 11.

The package is an **additive folder**, so existing tutorials need not be altered or overwritten. Add a link to this folder from the parent `../../../README.md` after review.

## Validate

```bash
pytest -q tests/
python validate_notebooks.py          # run all 12 notebooks sequentially (may take minutes)
```

To modify generated notebooks, edit `generate_notebooks.py`, regenerate with `python generate_notebooks.py`, and rerun checks.

## Files

- `notebooks/*.ipynb` — lessons, code, visualizations, tasks and exit tickets.
- `medlime_tutorials.py` — self-contained, documented educational functions.
- `generate_notebooks.py` — deterministic notebook source generator.
- `tests` — unit tests for data, perturbation, fitting, retrieval, and adaptation.
- `validate_notebooks.py` — executable-notebook smoke test.
- `requirements.txt` — Python dependencies.

Educational demonstration only; not intended as a medical device or clinical AI evaluation.
