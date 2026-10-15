"""
course_toolkit.py — shared helper functions for the BiologyToML curriculum
==========================================================================

Every notebook in ``notebooks/`` is *self-contained* (it runs alone on Google
Colab), so the helpers a notebook needs are copied verbatim into its
"🧰 Course toolkit" cell.  This file is the single reference copy of those
helpers: if you fix a bug here, copy the fix into the notebooks that use the
function (``python validate_notebooks.py`` reports every copy that differs).

Conventions used everywhere in the course
-----------------------------------------
* A data set is a matrix ``X`` with **N rows = samples** (individuals, patients,
  cells) and **J columns = features** (SNPs, genes, proteins), as in the 02-620
  regression slides.  Some 02-620 decks call the number of features *n*, *K* or
  *p*; the notebooks say so whenever a slide uses a different letter.
* Genotypes are coded 0/1/2 = number of copies of one chosen allele
  (the slides' coding AA = 0, AT = 1, TT = 2).
* Class labels are ``y ∈ {0, 1}`` (0 = healthy / ALL / negative); the SVM module
  converts them to ``{−1, +1}``.
* ``log`` is the natural logarithm; entropies use ``log2`` and are in bits.
* Randomness always flows through a NumPy ``Generator`` created from ``SEED``.

Only NumPy, pandas and Matplotlib are required.  Educational code: clarity over speed.
"""
from __future__ import annotations

import io
import os
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

__version__ = "1.0"

# ── Data locations ──────────────────────────────────────────────────────────
# Real data sets live in ../datasets/ (see datasets/README.md for provenance).
# Inside a clone of xulabs/edu they are read from disk; on Colab they are
# downloaded from GitHub and cached; offline, every loader falls back to a
# clearly labelled simulated stand-in so that the notebook still runs.
REPO_DATA_URL = "https://raw.githubusercontent.com/xulabs/edu/main/ml/tutorial/BiologyToML/datasets/{name}"
CACHE_DIR = os.environ.get("BIO2ML_CACHE", "course_data")


def fetch_course_file(name: str, timeout: float = 60.0) -> str | None:
    """Return a local path to the course data file ``name``, or ``None`` if it cannot be found.

    Looks in the repository's ``datasets/`` folder first (when the notebook runs inside a
    clone of xulabs/edu), then in the download cache, and finally downloads it from GitHub.
    """
    for base in ("../datasets", "datasets", "ml/tutorial/BiologyToML/datasets", CACHE_DIR):
        path = os.path.join(base, name)
        if os.path.exists(path) and os.path.getsize(path) > 0:
            return path
    dest = os.path.join(CACHE_DIR, name)
    os.makedirs(CACHE_DIR, exist_ok=True)
    try:
        with urllib.request.urlopen(REPO_DATA_URL.format(name=name), timeout=timeout) as r, \
                open(dest + ".part", "wb") as f:
            f.write(r.read())
        os.replace(dest + ".part", dest)
        return dest
    except Exception as e:  # noqa: BLE001 — any network problem → offline fallback
        print(f"⚠️  Could not obtain {name} ({type(e).__name__}); using a simulated stand-in instead.")
        return None


