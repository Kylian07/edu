"""Simple explanation evaluation; pay attention to evaluation assumptions."""
import numpy as np


def mask_iou(pred_mask, true_mask):
    pred = np.asarray(pred_mask, dtype=bool)
    true = np.asarray(true_mask, dtype=bool)
    union = np.logical_or(pred, true).sum()
    return float(np.logical_and(pred, true).sum()/union) if union else 1.0


def pointing_game(saliency, true_mask):
    a = np.asarray(saliency)
    truth = np.asarray(true_mask, dtype=bool)
    if a.shape != truth.shape:
        raise ValueError('shape mismatch')
    return int(truth.reshape(-1)[np.argmax(a)])


def area_under_precision_recall(saliency, true_mask):
    from sklearn.metrics import average_precision_score
    s = np.asarray(saliency).reshape(-1)
    y = np.asarray(true_mask, dtype=int).reshape(-1)
    if np.unique(y).size < 2:
        return float('nan')
    return float(average_precision_score(y, s))
