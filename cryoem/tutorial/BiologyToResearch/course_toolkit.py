"""
course_toolkit.py — shared helper functions for the BiologyToResearchV3 curriculum
==================================================================================

Every notebook in ``notebooks/`` is *self-contained* (it runs alone on Google
Colab), so the helpers a notebook needs are copied into its "🧰 Course toolkit"
cell.  This file is the single reference copy of those helpers: if you fix a
bug here, copy the fix into the notebooks that use the function
(``python validate_notebooks.py --toolkit-drift`` lists them).

Conventions used everywhere in the course
-----------------------------------------
* Volumes are NumPy arrays indexed ``vol[z, y, x]``; images are ``img[y, x]``.
* The electron beam travels along **z**.  Tilting is a rotation about the **y**
  axis, so the missing wedge lives in the (k_z, k_x) plane of Fourier space.
* Rotation matrices act on physical vectors written in **(x, y, z)** order.
  ``rotate_volume`` converts to array index order internally.
* Euler angles follow the **ZYZ** convention, R = Rz(phi) @ Ry(theta) @ Rz(psi)
  (active rotations, radians), the convention used by AITom/TomoMiner.
* Voxel size of all "molecular zoo" maps is 10 Å = 1 nm, the sampling used by
  most Xu-lab subtomogram papers (Gum-Net uses 1.2 nm, DISCA 1.33 nm).
* SNR (simulation) = var(signal) / var(noise), measured inside the box.

Only NumPy and SciPy are required.  Educational code: clarity over speed.
"""
from __future__ import annotations

import io
import os
import struct
import urllib.request

import numpy as np
from scipy import ndimage

__version__ = "1.0"

# ── Data sources ────────────────────────────────────────────────────────────
# Density templates made from PDB entries at 10 Å/voxel, distributed with the
# PolNet cryo-ET simulator (Martinez-Sanchez et al., Apache-2.0 licence).
# The commit is pinned so the files never change underneath the course.
POLNET_COMMIT = "73e613cc9162d26c7fd740ce3299bcb280a3e3b6"
POLNET_URL = ("https://raw.githubusercontent.com/anmartinezs/polnet/"
              + POLNET_COMMIT + "/data/templates/{kind}/{name}.{ext}")
# Real single-particle cryo-EM maps shipped with the NGL viewer test data (MIT).
NGL_COMMIT = "0db88033650614103be761f151efc923b66e977e"
NGL_URL = "https://raw.githubusercontent.com/nglviewer/ngl/" + NGL_COMMIT + "/data/{name}"

CACHE_DIR = os.environ.get("CRYO_COURSE_CACHE", "course_data")

# The "molecular zoo": names/organisms/masses from PolNet docs/molecules_table.md
ZOO = {
    "4v4r": dict(name="70S ribosome", organism="bacterial (E. coli / T. thermophilus)", mass_kDa=2277, symmetry="C1"),
    "4v7r": dict(name="80S ribosome", organism="S. cerevisiae", mass_kDa=5851, symmetry="C1"),
    "5mrc": dict(name="mitochondrial ribosome", organism="S. cerevisiae", mass_kDa=3325, symmetry="C1"),
    "3j9i": dict(name="20S proteasome", organism="Thermoplasma acidophilum", mass_kDa=659, symmetry="D7"),
    "6utj": dict(name="singly capped proteasome", organism="Thermoplasma acidophilum", mass_kDa=839, symmetry="C7"),
    "4cr2": dict(name="26S proteasome", organism="S. cerevisiae", mass_kDa=1309, symmetry="C1"),
    # NB: PolNet's 4V94 map holds TWO TRiC complexes side by side (1.95 MDa ≈ 2 × ~1 MDa).
    "4v94": dict(name="TRiC/CCT chaperonin (×2)", organism="S. cerevisiae", mass_kDa=1952, symmetry="C2"),
    "1bxn": dict(name="RuBisCO", organism="Cupriavidus necator", mass_kDa=280, symmetry="D4"),
    "1qvr": dict(name="ClpB chaperone", organism="Thermus thermophilus", mass_kDa=297, symmetry="C1"),
    "3cf3": dict(name="p97/VCP ATPase", organism="Mus musculus", mass_kDa=None, symmetry="C6"),
    "2cg9": dict(name="Hsp90–Sba1 chaperone", organism="S. cerevisiae", mass_kDa=None, symmetry="C2"),
    "1u6g": dict(name="Cand1–Cul1–Roc1 ligase", organism="H. sapiens", mass_kDa=239, symmetry="C1"),
    "3d2f": dict(name="Sse1p–Hsp70 chaperone", organism="S. cerevisiae / H. sapiens", mass_kDa=236, symmetry="C1"),
    "1s3x": dict(name="Hsp70 ATPase domain", organism="H. sapiens", mass_kDa=43, symmetry="C1"),
}