# ── Small tables reproduced from the 02-620 slides and textbooks ────────────
# Prostate cancer data (Stamey et al. 1989), as used in 02-620 Lecture 2 and in
# Hastie, Tibshirani & Friedman, "The Elements of Statistical Learning", §3.2.
# 97 men; 8 clinical measurements; outcome lpsa = log(prostate-specific antigen);
# 'train' marks the textbook's 67/30 training/test split.
PROSTATE_CSV = """lcavol,lweight,age,lbph,svi,lcp,gleason,pgg45,lpsa,train
-0.579818,2.76946,50,-1.38629,0,-1.38629,6,0,-0.430783,T
-0.994252,3.31963,58,-1.38629,0,-1.38629,6,0,-0.162519,T
-0.510826,2.69124,74,-1.38629,0,-1.38629,7,20,-0.162519,T
-1.20397,3.28279,58,-1.38629,0,-1.38629,6,0,-0.162519,T
0.751416,3.43237,62,-1.38629,0,-1.38629,6,0,0.371564,T
-1.04982,3.22883,50,-1.38629,0,-1.38629,6,0,0.765468,T
0.737164,3.47352,64,0.615186,0,-1.38629,6,0,0.765468,F
0.693147,3.53951,58,1.53687,0,-1.38629,6,0,0.854415,T
-0.776529,3.53951,47,-1.38629,0,-1.38629,6,0,1.04732,F
0.223144,3.24454,63,-1.38629,0,-1.38629,6,0,1.04732,F
0.254642,3.60414,65,-1.38629,0,-1.38629,6,0,1.26695,T
-1.34707,3.59868,63,1.26695,0,-1.38629,6,0,1.26695,T
1.61343,3.02286,63,-1.38629,0,-0.597837,7,30,1.26695,T
1.47705,2.99823,67,-1.38629,0,-1.38629,7,5,1.34807,T
1.20597,3.44202,57,-1.38629,0,-0.430783,7,5,1.39872,F
1.54116,3.06105,66,-1.38629,0,-1.38629,6,0,1.44692,T
-0.415515,3.51601,70,1.24415,0,-0.597837,7,30,1.47018,T
2.28849,3.64936,66,-1.38629,0,0.371564,6,0,1.4929,T
-0.562119,3.26767,41,-1.38629,0,-1.38629,6,0,1.55814,T
0.182322,3.82538,70,1.65823,0,-1.38629,6,0,1.59939,T
1.1474,3.41936,59,-1.38629,0,-1.38629,6,0,1.639,T
2.05924,3.50104,60,1.47476,0,1.34807,7,20,1.65823,F
-0.544727,3.37588,59,-0.798508,0,-1.38629,6,0,1.69562,T
1.78171,3.45157,63,0.438255,0,1.17866,7,60,1.7138,T
0.385262,3.6674,69,1.59939,0,-1.38629,6,0,1.73166,F
1.44692,3.12457,68,0.300105,0,-1.38629,6,0,1.76644,F
0.512824,3.71965,65,-1.38629,0,-0.798508,7,70,1.80006,T
-0.400478,3.86598,67,1.81645,0,-1.38629,7,20,1.81645,F
1.04028,3.12895,67,0.223144,0,0.0487902,7,80,1.84845,T
2.40964,3.37588,65,-1.38629,0,1.61939,6,0,1.89462,T
0.285179,4.09017,65,1.96291,0,-0.798508,6,0,1.92425,T
0.182322,3.80444,65,1.70475,0,-1.38629,6,0,2.00821,F
1.27536,3.03735,71,1.26695,0,-1.38629,6,0,2.00821,T
0.00995033,3.26767,54,-1.38629,0,-1.38629,6,0,2.02155,F
-0.0100503,3.21687,63,-1.38629,0,-0.798508,6,0,2.04769,T
1.30833,4.11985,64,2.17134,0,-1.38629,7,5,2.08567,F
1.42311,3.65713,73,-0.579819,0,1.65823,8,15,2.15756,T
0.457425,2.37491,64,-1.38629,0,-1.38629,7,15,2.19165,T
2.66096,4.08514,68,1.37372,1,1.83258,7,35,2.21375,T
0.797507,3.01308,56,0.936093,0,-0.162519,7,5,2.27727,T
0.620576,3.142,60,-1.38629,0,-1.38629,9,80,2.29757,T
1.4422,3.68261,68,-1.38629,0,-1.38629,7,10,2.30757,F
0.582216,3.86598,62,1.7138,0,-0.430783,6,0,2.32728,T
1.77156,3.89691,61,-1.38629,0,0.81093,7,6,2.37491,F
1.48614,3.4095,66,1.7492,0,-0.430783,7,20,2.52172,T
1.66393,3.39283,61,0.615186,0,-1.38629,7,15,2.55334,T
2.72785,3.99545,79,1.87947,1,2.65676,9,100,2.56879,T
1.16315,4.03512,68,1.7138,0,-0.430783,7,40,2.56879,F
1.74572,3.49802,43,-1.38629,0,-1.38629,6,0,2.59152,F
1.22083,3.56812,70,1.37372,0,-0.798508,6,0,2.59152,F
1.09192,3.9936,68,-1.38629,0,-1.38629,7,50,2.65676,T
1.66013,4.23483,64,2.07317,0,-1.38629,6,0,2.67759,T
0.512824,3.63363,64,1.4929,0,0.0487902,7,70,2.68444,F
2.12704,4.12147,68,1.76644,0,1.44692,7,40,2.69124,F
3.15359,3.51601,59,-1.38629,0,-1.38629,7,5,2.70471,F
1.26695,4.28013,66,2.12226,0,-1.38629,7,15,2.718,T
0.97456,2.86505,47,-1.38629,0,0.500775,7,4,2.78809,F
0.463734,3.76468,49,1.42311,0,-1.38629,6,0,2.79423,T
0.542324,4.17823,70,0.438255,0,-1.38629,7,20,2.80639,T
1.06126,3.85121,61,1.29473,0,-1.38629,7,40,2.81241,T
0.457425,4.5245,73,2.3263,0,-1.38629,6,0,2.842,T
1.99742,3.71965,63,1.61939,1,1.90954,7,40,2.85359,F
2.77571,3.52489,72,-1.38629,0,1.55814,9,95,2.85359,T
2.03471,3.91701,66,2.00821,1,2.11021,7,60,2.882,F
2.07317,3.62301,64,-1.38629,0,-1.38629,6,0,2.882,F
1.45862,3.83622,61,1.32176,0,-0.430783,7,20,2.88759,F
2.02287,3.87847,68,1.78339,0,1.32176,7,70,2.92047,T
2.19834,4.05091,72,2.30757,0,-0.430783,7,10,2.96269,T
-0.446287,4.40855,69,-1.38629,0,-1.38629,6,0,2.96269,T
1.19392,4.78038,72,2.3263,0,-0.798508,7,5,2.97298,T
1.86408,3.59319,60,-1.38629,1,1.32176,7,60,3.01308,T
1.16002,3.34109,77,1.7492,0,-1.38629,7,25,3.03735,T
1.21491,3.82538,69,-1.38629,1,0.223144,7,20,3.05636,F
1.83896,3.23672,60,0.438255,1,1.17866,9,90,3.07501,F
2.99923,3.84908,69,-1.38629,1,1.90954,7,20,3.27526,T
3.14113,3.26385,68,-0.0512933,1,2.42037,7,50,3.33755,T
2.01089,4.43379,72,2.12226,0,0.500775,7,60,3.39283,T
2.53766,4.35478,78,2.3263,0,-1.38629,7,10,3.4356,T
2.6483,3.58213,69,-1.38629,1,2.584,7,70,3.45789,T
2.77944,3.82319,63,-1.38629,0,0.371564,7,50,3.51304,F
1.46787,3.07038,66,0.559616,0,0.223144,7,40,3.51601,T
2.51366,3.47352,57,0.438255,0,2.32728,7,60,3.53076,T
2.61301,3.88875,77,-0.527633,1,0.559616,7,30,3.5653,T
2.67759,3.83838,65,1.11514,0,1.7492,9,70,3.57094,F
1.56235,3.70991,60,1.69562,0,0.81093,7,30,3.58768,T
3.30285,3.51898,64,-1.38629,1,2.32728,7,60,3.63099,T
2.02419,3.7317,58,1.639,0,-1.38629,6,0,3.68009,T
1.73166,3.36902,62,-1.38629,1,0.300105,7,30,3.71235,T
2.80759,4.71805,65,-1.38629,1,2.46385,7,60,3.98434,T
1.56235,3.69511,76,0.936093,1,0.81093,7,75,3.9936,T
3.24649,4.10182,68,-1.38629,0,-1.38629,6,0,4.02981,T
2.5329,3.67757,61,1.34807,1,-1.38629,7,15,4.12955,T
2.83027,3.8764,68,-1.38629,1,1.32176,7,60,4.38515,T
3.821,3.89691,44,-1.38629,1,2.16905,7,40,4.68444,T
2.90745,3.39619,52,-1.38629,1,2.46385,7,10,5.14312,F
2.88256,3.77391,68,1.55814,1,1.55814,7,80,5.47751,T
3.47197,3.975,68,0.438255,1,2.90417,7,20,5.58293,F
"""


