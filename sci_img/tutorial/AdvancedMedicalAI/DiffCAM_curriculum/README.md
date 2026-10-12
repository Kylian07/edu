# DiffCAM: From First-Year Biology to Explainable AI Research

**A complete, 40-week, tutorial-first course for first-year biology majors.**

The destination is the 2025 CVPR paper **DiffCAM: Data-Driven Saliency Maps by Capturing Feature Differences**, by Xingjian Li et al. The course builds from biological images and Python through linear algebra, statistics, neural networks, CAM/Grad-CAM, DiffCAM's derivation, evaluation, and an independent research capstone.

- **33 executable Jupyter tutorials** with experiments, short readings, exercises, and exit tickets.
- **Offline-first:** no external image datasets, accounts, pretrained models, or GPU needed for the main course.
- **Reproducible synthetic data:** toy cells and chest-like phantoms with known generated regions.
- **Reusable teaching code:** `diffcam_edu/` contains reference-aware saliency implementations, dataset generators, model helpers, and evaluation metrics.
- **Assessments:** mini-projects, mathematical reasoning, and a capstone with reproducible comparison.

> **Research and safety distinction:** These are educational exercises, *not* official authors' DiffCAM source code, not a reproduction of the paper's full benchmark settings, and not clinically validated software. Images and annotations are synthetic illustrations. A region highlighted by saliency is not automatically a causal feature or a diagnosis.

## Start in five minutes

Use Python 3.10+ and a clean environment:

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
# Required starting in Stage II (CNN/Grad-CAM):
python -m pip install -r requirements-torch.txt
jupyter lab
```

Open `00_orientation/01_biological_images.ipynb` first. Run each cell from top to bottom, answer the exercises, and finish the exit ticket. The notebook setup cell locates the repository root if Jupyter is started in it. You can run the earlier modules without PyTorch; advanced notebooks require CPU PyTorch (GPU is optional).

For Google Colab, upload or clone the **entire extracted folder**, install the dependencies, and change the runtime's current directory to `diffcam_curriculum` before running notebooks; uploading one notebook alone omits the helper package.

### Test your installation

```bash
python -m pytest -q tests
python scripts/check_notebooks.py --structure
# Longer: execute notebooks against your environment, stopping at the first failure
python scripts/check_notebooks.py --execute
```

## Curriculum structure

| Stage | Week(s) | Tutorials | What students learn |
|---|---|---:|---|
| Orientation | 1–2 | 2 | Biological images, salient differences, reference questions |
| Python and image analysis | 3–6 | 3 | Python, arrays, image processing |
| Linear algebra | 7–10 | 3 | Vectors, projections, matrix solving |
| Statistics | 11–14 | 3 | Distributions, covariance, regularization |
| Machine learning | 15–18 | 2 | Classification and leakage |
| Deep learning | 19–23 | 4 | Neural nets, CNNs, learned feature maps |
| Explainable AI | 24–27 | 4 | CAM, Grad-CAM, counterfactuals, evaluation |
| DiffCAM | 28–31 | 4 | Objective, proof, NumPy and PyTorch implementations |
| Evaluation | 32–34 | 3 | Reference selection, ablations, sanity checks |
| Biomedical applications | 35–37 | 3 | Region localization, frozen encoders, patch tokens |
| Research capstone | 38–40 | 2 | Comparative experiment and research report |

See [COURSE_MAP.md](COURSE_MAP.md) for an ordered, clickable listing of all 33 tutorials.

## What every notebook contains

1. The question, conceptual background, and intended learning outcome.
2. Setup and 2–3 **working examples** with visualizations or numeric experiments.
3. Two **independent exercises** designed for modifications and reflection.
4. An **exit ticket** checking conceptual understanding.
5. Follow-up links to the paper and supporting resources.

Exercise solutions are intentionally *not* filled into the student notebooks. The working experiments run without students completing the exercises. Instructors can use [notes/INSTRUCTOR_GUIDE.md](notes/INSTRUCTOR_GUIDE.md) to lead discussion and assess progress.

## Scientific center of the course

For a target feature embedding $z$, reference embeddings $\hat z_i$, reference mean $\hat\mu$, and within-reference scatter $S_v=\sum_i(\hat z_i-\hat\mu)(\hat z_i-\hat\mu)^T$, the key regularized direction is

$$
w\propto (S_v+\lambda I)^{-1}(z-\hat\mu).
$$

The teaching implementation computes this using a linear system solver, **not** explicit matrix inversion. The spatial map is a weighted sum of target feature channels, with explicit choices about signed versus positive-only attribution and display normalization. The notebook series derives the optimization, studies reference sensitivity, and connects the mathematical direction to model features.

Note that *scatter* and sample *covariance* differ by a factor of $N-1$; consequently regularization settings must be interpreted with the statistic used. The direction is only defined up to positive scaling by the Rayleigh quotient objective. We do not claim all displayed heatmaps are faithful to a model's predicted class.

## Suggested learning checkpoints

- **Week 14:** explain covariance, matrix rank, and why ridge regularization is needed.
- **Week 23:** train a small CNN and extract spatial channels and embeddings.
- **Week 27:** derive the CAM/Grad-CAM relationship and describe what each explains.
- **Week 31:** implement the DiffCAM core calculation on a learned feature extractor.
- **Week 34:** report a reference-set sensitivity study with suitable controls.
- **Week 40:** deliver a report with experimental results, ablations, limitations, and a research extension.

## Evaluation and grading

Recommended grading: **25%** guided notebooks and exit tickets, **25%** mini-projects, **20%** mathematical explanation/derivation, **30%** capstone. Reserve marks for stating what question is answered by the reference set, documenting negative controls, and recognizing the difference between localization and decision faithfulness.

## Dataset and model scope

| Artifact | Included? | What it supports |
|---|---|---|
| Synthetic cell images and known masks | Yes | CNN training, reference-aware saliency, ablations |
| Synthetic 2D cell measurements | Yes | Geometry, projections, covariance |
| Synthetic chest-like geometries | Yes | Practicing region metrics only |
| Actual chest X-rays | No | Requires separate approved access, preprocessing, annotation and patient splits |
| MNIST / ImageNet benchmarks | No | Can be added as an optional project requiring download |
| Pretrained SSL / ViT weights | No | The introductory notebooks demonstrate the concepts, not a full SSL/ViT implementation |
| Paper's official implementation | No | Teaching-only core method with documented simplifications |

## Paper and references

- [DiffCAM CVPR 2025 paper](https://openaccess.thecvf.com/content/CVPR2025/html/Li_DiffCAM_Data-Driven_Saliency_Maps_by_Capturing_Feature_Differences_CVPR_2025_paper.html)
- [DiffCAM CVPR 2025 PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_DiffCAM_Data-Driven_Saliency_Maps_by_Capturing_Feature_Differences_CVPR_2025_paper.pdf)
- [CAM (Zhou et al., CVPR 2016)](https://openaccess.thecvf.com/content_cvpr_2016/html/Zhou_Learning_Deep_Features_CVPR_2016_paper.html)
- [Grad-CAM (Selvaraju et al., ICCV 2017)](https://openaccess.thecvf.com/content_iccv_2017/html/Selvaraju_Grad-CAM_Visual_Explanations_ICCV_2017_paper.html)
- [Sanity Checks for Saliency Maps](https://arxiv.org/abs/1810.03292)
- [PyTorch tutorials](https://docs.pytorch.org/tutorials/)

## License and attribution

This independently authored teaching material is made available under the MIT License. It uses no redistributed CVPR paper figures or restricted patient data. Cite the original DiffCAM paper when discussing the method. See [LICENSE](LICENSE).
