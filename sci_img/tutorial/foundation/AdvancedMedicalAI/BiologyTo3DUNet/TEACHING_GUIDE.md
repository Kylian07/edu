# Teaching guide: 3D U-Net for first-year biology majors

## Classroom use

- **Format:** 15-minute concept demonstration, 25–45-minute guided notebook, 15-minute discussion and exit ticket. Students should submit a figure plus 2–4 sentences explaining what it shows.
- **Do not require calculus:** gradients are introduced operationally. Students can understand optimization without deriving backpropagation.
- **Scaffolding:** in early weeks pair-program the first exercise; in later weeks ask students to predict tensor shapes before executing code.
- **Access:** every default example generates its own data offline. GPU acceleration is optional; the MONAI dependency needs installation if absent.

## Exit tickets by notebook

| Notebook | One question to ask | Expected answer |
|---|---|---|
| 01 | Why is `len(values)` necessary? | It gives sample count; mean divides sum by count (and empty lists need care). |
| 02 | Does intensity represent physical cell volume? | No, intensity and volume are distinct and require calibration. |
| 03 | What does a false negative mean? | A real reference foreground pixel was omitted by the prediction. |
| 04 | Why normalize using training data only? | To avoid leaking information from the validation/test data. |
| 05 | What is a U-Net skip connection? | It combines high-resolution encoder features with decoder features. |
| 06 | Why does Z spacing affect physical volume? | Each voxel has a physical extent; voxel count alone omits spacing. |
| 07 | Why is model output `(N,1,D,H,W)`? | One foreground logit for every voxel in every input volume. |
| 08 | Why not deploy the synthetic model on CT? | Its training distribution is not representative of CT and has no real-data validation. |

## Suggested assessments

1. **Code execution (30%)**: run all required cells and pass included assertions.
2. **Figures and measurement (30%)**: submit one annotated figure or metric from the notebook.
3. **Scientific interpretation (30%)**: correctly explain limits, errors, and relevant units.
4. **Experiment design (10%)**: propose one controlled parameter change with an untouched validation split.

## Debugging guide

- `ModuleNotFoundError`: install `requirements.txt` in the same Jupyter kernel, or switch to Colab. The last notebook automatically installs MONAI when needed.
- Runtime too slow: leave the provided batch size and dataset size; use CPU or Colab GPU if available. Restart and run all if you change model architecture or tensor dimensions.
- `Expected 5D tensor`: add batch and channel axes (not extra spatial dimensions).
- U-Net concatenation shape error: input spatial dimensions must be divisible by the downsampling factor (2 in Notebooks 05/07, 4 in Notebook 08).
- Validation Dice low: inspect probability plots, training loss, class imbalance and thresholds. A low result is an investigation prompt, not a software error by itself.
- Missing NIfTI image: `USE_REAL_PAIR=False` keeps the default notebook fully self-contained; real data are optional and should be de-identified and authorized.

## Advanced project handoff

Ask a student to describe three changes required for a real volumetric segmentation project: (1) appropriate sample/specimen-level data splits and reliable labels, (2) metadata-aware orientation, spacing and intensity transforms, and (3) patch-based training, sliding-window inference, validation and error analysis. Send them to the existing `../AdvancedMedicalAI/Volume3DSegmentation/3d_medical_image_segmentation_monai.ipynb` once they can explain the above.