def load_prostate() -> pd.DataFrame:
    """Prostate cancer data of 02-620 Lecture 2 (97 men, 8 clinical predictors, outcome ``lpsa``)."""
    df = pd.read_csv(io.StringIO(PROSTATE_CSV))
    df["train"] = df["train"] == "T"
    return df


# PlayTennis (Mitchell, "Machine Learning", Table 3.2) — the decision-tree running example
# of 02-620 Lecture 5, plus the noisy example D15 used on the overfitting slides.
PLAY_TENNIS_ROWS = [
    ("D1", "Sunny", "Hot", "High", "Weak", "No"),
    ("D2", "Sunny", "Hot", "High", "Strong", "No"),
    ("D3", "Overcast", "Hot", "High", "Weak", "Yes"),
    ("D4", "Rain", "Mild", "High", "Weak", "Yes"),
    ("D5", "Rain", "Cool", "Normal", "Weak", "Yes"),
    ("D6", "Rain", "Cool", "Normal", "Strong", "No"),
    ("D7", "Overcast", "Cool", "Normal", "Strong", "Yes"),
    ("D8", "Sunny", "Mild", "High", "Weak", "No"),
    ("D9", "Sunny", "Cool", "Normal", "Weak", "Yes"),
    ("D10", "Rain", "Mild", "Normal", "Weak", "Yes"),
    ("D11", "Sunny", "Mild", "Normal", "Strong", "Yes"),
    ("D12", "Overcast", "Mild", "High", "Strong", "Yes"),
    ("D13", "Overcast", "Hot", "Normal", "Weak", "Yes"),
    ("D14", "Rain", "Mild", "High", "Strong", "No"),
]
PLAY_TENNIS_D15 = ("D15", "Sunny", "Hot", "Normal", "Strong", "No")