def _download(url: str, dest: str, timeout: float = 60.0) -> bool:
    """Download ``url`` to ``dest`` (no-op if it exists). Returns True on success."""
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return True
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r, open(dest + ".part", "wb") as f:
            f.write(r.read())
        os.replace(dest + ".part", dest)
        return True
    except Exception as exc:  # network blocked, offline, ...
        print(f"  ⚠️  download failed for {url.split('/')[-1]}: {type(exc).__name__}")
        return False


def read_mrc(path_or_bytes) -> tuple[np.ndarray, float]:
    """Minimal MRC2014 reader (modes 0, 1, 2, 6). Returns (array[z, y, x], voxel_size_Å).

    The MRC header is 1024 bytes of little-endian 32-bit words; words 1–3 are the
    grid size (nx, ny, nz), word 4 the data type, words 11–13 the cell size in Å,
    and word 24 the length of an optional extended header.
    """
    raw = path_or_bytes if isinstance(path_or_bytes, (bytes, bytearray)) else open(path_or_bytes, "rb").read()
    if raw[:2] == b"\x1f\x8b":  # gzip
        import gzip
        raw = gzip.decompress(raw)
    nx, ny, nz, mode = struct.unpack("<4i", raw[0:16])
    mx, my, mz = struct.unpack("<3i", raw[28:40])
    cella = struct.unpack("<3f", raw[40:52])
    mapc, mapr, maps = struct.unpack("<3i", raw[64:76])
    nsymbt = struct.unpack("<i", raw[92:96])[0]
    dtype = {0: np.int8, 1: np.int16, 2: np.float32, 6: np.uint16}[mode]
    data = np.frombuffer(raw, dtype=dtype, offset=1024 + nsymbt, count=nx * ny * nz)
    vol = data.reshape(nz, ny, nx).astype(np.float32)
    if (mapc, mapr, maps) != (1, 2, 3) and (mapc, mapr, maps) != (0, 0, 0):
        # reorder axes so that the array is [z, y, x]
        order = [3 - maps, 3 - mapr, 3 - mapc]
        vol = np.transpose(vol, np.argsort(order))
    voxel = float(cella[0] / mx) if mx > 0 else 1.0
    return vol, voxel


def fetch_zoo_map(pdb_id: str, voxel: str = "10A") -> tuple[np.ndarray, float, str]:
    """Return (density[z, y, x], voxel_size_Å, source) for a molecular-zoo entry.

    Tries the pinned PolNet template first; if the download fails (no internet),
    falls back to a *procedural* stand-in so the notebook still runs.
    """
    pdb_id = pdb_id.lower()
    dest = os.path.join(CACHE_DIR, f"polnet_{voxel}_{pdb_id}.mrc")
    url = POLNET_URL.format(kind=f"mrcs_{voxel}", name=pdb_id, ext="mrc")
    if _download(url, dest):
        vol, vs = read_mrc(dest)
        return vol, vs, f"PolNet template from PDB {pdb_id.upper()}"
    vol = procedural_molecule(pdb_id)
    return vol, 10.0, f"procedural stand-in for {pdb_id.upper()} (offline fallback)"


def fetch_ngl_map(name: str = "betaGal.mrc") -> tuple[np.ndarray, float, str] | None:
    """Download a real single-particle cryo-EM map distributed with the NGL viewer."""
    dest = os.path.join(CACHE_DIR, "ngl_" + name)
    if _download(NGL_URL.format(name=name), dest):
        vol, vs = read_mrc(dest)
        return vol, vs, f"NGL test map {name}"
    return None


