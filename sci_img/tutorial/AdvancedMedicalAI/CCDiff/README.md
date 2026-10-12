# CCDiff: Biology-first undergraduate tutorial track

**24 executable tutorials · 30 weeks · approximately 6–8 hours/week**

This learning package takes a first-year biology student from elementary programming to reading and critically evaluating:

> *CCDiff: Inverse Canonical Correlation Analysis for Discovering Visual Differences in Natural Language* (the 35-page NeurIPS 2026 manuscript supplied in the source conversation).

**What this package is:** a teaching pathway containing executable CPU-friendly simulations, intermediate mathematics, scientific exercises, instructor answers, and a minimal inspectable CCDiff-style pipeline. **What it is not:** the authors' official CCDiff code, a reproduced benchmark, a pretrained CLIP/BLIP release, or a diagnostic clinical system. The research manuscript is not bundled. The citation/page references are to the uploaded manuscript.

## Get started

Python 3.10+ recommended. From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate                 # Windows: .venv\Scripts\activate
pip install -e '.[notebooks,test]'
jupyter lab
```

Open `notebooks/T01_*.ipynb` and proceed in numerical order. The Markdown `.md` file beside each notebook is a searchable, low-bandwidth reading copy. The installed `ccdiff_edu` package supplies deterministic synthetic cell tables, stylized grayscale cell images, common math utilities, an offline CCDiff-style ranking implementation, and simple evaluation metrics.

If you're working without Jupyter, the Markdown versions contain every executable code snippet and can be pasted into a normal Python interpreter. `solutions/ANSWER_KEY.md` has sample answers, but **do the independent experiment first**.

## Curriculum at a glance

| Phase | Weeks | Tutorials | Capstone checkpoint |
|---|---:|---|---|
| A. Biological data and Python | 1–4 | T01–T04 | Load, quantify, and visualize biological data |
| B. Mathematical foundations | 5–10 | T05–T08 | Derive and distinguish similarity, covariance, correlation, PCA |
| C. ML and vision–language models | 11–15 | T09–T12 | Contrast sets using shared text/image-style vectors |
| D. Canonical correlation analysis | 16–21 | T13–T16 | Fit CCA and examine pairings and low-correlation directions |
| E. CCDiff's five algorithmic steps | 22–26 | T17–T20 | Implement set-specific selection, inverse CCA, and ranking |
| F. Evaluation and biomedical research | 27–30 | T21–T24 | Evaluate controls, critique assumptions, and present a capstone |

For the exact title, week and path of each lesson, see [`TUTORIAL_INDEX.json`](TUTORIAL_INDEX.json), or browse [`COURSE_MAP.md`](COURSE_MAP.md) with direct links to every tutorial.

## Crucial paper-specific ideas

1. **Set difference captioning** describes what is *more often true of a collection* rather than captioning one image.
2. **CLIP representations** place images and candidate text phrases in a comparable vector space. The paper uses ViT-bigG-14 CLIP in general-image experiments and CXR-CLIP for the medical experiment.
3. **Candidate selection** averages cosine similarities over images and selects top-*k* concepts for *each set*.
4. **Inverse CCA (the paper's terminology)** first fits *ordinary* CCA to opposing-set images and own-set candidate-text embeddings, then sorts the fitted components by ascending magnitude of canonical correlation. It is not a generic 'maximize anticorrelation' objective and is not guaranteed to identify exclusive features.
5. **Ranking** combines `S_corr = 1 - abs(rho)` with within-set similarity using `S = alpha*S_sim + (1-alpha)*S_corr`. Paper defaults include `top-k=20` and `alpha=0.3`; the small offline notebooks use smaller settings to prevent degenerate estimation and keep runtimes low.
6. **Data and pairing assumptions matter.** The paper uses modulo-based pairing of image and text embeddings without semantic one-to-one correspondence. We make students investigate shuffled pairings, null same-set controls, and direct mean-similarity baselines. Standard CCA requires row alignment for the usual interpretation of cross-covariance.
7. **Reported efficiency has a defined scope.** The paper claims no LLM token use during core difference discovery; candidate-generation models and GPT-4-based benchmark evaluation are distinct steps.

## Running checks

```bash
pytest -q
python scripts/check_notebooks.py --fast
# optional, slower: python scripts/check_notebooks.py --kernel
```

The fast checker executes **every code cell of every notebook** in an isolated Python namespace. Full `--kernel` mode additionally verifies the Jupyter execution environment and may take several minutes. Neither mode needs an API key or internet connection. It does *not* verify an exact replication of the authors' reported benchmark accuracies.

## Evaluation expectations

Students should never replace scientific evaluation with 'the model printed a plausible caption.' For each independent experiment, submit a table or plot, a measured comparison against a baseline, and one limitation. A good report can show failure: null experiments detecting spurious descriptions are valuable results.

### Optional use of real models

See [`OPTIONAL_REAL_MODELS.md`](OPTIONAL_REAL_MODELS.md) for a separately optional CLIP inference demonstration. Real model checkpoints may be large, need internet access and suitable hardware, and their image preprocessing and licensing terms must be respected. The supplied offline notebooks do not silently download these assets.

### Ethical/data limitations

The radiology experiments in the paper use MIMIC-CXR, which requires credentialed access and adherence to its license. This package contains **no patient radiographs, patient records, or clinical diagnosis model**. For first-year learners, stylized microscopy simulations provide safer and more transparent numerical ground truth. Clinical claims require domain experts and appropriate validation.

## Instructor guide

See [`INSTRUCTOR_GUIDE.md`](INSTRUCTOR_GUIDE.md) for learning objectives, weekly checkpoints, marking rubric, common misconceptions, and the suggested final project.

## Contents

```text
notebooks/               T01–T24 Jupyter notebooks and corresponding Markdown lessons
src/ccdiff_edu/          Synthetic data, baseline evaluation, inspectable toy CCDiff pipeline
solutions/ANSWER_KEY.md Answer explanations and instructor prompts
tests/                  Package unit tests
scripts/                Batch notebook execution / structural verification
TUTORIAL_INDEX.json     Machine-readable curriculum navigation
INSTRUCTOR_GUIDE.md    Assessment and teaching plan
OPTIONAL_REAL_MODELS.md Non-mandatory authentic CLIP demo
```