def load_play_tennis(noisy: bool = False) -> pd.DataFrame:
    """PlayTennis training data (14 days); ``noisy=True`` appends the mislabelled day D15."""
    rows = PLAY_TENNIS_ROWS + ([PLAY_TENNIS_D15] if noisy else [])
    return pd.DataFrame(rows, columns=["Day", "Outlook", "Temperature", "Humidity", "Wind", "PlayTennis"])


# The six-individual genotype table of 02-620 Lecture 3 (naïve Bayes).
# Columns: X1, X2, X3 = genotypes at three loci (0 = AA, 1 = AT, 2 = TT); Y = 1 cancer, 0 healthy.
NB_GENOTYPE_TABLE = np.array([
    [0, 0, 1, 1],
    [1, 0, 2, 1],
    [0, 2, 0, 1],
    [2, 0, 0, 0],
    [2, 1, 2, 0],
    [1, 2, 1, 0],
])

# The burglary/earthquake alarm network of 02-620 Lecture 8 (values from the slides).
# ALARM_CPTS[node][parent values] = P(node = 1 | parents); root nodes are keyed by ().
ALARM_PARENTS = {"B": (), "E": (), "A": ("B", "E"), "J": ("A",), "M": ("A",)}
ALARM_CPTS = {
    "B": {(): 0.05},
    "E": {(): 0.10},
    "A": {(1, 1): 0.95, (1, 0): 0.85, (0, 1): 0.50, (0, 0): 0.05},
    "J": {(1,): 0.70, (0,): 0.05},
    "M": {(1,): 0.80, (0,): 0.15},
}

