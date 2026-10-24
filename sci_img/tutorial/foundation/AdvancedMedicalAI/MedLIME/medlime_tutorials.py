"""CPU-friendly teaching utilities for a MedLIME-inspired learning track.

All images are synthetic (not medical data). Functions are intentionally small and
transparent, not research-grade or faithful implementations of the original paper.
"""
from dataclasses import dataclass
import numpy as np
from scipy.ndimage import gaussian_filter, uniform_filter
from sklearn.metrics import average_precision_score
import torch
from torch import nn
import torch.nn.functional as F

torch.set_num_threads(min(2, torch.get_num_threads()))
SIDE = 32
GRID = 4


def synthetic_image(seed=0, lesion=True, artifact=False):
    """A grayscale two-lobe *illustration* with an optional synthetic spot.

    Returns (image float32 32x32, lesion_mask bool 32x32). The shape is not
    anatomically realistic and must never be used as clinical evidence.
    """
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[:SIDE, :SIDE]
    left = ((xx - 11.5) / 6.0)**2 + ((yy-16)/10)**2 < 1
    right = ((xx - 20.5) / 6.0)**2 + ((yy-16)/10)**2 < 1
    body = ((xx-16)/14)**2 + ((yy-16)/15)**2 < 1
    image = np.full((SIDE, SIDE), 0.07, np.float32)
    image[body] = 0.36
    image[left | right] = 0.22
    image += (0.018 * rng.normal(size=image.shape)).astype(np.float32)
    mask = np.zeros_like(image, bool)
    if lesion:
        cx = int(rng.choice([10, 11, 12, 20, 21, 22]))
        cy = int(rng.integers(11, 22))
        mask = (xx-cx)**2 + (yy-cy)**2 <= int(rng.choice([4, 9]))
        image[mask] += 0.60
    if artifact:
        image[1:5, 1:5] = 0.96  # spurious bright scanner/label artifact
    return np.clip(image, 0, 1).astype('float32'), mask


def dataset(n=100, seed=0, positive_fraction=0.5, artifact=False):
    rng = np.random.default_rng(seed)
    images, labels, masks = [], [], []
    for _ in range(n):
        y = int(rng.random() < positive_fraction)
        x, m = synthetic_image(int(rng.integers(1, 2**30)), bool(y), artifact=artifact)
        images.append(x); labels.append(y); masks.append(m)
    return np.stack(images), np.asarray(labels, dtype=np.int64), np.stack(masks)


def show_images(images, titles=None, masks=None, ncols=4, cmap='gray', figsize=None):
    import matplotlib.pyplot as plt
    images = list(images)
    ncols = min(ncols, len(images))
    nrows = (len(images) + ncols - 1)//ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize or (3*ncols, 3*nrows), squeeze=False)
    for i, ax in enumerate(axes.flat):
        if i >= len(images): ax.axis('off'); continue
        ax.imshow(images[i], cmap=cmap, vmin=0 if cmap=='gray' else None,
                  vmax=1 if cmap=='gray' else None)
        if masks is not None: ax.contour(np.asarray(masks[i]).astype(float), [0.5], colors='lime', linewidths=1)
        ax.set_title(titles[i] if titles else str(i+1), fontsize=10)
        ax.axis('off')
    plt.tight_layout()
    return fig