def procedural_molecule(pdb_id: str, size: int = 40) -> np.ndarray:
    """Offline fallback: a coarse shape with the right size/symmetry flavour (1 nm voxels)."""
    g = (np.arange(size) - size / 2 + 0.5)
    z, y, x = np.meshgrid(g, g, g, indexing="ij")
    r = np.sqrt(x**2 + y**2)

    def blob(cz, cy, cx, s):
        return np.exp(-((z - cz)**2 + (y - cy)**2 + (x - cx)**2) / (2 * s**2))
    pid = pdb_id.lower()
    if pid in ("4v4r", "4v7r", "5mrc"):          # two unequal subunits
        v = blob(-3, 0, 0, 7.5) + 0.8 * blob(6, 2, 1, 5.5)
    elif pid in ("3j9i", "6utj", "4cr2"):        # stacked rings / barrel
        v = np.exp(-((r - 5.5)**2) / 4.0) * (np.abs(z) < 7.5)
        if pid != "3j9i":
            v = v + 0.8 * blob(10, 0, 0, 4)
    elif pid == "4v94":                          # double ring with cavity
        v = np.exp(-((r - 7)**2) / 6.0) * (np.abs(z) < 8)
    elif pid in ("3cf3", "1qvr"):                # hexameric ring
        ang = np.arctan2(y, x)
        v = np.exp(-((r - 5)**2) / 3.0) * (np.abs(z) < 4) * (1 + 0.5 * np.cos(6 * ang))
    elif pid == "1bxn":                          # compact ball
        v = blob(0, 0, 0, 4.5)
    else:                                        # small asymmetric blob
        v = blob(0, 0, 0, 3) + 0.5 * blob(2, 2, 0, 2)
    return ndimage.gaussian_filter(v.astype(np.float32), 1.0)


def prepare_map(vol: np.ndarray, size: int = 32, sigma: float = 1.0) -> np.ndarray:
    """Low-pass, centre (by centre of mass), crop/pad to ``size``³ and scale to [0, 1].

    PolNet templates are sharp sums of atoms; a Gaussian blur of ~1 voxel (1 nm)
    mimics the resolution of a cellular tomogram.
    """
    v = ndimage.gaussian_filter(np.clip(vol, 0, None).astype(np.float32), sigma)
    com = np.array(ndimage.center_of_mass(v))
    shift = np.array(v.shape) / 2 - 0.5 - com
    v = ndimage.shift(v, shift, order=1)
    out = np.zeros((size, size, size), np.float32)
    s = np.array(v.shape)
    src0 = np.maximum((s - size) // 2, 0)
    dst0 = np.maximum((size - s) // 2, 0)
    n = np.minimum(s, size)
    out[dst0[0]:dst0[0] + n[0], dst0[1]:dst0[1] + n[1], dst0[2]:dst0[2] + n[2]] = \
        v[src0[0]:src0[0] + n[0], src0[1]:src0[1] + n[1], src0[2]:src0[2] + n[2]]
    out -= out.min()
    return out / (out.max() + 1e-12)


def load_zoo(ids=("4v4r", "3j9i", "6utj", "1bxn"), size: int = 32, sigma: float = 1.0,
             verbose: bool = True) -> dict:
    """Fetch and prepare several zoo maps. Returns {pdb_id: volume(size³)}."""
    zoo = {}
    for pid in ids:
        raw, vs, src = fetch_zoo_map(pid)
        zoo[pid] = prepare_map(raw, size=size, sigma=sigma)
        if verbose:
            print(f"  {pid.upper():5s} {ZOO.get(pid, {}).get('name', ''):28s} raw {raw.shape} @ {vs:.0f} Å/voxel  ← {src}")
    return zoo


# ── Rotations ───────────────────────────────────────────────────────────────
def rot_x(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])


def rot_y(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])


