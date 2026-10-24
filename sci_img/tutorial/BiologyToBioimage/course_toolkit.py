"""Shared helpers for BiologyToBioimage.

Every data set and every figure in this course is produced by code — nothing is downloaded or
read from disk. This module is the reference implementation; each notebook carries a *verbatim*
copy of the functions it actually uses (see DATA.md and the validator), so every notebook still
runs on its own in Google Colab. Keep this file and the copies in the notebooks identical.

Sections
--------
1. Random, noise and image-formation primitives (PSF, Gaussian/Poisson/impulse/periodic noise)
2. Synthetic bioimages (nuclei/cells, two-channel, time-lapse, spatial point patterns,
   registration pairs, degraded images)
3. Classical filtering and feature detection (convolution, Sobel, Canny steps, Hough transform,
   Gaussian fitting, GLCM/Haralick-style texture, morphological features, Mahalanobis distance)
4. Classical segmentation (1-D Gaussian-mixture EM / thresholding, watershed, SLIC superpixels,
   a toy normalized cut, Chan-Vese)
5. Detection, tracking and registration (IoU, NMS, Hungarian assignment, a constant-velocity
   Kalman filter, rigid-transform estimation, mutual information)
6. Dimensionality reduction (PCA by SVD)
7. Denoising / restoration / super-resolution (FFT low-pass, Wiener filter, PSNR, a simple SSIM)
8. Segmentation & detection metrics (Dice, IoU, precision/recall/F1)
9. Spatial statistics and colocalization (nearest-neighbour distances, Clark–Evans index,
   Ripley's L, a CSR null, Pearson and Manders colocalization coefficients)
10. Plotting helpers (Matplotlib only; no stored images)
"""
from __future__ import annotations

__version__ = "1.0"

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from scipy.optimize import linear_sum_assignment

# ============================================================================
# 1. Random, noise and image-formation primitives
# ============================================================================

def gaussian_psf(sigma: float, radius: int | None = None) -> np.ndarray:
    """A normalised 2-D Gaussian point-spread function (the microscope's blur kernel)."""
    if radius is None:
        radius = max(1, int(np.ceil(3 * sigma)))
    ax = np.arange(-radius, radius + 1)
    xx, yy = np.meshgrid(ax, ax)
    k = np.exp(-(xx ** 2 + yy ** 2) / (2 * sigma ** 2))
    return k / k.sum()


def add_gaussian_noise(image: np.ndarray, sigma: float, rng: np.random.Generator) -> np.ndarray:
    """Additive Gaussian (read) noise: the classic noise floor of a camera sensor."""
    return image + rng.normal(0.0, sigma, size=image.shape)


def add_poisson_noise(image: np.ndarray, peak: float, rng: np.random.Generator) -> np.ndarray:
    """Shot noise: rescale to a target photon count ``peak`` and sample a Poisson at every pixel."""
    scaled = np.clip(image, 0, None) * peak
    return rng.poisson(scaled).astype(float) / peak


def add_salt_pepper_noise(image: np.ndarray, amount: float, rng: np.random.Generator) -> np.ndarray:
    """Impulse noise: a random ``amount`` fraction of pixels are slammed to 0 or 1."""
    out = image.copy()
    mask = rng.random(image.shape) < amount
    salt = rng.random(image.shape) < 0.5
    out[mask & salt] = image.max()
    out[mask & ~salt] = image.min()
    return out


def add_periodic_noise(image: np.ndarray, amplitude: float, freq: tuple[float, float]) -> np.ndarray:
    """Periodic (structured) noise: a sinusoidal stripe pattern, as from scan-line pickup."""
    h, w = image.shape
    yy, xx = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
    return image + amplitude * np.sin(2 * np.pi * (freq[0] * yy / h + freq[1] * xx / w))


def blur_image(image: np.ndarray, psf: np.ndarray) -> np.ndarray:
    """Convolve an image with a point-spread function (microscope optical blur)."""
    return ndi.convolve(image, psf, mode="reflect")


# ============================================================================
# 2. Synthetic bioimages
# ============================================================================

SHAPE_CLASSES = ("round", "elongated", "kidney", "ring", "dividing", "irregular")