# The two-dice hidden Markov model of 02-620 Lecture 12 (values from the slides).
DICE_HMM = {
    "states": ("A", "B"),
    "faces": (1, 2, 3, 4, 5, 6),
    "pi": np.array([0.7, 0.3]),                              # initial state probabilities
    "A": np.array([[0.8, 0.2],                               # A[i, j] = P(q_t = j | q_{t-1} = i)
                   [0.2, 0.8]]),
    "B": np.array([[0.3, 0.2, 0.2, 0.1, 0.1, 0.1],           # B[i, k] = P(o_t = face k+1 | q_t = i)
                   [0.1, 0.1, 0.1, 0.2, 0.2, 0.3]]),
}

# Consensus protein-signalling network of Sachs et al. (2005), 20 directed edges, as
# distributed with the sparsebn R package — the reference network (a literature consensus,
# not an infallible ground truth) against which Modules 15–18 and 24 score learned graphs.
SACHS_PROTEINS = ["raf", "mek", "plc", "pip2", "pip3", "erk", "akt", "pka", "pkc", "p38", "jnk"]
SACHS_CONSENSUS_EDGES = [
    ("pka", "raf"), ("pkc", "raf"), ("raf", "mek"), ("pka", "mek"), ("pkc", "mek"),
    ("pip3", "plc"), ("plc", "pip2"), ("pip3", "pip2"), ("mek", "erk"), ("pka", "erk"),
    ("pip3", "akt"), ("erk", "akt"), ("pka", "akt"), ("pkc", "pka"), ("plc", "pkc"),
    ("pip2", "pkc"), ("pka", "p38"), ("pkc", "p38"), ("pka", "jnk"), ("pkc", "jnk"),
]


# ── Real data sets with simulated fallbacks ─────────────────────────────────
def simulate_golub_like(rng: np.random.Generator) -> dict:
    """Simulated stand-in for the Golub data: 72 samples (47 'ALL', 25 'AML') × 3,571 genes.

    Log10-scale expression with gene-specific means, correlated gene modules and
    60 genes that differ between the classes.  Same keys as ``load_golub``.
    """
    n_all, n_aml, J = 47, 25, 3571
    y = np.r_[np.zeros(n_all, int), np.ones(n_aml, int)]
    base = rng.normal(2.6, 0.45, J)
    modules = rng.normal(0, 1, (len(y), 20))                  # 20 hidden "programmes"
    loading = rng.normal(0, 0.15, (20, J)) * (rng.random((20, J)) < 0.1)
    X = base + modules @ loading + rng.normal(0, 0.25, (len(y), J))
    informative = rng.choice(J, 60, replace=False)
    X[:, informative] += np.outer(y - 0.5, rng.choice([-1, 1], 60) * rng.uniform(0.4, 0.9, 60))
    is_train = np.r_[np.arange(n_all) < 27, np.arange(n_aml) < 11]
    return dict(X=X, y=y, labels=np.where(y == 1, "AML", "ALL"), genes=np.array([f"gene{j:04d}" for j in range(J)]),
                is_train=is_train, sample_id=np.arange(1, len(y) + 1), source="SIMULATED stand-in (offline)")


def load_golub() -> dict:
    """Golub et al. (1999) leukaemia expression data, preprocessed as in Dudoit et al. (2002).

    Returns a dict with ``X`` (72 × 3,571, log10 expression), ``y`` (0 = ALL, 1 = AML),
    ``labels``, ``genes`` (Affymetrix probe IDs), ``is_train`` (the original 38/34 split),
    ``sample_id`` and ``source``.  Falls back to ``simulate_golub_like`` when offline.

    Raw intensities were clipped to [100, 16000] before the log10, so the value 2.0 means
    "at or below the detection limit" (about 20 % of all entries).  Some genes are therefore
    constant within a class — per-class variance estimates need a small floor.
    """
    path = fetch_course_file("golub_leukemia.csv.gz")
    if path is None:
        return simulate_golub_like(np.random.default_rng(1999))
    df = pd.read_csv(path)
    return dict(X=df.iloc[:, 3:].to_numpy(float), y=(df["label"] == "AML").to_numpy(int),
                labels=df["label"].to_numpy(), genes=np.array(df.columns[3:]),
                is_train=(df["golub_split"] == "train").to_numpy(), sample_id=df["sample_id"].to_numpy(),
                source="Golub et al. 1999 (real data)")


