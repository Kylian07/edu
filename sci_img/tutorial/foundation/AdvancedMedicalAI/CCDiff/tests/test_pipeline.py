import numpy as np
import pytest
from ccdiff_edu import (make_cell_table, make_cell_images, make_shared_toy_embeddings,
                        normalize_rows, ccdiff_bidirectional, acc_at_k, bootstrap_ci)
from ccdiff_edu.pipeline import score_candidates

def test_toy_data_shapes():
    d=make_cell_table(8)
    assert d.shape==(16,6)
    images=make_cell_images(4,size=24)
    assert images['A'].shape==(4,24,24)

def test_normalize():
    x=normalize_rows([[3,4],[0,0]])
    assert np.allclose(x[0],[.6,.8])
    assert np.isfinite(x).all()

def test_ranking_pipeline():
    a,b,text,labels=make_shared_toy_embeddings(40)
    out=ccdiff_bidirectional(a,b,text,labels,top_k=8,n_components=3)
    for side in ('A_vs_B','B_vs_A'):
        assert len(out[side]['ranked'])>=1
        assert all(np.isfinite(v['score']) for v in out[side]['ranked'])
        assert all(0<=v['score']<=1+1e-8 for v in out[side]['ranked'])

def test_score_formula():
    selection={'relevance':np.array([.2,.6])}
    ranked=score_candidates([{'label':'x','rho':.1,'relevance':.6}],selection,alpha=.3)
    assert ranked[0]['score']==pytest.approx(.3*1+.7*.9)

def test_metric():
    assert acc_at_k([['a','b'],['c','d']],['b','c'],k=1)==.5
    assert acc_at_k([['a','b'],['c','d']],['b','c'],k=2)==1.
    ci=bootstrap_ci([0,1,0,1],n_boot=80)
    assert 0<=ci[0]<=ci[1]<=1