def _draw_blob(canvas: np.ndarray, cy: float, cx: float, r: float, shape: str,
                rng: np.random.Generator, angle: float = 0.0) -> None:
    """Add one synthetic nucleus/cell of the given shape class onto ``canvas`` (in place, additive)."""
    size = canvas.shape[0]
    yy, xx = np.meshgrid(np.arange(size), np.arange(size), indexing="ij")
    y, x = yy - cy, xx - cx
    ca, sa = np.cos(angle), np.sin(angle)
    yr, xr = ca * y + sa * x, -sa * y + ca * x  # rotate into the blob's own frame
    if shape == "round":
        d = (yr / r) ** 2 + (xr / r) ** 2
        canvas += np.exp(-d * 2.0)
    elif shape == "elongated":
        d = (yr / (r * 0.55)) ** 2 + (xr / (r * 1.7)) ** 2
        canvas += np.exp(-d * 2.0)
    elif shape == "kidney":
        d = (yr / r) ** 2 + (xr / r) ** 2
        dent = np.exp(-((yr - 0.0) ** 2 + (xr - r * 0.9) ** 2) / (2 * (r * 0.5) ** 2))
        canvas += np.clip(np.exp(-d * 2.0) - 0.9 * dent, 0, None)
    elif shape == "ring":
        d = np.sqrt(yr ** 2 + xr ** 2)
        canvas += np.exp(-((d - r) ** 2) / (2 * (r * 0.28) ** 2))
    elif shape == "dividing":
        sep = r * 1.1
        for sign in (-1, 1):
            d = ((yr - sign * sep * 0.5) / (r * 0.75)) ** 2 + (xr / (r * 0.75)) ** 2
            canvas += np.exp(-d * 2.0)
    else:  # irregular: a round blob perturbed by a few random bumps
        d = (yr / r) ** 2 + (xr / r) ** 2
        base = np.exp(-d * 2.0)
        for _ in range(3):
            bx, by = rng.uniform(-r, r, size=2)
            bump = np.exp(-(((yr - by) ** 2 + (xr - bx) ** 2) / (2 * (r * 0.45) ** 2)))
            base = np.clip(base + 0.5 * bump, 0, 1.3)
        canvas += base


def simulate_nuclei_image(n_cells: int = 25, size: int = 160, touching: bool = False,
                           shape_classes: tuple[str, ...] | None = None,
                           psf_sigma: float = 1.2, background: float = 0.05,
                           noise_sigma: float = 0.03, seed: int = 0):
    """A SIMULATED single-channel fluorescence image of cell nuclei/cells.

    Returns ``image`` (size x size, background + PSF-blurred blobs + Gaussian noise),
    ``instance_mask`` (0 = background, 1..n_cells = one integer id per cell, the ground truth
    for segmentation/detection/tracking), ``centroids`` (n_cells x 2, row, col), ``shape_labels``
    (one of SHAPE_CLASSES per cell, the ground truth for classification), and ``boxes`` (n_cells x 4,
    ymin, xmin, ymax, xmax — the ground truth for detection).
    """
    rng = np.random.default_rng(seed)
    classes = shape_classes or SHAPE_CLASSES
    image = np.full((size, size), background, dtype=float)
    instance_mask = np.zeros((size, size), dtype=int)
    centroids, labels, boxes = [], [], []
    margin = size * 0.12
    min_sep = size * 0.11 if not touching else size * 0.065
    placed = []
    attempts = 0
    while len(placed) < n_cells and attempts < n_cells * 60:
        attempts += 1
        cy, cx = rng.uniform(margin, size - margin, size=2)
        if all(np.hypot(cy - py, cx - px) > min_sep for py, px in placed):
            placed.append((cy, cx))
    for i, (cy, cx) in enumerate(placed):
        shape = classes[rng.integers(len(classes))]
        r = rng.uniform(size * 0.028, size * 0.045)
        angle = rng.uniform(0, 2 * np.pi)
        single = np.zeros_like(image)
        _draw_blob(single, cy, cx, r, shape, rng, angle)
        image += single
        this_mask = single > 0.25
        instance_mask[this_mask & (instance_mask == 0)] = i + 1
        centroids.append((cy, cx))
        labels.append(shape)
        ys, xs = np.where(this_mask)
        if len(ys):
            boxes.append((ys.min(), xs.min(), ys.max(), xs.max()))
        else:
            boxes.append((cy - r, cx - r, cy + r, cx + r))
    image = blur_image(image, gaussian_psf(psf_sigma))
    image = add_gaussian_noise(image, noise_sigma, rng)
    image = np.clip(image, 0, None)
    return dict(image=image, instance_mask=instance_mask, centroids=np.array(centroids),
                shape_labels=np.array(labels), boxes=np.array(boxes), source="SIMULATED")


def simulate_two_channel_image(size: int = 160, n_spots: int = 60, association: float = 0.7,
                                psf_sigma: float = 1.3, seed: int = 0):
    """Two SIMULATED fluorescence channels (protein A, protein B) with a known association.

    ``association`` in [0, 1] is the fraction of channel-B spots placed near an existing
    channel-A spot (true colocalization); the rest are placed independently at random. Returns
    ``chA``, ``chB`` (size x size images), ``points_a``, ``points_b`` (coordinates) and
    ``true_association`` (the parameter used, for the ground-truth check).
    """
    rng = np.random.default_rng(seed)
    margin = size * 0.08
    pts_a = rng.uniform(margin, size - margin, size=(n_spots, 2))
    pts_b = []
    for i in range(n_spots):
        if rng.random() < association:
            jitter = rng.normal(0, size * 0.015, size=2)
            pts_b.append(np.clip(pts_a[i] + jitter, margin, size - margin))
        else:
            pts_b.append(rng.uniform(margin, size - margin, size=2))
    pts_b = np.array(pts_b)

    def _render(pts):
        canvas = np.zeros((size, size))
        for cy, cx in pts:
            _draw_blob(canvas, cy, cx, size * 0.018, "round", rng)
        canvas = blur_image(canvas, gaussian_psf(psf_sigma))
        return add_gaussian_noise(canvas, 0.02, rng).clip(0, None)

    chA, chB = _render(pts_a), _render(pts_b)
    return dict(chA=chA, chB=chB, points_a=pts_a, points_b=pts_b,
                true_association=association, source="SIMULATED")