def simulate_sachs_like(rng: np.random.Generator, n: int = 2603, kind: str = "continuous") -> pd.DataFrame:
    """Simulated stand-in for the Sachs data: a linear-Gaussian model on the consensus network."""
    order = ["pip3", "plc", "pip2", "pkc", "pka", "raf", "mek", "erk", "akt", "p38", "jnk"]  # topological
    parents = {p: [a for a, b in SACHS_CONSENSUS_EDGES if b == p] for p in SACHS_PROTEINS}
    data = {}
    for node in order:
        value = rng.normal(0, 1, n)
        for par in parents[node]:
            value = value + rng.choice([-1, 1]) * rng.uniform(0.4, 0.8) * data[par]
        data[node] = (value - value.mean()) / value.std()
    df = pd.DataFrame({p: data[p] for p in SACHS_PROTEINS})
    if kind == "discrete":
        df = df.apply(lambda c: pd.qcut(c, 3, labels=False)).astype(int)
    return df


def load_sachs(kind: str = "continuous", observational_only: bool = True) -> dict:
    """Sachs et al. (2005) single-cell phospho-protein measurements (flow cytometry).

    ``kind='continuous'`` gives log-scale intensities (7,466 cells), ``'discrete'`` the
    low/medium/high (0/1/2) version (5,400 cells).  With ``observational_only=True`` only
    cells without a targeted perturbation are returned.  Returns a dict with ``data``
    (DataFrame, 11 proteins), ``intervention``, ``edges`` (consensus network) and ``source``.
    """
    path = fetch_course_file(f"sachs_cytometry_{kind}.csv.gz")
    if path is None:
        df = simulate_sachs_like(np.random.default_rng(2005), kind=kind)
        ivn, source = np.array(["none"] * len(df)), "SIMULATED stand-in (offline)"
    else:
        full = pd.read_csv(path)
        df, ivn, source = full[SACHS_PROTEINS], full["intervention"].to_numpy(), "Sachs et al. 2005 (real data)"
    if observational_only:
        keep = ivn == "none"
        df, ivn = df[keep].reset_index(drop=True), ivn[keep]
    return dict(data=df, intervention=ivn, edges=list(SACHS_CONSENSUS_EDGES), source=source)


# ── Simulators ──────────────────────────────────────────────────────────────
def simulate_genotypes(rng: np.random.Generator, n_samples: int, n_snps: int, n_pops: int = 1,
                       fst: float = 0.0, maf_range=(0.05, 0.5)):
    """Simulate 0/1/2 genotypes under Hardy–Weinberg equilibrium.

    Each SNP gets an ancestral allele frequency drawn uniformly from ``maf_range``.  With
    ``n_pops > 1`` and ``fst > 0`` every population's frequency is drawn from the
    Balding–Nichols model Beta(p(1−F)/F, (1−p)(1−F)/F).  Samples are split evenly across
    populations.  Returns ``(G, pop, freqs)``: the N × J genotype matrix, the population of
    each sample and the n_pops × J matrix of population allele frequencies.

    ``G`` is stored as int8 to save memory: convert with ``G.astype(float)`` before arithmetic
    whose intermediate results can exceed 127.  A rare SNP can come out monomorphic (no
    variation) in a small sample — skip such columns in per-SNP tests.
    """
    p = rng.uniform(*maf_range, n_snps)
    if n_pops > 1 and fst > 0:
        a, b = p * (1 - fst) / fst, (1 - p) * (1 - fst) / fst
        freqs = np.clip(rng.beta(a, b, size=(n_pops, n_snps)), 0.001, 0.999)
    else:
        freqs = np.tile(p, (n_pops, 1))
    pop = np.repeat(np.arange(n_pops), int(np.ceil(n_samples / n_pops)))[:n_samples]
    G = rng.binomial(2, freqs[pop]).astype(np.int8)
    return G, pop, freqs