def patch_ids(side=SIDE, grid=GRID):
    if side % grid: raise ValueError('side must be divisible by grid')
    return (np.arange(side)[:,None] // (side//grid))*grid + (np.arange(side)[None,:] // (side//grid))


def patch_mask(image, keep, grid=GRID, fill='zero'):
    image = np.asarray(image, dtype=np.float32)
    keep = np.asarray(keep, dtype=np.float32)
    pids = patch_ids(image.shape[0], grid)
    if keep.shape != (grid*grid,): raise ValueError('mask must contain grid**2 entries')
    visible = keep[pids] > .5
    if fill == 'zero': base = np.zeros_like(image)
    elif fill == 'mean': base = np.full_like(image, image.mean())
    elif fill == 'blur': base = gaussian_filter(image, sigma=3)
    else: raise ValueError('fill: zero/mean/blur')
    return np.where(visible, image, base).astype(np.float32)


def random_patch_masks(n=128, grid=GRID, seed=0):
    rng = np.random.default_rng(seed)
    masks = np.zeros((n, grid**2), np.float32)
    masks[0] = 1.0
    for i in range(1, n):
        p = rng.uniform(.30, .75)
        masks[i] = (rng.random(grid**2) < p).astype(np.float32)
        if not masks[i].any(): masks[i,rng.integers(grid**2)] = 1
    return masks


class ToyBlackBox(nn.Module):
    """Fixed differentiable brightness-spot detector (not a learned classifier).

    Explainers only use ``predict_proba``, which exposes no internal gradients.
    The forward method is available *solely* for the adaptation lesson.
    """
    def __init__(self):
        super().__init__()

    def forward(self, tensor):
        if tensor.ndim == 3: tensor = tensor[:, None]
        local = F.avg_pool2d(tensor, kernel_size=3, stride=1, padding=1)
        # Ignore edges so the synthetic scanner artifact creates a controlled failure case.
        central = local[:, :, 5:-5, 5:-5]
        # Soft maximum keeps gradient flow through several nearby pixels.
        vmax = torch.logsumexp(18 * central.flatten(1), dim=1) / 18 - np.log(central[0].numel())/18
        return torch.sigmoid(35*(vmax-0.57))

    def predict_proba(self, images):
        x = np.asarray(images, np.float32)
        if x.ndim == 2: x=x[None]
        with torch.no_grad():
            return self(torch.from_numpy(x.copy())).detach().cpu().numpy()


def masked_examples(image, masks, fill='zero', inpainter=None, grid=GRID):
    if fill == 'learned':
        if inpainter is None: raise ValueError('learned masking requires inpainter')
        # A *batch* of 100+ reconstructions is much faster on student CPUs.
        obs=(np.asarray(masks)[:, patch_ids(image.shape[0], grid)] > .5).astype(np.float32)
        data=np.broadcast_to(np.asarray(image, np.float32), obs.shape)
        masked=torch.from_numpy((obs*data)[:,None].copy())
        valid=torch.from_numpy(obs[:,None].copy())
        generated=[]
        with torch.no_grad():
            for i in range(0, len(masks), 32):
                generated.append(inpainter(masked[i:i+32],valid[i:i+32]).numpy())
        reconstruction=np.concatenate(generated,axis=0)[:,0]
        return (data*obs + reconstruction*(1-obs)).astype(np.float32)
    return np.stack([patch_mask(image,keep,grid=grid,fill=fill) for keep in masks])


def lime_kernel(masks, bandwidth=.75):
    # Normalized binary Hamming distance to the unmasked query.
    dist = np.sqrt(np.mean((1.-np.asarray(masks))**2, axis=1))
    return np.exp(-(dist/bandwidth)**2).astype(np.float64)


def fit_surrogate(masks, scores, sample_weight=None, l1=0., l2=0., prior=None,
                  steps=350):
    """Proximal gradient local linear regression with intercept; optional EBR prior.

    Loss is mean(weight*(prediction-score)^2)+l1*||w||_1+l2*||w-prior||_2^2.
    Used as a mathematical *teaching analogue* of EBR, not exact paper code.
    """
    x = np.asarray(masks, np.float64)
    y = np.asarray(scores, np.float64).reshape(-1)
    n,p = x.shape
    weights = np.ones(n) if sample_weight is None else np.asarray(sample_weight, np.float64)
    weights = weights / max(weights.mean(),1e-10)
    ref = np.zeros(p) if prior is None else np.asarray(prior, np.float64)
    if ref.shape != (p,): raise ValueError('prior has incorrect dimensions')
    x_aug = np.c_[np.ones(n), x]
    # Lipschitz bound of squared loss + quadratic regularizer.
    L = 2*np.linalg.norm(x_aug * np.sqrt(weights[:,None]), 2)**2/n + 2*l2 + 1e-8
    coef = np.zeros(p+1); coef[0] = np.average(y, weights=weights)
    for _ in range(steps):
        resid = x_aug @ coef - y
        grad = 2 * (x_aug.T @ (weights * resid))/n
        grad[1:] += 2*l2*(coef[1:] - ref)
        new = coef - grad/L
        new[1:] = np.sign(new[1:]) * np.maximum(0., np.abs(new[1:]) - l1/L)
        if np.linalg.norm(new-coef) < 1e-8: coef=new; break
        coef=new
    residual = y - x_aug @ coef
    ss_res=np.average(residual**2, weights=weights)
    ss_tot=np.average((y-np.average(y,weights=weights))**2, weights=weights)
    r2= 1-ss_res/max(ss_tot,1e-12)
    return {'intercept':float(coef[0]), 'coef':coef[1:], 'r2':float(r2)}


def coef_map(coef, grid=GRID, side=SIDE):
    return np.asarray(coef).reshape(grid,grid).repeat(side//grid,0).repeat(side//grid,1)


def lime_explain(image, black_box=None, n=160, seed=0, fill='zero', inpainter=None,
                 grid=GRID, l1=0., l2=0., prior=None, adapt=None):
    predictor = ToyBlackBox() if black_box is None else black_box
    keep = random_patch_masks(n, grid=grid, seed=seed)
    pert = masked_examples(image, keep, fill=fill, inpainter=inpainter, grid=grid)
    if adapt is not None: pert = adapt.apply(pert)
    scores = predictor.predict_proba(pert)
    fit = fit_surrogate(keep, scores, lime_kernel(keep), l1=l1, l2=l2, prior=prior)
    fit.update({'map':coef_map(fit['coef'],grid=grid,side=image.shape[0]),
                'masks':keep, 'scores':scores, 'images':pert})
    return fit


def auprc(mask, heatmap):
    """Pixelwise average precision. Continuous nonconstant scores preferred."""
    y = np.asarray(mask,bool).reshape(-1)
    if not y.any(): return float('nan')  # no lesion: localization undefined
    return float(average_precision_score(y.astype(int), np.asarray(heatmap).reshape(-1)))


def nearest_reference(query, library, k=5):
    """Cosine kNN on pooled intensities; no query label or mask is ever accessed."""
    if k < 1: raise ValueError('k >= 1')
    def emb(images):
        return np.stack([uniform_filter(z, size=4)[::4,::4].reshape(-1) for z in images])
    v = emb(np.asarray(library)); q=emb(np.asarray(query)[None])[0]
    denom=(np.linalg.norm(v,axis=1)*np.linalg.norm(q)+1e-12)
    similarity=(v@q)/denom
    idx=np.argsort(-similarity)[:k]
    return idx, similarity[idx]


def evidence_prior(query, reference_images, reference_coef, k=5, bandwidth=.1):
    ids, sims = nearest_reference(query, reference_images, k=k)
    # Similarities -> nonnegative normalized kernel weights (stable softmax).
    weights = np.exp((sims-sims.max()) / bandwidth)
    weights /= weights.sum()
    return np.average(np.asarray(reference_coef)[ids], axis=0, weights=weights), ids, weights


class TinyInpainter(nn.Module):
    """Learned masked-image reconstructor; intentionally *not* a transformer MAE."""
    def __init__(self):
        super().__init__()
        self.net=nn.Sequential(nn.Conv2d(2, 12, 5, padding=2), nn.ReLU(),
                              nn.Conv2d(12, 12, 3, padding=1), nn.ReLU(),
                              nn.Conv2d(12, 1, 3, padding=1), nn.Sigmoid())
    def forward(self, masked, observed):
        return self.net(torch.cat([masked, observed], 1))


def train_inpainter(n=96, epochs=8, seed=9):
    """CPU-friendly self-supervised training. Output shape matches input images."""
    torch.manual_seed(seed)
    imgs,_,_=dataset(n=n, seed=seed)
    rng = np.random.default_rng(seed)
    samples=[]; observed=[]
    pid=patch_ids()
    for img in imgs:
        keep=(rng.random(GRID*GRID)<rng.uniform(.35,.8)).astype(float)
        o=keep[pid].astype(np.float32)
        samples.append(img*o); observed.append(o)
    full=torch.tensor(imgs[:,None]); masked=torch.tensor(np.asarray(samples)[:,None]);
    obs=torch.tensor(np.asarray(observed)[:,None]); model=TinyInpainter()
    opt=torch.optim.Adam(model.parameters(),lr=.004)
    losses=[]
    for _ in range(epochs):
        perm=torch.randperm(n)
        for inds in perm.split(24):
            rec=model(masked[inds],obs[inds])
            # Penalize missing pixels more, but avoid sacrificing visible tissue.
            weights=(1-obs[inds])*2+0.2
            loss=((rec-full[inds])**2*weights).mean()
            opt.zero_grad();loss.backward();opt.step()
        losses.append(float(loss.item()))
    model.eval()
    return model, losses


def inpaint(image, keep, model, grid=GRID):
    obs=(np.asarray(keep)[patch_ids(image.shape[0],grid)]>.5).astype(np.float32)
    xx=torch.from_numpy((np.asarray(image)*obs)[None,None].astype(np.float32))
    oo=torch.from_numpy(obs[None,None])
    with torch.no_grad(): reconstruction=model(xx,oo)[0,0].numpy()
    # The observed patches must not be altered by the reconstructor.
    return (np.asarray(image)*obs + reconstruction*(1-obs)).astype(np.float32)


@dataclass
class AffineAdapter:
    scale: float=1.0
    bias: float=0.0
    def apply(self, images):
        return np.clip(np.asarray(images)*self.scale+self.bias,0,1).astype(np.float32)


def supervised_adapt(query, true_label, predictor=None, steps=70, lr=.045, weight_decay=0.06):
    """Illustrative supervised, single-query input adaptation using a FROZEN model.

    This requires a TRUE query label and predictor gradients: unlike black-box LIME,
    it is not a deployment-ready test-time method. Only to teach the mechanism.
    """
    if true_label not in (0,1): raise ValueError('true_label should be 0 or 1')
    model=ToyBlackBox() if predictor is None else predictor
    for p in model.parameters(): p.requires_grad_(False)
    scale=torch.tensor(1.,requires_grad=True); bias=torch.tensor(0.,requires_grad=True)
    opt=torch.optim.Adam([scale,bias],lr=lr)
    xx=torch.as_tensor(np.asarray(query)[None,None].copy(),dtype=torch.float32)
    target=torch.tensor([float(true_label)],dtype=torch.float32)
    history=[]
    for _ in range(steps):
        transformed=(xx*scale+bias).clamp(0,1)
        prob=model(transformed)
        loss=F.binary_cross_entropy(prob,target)+weight_decay*((scale-1)**2+bias**2)
        opt.zero_grad();loss.backward();opt.step()
        history.append(float(loss.detach()))
    return AffineAdapter(float(scale.detach()),float(bias.detach())),history
