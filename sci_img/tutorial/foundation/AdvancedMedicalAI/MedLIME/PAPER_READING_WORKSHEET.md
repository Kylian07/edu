# Paper reading worksheet — MedLIME, CVPR 2026

Read the primary paper and supplement after completing Notebooks 01–11. This worksheet is a student exercise: answers should be supported by citations to paper section numbers, equations, figure numbers, and experiments.

## 1. Reconstruct the method

- Draw the input, the pretrained/reconstruction components, the trainable test-time adaptation components, the black-box classifier, the reference library, and the final saliency output. Label every arrow with a data type.
- State the mathematical input/output of Generative Masking, Supervised Test-Time Adaptation, and Evidence-Based Regularization.
- For each module, identify what needs to be pretrained, what needs labels, what is frozen, and what is optimized for a query.
- List all places where information about the test query can enter the pipeline. Which ones could produce leakage under different evaluation protocols?

## 2. Derive and inspect the objective

- Re-derive the ordinary LIME weighted least-squares objective for binary patch presence vectors.
- Write the exact evidence regularization term from the paper, *not the toy notebook*, and explain its constants.
- Explain the role of sparsity. What is the trade-off between a sparse heatmap and identifying multiple lesion regions?
- Compare the paper's formula with `fit_surrogate` in this package; list every approximation.

## 3. Design controlled comparisons

Build a table with columns `Method`, `Reconstructor`, `Adaptation`, `Reference evidence`, `True labels used at test time`, `Number of model calls`, `AUPRC`, `Uncertainty`.

At minimum compare LIME, GM only, GM+EBR, GM+STTA, full MedLIME, and at least one other explanatory baseline. Keep the classifier, patient splits, test set, and localization annotation constant where possible.

## 4. Error and uncertainty analysis

- Find three cases where reconstructed missing content obscures the actual synthetic lesion.
- Show whether the nearest-neighbor evidence can be wrong for rare or spatially unusual lesions.
- Record what happens when the number of masks is halved.
- Use paired per-image differences and bootstrap confidence intervals for localization AUPRC when the dataset is large enough.
- Distinguish the statements “saliency overlaps an annotated lesion” and “the classifier relied on that lesion to make its prediction.”

## 5. Final deliverable

Write a 4–6 page report with summary, block diagram, exact mathematical formulation, experimental design, results, error analysis, ethical limitations, and the most promising proposed extension. Include runnable code and a README with environment versions. Do not claim clinical validation or exact reproduction when using this teaching code.
