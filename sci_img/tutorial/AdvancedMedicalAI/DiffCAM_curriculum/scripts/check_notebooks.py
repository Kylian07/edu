"""Validate/execute notebooks in teaching order.
Usage: python scripts/check_notebooks.py --structure
       python scripts/check_notebooks.py --execute
"""
import argparse
from pathlib import Path
import nbformat

root=Path(__file__).resolve().parents[1]
notebooks=sorted(p for p in root.rglob('*.ipynb') if '.ipynb_checkpoints' not in p.parts)
parser=argparse.ArgumentParser()
mode=parser.add_mutually_exclusive_group(required=True)
mode.add_argument('--execute', action='store_true')
mode.add_argument('--structure', action='store_true')
args=parser.parse_args()
print('Found',len(notebooks),'notebooks',flush=True)
if args.execute:
    from nbclient import NotebookClient
for i,p in enumerate(notebooks,1):
    nb=nbformat.read(p,as_version=4)
    nbformat.validate(nb)
    if args.execute:
        try:
            NotebookClient(nb,timeout=180,kernel_name='python3',resources={'metadata':{'path':str(root)}},allow_errors=False).execute()
        except Exception as e:
            print('FAILED:',p.relative_to(root),str(e)[:900],flush=True)
            raise
    print(f'{i:02d}/{len(notebooks)} OK {p.relative_to(root)}',flush=True)
print('SUCCESS')