def rot_z(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def euler_zyz_to_matrix(phi, theta, psi):
    """R = Rz(phi) · Ry(theta) · Rz(psi)  (radians, acting on (x, y, z) vectors)."""
    return rot_z(phi) @ rot_y(theta) @ rot_z(psi)


def matrix_to_euler_zyz(R):
    """Inverse of :func:`euler_zyz_to_matrix` (one of the two equivalent solutions)."""
    theta = np.arccos(np.clip(R[2, 2], -1, 1))
    if np.isclose(np.sin(theta), 0):
        return np.arctan2(R[1, 0], R[0, 0]), theta, 0.0
    return np.arctan2(R[1, 2], R[0, 2]), theta, np.arctan2(R[2, 1], -R[2, 0])


def random_rotation(rng: np.random.Generator) -> np.ndarray:
    """Uniformly random proper rotation (det = +1) from a random unit quaternion."""
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    w, x, y, z = q
    return np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def rotation_angle_deg(R1, R2) -> float:
    """Geodesic distance between two rotations: arccos((tr(R1ᵀR2) − 1)/2), in degrees."""
    c = (np.trace(R1.T @ R2) - 1) / 2
    return float(np.degrees(np.arccos(np.clip(c, -1, 1))))


_P = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], float)  # (x,y,z) <-> (z,y,x)


def rotate_volume(vol: np.ndarray, R: np.ndarray, shift_xyz=(0, 0, 0), order: int = 1,
                  cval: float = 0.0) -> np.ndarray:
    """Rotate a volume about its centre by R (then translate by shift, in voxels, (x,y,z)).

    out(p) = vol(Rᵀ (p − c − t) + c): the *object* is rotated by R and moved by t.
    """
    R_idx = _P @ R @ _P                       # same rotation written in (z, y, x) index order
    c = (np.array(vol.shape) - 1) / 2.0
    t_idx = _P @ np.asarray(shift_xyz, float)
    M = R_idx.T                               # inverse rotation maps output -> input
    offset = c - M @ (c + t_idx)
    return ndimage.affine_transform(vol, M, offset=offset, order=order, mode="constant", cval=cval)


def rotate_image(img: np.ndarray, angle_rad: float, shift_xy=(0, 0), order: int = 1) -> np.ndarray:
    """2D analogue of :func:`rotate_volume` (counter-clockwise in the (x, y) plane)."""
    c, s = np.cos(angle_rad), np.sin(angle_rad)
    R = np.array([[c, -s], [s, c]])
    R_idx = R[::-1, ::-1]                      # (x,y) -> (y,x)
    ctr = (np.array(img.shape) - 1) / 2.0
    t_idx = np.asarray(shift_xy, float)[::-1]
    M = R_idx.T
    return ndimage.affine_transform(img, M, offset=ctr - M @ (ctr + t_idx), order=order, mode="constant")


# ── Fourier space ───────────────────────────────────────────────────────────
def freq_grid(shape):
    """Frequency coordinates (cycles/voxel) for an unshifted FFT; returns list per axis."""
    return np.meshgrid(*[np.fft.fftfreq(n) for n in shape], indexing="ij")


def radial_frequency(shape) -> np.ndarray:
    """|k| in cycles/voxel for every coefficient of an unshifted FFT."""
    return np.sqrt(sum(k**2 for k in freq_grid(shape)))


def missing_wedge_mask(shape, tilt_max_deg: float = 60.0) -> np.ndarray:
    """Binary Fourier mask of a single-axis tilt series about y (±tilt_max).

    A coefficient (k_z, k_y, k_x) is measured if |k_z| ≤ |k_x|·tan(tilt_max)
    — the formula M(ξ) = 1(|ξ_3| ≤ |ξ_1| tan θ) used by Xu et al. (2012).
    For 2D images [z, x] pass a 2-tuple shape.
    """
    k = freq_grid(shape)
    kz, kx = k[0], k[-1]
    m = np.abs(kz) <= np.abs(kx) * np.tan(np.radians(tilt_max_deg)) + 1e-9
    m[(0,) * len(shape)] = True               # keep the mean (DC) term
    return m.astype(np.float32)