def simulate_time_lapse(n_frames: int = 20, n_particles: int = 12, size: int = 160,
                         speed: float = 2.5, division_prob: float = 0.03,
                         seed: int = 0):
    """A SIMULATED time-lapse of moving, occasionally dividing particles/cells.

    Returns ``frames`` (list of n_frames images), ``tracks`` (dict: true track id -> list of
    (frame, y, x)), and ``lineage`` (dict: child track id -> parent track id, for divisions).
    """
    rng = np.random.default_rng(seed)
    margin = size * 0.1
    positions = {i: np.array([rng.uniform(margin, size - margin), rng.uniform(margin, size - margin)])
                 for i in range(n_particles)}
    velocities = {i: rng.normal(0, speed, size=2) for i in positions}
    tracks = {i: [] for i in positions}
    lineage = {}
    next_id = n_particles
    frames = []
    for t in range(n_frames):
        canvas = np.full((size, size), 0.05)
        for pid in list(positions):
            positions[pid] = np.clip(positions[pid] + velocities[pid], margin, size - margin)
            for k in (0, 1):
                if positions[pid][k] in (margin, size - margin):
                    velocities[pid][k] *= -1
            _draw_blob(canvas, *positions[pid], size * 0.03, "round", rng)
            tracks[pid].append((t, *positions[pid]))
            if t > 2 and rng.random() < division_prob and len(positions) < n_particles * 3:
                child = next_id
                next_id += 1
                positions[child] = positions[pid] + rng.normal(0, 3, size=2)
                velocities[child] = -velocities[pid] + rng.normal(0, speed * 0.3, size=2)
                tracks[child] = []
                lineage[child] = pid
        canvas = blur_image(canvas, gaussian_psf(1.1))
        frames.append(add_gaussian_noise(canvas, 0.02, rng).clip(0, None))
    return dict(frames=frames, tracks=tracks, lineage=lineage, source="SIMULATED")


def simulate_point_pattern(n_points: int = 150, size: float = 100.0,
                            pattern: str = "random", cluster_std: float = 4.0,
                            n_clusters: int = 8, min_dist: float = 0.0,
                            seed: int = 0) -> np.ndarray:
    """SIMULATED 2-D point coordinates with a known spatial ``pattern``.

    ``pattern`` is one of ``"random"`` (complete spatial randomness), ``"clustered"``
    (Gaussian clumps around ``n_clusters`` parents) or ``"dispersed"`` (points repel each
    other, enforcing roughly ``min_dist``). Returns an (n_points, 2) array; the pattern name
    is the ground truth used in the 🧪 checks.
    """
    rng = np.random.default_rng(seed)
    if pattern == "random":
        pts = rng.uniform(0, size, size=(n_points, 2))
    elif pattern == "clustered":
        centers = rng.uniform(size * 0.15, size * 0.85, size=(n_clusters, 2))
        choice = rng.integers(0, n_clusters, size=n_points)
        pts = centers[choice] + rng.normal(0, cluster_std, size=(n_points, 2))
        pts = np.clip(pts, 0, size)
    elif pattern == "dispersed":
        min_dist = min_dist or size / np.sqrt(n_points) * 0.9
        pts = []
        attempts = 0
        while len(pts) < n_points and attempts < n_points * 200:
            attempts += 1
            cand = rng.uniform(0, size, size=2)
            if all(np.hypot(*(cand - p)) > min_dist for p in pts):
                pts.append(cand)
        pts = np.array(pts)
    else:
        raise ValueError(f"unknown pattern {pattern!r}")
    return pts


def simulate_registration_pair(sim: dict, angle_deg: float = 12.0, translation: tuple = (8.0, -5.0),
                                scale: float = 1.0, seed: int = 0):
    """Make a SIMULATED 'moving' image by applying a known rigid/similarity transform to ``sim['image']``.

    Returns ``fixed``, ``moving`` and ``true_params`` (angle in degrees, translation (dy, dx), scale) —
    the ground truth that a registration algorithm should recover.
    """
    fixed = sim["image"]
    theta = np.deg2rad(angle_deg)
    matrix = scale * np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    center = np.array(fixed.shape) / 2
    offset = center - matrix @ center - np.array(translation)
    moving = ndi.affine_transform(fixed, matrix, offset=offset, order=1, mode="constant", cval=fixed.min())
    rng = np.random.default_rng(seed)
    moving = add_gaussian_noise(moving, 0.01, rng).clip(0, None)
    return dict(fixed=fixed, moving=moving,
                true_params=dict(angle_deg=angle_deg, translation=translation, scale=scale),
                source="SIMULATED")


def degrade_image(image: np.ndarray, psf_sigma: float = 1.5, noise_sigma: float = 0.04,
                   seed: int = 0) -> dict:
    """Blur + noise a clean image with a KNOWN point-spread function (the forward model of
    restoration/deconvolution). Returns ``degraded`` and the ``psf`` used."""
    rng = np.random.default_rng(seed)
    psf = gaussian_psf(psf_sigma)
    degraded = blur_image(image, psf)
    degraded = add_gaussian_noise(degraded, noise_sigma, rng).clip(0, None)
    return dict(degraded=degraded, psf=psf, psf_sigma=psf_sigma, noise_sigma=noise_sigma)


