"""Validate the 26 notebooks and optionally run their cells via nbclient."""
from pathlib import Path
import sys
import nbformat
from nbformat.validator import validate

folder=Path(__file__).resolve().parent/'notebooks'
paths=sorted(folder.glob('*.ipynb'))
assert len(paths)==26,f'Expected 26 notebooks, found {len(paths)}'
for path in paths:
 nb=nbformat.read(path,as_version=4)
 validate(nb)
 assert nb.cells[0].cell_type=='markdown'
 assert any(c.cell_type=='code' for c in nb.cells)
 print('schema ok',path.name)
if '--execute' in sys.argv:
 from nbclient import NotebookClient
 for path in paths:
  nb=nbformat.read(path,as_version=4)
  try:
   NotebookClient(nb,timeout=150,kernel_name='python3').execute()
   print('execute ok',path.name)
  except Exception as e:
   print('EXECUTION FAILED:',path,e)
   raise
