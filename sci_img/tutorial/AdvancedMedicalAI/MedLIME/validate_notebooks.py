"""Sequentially smoke-test code cells in clean per-notebook Python namespaces.

Fast smoke check, not a substitute for a fully isolated Jupyter kernel test.
"""
from pathlib import Path
import os, time, traceback
import nbformat
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.show=lambda *a,**k: plt.close('all')
root=Path(__file__).resolve().parent
passed=0
os.chdir(root)
for path in sorted((root/'notebooks').glob('*.ipynb')):
    start=time.time();print('RUN',path.name,flush=True)
    nb=nbformat.read(path,as_version=4)
    ns={'__name__':'__main__'}
    for i,c in enumerate(nb.cells):
        if c.cell_type == 'code':
            try: exec(compile(c.source,f'{path.name} cell {i}','exec'),ns)
            except Exception: traceback.print_exc();raise
    print('PASS',path.name,round(time.time()-start,2),'seconds',flush=True)
    passed += 1

assert passed==12, f"Expected 12, ran {passed}"
print(f"All {passed} notebooks passed sequential code-cell smoke tests.")
