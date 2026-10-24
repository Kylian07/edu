"""Small, offline-first teaching helpers for the DiffCAM curriculum.
Not an official implementation of the CVPR 2025 paper.
"""
from .data import make_cell_images, make_tabular_cells, make_chest_phantoms
from .math import diffcam_weights, diffcam_map, normalize_map, reference_scatter
from .evaluation import mask_iou, pointing_game, area_under_precision_recall