def simulate_quantitative_trait(rng: np.random.Generator, G: np.ndarray, n_causal: int = 5,
                                h2: float = 0.5, causal=None):
    """Simulate a quantitative phenotype y = G·β + ε with ``n_causal`` causal SNPs.

    The genetic part is scaled so that it explains a fraction ``h2`` (the heritability) of
    the phenotypic variance.  Returns ``(y, beta, causal_idx)``.
    """
    N, J = G.shape
    causal_idx = np.sort(rng.choice(J, n_causal, replace=False) if causal is None else np.asarray(causal))
    beta = np.zeros(J)
    beta[causal_idx] = rng.choice([-1, 1], len(causal_idx)) * rng.uniform(0.5, 1.0, len(causal_idx))
    g = G @ beta
    scale = np.sqrt(h2 / g.var()) if g.var() > 0 else 0.0
    beta *= scale
    y = G @ beta + rng.normal(0, np.sqrt(1 - h2), N)
    return y, beta, causal_idx


# ── Small numerical helpers ─────────────────────────────────────────────────
def sigmoid(z):
    """Logistic function 1 / (1 + e^(−z)), written via tanh so that it never overflows."""
    return 0.5 * (1.0 + np.tanh(0.5 * np.asarray(z, float)))


def logsumexp(a, axis=None):
    """log(Σ exp(a)) computed stably (subtract the maximum first)."""
    a = np.asarray(a, float)
    m = np.max(a, axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0.0)
    out = np.log(np.sum(np.exp(a - m), axis=axis, keepdims=True)) + m
    return np.squeeze(out, axis=axis) if axis is not None else out.item()


def standardize(X, mean=None, sd=None):
    """Z-score the columns of X. Pass the training mean/sd to transform test data the same way.

    Returns ``(Z, mean, sd)``; constant columns get sd = 1 so they map to 0.
    """
    X = np.asarray(X, float)
    mean = X.mean(axis=0) if mean is None else mean
    sd = X.std(axis=0) if sd is None else sd
    sd = np.where(sd > 0, sd, 1.0)
    return (X - mean) / sd, mean, sd


def train_test_indices(n: int, test_frac: float, rng: np.random.Generator, stratify=None):
    """Random train/test split of ``n`` samples; ``stratify`` keeps class proportions equal."""
    if stratify is None:
        perm = rng.permutation(n)
        n_test = int(round(test_frac * n))
        return np.sort(perm[n_test:]), np.sort(perm[:n_test])
    stratify = np.asarray(stratify)
    train, test = [], []
    for c in np.unique(stratify):
        idx = rng.permutation(np.flatnonzero(stratify == c))
        n_test = int(round(test_frac * len(idx)))
        test += list(idx[:n_test])
        train += list(idx[n_test:])
    return np.sort(train), np.sort(test)


def accuracy(y_true, y_pred) -> float:
    """Fraction of correct predictions."""
    return float(np.mean(np.asarray(y_true) == np.asarray(y_pred)))


def confusion_counts(y_true, y_pred) -> dict:
    """True/false positives/negatives for binary labels (1 = positive)."""
    y_true, y_pred = np.asarray(y_true).astype(int), np.asarray(y_pred).astype(int)
    return dict(TP=int(np.sum((y_pred == 1) & (y_true == 1))), FP=int(np.sum((y_pred == 1) & (y_true == 0))),
                FN=int(np.sum((y_pred == 0) & (y_true == 1))), TN=int(np.sum((y_pred == 0) & (y_true == 0))))


def precision_recall_f1(y_true, y_pred):
    """Precision TP/(TP+FP), recall TP/(TP+FN) and their harmonic mean F1 (0 when undefined)."""
    c = confusion_counts(y_true, y_pred)
    precision = c["TP"] / (c["TP"] + c["FP"]) if c["TP"] + c["FP"] else 0.0
    recall = c["TP"] / (c["TP"] + c["FN"]) if c["TP"] + c["FN"] else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return precision, recall, f1


