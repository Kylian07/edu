#!/usr/bin/env python3
"""Check the BiologyToResearchV3 course.

    python validate_notebooks.py            # structure, outputs stripped, toolkit copies, Colab badges, relative links
    python validate_notebooks.py --execute  # ...and execute every notebook (≈ 35–45 min on a laptop CPU)
    python validate_notebooks.py --execute 23 26   # execute only modules 23 and 26

Exit status is non-zero if any check fails.
"""
import ast
import os
import re
import sys
import time
from pathlib import Path

import nbformat
from nbformat.validator import validate

ROOT = Path(__file__).resolve().parent
NB_DIR = ROOT / "notebooks"
COLAB = "https://colab.research.google.com/github/xulabs/edu/blob/main/cryoem/tutorial/BiologyToResearchV3/notebooks/"
EXPECTED = 27
problems = []


def fail(msg):
    problems.append(msg)
    print("  ✗", msg)


# ── reference toolkit definitions ──
toolkit_src = (ROOT / "course_toolkit.py").read_text()
toolkit = {}
for node in ast.parse(toolkit_src).body:
    if isinstance(node, ast.FunctionDef):
        toolkit[node.name] = ast.dump(node)
    elif isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
        toolkit[node.targets[0].id] = ast.dump(node)


def check_links(text, base, where):
    """Every relative markdown link must point to an existing file or folder."""
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"^(https?:|mailto:|#|\\)", target):
            continue
        path = (base / target.split("#")[0]).resolve()
        if not path.exists():
            fail(f"{where}: broken relative link → {target}")


# ── notebooks ──
paths = sorted(NB_DIR.glob("*.ipynb"))
print(f"Found {len(paths)} notebooks")
if len(paths) != EXPECTED:
    fail(f"expected {EXPECTED} notebooks, found {len(paths)}")
for i, path in enumerate(paths):
    print(f"• {path.name}")
    nb = nbformat.read(path, as_version=4)
    try:
        validate(nb)
    except Exception as e:  # noqa: BLE001
        fail(f"{path.name}: invalid notebook schema ({e})")
    if not path.name.startswith(f"{i:02d}_"):
        fail(f"{path.name}: expected module number {i:02d}")
    if nb.cells[0].cell_type != "markdown":
        fail(f"{path.name}: first cell must be markdown")
    first = nb.cells[0].source
    if COLAB + path.name not in first:
        fail(f"{path.name}: Colab badge missing or pointing elsewhere")
    for key in ("Hardware target", "Prerequisites", "Estimated time", "Lab papers covered"):
        if key not in first:
            fail(f"{path.name}: key-information table lacks '{key}'")
    md = "\n".join(c.source for c in nb.cells if c.cell_type == "markdown")
    for section in ("Learning objectives", "Checkpoint", "Questions", "References"):
        if section not in md:
            fail(f"{path.name}: missing '{section}' section")
    check_links(md, NB_DIR, path.name)
    code_cells = [c for c in nb.cells if c.cell_type == "code"]
    if any(c.get("outputs") or c.get("execution_count") for c in code_cells):
        fail(f"{path.name}: outputs must be stripped before committing")
    code = "\n".join(c.source for c in code_cells if not c.source.lstrip().startswith(("!", "%")))
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        fail(f"{path.name}: code does not parse ({e})")
        continue
    for node in tree.body:
        name = node.name if isinstance(node, ast.FunctionDef) else (
            node.targets[0].id if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) else None)
        if name in toolkit and ast.dump(node) != toolkit[name]:
            fail(f"{path.name}: toolkit copy of '{name}' differs from course_toolkit.py")

# ── companion documents ──
for doc in ["README.md", "PAPER_ATLAS.md", "READING_GUIDE.md", "GLOSSARY.md", "INSTRUCTOR_GUIDE.md"]:
    p = ROOT / doc
    if not p.exists():
        fail(f"missing {doc}")
        continue
    check_links(p.read_text(), ROOT, doc)
print(f"\nStructural checks: {'OK' if not problems else f'{len(problems)} problem(s)'}")

# ── optional execution ──
if "--execute" in sys.argv:
    from nbclient import NotebookClient

    only = {a for a in sys.argv[1:] if a.isdigit()}
    os.environ.setdefault("OMP_NUM_THREADS", "2")
    for path in paths:
        if only and path.name[:2] not in only:
            continue
        nb = nbformat.read(path, as_version=4)
        t0 = time.time()
        try:
            NotebookClient(nb, timeout=1200, kernel_name="python3", resources={"metadata": {"path": str(NB_DIR)}}).execute()
            print(f"  ✓ executed {path.name} in {time.time() - t0:.0f} s")
        except Exception as e:  # noqa: BLE001
            fail(f"{path.name}: execution failed — {type(e).__name__}: {str(e)[:300]}")

sys.exit(1 if problems else 0)
