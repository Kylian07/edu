"""Small offline helpers for a biology-oriented CCDiff learning track."""
from ccdiff_edu.toy_data import make_cell_table, make_cell_images, make_shared_toy_embeddings
from ccdiff_edu.pipeline import (normalize_rows, select_concepts, inverse_cca_candidates,
                                 score_candidates, ccdiff_direction, ccdiff_bidirectional)
from ccdiff_edu.metrics import acc_at_k, bootstrap_ci
__version__ = '1.0.0'
