"""Reproducible simulations, not measurements from real patients or cells."""
import numpy as np
import pandas as pd


def make_cell_table(n=120, seed=7):
    """Synthetic A/B cellular phenotype table: one row per imagined specimen."""
    rng = np.random.default_rng(seed)
    conditions = np.array(['A'] * n + ['B'] * n)
    elongation = np.r_[rng.normal(1.8, .24, n), rng.normal(1.2, .24, n)]
    area = rng.normal(100, 15, 2*n) + 5*(conditions == 'B')
    nuclear_area = .29*area + rng.normal(0, 6, 2*n)
    intensity = rng.normal(.55, .07, 2*n) + .07*(conditions == 'B')
    batch = rng.choice(['batch1', 'batch2'], 2*n)
    return pd.DataFrame({'condition': conditions, 'elongation': elongation,
                         'area': area, 'nuclear_area': nuclear_area,
                         'intensity': intensity, 'batch': batch})


def make_cell_images(n=24, size=48, seed=7):
    """Simplified ellipse-like cell shapes with noisy background. A elongated, B rounder."""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[:size, :size]
    datasets = {}
    for cond in ['A', 'B']:
        out = []
        for i in range(n):
            cx, cy = size/2 + rng.normal(0,2), size/2 + rng.normal(0,2)
            long_axis = rng.uniform(11, 15) if cond == 'A' else rng.uniform(9, 12)
            short_axis = rng.uniform(4, 7) if cond == 'A' else rng.uniform(9, 12)
            theta = rng.uniform(-.4, .4)
            xr = (xx-cx)*np.cos(theta)+(yy-cy)*np.sin(theta)
            yr = -(xx-cx)*np.sin(theta)+(yy-cy)*np.cos(theta)
            mask = (xr/long_axis)**2 + (yr/short_axis)**2 <= 1
            image = rng.normal(.08, .02, (size,size)) + mask*rng.uniform(.6,.8)
            out.append(np.clip(image,0,1))
        datasets[cond] = np.asarray(out)
    return datasets


def make_shared_toy_embeddings(n=80, seed=7):
    """Correlated synthetic image/text vectors in one 6-D feature space.

    Not CLIP; the text vectors are simple concept prototypes.
    """
    rng = np.random.default_rng(seed)
    labels = ['elongated cell', 'round cell', 'bright staining',
              'low staining', 'large nucleus', 'small nucleus',
              'cells on glass', 'blurred image', 'granular texture',
              'clear background', 'irregular membrane', 'symmetric cell']
    # Axes: elongation, brightness, nucleus size, background, texture, membrane
    prototypes = np.array([
        [2,0,0,0,0,0], [-2,0,0,0,0,0], [0,2,0,0,0,0], [0,-2,0,0,0,0],
        [0,0,2,0,0,0], [0,0,-2,0,0,0], [0,0,0,2,0,0], [0,0,0,-2,0,0],
        [0,0,0,0,2,0], [0,0,0,0,-2,0], [0,0,0,0,0,2], [0,0,0,0,0,-2]], dtype=float)
    a = rng.normal(scale=.45, size=(n,6))
    b = rng.normal(scale=.45, size=(n,6))
    a[:,0] += 1.3
    b[:,0] -= 1.3
    a[:,1] -= .20
    b[:,1] += .20
    return a,b,prototypes,labels
