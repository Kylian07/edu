"""Educational DiffCAM core: target-to-reference covariance-aware direction."""
import numpy as np


def reference_scatter(references):
    refs = np.asarray(references, dtype=np.float64)
    if refs.ndim != 2 or refs.shape[0] < 2:
        raise ValueError('references must have shape (N>=2, C)')
    mu = refs.mean(axis=0)
    center = refs - mu
    return mu, center.T @ center


def diffcam_weights(target, references, ridge=1e-2, unit_norm=False):
    """Return w from (S_v + ridge I) w = target - mean(reference).

    S_v is UNNORMALIZED within-group scatter (matches the pedagogical
    derivation). Multiplying all scatter terms changes ridge's effective size.
    Use the same definition for empirical comparisons. The returned direction
    is signed; selecting ReLU/normalization is a separate visualization choice.
    This is a faithful *core direction* implementation, not a complete
    reproduction of all settings/variants in the paper.
    """
    target = np.asarray(target, dtype=np.float64).reshape(-1)
    mean, scatter = reference_scatter(references)
    if mean.shape != target.shape:
        raise ValueError('target and reference feature dimensions differ')
    if ridge <= 0:
        raise ValueError('ridge must be > 0 for stable linear solve')
    w = np.linalg.solve(scatter + float(ridge) * np.eye(target.size), target-mean)
    if unit_norm:
        w /= np.linalg.norm(w) + 1e-12
    return w


def normalize_map(saliency):
    arr = np.asarray(saliency, dtype=float)
    return (arr-arr.min())/(np.ptp(arr)+1e-12)


def diffcam_map(feature_maps, weights, positive_only=True):
    """Aggregate spatial maps of shape [C,H,W] with feature weights [C]."""
    maps = np.asarray(feature_maps, dtype=np.float64)
    w = np.asarray(weights, dtype=np.float64)
    if maps.ndim != 3 or maps.shape[0] != w.size:
        raise ValueError('expected maps [C,H,W] and matching weights [C]')
    result = np.einsum('c,chw->hw', w, maps)
    if positive_only:
        result = np.maximum(result, 0.)
    return result
