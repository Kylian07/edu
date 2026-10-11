# From biology basics to 3D U-Net

**Audience:** first-year undergraduate biology majors with no assumed coding, calculus, or machine-learning background.  
**Goal:** confidently run, modify, and interpret a small 3D U-Net before attempting the advanced MONAI spleen-segmentation tutorial.  
**Format:** eight self-contained, notebook-first lessons with synthetic, openly generated practice data.  
**Effort:** about 8–10 weeks at 3–5 hours/week, including practice and review.

> These are educational exercises, **not diagnostic tools**. All generated data are synthetic. The optional real-data loading section must use appropriately licensed, de-identified data.

## Run the notebooks

**Google Colab:** Once these files have been merged into `xulabs/edu` on the `main` branch, click a notebook path in the table below or use the links starting `https://colab.research.google.com/github/xulabs/edu/blob/main/sci_img/tutorial/BiologyTo3DUNet/`. Until then, upload a notebook from the ZIP into Colab with **File → Upload notebook**. Go through cells in order using Shift+Enter. If the Colab runtime resets, choose **Runtime → Run all**.

**Local:** With Python 3.10+:

```bash
python -m pip install -r sci_img/tutorial/BiologyTo3DUNet/requirements.txt
python -m pip install jupyterlab
jupyter lab
```

Run from a clone of this repository, or install requirements from the extracted folder if you have downloaded the ZIP separately. The first 3 lessons need NumPy and Matplotlib; lessons 4–7 also need PyTorch; lesson 8 adds MONAI. The last notebook can install MONAI automatically if internet access is available. All lessons run on CPU; GPU is optional (especially for lessons 7–8). Download and installation are the only network requirements.

## Learning route

| Week | Tutorial | Student can ... | Practice artifact |
|---|---|---|---|
| 1 | [`01_python_colab.ipynb`](01_python_colab.ipynb) | edit code, summarize cell measurements | a reusable averaging / proportion function |
| 2 | [`02_images_as_arrays.ipynb`](02_images_as_arrays.ipynb) | read an image as a NumPy array, crop, visualize | intensity histogram, threshold mask |
| 3 | [`03_biological_segmentation.ipynb`](03_biological_segmentation.ipynb) | distinguish ground truth and prediction; evaluate Dice / IoU | error map and threshold experiment |
| 4 | [`04_neural_network_basics.ipynb`](04_neural_network_basics.ipynb) | explain gradient-based learning, training vs validation | classification loss curves |
| 5 | [`05_cnn_and_unet.ipynb`](05_cnn_and_unet.ipynb) | identify convolution, pooling and skip connections | trained tiny 2D U-Net and masks |
| 6 | [`06_3d_image_fundamentals.ipynb`](06_3d_image_fundamentals.ipynb) | navigate orthogonal slices and physical voxel spacing | three-plane image and volume calculation |
| 7 | [`07_tiny_3d_unet.ipynb`](07_tiny_3d_unet.ipynb) | implement and train a 3D U-Net | validation Dice and predicted masks |
| 8–10 | [`08_guided_monai_3d.ipynb`](08_guided_monai_3d.ipynb) | run MONAI transform/training/inference workflow | held-out predictions and a real-data readiness checklist |

**Bridge to advanced existing materials:**

- [PyTorch tensor foundations](../ComputationalSignalBase/PyTorchTensorBasic/) — optional reinforcement after Notebook 02.
- [Image segmentation](../SpatialPerceptionAnalysis/ImageSegmentation/) — optional classical and deep-learning comparison after Notebook 03.
- [Simple MONAI 2D segmentation](../AdvancedMedicalAI/MedicalImageSegmentation/) — extra practice after Notebook 05.
- [3D spleen CT segmentation with MONAI](../AdvancedMedicalAI/Volume3DSegmentation/3d_medical_image_segmentation_monai.ipynb) — **advanced capstone after Notebook 08**, large real data and GPU recommended.

## Self-assessment checklist

- [ ] I can tell the difference between image intensities, reference masks and predictions.
- [ ] I can interpret `shape` for 2D `(H,W)`, 3D `(D,H,W)` and neural-network `(N,C,D,H,W)` data.
- [ ] I can calculate Dice and describe true positives, false positives and false negatives.
- [ ] I can explain loss, gradients, optimizer steps, training/validation split and overfitting.
- [ ] I can draw the U-Net encoder, decoder and skip connections.
- [ ] I can compute physical volumes using voxel spacing.
- [ ] I can train a small 3D segmentation model, look at failed predictions, and explain the limits of synthetic data.
- [ ] I can name what MONAI handles in the advanced spleen segmentation workflow.

## Teaching notes and common problems

- Each notebook is self-contained, seeded, and includes at least one exercise and executable self-check; see `TEACHING_GUIDE.md` for assessment suggestions.
- Do not interpret synthetic morphology features as statements about actual disease or cell state.
- Avoid training or evaluating on the same examples; on real data split by **patient/specimen**, not random adjacent slices or overlapping patches.
- A 3D convolution expects five dimensions `(batch, channel, depth, height, width)`; a 2D convolution expects four `(batch, channel, height, width)`.
- `Dice` of 1 means perfect overlap; inspect false positives and false negatives in addition to numerical metrics.
- If training is slow, use Colab CPU with the default small datasets; do not increase volume sizes to real CT dimensions in beginner lessons.
- For production-grade projects, data governance, annotation protocols, subject-level splitting, domain shift, reproducibility, and quantitative generalization require additional review.

## Maintainer integration

Add a link to this folder in the parent [`tutorial/README.md`](../README.md), ideally in the **Who this is for** and **Suggested Learning Paths** sections:

```markdown
| First-year biology undergraduate, no Python yet | [Biology to 3D U-Net beginner pathway](BiologyTo3DUNet/) |
```

These links become functional on GitHub after the folder has been committed. No files elsewhere in the existing repository need to be overwritten.