# ============================================================================
# 3. Classical filtering and feature detection
# ============================================================================

SOBEL_X = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float)
SOBEL_Y = SOBEL_X.T


def sobel_gradients(image: np.ndarray):
    """Image gradients by the Sobel operator: returns (gx, gy, magnitude, orientation_radians)."""
    gx = ndi.correlate(image, SOBEL_X, mode="reflect")
    gy = ndi.correlate(image, SOBEL_Y, mode="reflect")
    mag = np.hypot(gx, gy)
    ori = np.arctan2(gy, gx)
    return gx, gy, mag, ori


def non_max_suppression_edges(mag: np.ndarray, ori: np.ndarray) -> np.ndarray:
    """Thin a gradient-magnitude image to 1-pixel-wide ridges along the gradient direction
    (the Canny edge detector's non-maximum-suppression step)."""
    angle = (np.rad2deg(ori) % 180)
    out = np.zeros_like(mag)
    padded = np.pad(mag, 1, mode="edge")
    h, w = mag.shape
    for dy, dx, lo, hi in ((0, 1, -22.5, 22.5), (1, 1, 22.5, 67.5),
                           (1, 0, 67.5, 112.5), (1, -1, 112.5, 157.5)):
        sel = ((angle >= lo) & (angle < hi)) if lo >= 0 else ((angle >= lo + 180) | (angle < hi))
        a = padded[1 + dy:1 + dy + h, 1 + dx:1 + dx + w]
        b = padded[1 - dy:1 - dy + h, 1 - dx:1 - dx + w]
        keep = sel & (mag >= a) & (mag >= b)
        out[keep] = mag[keep]
    return out


def hysteresis_threshold(mag: np.ndarray, low: float, high: float) -> np.ndarray:
    """Canny's hysteresis thresholding: keep strong edges (> high) and weak edges (> low) that
    are 8-connected to a strong edge."""
    strong = mag > high
    weak = (mag > low) & ~strong
    labeled, n = ndi.label(strong | weak, structure=np.ones((3, 3)))
    keep = np.zeros_like(strong)
    strong_labels = set(labeled[strong])
    for lbl in strong_labels:
        if lbl:
            keep |= labeled == lbl
    return keep


def hough_lines(edge_image: np.ndarray, n_theta: int = 180, n_rho: int = 200):
    """A from-scratch Hough transform for lines: returns the (rho, theta) accumulator and its
    rho/theta bin edges, given a binary edge image."""
    h, w = edge_image.shape
    diag = np.hypot(h, w)
    thetas = np.linspace(-np.pi / 2, np.pi / 2, n_theta)
    rhos = np.linspace(-diag, diag, n_rho)
    acc = np.zeros((n_rho, n_theta), dtype=int)
    ys, xs = np.nonzero(edge_image)
    cos_t, sin_t = np.cos(thetas), np.sin(thetas)
    for y, x in zip(ys, xs):
        rho_vals = x * cos_t + y * sin_t
        bins = np.clip(((rho_vals + diag) / (2 * diag) * (n_rho - 1)).astype(int), 0, n_rho - 1)
        acc[bins, np.arange(n_theta)] += 1
    return acc, rhos, thetas


def fit_gaussian_spot(patch: np.ndarray):
    """Sub-pixel localisation of one bright spot: fit a 2-D Gaussian's centroid by intensity-
    weighted moments (the simple, closed-form version of 'Gaussian fitting' spot localisation)."""
    yy, xx = np.meshgrid(np.arange(patch.shape[0]), np.arange(patch.shape[1]), indexing="ij")
    w = np.clip(patch - patch.min(), 0, None)
    total = w.sum()
    if total <= 0:
        return patch.shape[0] / 2, patch.shape[1] / 2
    cy = (w * yy).sum() / total
    cx = (w * xx).sum() / total
    return cy, cx


def glcm_features(image: np.ndarray, levels: int = 8, dx: int = 1, dy: int = 0):
    """Haralick-style texture features from a grey-level co-occurrence matrix (GLCM).

    Quantises ``image`` to ``levels`` grey levels, builds the co-occurrence matrix for the
    offset (dy, dx), and returns a dict of contrast, energy (angular second moment),
    homogeneity and correlation.
    """
    img = image - image.min()
    img = img / (img.max() + 1e-9)
    q = np.clip((img * (levels - 1)).round().astype(int), 0, levels - 1)
    h, w = q.shape
    glcm = np.zeros((levels, levels))
    y0, y1 = max(0, -dy), h - max(0, dy)
    x0, x1 = max(0, -dx), w - max(0, dx)
    a = q[y0:y1, x0:x1]
    b = q[y0 + dy:y1 + dy, x0 + dx:x1 + dx]
    for i, j in zip(a.ravel(), b.ravel()):
        glcm[i, j] += 1
    glcm /= glcm.sum() + 1e-9
    i_idx, j_idx = np.meshgrid(np.arange(levels), np.arange(levels), indexing="ij")
    mu_i, mu_j = (glcm * i_idx).sum(), (glcm * j_idx).sum()
    sig_i = np.sqrt((glcm * (i_idx - mu_i) ** 2).sum()) + 1e-9
    sig_j = np.sqrt((glcm * (j_idx - mu_j) ** 2).sum()) + 1e-9
    contrast = (glcm * (i_idx - j_idx) ** 2).sum()
    energy = (glcm ** 2).sum()
    homogeneity = (glcm / (1 + np.abs(i_idx - j_idx))).sum()
    correlation = ((glcm * (i_idx - mu_i) * (j_idx - mu_j)).sum()) / (sig_i * sig_j)
    return dict(contrast=contrast, energy=energy, homogeneity=homogeneity, correlation=correlation)


