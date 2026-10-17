#!/usr/bin/env python3
"""Download, once, every PDB entry the course uses, into the cache folder outside the repository.

The notebooks download what they need by themselves the first time they run. Run this script instead when you want
to prepare a computer (or a classroom image) in advance, or to check which file — deposited entry or biological
assembly — each zoo molecule is built from:

    python fetch_structures.py                     # cache in ~/.cache/biology_to_research/pdb
    python fetch_structures.py --cache ./pdb_cache # or in a folder of your choice
                                                   # (then set BIO2RESEARCH_PDB_CACHE=./pdb_cache for the notebooks)

Nothing is written into the repository. Requires only NumPy and SciPy (the course toolkit).
"""
import argparse
import os
import sys
import time

parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
parser.add_argument("--cache", help="folder for the downloaded files (default: ~/.cache/biology_to_research/pdb)")
args = parser.parse_args()
if args.cache:
    os.environ["BIO2RESEARCH_PDB_CACHE"] = os.path.abspath(args.cache)
os.environ.pop("BIO2RESEARCH_STANDINS", None)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import course_toolkit as tk  # noqa: E402

print(f"cache folder: {tk.pdb_cache_dir()}\n")
entries = list(tk.ZOO) + list(tk._EXTRA_ENTRIES)
info = {**tk.ZOO, **tk._EXTRA_ENTRIES}
failed = []
print(f"{'entry':6s} {'molecule':28s} {'atoms':>9s} {'mass':>9s} {'reference':>9s}  file used")
for pid in entries:
    t0 = time.time()
    atoms, desc = tk.pdb_atoms(pid)
    if atoms is None:
        failed.append(pid)
        print(f"{pid.upper():6s} {info[pid]['name']:28s} {'—':>9s} {'—':>9s} {info[pid]['mass_kDa']:>6d} kDa  FAILED: {desc}")
        continue
    kind = "assembly 1" if "assembly" in desc else "entry"
    print(f"{pid.upper():6s} {info[pid]['name']:28s} {len(atoms['xyz']):>9,d} {tk.model_mass_kDa(atoms):>5.0f} kDa "
          f"{info[pid]['mass_kDa']:>5d} kDa  {kind} ({time.time() - t0:.1f} s)")
lines, src = tk.pdb_text_lines("1bxn")                       # Module 01 reads one file in the legacy PDB format
print(f"\nlegacy-format file for Module 01: {src}")
if "stand-in" in src:
    failed.append("1bxn (legacy PDB format)")
total = sum(os.path.getsize(os.path.join(tk.pdb_cache_dir(), f)) for f in os.listdir(tk.pdb_cache_dir())) \
    if os.path.isdir(tk.pdb_cache_dir()) else 0
print(f"cache size: {total / 1e6:.1f} MB")
if failed:
    print("\n⚠️ could not download:", ", ".join(failed), "— the notebooks will use code-built stand-ins for these.")
    sys.exit(1)
print("\n✅ all structures are cached; the notebooks will use the real PDB models.")