def one_hot_dna(seq: str) -> np.ndarray:
    """One-hot encode a DNA string as an L × 4 array with columns A, C, G, T (N → all zeros)."""
    lookup = {"A": 0, "C": 1, "G": 2, "T": 3}
    out = np.zeros((len(seq), 4))
    for i, base in enumerate(seq.upper()):
        if base in lookup:
            out[i, lookup[base]] = 1.0
    return out


# ── Plotting ────────────────────────────────────────────────────────────────
CLASS_COLORS = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#8c564b"]


def plot_decision_regions(predict, X, y, ax=None, resolution: int = 200, title: str = "",
                          class_names=None, pad: float = 0.5):
    """Shade the regions a 2-feature classifier assigns to each class and overlay the data.

    ``predict`` maps an (M, 2) array to M integer labels 0, 1, 2, …
    """
    X, y = np.asarray(X, float), np.asarray(y).astype(int)
    ax = ax or plt.gca()
    x0, x1 = X[:, 0].min() - pad, X[:, 0].max() + pad
    y0, y1 = X[:, 1].min() - pad, X[:, 1].max() + pad
    gx, gy = np.meshgrid(np.linspace(x0, x1, resolution), np.linspace(y0, y1, resolution))
    Z = np.asarray(predict(np.c_[gx.ravel(), gy.ravel()])).astype(int).reshape(gx.shape)
    k = max(int(y.max()), int(Z.max())) + 1
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(CLASS_COLORS[:k])
    ax.contourf(gx, gy, Z, levels=np.arange(k + 1) - 0.5, cmap=cmap, alpha=0.18)
    ax.contour(gx, gy, Z, levels=np.arange(k) + 0.5, colors="k", linewidths=0.8)
    for c in range(k):
        m = y == c
        if m.any():
            ax.scatter(X[m, 0], X[m, 1], s=18, color=CLASS_COLORS[c], edgecolor="k", linewidth=0.3,
                       label=(class_names[c] if class_names is not None else f"class {c}"))
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1)
    if title:
        ax.set_title(title)
    return ax


def draw_graph(edges, pos: dict, directed: bool = True, ax=None, highlight=None, node_color: str = "#9ecae1",
               highlight_color: str = "#fdae6b", radius: float = 0.07, title: str = "", edge_labels=None):
    """Draw a small graph with Matplotlib only.

    ``edges`` is a list of (u, v) pairs, ``pos`` maps every node to (x, y) in [0, 1]².
    ``highlight`` is a set of nodes to colour differently (e.g. observed evidence).
    """
    from matplotlib.patches import Circle, FancyArrowPatch
    ax = ax or plt.gca()
    highlight = set(highlight or [])
    for i, (u, v) in enumerate(edges):
        (x0, y0), (x1, y1) = pos[u], pos[v]
        d = np.hypot(x1 - x0, y1 - y0) or 1.0
        sx, sy = x0 + (x1 - x0) * radius / d, y0 + (y1 - y0) * radius / d
        ex, ey = x1 - (x1 - x0) * radius / d, y1 - (y1 - y0) * radius / d
        ax.add_patch(FancyArrowPatch((sx, sy), (ex, ey), arrowstyle="-|>" if directed else "-",
                                     mutation_scale=12, lw=1.2, color="0.25"))
        if edge_labels is not None:
            ax.text((x0 + x1) / 2, (y0 + y1) / 2, str(edge_labels[i]), fontsize=7, color="0.2",
                    ha="center", va="center", bbox=dict(fc="white", ec="none", alpha=0.7, pad=0.5))
    for node, (x, y) in pos.items():
        ax.add_patch(Circle((x, y), radius, fc=highlight_color if node in highlight else node_color,
                            ec="0.2", lw=1, zorder=3))
        ax.text(x, y, str(node), ha="center", va="center", fontsize=9, zorder=4)
    ax.set_xlim(-0.1, 1.1); ax.set_ylim(-0.1, 1.1); ax.set_aspect("equal"); ax.axis("off")
    if title:
        ax.set_title(title)
    return ax
