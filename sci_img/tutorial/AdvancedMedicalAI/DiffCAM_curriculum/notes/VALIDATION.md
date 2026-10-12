# Verification record

The course package was created and tested on 2026-10-11.

- `python -m pytest -q tests`: **5 passed**.
- `python scripts/check_notebooks.py --structure`: **33/33 validated**.
- `python scripts/check_notebooks.py --execute`: **33/33 executed successfully** in order using a Python 3.13 CPU environment with installed dependencies.

Notebook execution was checked programmatically in a temporary kernel; we intentionally do not check generated execution outputs into the student notebooks. The notebook client issued one nonfatal asynchronous kernel-cleanup warning during automated execution, without a cell failure. Results from stochastic learning exercises can vary with library version, hardware, and seeds.

Re-run these commands after editing code or notebooks. This educational implementation is not a reproduction of DiffCAM's published benchmarks or medical validation.
