# 12 — CTF Estimation & Correction from Real Micrographs

## Overview

In cryo-electron microscopy, phase contrast imaging of weak-phase specimens requires deliberate defocusing. This defocus—alongside the microscope's spherical aberration—modulates image contrast through the **Contrast Transfer Function (CTF)**. The CTF introduces oscillating bands of vanishing contrast and phase inversions known as **Thon rings**. Reconstructing accurate high-resolution structures requires estimating the exact defocus and optical parameters from the micrograph's power spectrum and correcting for CTF distortions.

Unlike synthetic simulations, this module fits the CTF directly from a real **apoferritin** micrograph from **EMPIAR-10146** (cisTEM tutorial dataset) using documented microscope parameters (300 kV, $C_s = 0.0$ mm, 1.5 Å/pixel). You will compute the experimental 2D power spectrum, radially average it, subtract the background noise envelope, fit defocus via grid search, evaluate fit quality using a classic half-and-half diagnostic display, and apply phase-flip correction.

---

## What you will learn

- **The CTF equation & Thon rings:** Mathematical formulation of defocus $\Delta z$, spherical aberration $C_s$, wavelength $\lambda$, and amplitude contrast $Q_0$; why zero-crossings cause information loss and contrast inversions.
- **Power spectrum analysis:** Generating 2D power spectra via FFT, computing radial rotational averages, and identifying Thon ring extrema.
- **Background envelope subtraction:** Stripping the smooth, monotonically decaying inelastic scattering background to isolate oscillating CTF signal.
- **Defocus fitting:** Cross-correlating experimental background-subtracted 1D radial profiles against theoretical $\text{CTF}(k)^2$ models over candidate defocus ranges.
- **Diagnostic visualization:** Constructing CTFFIND-style split diagnostics (half experimental power spectrum, half theoretical $|\text{CTF}|$ rings) to validate fit fidelity.
- **Phase-flip correction:** Inverting the sign of corrupted Fourier components to restore phase coherence prior to particle averaging.
- **Production methods:** Algorithmic designs in CTFFIND4, Gctf, cryoSPARC Patch CTF, and Wiener filtering.

---

## Notebooks

| File | Description |
|------|-------------|
| [`ctf_estimation_tutorial.ipynb`](ctf_estimation_tutorial.ipynb) | Hands-on tutorial fitting defocus parameters and applying phase-flip correction directly on a real EMPIAR-10146 apoferritin micrograph. |

---

## Key References

- Rohou, A. & Grigorieff, N. (2015). CTFFIND4: Fast and accurate defocus estimation from electron micrographs. *Journal of Structural Biology* 192(2), 216–221.
- Zhang, K. (2016). Gctf: Real-time CTF determination and correction. *Journal of Structural Biology* 193(1), 1–12.
- Grant, T., Rohou, A. & Grigorieff, N. (2018). cisTEM, user-friendly software for single-particle electron microscopy. *eLife* 7, e35383.
- Frank, J. (2006). *Three-Dimensional Electron Microscopy of Macromolecular Assemblies*. Oxford University Press.
