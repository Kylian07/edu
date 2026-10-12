"""Reproducible *synthetic* biological image and feature data.
These illustrations are not medical observations and must not be used clinically.
"""
import numpy as np


def make_tabular_cells(n_per_group=75, seed=17):
    """Return (features, labels): correlated [area, intensity] toy measurements."""
    rng = np.random.default_rng(seed)
    cov = np.array([[1.6, 1.05], [1.05, 1.25]])
    healthy = rng.multivariate_normal([4.8, 5.1], cov, n_per_group)
    changed = rng.multivariate_normal([6.1, 4.8], cov, n_per_group)
    return np.vstack([healthy, changed]), np.r_[np.zeros(n_per_group, int), np.ones(n_per_group, int)]


def make_cell_images(n=160, size=32, seed=17, artifact_strength=0.0):
    """Return (images [N,H,W], labels, ground_truth_region_masks).

    Images contain synthetic elliptical cell bodies and nuclei. Label 1 has an
    additional bright spot with a known mask. Optional corner marker is a
    spurious image-acquisition artifact intentionally correlated with label 1.
    """
    if size < 24:
        raise ValueError("size must be at least 24")
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[:size, :size]
    images = np.empty((n, size, size), dtype=np.float32)
    labels = np.arange(n) % 2
    rng.shuffle(labels)
    masks = np.zeros_like(images, dtype=bool)
    for i, label in enumerate(labels):
        cy = size / 2 + rng.normal(0, 1.3)
        cx = size / 2 + rng.normal(0, 1.3)
        cell = ((yy - cy) / (size * 0.34)) ** 2 + ((xx - cx) / (size * 0.38)) ** 2 <= 1
        nucleus = ((yy - cy) / (size * 0.16)) ** 2 + ((xx - cx) / (size * 0.17)) ** 2 <= 1
        arr = 0.04 + 0.10 * rng.standard_normal((size, size))
        arr += cell * 0.22 + nucleus * 0.24
        arr += (xx / size) * rng.uniform(-0.03, 0.03)
        if label:
            lesion_y = cy - size * 0.17
            lesion_x = cx + size * 0.20
            lesion = (yy - lesion_y)**2 + (xx - lesion_x)**2 <= (size * 0.095)**2
            arr += lesion * 0.55
            masks[i] = lesion
            if artifact_strength:
                arr[:4, :4] += float(artifact_strength)
        images[i] = np.clip(arr, 0, 1).astype(np.float32)
    return images, labels.astype(int), masks


def make_chest_phantoms(n=24, size=64, seed=42):
    """Illustrative geometric chest-like phantoms, NOT actual radiographs."""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[:size, :size]
    frames = []
    masks = []
    for i in range(n):
        L = ((yy-size*.49)/(size*.33))**2 + ((xx-size*.36)/(size*.17))**2 < 1
        R = ((yy-size*.49)/(size*.33))**2 + ((xx-size*.64)/(size*.17))**2 < 1
        base = np.full((size,size), .4, dtype=float)
        base[L|R] = .12
        base += rng.normal(0, .018, (size,size))
        my, mx = size*(.42 + rng.uniform(-.08,.08)), size*(.35 if i%2 else .65)
        lesion = ((yy-my)**2+(xx-mx)**2 < (size*.08)**2) & (L|R)
        if i%2:
            base[lesion] += .42
            masks.append(lesion)
        else:
            masks.append(np.zeros_like(lesion))
        frames.append(np.clip(base, 0, 1))
    return np.asarray(frames, dtype=np.float32), np.asarray([i%2 for i in range(n)]), np.asarray(masks)