def apply_fourier_mask(vol: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Multiply the FFT of ``vol`` by ``mask`` (unshifted layout) and return the real part."""
    return np.real(np.fft.ifftn(np.fft.fftn(vol) * mask)).astype(np.float32)


def lowpass(vol: np.ndarray, cutoff: float, soft: float = 0.02) -> np.ndarray:
    """Soft low-pass filter; ``cutoff`` in cycles/voxel (0.5 = Nyquist)."""
    k = radial_frequency(vol.shape)
    filt = 1 / (1 + np.exp((k - cutoff) / soft))
    return apply_fourier_mask(vol, filt)


def add_noise_snr(signal: np.ndarray, snr: float, rng: np.random.Generator) -> np.ndarray:
    """Add white Gaussian noise so that var(signal)/var(noise) = snr."""
    sigma = np.sqrt(signal.var() / snr)
    return (signal + rng.normal(0, sigma, signal.shape)).astype(np.float32)


def normalize(v: np.ndarray) -> np.ndarray:
    """Zero mean, unit standard deviation."""
    return ((v - v.mean()) / (v.std() + 1e-12)).astype(np.float32)


def pearson(a: np.ndarray, b: np.ndarray) -> float:
    """Pearson correlation of two arrays (flattened)."""
    a = a.ravel() - a.mean()
    b = b.ravel() - b.mean()
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


# ── Electron optics ─────────────────────────────────────────────────────────
def electron_wavelength_A(kV: float = 300.0) -> float:
    """Relativistic electron wavelength in Å (0.0197 Å at 300 kV)."""
    V = kV * 1e3
    return 12.2643 / np.sqrt(V * (1 + 0.978466e-6 * V))


def ctf_2d(shape, pixel_A: float, defocus_um: float = 3.0, kV: float = 300.0,
           Cs_mm: float = 2.7, amp_contrast: float = 0.07, B: float = 0.0) -> np.ndarray:
    """Contrast transfer function on an unshifted FFT grid (underfocus is positive).

    CTF(k) = −[√(1−A²)·sin χ(k) + A·cos χ(k)]·exp(−B k²/4),
    χ(k) = π λ Δf k² − (π/2) C_s λ³ k⁴, with k in 1/Å.
    """
    lam = electron_wavelength_A(kV)
    k2 = sum(kk**2 for kk in freq_grid(shape)) / pixel_A**2
    dz = defocus_um * 1e4
    cs = Cs_mm * 1e7
    chi = np.pi * lam * dz * k2 - 0.5 * np.pi * cs * lam**3 * k2**2
    ctf = -(np.sqrt(1 - amp_contrast**2) * np.sin(chi) + amp_contrast * np.cos(chi))
    return (ctf * np.exp(-B * k2 / 4)).astype(np.float32)


# ── Tomography ──────────────────────────────────────────────────────────────
def project_tilt_series(vol: np.ndarray, angles_deg) -> np.ndarray:
    """Tilt-series projections of vol[z, y, x] about the y axis → array[n_tilts, y, x]."""
    return np.stack([ndimage.rotate(vol, a, axes=(0, 2), reshape=False, order=1).sum(axis=0)
                     for a in angles_deg]).astype(np.float32)


def weighted_back_projection(tilts: np.ndarray, angles_deg, nz: int) -> np.ndarray:
    """Weighted (ramp-filtered) back-projection of a y-axis tilt series → vol[nz, y, x]."""
    n, ny, nx = tilts.shape
    ramp = np.abs(np.fft.fftfreq(nx))[None, None, :]
    filt = np.real(np.fft.ifft(np.fft.fft(tilts, axis=2) * ramp, axis=2))
    rec = np.zeros((nz, ny, nx), np.float32)
    for img, a in zip(filt, angles_deg):
        smear = np.broadcast_to(img[None], (nz, ny, nx))
        rec += ndimage.rotate(smear, -a, axes=(0, 2), reshape=False, order=1)
    return rec / n


def simulate_subtomogram(template: np.ndarray, rng: np.random.Generator, snr: float = 0.1,
                         tilt_max_deg: float | None = 60.0, max_shift: float = 0.0,
                         R: np.ndarray | None = None):
    """Randomly rotate/shift a template, impose a missing wedge and add noise.

    Returns (subtomogram, R, shift_xyz).  This 'direct' simulation (Fourier mask +
    white noise) is the fast approximation used by many Xu-lab benchmarks.
    """
    R = random_rotation(rng) if R is None else R
    t = rng.uniform(-max_shift, max_shift, 3) if max_shift > 0 else np.zeros(3)
    v = rotate_volume(template, R, t)
    if tilt_max_deg is not None:
        v = apply_fourier_mask(v, missing_wedge_mask(v.shape, tilt_max_deg))
    return add_noise_snr(v, snr, rng), R, t


# ── Validation ──────────────────────────────────────────────────────────────
def fsc(v1: np.ndarray, v2: np.ndarray, pixel_A: float = 10.0, n_shells: int | None = None):
    """Fourier shell (ring, in 2D) correlation. Returns (frequency_1/Å, fsc, n_coeffs)."""
    F1, F2 = np.fft.fftn(v1), np.fft.fftn(v2)
    k = radial_frequency(v1.shape)
    n_shells = n_shells or min(v1.shape) // 2
    idx = np.minimum((k * 2 * n_shells).astype(int), n_shells)
    num = np.bincount(idx.ravel(), (F1 * np.conj(F2)).real.ravel(), n_shells + 1)
    d1 = np.bincount(idx.ravel(), (np.abs(F1)**2).ravel(), n_shells + 1)
    d2 = np.bincount(idx.ravel(), (np.abs(F2)**2).ravel(), n_shells + 1)
    cnt = np.bincount(idx.ravel(), minlength=n_shells + 1)
    curve = num / np.sqrt(d1 * d2 + 1e-20)
    freq = (np.arange(n_shells + 1) + 0.5) / (2 * n_shells) / pixel_A
    return freq[:n_shells], curve[:n_shells], cnt[:n_shells]


def resolution_at(freq, curve, threshold: float = 0.143) -> float:
    """First crossing of the FSC curve below ``threshold`` → resolution in Å."""
    below = np.where(curve[1:] < threshold)[0]
    if len(below) == 0:
        return float(1 / freq[-1])
    i = below[0] + 1
    f0, f1, c0, c1 = freq[i - 1], freq[i], curve[i - 1], curve[i]
    f = f0 + (threshold - c0) * (f1 - f0) / (c1 - c0 + 1e-12)
    return float(1 / f)


# ── Metrics ─────────────────────────────────────────────────────────────────
def match_points(pred, true, radius: float):
    """Greedy one-to-one matching of predicted to true coordinates within ``radius``.

    Returns dict(precision, recall, f1, tp, fp, fn).
    """
    true = np.asarray(true, float)
    pred = np.asarray(pred, float).reshape(-1, true.shape[-1] if true.ndim == 2 else 3)
    if len(pred) == 0 or len(true) == 0:
        tp = 0
    else:
        d = np.linalg.norm(pred[:, None, :] - true[None, :, :], axis=-1)
        used_p, used_t, tp = set(), set(), 0
        for i, j in zip(*np.unravel_index(np.argsort(d, axis=None), d.shape)):
            if d[i, j] > radius:
                break
            if i not in used_p and j not in used_t:
                used_p.add(i); used_t.add(j); tp += 1
    fp, fn = len(pred) - tp, len(true) - tp
    p = tp / max(len(pred), 1)
    r = tp / max(len(true), 1)
    return dict(precision=p, recall=r, f1=2 * p * r / max(p + r, 1e-12), tp=tp, fp=fp, fn=fn)


def hungarian_accuracy(y_true, y_pred) -> float:
    """Clustering accuracy after the best one-to-one relabelling (Hungarian algorithm)."""
    from scipy.optimize import linear_sum_assignment
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    ct = np.zeros((y_pred.max() + 1, y_true.max() + 1))
    np.add.at(ct, (y_pred, y_true), 1)
    r, c = linear_sum_assignment(-ct)
    return float(ct[r, c].sum() / len(y_true))


# ── Crowded "in silico cell" ────────────────────────────────────────────────
def support_radius(t: np.ndarray, level: float = 0.1) -> float:
    """Radius (voxels) of the smallest centred sphere containing all voxels above ``level``·max."""
    pts = np.argwhere(t > level * t.max())
    if len(pts) == 0:
        return t.shape[0] / 2
    c = (np.array(t.shape) - 1) / 2
    return float(np.linalg.norm(pts - c, axis=1).max()) + 1.0


def make_crowded_cell(templates: dict, counts: dict, shape=(48, 160, 160), rng=None,
                      membrane: bool = True, tries_per_particle: int = 400):
    """Pack randomly rotated templates into a volume without overlap (bounding spheres).

    A simple rejection-sampling stand-in for the packing used by Pei et al. (2016)
    and Liu et al. (2020).  Particles are placed in random class order so that every
    class gets a fair chance.  Returns (clean_volume, particles) where each particle
    is dict(cls, center_zyx, R).  Optionally adds a spherical membrane vesicle.
    """
    rng = rng or np.random.default_rng(0)
    vol = np.zeros(shape, np.float32)
    occ_c, occ_r, particles = [], [], []
    if membrane:  # a vesicle: thin shell, ~4 nm thick lipid bilayer at 1 nm/voxel
        zc, yc, xc = shape[0] / 2, shape[1] * 0.78, shape[2] * 0.22
        rad = min(shape[1], shape[2]) * 0.16
        g = np.meshgrid(*[np.arange(n) for n in shape], indexing="ij")
        d = np.sqrt((g[0] - zc)**2 + (g[1] - yc)**2 + (g[2] - xc)**2)
        vol += 0.6 * np.exp(-((d - rad)**2) / (2 * 1.5**2))
        occ_c.append(np.array([zc, yc, xc])); occ_r.append(rad + 3)
    radii = {cls: support_radius(templates[cls], level=0.35) for cls in counts}
    order = [cls for cls, n in counts.items() for _ in range(n)]
    rng.shuffle(order)
    for cls in order:
        t, rad_t = templates[cls], radii[cls]
        for _ in range(tries_per_particle):
            c = np.array([rng.uniform(rad_t, s - rad_t) if s > 2 * rad_t else s / 2 for s in shape])
            if any(np.linalg.norm(c - oc) < rad_t + orr for oc, orr in zip(occ_c, occ_r)):
                continue
            R = random_rotation(rng)
            sub = rotate_volume(t, R)
            h = np.array(sub.shape) // 2
            lo = np.round(c).astype(int) - h
            sl_v, sl_s = [], []
            for a in range(3):
                a0, a1 = max(lo[a], 0), min(lo[a] + sub.shape[a], shape[a])
                sl_v.append(slice(a0, a1)); sl_s.append(slice(a0 - lo[a], a1 - lo[a]))
            vol[tuple(sl_v)] += sub[tuple(sl_s)]
            occ_c.append(c); occ_r.append(rad_t)
            particles.append(dict(cls=cls, center_zyx=c, R=R))
            break
    return vol, particles


def simulate_tomogram(clean: np.ndarray, rng, snr: float = 0.05, tilt_max_deg: float = 60.0,
                      ctf_pixel_A: float | None = 10.0, defocus_um: float = 5.0) -> np.ndarray:
    """Fast tomogram simulation: (optional 3D CTF-like filter) → missing wedge → noise.

    The CTF is applied isotropically here (a simplification of per-tilt CTF).
    """
    v = clean
    if ctf_pixel_A:
        ctf = ctf_2d(clean.shape, ctf_pixel_A, defocus_um=defocus_um, kV=300, B=0)
        v = apply_fourier_mask(v, -ctf)          # sign flip: dense objects appear bright
    v = apply_fourier_mask(v, missing_wedge_mask(v.shape, tilt_max_deg))
    return add_noise_snr(v, snr, rng)


# ── Plotting ────────────────────────────────────────────────────────────────
def show_orthoslices(vol, title: str = "", axes=None, cmap: str = "gray"):
    """Show the three central orthogonal slices (xy, xz, yz) of a volume."""
    import matplotlib.pyplot as plt
    if axes is None:
        _, axes = plt.subplots(1, 3, figsize=(7.5, 2.6))
    z, y, x = (np.array(vol.shape) // 2)
    for ax, im, lab in zip(axes, [vol[z], vol[:, y, :], vol[:, :, x]], ["xy (z mid)", "xz (y mid)", "yz (x mid)"]):
        ax.imshow(im, cmap=cmap)
        ax.set_title(f"{title} {lab}".strip(), fontsize=8)
        ax.axis("off")
    return axes
