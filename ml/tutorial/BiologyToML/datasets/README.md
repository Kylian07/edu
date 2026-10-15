# Datasets shipped with BiologyToML

Three small, real, public data sets are stored here so that every notebook can use real
biology on a free Colab CPU. The notebooks read them through the toolkit loaders
(`load_golub`, `load_sachs`), which look in this folder first, then download the file from
this repository on GitHub, and, offline, fall back to a clearly labelled simulated stand-in.
Two further tables (prostate cancer, PlayTennis) are small enough to live inside
[`course_toolkit.py`](../course_toolkit.py).

All files are rebuilt from **pinned** upstream commits by [`make_datasets.py`](make_datasets.py)
(`python -m pip install rdata pandas numpy && python make_datasets.py`).

| File | Content | Used in modules |
|---|---|---|
| `golub_leukemia.csv.gz` (0.5 MB) | 72 bone-marrow/blood samples × 3,571 genes, log10 expression; columns `sample_id`, `label` (ALL/AML), `golub_split` (train/test), then one column per Affymetrix probe | 00–05, 08, 09, 11–14, 22–24 |
| `sachs_cytometry_continuous.csv.gz` (0.2 MB) | 7,466 single T cells × 11 phospho-proteins (log scale) + `intervention` | 18, 24 |
| `sachs_cytometry_discrete.csv.gz` (11 kB) | 5,400 cells × the same 11 proteins discretised into 0/1/2 (low/medium/high) + `intervention` | 16, 17, 24 |
| `sachs_consensus_edges.csv` | the 20-edge consensus signalling network (`parent`, `child`) | 15–18, 23, 24 |

## Provenance and preprocessing

**Golub et al. (1999) leukaemia data.** Source: the `golub` object of the
[datamicroarray](https://github.com/ramhiser/datamicroarray) R package, commit
`a95f6f68ed3debf48ee54f198435fa12aa655b16` (72 samples × 7,129 probes; 47 acute lymphoblastic
leukaemia, ALL, and 25 acute myeloid leukaemia, AML; the original 38/34 train/test split, 27/11
and 20/14 ALL/AML). Preprocessed exactly as in Dudoit, Fridlyand & Speed (2002): intensities
clipped to [100, 16000]; genes kept if max/min > 5 and max − min > 500 (3,571 genes); log10.

> ⚠️ Because of the clipping, the value **2.0 = log10(100) means "at or below the detection
> limit"**; about 20 % of all entries sit exactly there, and some genes are constant within one
> class. Gaussian models fitted per class (naïve Bayes, mixtures, QDA) need a small variance
> floor — Modules 08 and 13 show what goes wrong without one. The arrays are not normalised per
> sample: after standardising genes, the first principal component tracks each array's overall
> brightness (Module 14).

**Sachs et al. (2005) flow-cytometry data.** Source: the `cytometryContinuous` and
`cytometryDiscrete` objects of the [sparsebn](https://github.com/cran/sparsebn) R package,
commit `bddb679b4a71fd4927c0981c1a7c126e57ca0586`. Single-cell measurements of 11
phosphorylated proteins and phospholipids in human primary CD4⁺ T cells (raf, mek, plc = PLCγ,
pip2, pip3, erk, akt, pka, pkc, p38, jnk). The `intervention` column names the molecule that was
targeted by a perturbation (`none` = no targeted perturbation; 2,603 continuous and 1,800
discrete cells). The loaders return only the unperturbed cells by default
(`observational_only=True`). In the unperturbed discrete data, plc, pip2, pkc, p38 and jnk use
only two of the three levels; Modules 16–17 recode to the levels actually observed.

**Consensus network.** The 20 directed edges listed with the sparsebn data (also hard-coded as
`SACHS_CONSENSUS_EDGES` in the toolkit). It is a literature-curated *reference*, not an
infallible ground truth: Module 16 shows that the unperturbed data reject one of its
independence predictions.

**Prostate cancer data** (inside the toolkit as `PROSTATE_CSV`). Stamey et al. (1989), as
distributed with *The Elements of Statistical Learning* (R package
[ElemStatLearn](https://github.com/cran/ElemStatLearn), commit
`253e54016d004ac67879b594311651be3debbed4`): 97 men, 8 clinical predictors, outcome `lpsa`,
and the textbook's 67/30 train/test split. OLS on predictors standardised with all 97 men
reproduces ESL Table 3.2 (test MSE 0.521).

**PlayTennis** (inside the toolkit). Mitchell (1997), *Machine Learning*, Table 3.2 — the
decision-tree example of the 02-620 slides — plus the noisy day D15 shown on the slides.

## References

- Golub T. R. *et al.* (1999) Molecular classification of cancer: class discovery and class
  prediction by gene expression monitoring. *Science* 286:531–537.
- Dudoit S., Fridlyand J., Speed T. P. (2002) Comparison of discrimination methods for the
  classification of tumors using gene expression data. *JASA* 97:77–87.
- Sachs K., Perez O., Pe'er D., Lauffenburger D. A., Nolan G. P. (2005) Causal protein-signaling
  networks derived from multiparameter single-cell data. *Science* 308:523–529.
- Stamey T. A. *et al.* (1989) Prostate specific antigen in the diagnosis and treatment of
  adenocarcinoma of the prostate. II. Radical prostatectomy treated patients. *J Urol* 141:1076–1083.
- Hastie T., Tibshirani R., Friedman J. (2009) *The Elements of Statistical Learning*, 2nd ed. Springer.
- Mitchell T. M. (1997) *Machine Learning*. McGraw-Hill.

The data are used for research and education only, not for clinical diagnosis.
