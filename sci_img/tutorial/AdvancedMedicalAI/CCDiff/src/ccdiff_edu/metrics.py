"""Simple evaluation helpers. Dataset-specific paper eval uses an LLM judge instead."""
import numpy as np

def acc_at_k(predicted_lists,ground_truth, k=1):
    """Literal exact-label retrieval Acc@k, for educational toy exercises only."""
    if len(predicted_lists)!=len(ground_truth) or not ground_truth:
        raise ValueError('predictions/ground-truth must be equally long and nonempty')
    return float(np.mean([truth in predictions[:k] for predictions,truth in
                           zip(predicted_lists,ground_truth)]))

def bootstrap_ci(samples,stat=np.mean,n_boot=1000,seed=7):
    x=np.asarray(samples)
    if len(x)==0:
        raise ValueError('empty input')
    rng=np.random.default_rng(seed)
    estimates=[stat(x[rng.integers(0,len(x),size=len(x))]) for _ in range(n_boot)]
    return tuple(float(v) for v in np.percentile(estimates,[2.5,97.5]))