def shape_features(mask: np.ndarray) -> dict:
    """Simple morphological/shape features of a binary blob mask: area, perimeter (boundary
    pixel count), equivalent-circle compactness, and the aspect ratio of its bounding box."""
    area = mask.sum()
    eroded = ndi.binary_erosion(mask)
    perimeter = max(1, (mask & ~eroded).sum())
    compactness = 4 * np.pi * area / (perimeter ** 2 + 1e-9)  # 1.0 for a perfect circle
    ys, xs = np.nonzero(mask)
    if len(ys) == 0:
        return dict(area=0, perimeter=0, compactness=0.0, aspect_ratio=1.0)
    h = ys.max() - ys.min() + 1
    w = xs.max() - xs.min() + 1
    aspect_ratio = max(h, w) / max(1, min(h, w))
    return dict(area=float(area), perimeter=float(perimeter),
                compactness=float(compactness), aspect_ratio=float(aspect_ratio))


def mahalanobis_distance(x: np.ndarray, mean: np.ndarray, cov_inv: np.ndarray) -> float:
    """Mahalanobis distance of a feature vector ``x`` from a class with the given mean and the
    INVERSE of its covariance matrix (pass ``np.linalg.pinv(cov)`` once, reuse for every point)."""
    d = x - mean
    return float(np.sqrt(d @ cov_inv @ d))


# ============================================================================
# 4. Classical segmentation
# ============================================================================

def em_gaussian_mixture_1d(values: np.ndarray, k: int = 2, n_iter: int = 50, seed: int = 0):
    """From-scratch EM for a 1-D Gaussian mixture (the classic histogram-based way to pick a
    threshold: fit k components to the pixel-intensity histogram, e.g. background vs.
    foreground). Returns ``means``, ``stds``, ``weights`` and the final ``responsibilities``
    (n_values x k)."""
    rng = np.random.default_rng(seed)
    x = values.reshape(-1)
    means = rng.choice(x, size=k, replace=False).astype(float)
    stds = np.full(k, x.std() + 1e-6)
    weights = np.full(k, 1.0 / k)
    for _ in range(n_iter):
        # E-step: responsibilities via each component's Gaussian density
        dens = np.stack([
            weights[j] / (stds[j] * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - means[j]) / stds[j]) ** 2)
            for j in range(k)], axis=1)
        resp = dens / (dens.sum(axis=1, keepdims=True) + 1e-12)
        # M-step: weighted means/variances/weights
        nk = resp.sum(axis=0) + 1e-12
        means = (resp * x[:, None]).sum(axis=0) / nk
        stds = np.sqrt((resp * (x[:, None] - means) ** 2).sum(axis=0) / nk) + 1e-6
        weights = nk / len(x)
    return dict(means=means, stds=stds, weights=weights, responsibilities=resp)


def watershed_labels(image: np.ndarray, min_distance: int = 7) -> np.ndarray:
    """Marker-controlled watershed segmentation of a blobby intensity image: finds markers at
    local intensity maxima (one per expected object) and floods from them. Returns an integer
    label image (0 = background)."""
    from skimage.feature import peak_local_max
    from skimage.segmentation import watershed as _watershed
    smooth = ndi.gaussian_filter(image, 1.0)
    coords = peak_local_max(smooth, min_distance=min_distance, labels=smooth > smooth.mean())
    markers = np.zeros(image.shape, dtype=int)
    for i, (y, x) in enumerate(coords, start=1):
        markers[y, x] = i
    markers = ndi.label(ndi.binary_dilation(markers > 0, iterations=2))[0] if coords.size else markers
    elevation = -smooth
    return _watershed(elevation, markers=markers, mask=smooth > smooth.mean() * 0.6)


def slic_superpixels(image: np.ndarray, n_segments: int = 100) -> np.ndarray:
    """Simple Linear Iterative Clustering super-pixels (over-segmentation into compact,
    similar-intensity patches) — thin wrapper so the notebooks can call one function name."""
    from skimage.segmentation import slic
    rgb = np.stack([image] * 3, axis=-1)
    return slic(rgb, n_segments=n_segments, channel_axis=-1, start_label=1)


