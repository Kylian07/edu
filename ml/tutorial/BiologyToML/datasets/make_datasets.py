#!/usr/bin/env python3
"""Rebuild the small real datasets shipped with the BiologyToML course.

    python -m pip install rdata pandas numpy
    python make_datasets.py            # writes the files next to this script

Every source is downloaded from a *pinned commit* so that the files are reproducible
byte-for-byte. The notebooks never need this script: they read the files written here
(or download them from the xulabs/edu repository) and fall back to simulated stand-ins
when offline.

Files written
-------------
golub_leukemia.csv.gz          72 bone-marrow/blood samples x 3,571 genes (log10 expression),
                               ALL/AML label, the original 38/34 train/test split.
sachs_cytometry_continuous.csv.gz
                               7,466 single cells x 11 phospho-proteins (log scale) +
                               the perturbation each cell received.
sachs_cytometry_discrete.csv.gz
                               5,400 cells x 11 proteins discretised into low/medium/high (0/1/2).
sachs_consensus_edges.csv      the 20-edge consensus signalling network used as "ground truth".
"""
from __future__ import annotations

import io
import os
import urllib.request

import numpy as np
import pandas as pd
import rdata

HERE = os.path.dirname(os.path.abspath(__file__))

# ── pinned sources ──
GOLUB_URL = ("https://raw.githubusercontent.com/ramhiser/datamicroarray/"
             "a95f6f68ed3debf48ee54f198435fa12aa655b16/data/golub.RData")
SACHS_URL = ("https://raw.githubusercontent.com/cran/sparsebn/"
             "bddb679b4a71fd4927c0981c1a7c126e57ca0586/data/{name}.rda")
PROTEINS = ["raf", "mek", "plc", "pip2", "pip3", "erk", "akt", "pka", "pkc", "p38", "jnk"]


def _read_rda(url: str) -> dict:
    """Download an .rda/.RData file and parse it with the pure-Python ``rdata`` package."""
    with urllib.request.urlopen(url, timeout=120) as r:
        raw = r.read()
    path = os.path.join(HERE, "_tmp.rda")
    with open(path, "wb") as f:
        f.write(raw)
    try:
        return rdata.read_rda(path)
    finally:
        os.remove(path)


def make_golub() -> None:
    """Golub et al. (1999) leukemia data, preprocessed as in Dudoit, Fridlyand & Speed (2002):
    floor 100, ceiling 16,000; keep genes with max/min > 5 and max - min > 500; log10."""
    g = _read_rda(GOLUB_URL)
    x = g["golub"]["x"]
    X = np.asarray(x, float)
    samples = [str(s) for s in x.coords["dim_0"].values]
    genes = [str(s) for s in x.coords["dim_1"].values]
    labels = np.asarray(list(g["golub"]["y"]))
    train_ids = {str(s) for s in g["golub_train"]["x"].coords["dim_0"].values}
    Xc = np.clip(X, 100, 16000)
    keep = (Xc.max(0) / Xc.min(0) > 5) & (Xc.max(0) - Xc.min(0) > 500)
    L = np.round(np.log10(Xc[:, keep]), 4)
    df = pd.DataFrame(L, columns=[gn for gn, k in zip(genes, keep) if k])
    df.insert(0, "golub_split", ["train" if s in train_ids else "test" for s in samples])
    df.insert(0, "label", labels)
    df.insert(0, "sample_id", samples)
    df = df.sort_values("sample_id", key=lambda s: s.astype(int)).reset_index(drop=True)
    df.to_csv(os.path.join(HERE, "golub_leukemia.csv.gz"), index=False, compression="gzip")
    print(f"golub_leukemia.csv.gz: {df.shape[0]} samples x {keep.sum()} genes "
          f"({(labels == 'ALL').sum()} ALL / {(labels == 'AML').sum()} AML)")


def make_sachs() -> None:
    """Sachs et al. (2005) flow-cytometry signalling data as distributed with the sparsebn R package."""
    for kind in ("continuous", "discrete"):
        d = _read_rda(SACHS_URL.format(name="cytometry" + kind.capitalize()))
        obj = list(d.values())[0]
        df = obj["data"].copy()
        df.columns = PROTEINS
        ivn = ["none" if (i is None or len(i) == 0) else ",".join(map(str, i)) for i in obj["ivn"]]
        df["intervention"] = ivn
        if kind == "continuous":
            df[PROTEINS] = df[PROTEINS].astype(float).round(4)
        else:
            df[PROTEINS] = df[PROTEINS].astype(int)
        df.to_csv(os.path.join(HERE, f"sachs_cytometry_{kind}.csv.gz"), index=False, compression="gzip")
        print(f"sachs_cytometry_{kind}.csv.gz: {df.shape[0]} cells x {len(PROTEINS)} proteins; "
              f"interventions {df['intervention'].value_counts().to_dict()}")
        if kind == "continuous":
            rows = []
            for child, parents in obj["dag"].items():
                for p in np.atleast_1d(parents):
                    rows.append((PROTEINS[int(p) - 1], str(child)))
            edges = pd.DataFrame(rows, columns=["parent", "child"])
            edges.to_csv(os.path.join(HERE, "sachs_consensus_edges.csv"), index=False)
            print(f"sachs_consensus_edges.csv: {len(edges)} directed edges")


if __name__ == "__main__":
    make_golub()
    make_sachs()
