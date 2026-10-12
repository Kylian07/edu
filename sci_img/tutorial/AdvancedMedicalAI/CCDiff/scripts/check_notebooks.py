"""Validate all 24 core notebooks; fast mode or independent Jupyter kernels.

Usage:
 python scripts/check_notebooks.py --fast    # fast CPU in-process exec of every cell
 python scripts/check_notebooks.py --kernel  # slower end-to-end nbclient Jupyter test
"""
from pathlib import Path
import argparse
import os
import sys
import nbformat
root=Path(__file__).resolve().parents[1]
nbpaths=sorted((root/'notebooks').glob('T*.ipynb'))


def fast_check():
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import pyplot as plt
    for j,path in enumerate(nbpaths,1):
        print(f'[{j:02d}/{len(nbpaths)}] {path.name}',flush=True)
        nb=nbformat.read(path,as_version=4)
        ns={'__name__':'__main__'}
        for i,c in enumerate(nb.cells):
            if c.cell_type=='code':
                try:
                    exec(compile(c.source, f'{path}:cell{i}', 'exec'),ns)
                except BaseException as exc:
                    raise RuntimeError(f'Failure in {path.name} code cell {i}') from exc
            plt.close('all')


def full_kernel_check():
    from nbclient import NotebookClient
    for j,path in enumerate(nbpaths,1):
        print(f'[{j:02d}/{len(nbpaths)}] {path.name}',flush=True)
        nb=nbformat.read(path,as_version=4)
        NotebookClient(nb,timeout=180,kernel_name='python3',
                       resources={'metadata':{'path':str(root)}}).execute()


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--fast',action='store_true',help='Run Python cells in isolated namespaces; default')
    group.add_argument('--kernel',action='store_true',help='Run each notebook in a full Jupyter kernel')
    args=parser.parse_args()
    if len(nbpaths)!=24:
        raise RuntimeError(f'Expected exactly 24 notebooks, found {len(nbpaths)}')
    sys.path.insert(0,str(root/'src'))
    os.chdir(root)
    if args.kernel:
        full_kernel_check()
    else:
        fast_check()
    print(f'PASS: {len(nbpaths)} notebooks validated successfully.')
