# Merge instructions for xulabs/edu

This archive was authored as a **new additive folder** intended for `sci_img/tutorial/MedLIME/`. It has **not** been pushed to the upstream GitHub repository.

1. Clone `https://github.com/xulabs/edu` on a machine with GitHub access.
2. Copy the archive's `sci_img/tutorial/MedLIME/` folder to `edu/sci_img/tutorial/MedLIME/`.
3. From the new folder, install dependencies and run `pytest -q tests/` and `python validate_notebooks.py`.
4. Add the following link under the repository's main `../../../README.md` roadmap:

   ```markdown
   ### Paper study track — MedLIME for first-year biology students
   Twelve progressive, CPU-friendly notebooks teaching medical image labels,
   local explainability, perturbation, reconstruction, test-time adaptation,
   evidence priors, and a reproducible synthetic ablation study.
   ➜ [`MedLIME/`](MedLIME/README.md)
   ```

5. Create a feature branch, review the medical and pedagogical claims, and open a pull request.

**Scope note:** The teaching code does not implement the paper's pretrained MAE, precise test-time training scheme, or research-scale evaluation. Preserve the caveats in README and notebooks when merging.
