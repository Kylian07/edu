# 05 — Stereo Vision & Depth Estimation

## Overview

In computer vision and spatial perception, understanding the 3D structure of a scene from 2D observations is a fundamental challenge. Just as humans use binocular vision to perceive depth, robotic and computational systems can reconstruct 3D space by comparing images from two cameras offset by a known distance.

**Stereo Vision** computes the depth of points in a scene by matching corresponding pixels across a pair of images. This module covers the mathematical principles of stereo geometry, camera calibration, triangulation, the importance of stereo rectification in reducing the search space from 2D to 1D scanlines, block matching cost functions (SAD, SSD, NCC), common matching failure modes, and energy optimization techniques to produce smooth depth maps.

---

## What you will learn

### 1. Stereo Geometry & Disparity

For a rectified parallel camera setup with baseline $B$ (horizontal separation) and focal length $f$, a 3D point $(X, Y, Z)$ projects to coordinates $u_L$ and $u_R$ in the left and right images:

$$u_L = \frac{fX}{Z} + c_x$$

$$u_R = \frac{f(X - B)}{Z} + c_x$$

The horizontal **disparity** $d$ is defined as the difference between corresponding coordinates:

$$d = u_L - u_R = \frac{fB}{Z}$$

This establishes the fundamental relationship where depth $Z$ is inversely proportional to disparity:

$$Z = \frac{fB}{d}$$

### 2. Triangulation via DLT

When camera matrices $P_1$ and $P_2$ are known, a 3D point $\mathbf{X}$ can be reconstructed from its image observations $\mathbf{x}_1$ and $\mathbf{x}_2$ using the cross-product constraint $\mathbf{x} \times (P\mathbf{X}) = \mathbf{0}$. This yields a linear system $A\mathbf{X} = \mathbf{0}$, solved using Singular Value Decomposition (SVD) with the Direct Linear Transform (DLT) algorithm.

### 3. Stereo Rectification

In general unrectified setups, matching points lie along arbitrary 2D epipolar lines defined by the fundamental matrix constraint $\mathbf{x}_R^T F\mathbf{x}_L = 0$.
**Stereo Rectification** applies homographies $H_L$ and $H_R$ to the left and right images to align the epipolar lines with horizontal scanlines ($\tilde{v}_L \approx \tilde{v}_R$), simplifying the correspondence search to a 1D line search.

### 4. Matching Costs: SAD, SSD, and NCC

To find correspondences along scanlines, local patches are compared using:
- **Sum of Absolute Differences (SAD):** $\sum |p_i - q_i|$ (Fast, sensitive to illumination changes)
- **Sum of Squared Differences (SSD):** $\sum (p_i - q_i)^2$ (L2 norm, sensitive to illumination)
- **Normalized Cross-Correlation (NCC):** Measures similarity robustly under gain and bias changes:

$$\text{NCC}(p, q) = \frac{\sum (p_i - \bar{p})(q_i - \bar{q})}{\sqrt{\sum (p_i - \bar{p})^2}\sqrt{\sum (q_i - \bar{q})^2} + \epsilon}$$

### 5. Failure Cases in Block Matching

- **Textureless regions:** Lack of gradient makes matching ambiguous.
- **Repeated patterns:** Periodic textures produce multiple local minima in matching cost.
- **Specularities:** Non-Lambertian surfaces change appearance between camera views.
- **Occlusions:** Points visible to one camera but blocked to the other.

---

## Notebooks

| File | Description |
|------|-------------|
| `stereo.ipynb` | A concept-first guide to stereo vision. Includes mathematical derivation of disparity-to-depth, triangulation implementation from scratch using DLT, epipolar line analysis, block matching algorithms (SAD, SSD, NCC), window size trade-off evaluation, repeated pattern diagnostics, and energy-based smoothing. |

---

## Setup

```bash
pip install numpy matplotlib opencv-python
```

---

## Hardware Requirements

| Task | GPU needed | Notes |
|------|-----------|-------|
| Block matching and triangulation | No | CPU computation is sufficient for the provided synthetic examples |

---

## Common errors and how to fix them

| Error | Likely cause | Fix |
|-------|-------------|-----|
| Noisy disparity boundaries | Block matching window too small | Increase window size (e.g. from 3 to 7 or 15) to include more context |
| Blurry boundaries / edge fattening | Block matching window too large | Decrease window size, or use a bilateral/guided filter to refine edges |
| Triangulation error increases significantly | Large pixel noise or calibration error | Calibrate cameras precisely; use sub-pixel refinement for correspondence matching |
| Repeated pattern matching failure | Cost function matches incorrect cycles | Integrate a global smoothness constraint (MRF/Belief Propagation) or use structured light |

---

## Tips for beginners

- Start by changing the camera baseline $B$ and focal length $f$ to see their mathematical effect on the disparity-to-depth curve.
- Pay attention to the window size trade-off: small windows provide high-resolution details but are prone to random noise; large windows are noise-resistant but blur depth boundaries.
- Analyze the repeated pattern section to see how matching costs form multiple identical peaks, which is the primary reason passive stereo fails in environments with grids or stripes.
