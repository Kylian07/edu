"""Pedagogical CCDiff-like implementation of Algorithm 1, Section 3.

Do not mistake this for the authors' official implementation. Differences:
- Feature vectors can be synthetic rather than CLIP embeddings.
- Modulo pairing is deterministic by default; a randomized variant is exposed.
- CCA uses scikit-learn and may be statistically unstable with tiny / repeated samples.
- Guarded standardization and min-max normalization handle degenerate examples.
- Returns diagnostic fields rather than hiding intermediate quantities.
"""
import numpy as np
from sklearn.cross_decomposition import CCA
from sklearn.preprocessing import StandardScaler


def normalize_rows(v, eps=1e-12):
    v = np.asarray(v, dtype=float)
    return v / np.maximum(np.linalg.norm(v, axis=1, keepdims=True), eps)


def select_concepts(images, concept_embeddings, labels, top_k=8):
    """Section 3.4: average cosine across an image set for every concept."""
    x = normalize_rows(images)
    y = normalize_rows(concept_embeddings)
    scores = (x @ y.T).mean(axis=0)
    ids = np.argsort(-scores, kind='stable')[:min(top_k, len(scores))]
    return {'indices':ids, 'labels':[labels[i] for i in ids],
            'embeddings':np.asarray(concept_embeddings, dtype=float)[ids],
            'relevance':scores[ids], 'all_relevance':scores}


def inverse_cca_candidates(opposing_images, own_selection, n_components=3,
                           seed=0, shuffle=False, reg_perturb=0.0):
    """Section 3.5: opposing images are paired with own-set concepts.

    CCA assumes *paired observations*. This modulo construction is heuristic:
    results must be checked against null and randomized-pairing controls.
    """
    xi = np.asarray(opposing_images, dtype=float)
    text = np.asarray(own_selection['embeddings'], dtype=float)
    if xi.ndim != 2 or text.ndim != 2 or xi.shape[1] != text.shape[1]:
        raise ValueError('Image and text embedding matrices need the same width')
    if xi.shape[0] < 4 or text.shape[0] < 3:
        raise ValueError('Use at least four images and three text concepts')
    indices = np.arange(len(xi)) % len(text)
    if shuffle:
        np.random.default_rng(seed).shuffle(indices)
    yp = text[indices]
    # The paper standardizes each original set, then pairs it. Scaling the
    # selected text pool before pairing matches this order, not pair-weighted scaling.
    scaler_x,scaler_y = StandardScaler(),StandardScaler()
    xstd=scaler_x.fit_transform(xi)
    ystd=scaler_y.fit_transform(text)[indices]
    if reg_perturb:
        rng = np.random.default_rng(seed)
        xstd += rng.normal(scale=reg_perturb, size=xstd.shape)
    n_max = min(n_components, xi.shape[1], len(xi)-1, len(text)-1)
    if n_max < 1:
        raise ValueError('Not enough nondegenerate dimensions')
    cca=CCA(n_components=n_max,max_iter=2000,scale=False)
    xp,yt=cca.fit_transform(xstd, ystd)
    # Pearson correlation of *sample-wise paired* canonical variates.
    rhos=np.array([np.corrcoef(xp[:,i],yt[:,i])[0,1] for i in range(n_max)])
    # Avoid division-by-zero if a column was constant in the candidate pool.
    rhos=np.nan_to_num(rhos,nan=0.0)
    order=np.argsort(np.abs(rhos), kind='stable')
    # Compare original text embeddings to raw-space canonical text directions.
    # CCA's y_weights_ are coefficients for standardized columns.
    # Sign is arbitrary for a canonical pair; we preserve fitted sign and expose it.
    y_std=np.where(scaler_y.scale_ < 1e-12, 1., scaler_y.scale_)
    text_normalized=normalize_rows(text)
    output=[]
    for comp in order:
        raw_direction=cca.y_weights_[:,comp] / y_std
        unit_dir=raw_direction / max(np.linalg.norm(raw_direction),1e-12)
        distances=text_normalized @ unit_dir
        j=int(np.argmax(distances))
        output.append({'label':own_selection['labels'][j], 'component':int(comp),
                       'rho':float(rhos[comp]), 'relevance':float(own_selection['relevance'][j]),
                       'cosine_to_direction':float(distances[j]), 'concept_index':j})
    return output


def score_candidates(candidates, selection, alpha=.3):
    """Section 3.6: alpha*within + (1-alpha)*(1-|rho|)."""
    if not (0 <= alpha <= 1):
        raise ValueError('alpha must be between 0 and 1')
    r=np.asarray(selection['relevance'])
    spread=float(r.max()-r.min())
    # Convention for degenerate all-equal relevance: neutral 0 rather than NaN.
    smin=float(r.min())
    items=[]
    for v in candidates:
        sim=(v['relevance']-smin)/spread if spread>1e-12 else 0.
        corr=1-abs(v['rho'])
        items.append({**v,'within_score':float(sim),'inverse_score':float(corr),
                      'score':float(alpha*sim+(1-alpha)*corr)})
    # Deduplicate keeping highest score; see Appendix B.2.
    unique={}
    for item in items:
        t=item['label']
        if t not in unique or item['score'] > unique[t]['score']:
            unique[t]=item
    return sorted(unique.values(),key=lambda d:-d['score'])


def ccdiff_direction(own_images, opposing_images, concept_embeddings,
                     labels,top_k=8,n_components=3,alpha=.3,seed=0,shuffle=False):
    selection=select_concepts(own_images,concept_embeddings,labels,top_k=top_k)
    candidate=inverse_cca_candidates(opposing_images,selection,
                n_components=n_components,seed=seed,shuffle=shuffle)
    return {'selection':selection,
            'ranked':score_candidates(candidate,selection,alpha=alpha)}


def ccdiff_bidirectional(a,b,concept_embeddings,labels,**kwargs):
    return {'A_vs_B':ccdiff_direction(a,b,concept_embeddings,labels,**kwargs),
            'B_vs_A':ccdiff_direction(b,a,concept_embeddings,labels,**kwargs)}