def toy_normalized_cut(affinity: np.ndarray) -> np.ndarray:
    """Split a small weighted graph (``affinity``, n x n, symmetric, non-negative) into two
    groups by the normalized-cut spectral relaxation: the Fiedler vector (second-smallest
    eigenvector) of the normalized graph Laplacian. Returns a length-n array of 0/1 group labels."""
    d = affinity.sum(axis=1)
    d_inv_sqrt = np.diag(1.0 / np.sqrt(np.clip(d, 1e-9, None)))
    laplacian = np.diag(d) - affinity
    normalized = d_inv_sqrt @ laplacian @ d_inv_sqrt
    eigvals, eigvecs = np.linalg.eigh(normalized)
    fiedler = eigvecs[:, 1]  # eigvals[0] ~ 0 is the trivial constant eigenvector
    return (fiedler > np.median(fiedler)).astype(int)


def chan_vese_step(image: np.ndarray, phi: np.ndarray, mu: float = 0.2, dt: float = 0.5):
    """One explicit-Euler update of the Chan–Vese active-contour (level-set) evolution: moves
    the zero level set of ``phi`` to better separate the two regions of (near-)constant
    intensity it currently implies. Returns the updated ``phi``."""
    inside = phi > 0
    c1 = image[inside].mean() if inside.any() else image.mean()
    c2 = image[~inside].mean() if (~inside).any() else image.mean()
    grad_y, grad_x = np.gradient(phi)
    grad_mag = np.hypot(grad_y, grad_x) + 1e-6
    kappa = (np.gradient(grad_y / grad_mag, axis=0) + np.gradient(grad_x / grad_mag, axis=1))
    force = -(image - c1) ** 2 + (image - c2) ** 2
    return phi + dt * grad_mag * (mu * kappa + force)


# ============================================================================
# 5. Detection, tracking and registration
# ============================================================================

def iou_boxes(box_a, box_b) -> float:
    """Intersection-over-union of two (ymin, xmin, ymax, xmax) boxes."""
    ya, xa, yA, xA = box_a
    yb, xb, yB, xB = box_b
    iy0, ix0 = max(ya, yb), max(xa, xb)
    iy1, ix1 = min(yA, yB), min(xA, xB)
    inter = max(0, iy1 - iy0) * max(0, ix1 - ix0)
    area_a = max(0, yA - ya) * max(0, xA - xa)
    area_b = max(0, yB - yb) * max(0, xB - xb)
    union = area_a + area_b - inter
    return inter / union if union > 0 else 0.0


def non_max_suppression_boxes(boxes: np.ndarray, scores: np.ndarray, iou_threshold: float = 0.3):
    """Greedy non-maximum suppression: keep the highest-scoring box, remove boxes that overlap
    it by more than ``iou_threshold``, repeat. Returns the kept indices (into ``boxes``)."""
    order = np.argsort(-scores)
    keep = []
    while len(order):
        i = order[0]
        keep.append(i)
        rest = order[1:]
        order = np.array([j for j in rest if iou_boxes(boxes[i], boxes[j]) <= iou_threshold])
    return keep


def hungarian_assignment(cost_matrix: np.ndarray):
    """The Hungarian algorithm for the linear assignment problem: the lowest-total-cost one-to-
    one matching between rows and columns of ``cost_matrix``. Returns (row_ind, col_ind)."""
    return linear_sum_assignment(cost_matrix)


class ConstantVelocityKalman:
    """A minimal 2-D constant-velocity Kalman filter for one tracked point (state = y, x, vy, vx)."""

    def __init__(self, y0: float, x0: float, process_var: float = 1.0, meas_var: float = 4.0):
        self.x = np.array([y0, x0, 0.0, 0.0])
        self.P = np.eye(4) * 10.0
        self.F = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=float)
        self.H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=float)
        self.Q = np.eye(4) * process_var
        self.R = np.eye(2) * meas_var

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q
        return self.x[:2].copy()

    def update(self, measurement: np.ndarray):
        y = measurement - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(4) - K @ self.H) @ self.P
        return self.x[:2].copy()


def estimate_rigid_transform(src_pts: np.ndarray, dst_pts: np.ndarray):
    """Least-squares rigid (rotation + translation) transform that best maps ``src_pts`` onto
    ``dst_pts`` (point-set registration via the Kabsch algorithm). Returns (R, t) such that
    dst ≈ src @ R.T + t."""
    src_mean, dst_mean = src_pts.mean(axis=0), dst_pts.mean(axis=0)
    src_c, dst_c = src_pts - src_mean, dst_pts - dst_mean
    H = src_c.T @ dst_c
    U, _, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    R = Vt.T @ np.diag([1, d]) @ U.T
    t = dst_mean - R @ src_mean
    return R, t


def mutual_information(image_a: np.ndarray, image_b: np.ndarray, bins: int = 32) -> float:
    """Mutual information between two co-registered images, estimated from their 2-D joint
    intensity histogram — the similarity metric of choice for multi-modal registration, where
    intensities are related but not linearly (unlike single-modality correlation)."""
    hist2d, _, _ = np.histogram2d(image_a.ravel(), image_b.ravel(), bins=bins)
    pxy = hist2d / hist2d.sum()
    px, py = pxy.sum(axis=1), pxy.sum(axis=0)
    px_py = px[:, None] * py[None, :]
    nz = pxy > 0
    return float(np.sum(pxy[nz] * np.log(pxy[nz] / px_py[nz])))


# ============================================================================
# 6. Dimensionality reduction
# ============================================================================

def pca(X: np.ndarray, n_components: int = 2):
    """Principal component analysis by SVD of the column-centred data. Returns the projected
    scores (N x n_components), the components (n_components x J) and the explained-variance
    ratio of each component."""
    mean = X.mean(axis=0)
    Xc = X - mean
    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
    scores = (U * S)[:, :n_components]
    explained = (S ** 2) / np.sum(S ** 2)
    return scores, Vt[:n_components], explained[:n_components]


# ============================================================================
# 7. Denoising / restoration / super-resolution
# ============================================================================

def fft_lowpass_denoise(image: np.ndarray, cutoff_frac: float = 0.15) -> np.ndarray:
    """Denoise by zeroing high spatial frequencies in the Fourier domain (an ideal low-pass
    filter at ``cutoff_frac`` of the Nyquist frequency), then inverse-transforming."""
    f = np.fft.fftshift(np.fft.fft2(image))
    h, w = image.shape
    yy, xx = np.meshgrid(np.arange(h) - h / 2, np.arange(w) - w / 2, indexing="ij")
    radius = np.hypot(yy, xx) / (min(h, w) / 2)
    f[radius > cutoff_frac] = 0
    return np.real(np.fft.ifft2(np.fft.ifftshift(f)))


def wiener_deconvolve(degraded: np.ndarray, psf: np.ndarray, noise_to_signal: float = 0.01) -> np.ndarray:
    """Wiener deconvolution: inverse-filter a blurred, noisy image given its (known) PSF and an
    estimated noise-to-signal power ratio, which regularises the inverse near-zero frequencies."""
    h, w = degraded.shape
    psf_padded = np.zeros((h, w))
    ph, pw = psf.shape
    psf_padded[:ph, :pw] = psf
    psf_padded = np.roll(psf_padded, (-ph // 2, -pw // 2), axis=(0, 1))
    H = np.fft.fft2(psf_padded)
    G = np.fft.fft2(degraded)
    Hc = np.conj(H)
    wiener = Hc / (H * Hc + noise_to_signal)
    return np.real(np.fft.ifft2(wiener * G))


def psnr(reference: np.ndarray, estimate: np.ndarray, data_range: float | None = None) -> float:
    """Peak signal-to-noise ratio (dB) between a reference and an estimate; higher is better."""
    data_range = data_range or (reference.max() - reference.min() + 1e-9)
    mse = np.mean((reference - estimate) ** 2)
    if mse <= 1e-12:
        return float("inf")
    return 10 * np.log10(data_range ** 2 / mse)


def simple_ssim(a: np.ndarray, b: np.ndarray, data_range: float | None = None) -> float:
    """A simplified, global (whole-image, not windowed) structural-similarity index: combines
    luminance, contrast and structure agreement; 1.0 = identical. For a full windowed SSIM use
    ``skimage.metrics.structural_similarity``."""
    data_range = data_range or (max(a.max(), b.max()) - min(a.min(), b.min()) + 1e-9)
    c1, c2 = (0.01 * data_range) ** 2, (0.03 * data_range) ** 2
    mu_a, mu_b = a.mean(), b.mean()
    var_a, var_b = a.var(), b.var()
    cov = ((a - mu_a) * (b - mu_b)).mean()
    return float(((2 * mu_a * mu_b + c1) * (2 * cov + c2)) /
                 ((mu_a ** 2 + mu_b ** 2 + c1) * (var_a + var_b + c2)))


# ============================================================================
# 8. Segmentation & detection metrics
# ============================================================================

def dice_coefficient(mask_a: np.ndarray, mask_b: np.ndarray) -> float:
    """Dice/F1 overlap of two binary masks: 2|A∩B| / (|A|+|B|)."""
    a, b = mask_a.astype(bool), mask_b.astype(bool)
    inter = (a & b).sum()
    denom = a.sum() + b.sum()
    return float(2 * inter / denom) if denom > 0 else 1.0


def iou_masks(mask_a: np.ndarray, mask_b: np.ndarray) -> float:
    """Intersection-over-union of two binary masks."""
    a, b = mask_a.astype(bool), mask_b.astype(bool)
    union = (a | b).sum()
    return float((a & b).sum() / union) if union > 0 else 1.0


def precision_recall_f1(y_true: np.ndarray, y_pred: np.ndarray):
    """Precision TP/(TP+FP), recall TP/(TP+FN) and their harmonic mean F1 for binary labels
    (1 = positive). Returns (precision, recall, f1)."""
    y_true, y_pred = np.asarray(y_true).astype(int), np.asarray(y_pred).astype(int)
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return precision, recall, f1


# ============================================================================
# 9. Spatial statistics and colocalization
# ============================================================================

def nearest_neighbor_distances(points: np.ndarray, other: np.ndarray | None = None) -> np.ndarray:
    """For each point, the distance to its nearest neighbour (in ``other`` if given — a CROSS
    nearest-neighbour distance between two populations — else in ``points`` itself)."""
    target = points if other is None else other
    d = np.sqrt(((points[:, None, :] - target[None, :, :]) ** 2).sum(axis=2))
    if other is None:
        np.fill_diagonal(d, np.inf)
    return d.min(axis=1)


def clark_evans_index(points: np.ndarray, area: float) -> float:
    """The Clark–Evans index: observed mean nearest-neighbour distance divided by the distance
    expected under complete spatial randomness (CSR) at the same point density. CE < 1 means
    clustering, CE ≈ 1 random, CE > 1 dispersion/regularity."""
    n = len(points)
    observed = nearest_neighbor_distances(points).mean()
    density = n / area
    expected = 1.0 / (2 * np.sqrt(density))
    return float(observed / expected)


def ripley_l(points: np.ndarray, radii: np.ndarray, area: float) -> np.ndarray:
    """Ripley's L function L(r) − r at each radius in ``radii``: positive means more
    neighbours within r than expected under CSR (clustering at that scale), negative means
    fewer (dispersion); edge correction is omitted for simplicity (use a border guard band)."""
    n = len(points)
    d = np.sqrt(((points[:, None, :] - points[None, :, :]) ** 2).sum(axis=2))
    np.fill_diagonal(d, np.inf)
    density = n / area
    l_vals = []
    for r in radii:
        counts = (d <= r).sum(axis=1).mean()
        k_r = counts / density
        l_vals.append(np.sqrt(k_r / np.pi) - r)
    return np.array(l_vals)


def csr_envelope(n_points: int, size: float, radii: np.ndarray, n_sims: int = 20, seed: int = 0):
    """Monte Carlo null distribution (complete spatial randomness) for Ripley's L: simulate
    ``n_sims`` random point sets of the same size/density and return the (low, high) envelope
    of L(r) − r across simulations, for comparison with an observed curve."""
    rng = np.random.default_rng(seed)
    curves = []
    for s in range(n_sims):
        pts = rng.uniform(0, size, size=(n_points, 2))
        curves.append(ripley_l(pts, radii, size ** 2))
    curves = np.array(curves)
    return curves.min(axis=0), curves.max(axis=0)


def pearson_colocalization(ch_a: np.ndarray, ch_b: np.ndarray, mask: np.ndarray | None = None) -> float:
    """Pearson's colocalization coefficient: the ordinary linear correlation between two
    channels' pixel intensities, restricted to ``mask`` if given (e.g. just the cell interior)."""
    a = ch_a[mask] if mask is not None else ch_a.ravel()
    b = ch_b[mask] if mask is not None else ch_b.ravel()
    a, b = a - a.mean(), b - b.mean()
    denom = np.sqrt((a ** 2).sum() * (b ** 2).sum())
    return float((a * b).sum() / denom) if denom > 0 else 0.0


def manders_coefficients(ch_a: np.ndarray, ch_b: np.ndarray, thr_a: float, thr_b: float):
    """Manders' colocalization coefficients M1, M2 at the given intensity thresholds: the
    fraction of channel A's (resp. B's) total signal that sits in pixels where the OTHER
    channel is also above its threshold."""
    pos_b = ch_b > thr_b
    pos_a = ch_a > thr_a
    m1 = ch_a[pos_b].sum() / (ch_a.sum() + 1e-9)
    m2 = ch_b[pos_a].sum() / (ch_b.sum() + 1e-9)
    return float(m1), float(m2)


# ============================================================================
# 10. Plotting helpers (Matplotlib only; nothing stored)
# ============================================================================

def show_image(ax, image: np.ndarray, title: str = "", cmap: str = "gray"):
    """Show one image on a given Matplotlib axis, titled, with ticks removed."""
    ax.imshow(image, cmap=cmap)
    ax.set_title(title, fontsize=10)
    ax.set_xticks([]); ax.set_yticks([])


def show_image_grid(images, titles=None, ncols: int = 4, cmap: str = "gray", figsize_scale: float = 2.6):
    """A grid of images with Matplotlib, one subplot each, titles optional."""
    n = len(images)
    ncols = min(ncols, n)
    nrows = int(np.ceil(n / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(figsize_scale * ncols, figsize_scale * nrows))
    axes = np.atleast_1d(axes).ravel()
    for i, img in enumerate(images):
        show_image(axes[i], img, titles[i] if titles else "", cmap=cmap)
    for ax in axes[n:]:
        ax.axis("off")
    fig.tight_layout()
    return fig, axes


def overlay_boxes(ax, boxes, color: str = "lime", linewidth: float = 1.5):
    """Draw (ymin, xmin, ymax, xmax) boxes as rectangles on an existing image axis."""
    import matplotlib.patches as patches
    for ymin, xmin, ymax, xmax in boxes:
        rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                  linewidth=linewidth, edgecolor=color, facecolor="none")
        ax.add_patch(rect)


def plot_tracks(ax, tracks: dict, min_len: int = 2):
    """Plot every track in a ``{id: [(t, y, x), ...]}`` dict as a coloured polyline."""
    for tid, pts in tracks.items():
        if len(pts) < min_len:
            continue
        arr = np.array(pts)
        ax.plot(arr[:, 2], arr[:, 1], marker="o", markersize=2, linewidth=1)
    ax.invert_yaxis()
    ax.set_aspect("equal")
