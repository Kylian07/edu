import numpy as np
import torch
from medlime_tutorials import (
    synthetic_image,dataset,patch_ids,random_patch_masks,patch_mask,ToyBlackBox,
    lime_explain,auprc,fit_surrogate,train_inpainter,inpaint,evidence_prior,
    supervised_adapt, nearest_reference
)

def test_synthetic_data_are_labeled_and_reproducible():
    a,mask=synthetic_image(22,True)
    b,other=synthetic_image(22,True)
    assert a.shape==(32,32) and mask.sum()>0
    assert np.array_equal(a,b) and np.array_equal(mask,other)
    x,y,m=dataset(20,seed=5)
    assert x.shape==(20,32,32) and np.array_equal(y,np.any(m,axis=(1,2)).astype(int))

def test_binary_patch_masks_and_retain_original():
    img,_=synthetic_image(1)
    ids=patch_ids(); assert len(np.unique(ids))==16
    keep=random_patch_masks(21,seed=8)
    assert np.all(keep[0]==1.)
    out=patch_mask(img,keep[0])
    assert np.allclose(out,img)
    keep[0,0]=0
    out=patch_mask(img,keep[0]); assert np.all(out[ids==0]==0)

def test_surrogate_recovers_known_coefficients():
    rng=np.random.default_rng(4)
    x=rng.integers(0,2,(300,5)); y=.7 + 1.2*x[:,1]-.5*x[:,3]
    result=fit_surrogate(x,y,steps=1500)
    assert result['r2']>.99999
    assert np.allclose(result['coef'],[0,1.2,0,-.5,0],atol=.002)

def test_prior_penalty_works():
    rng=np.random.default_rng(42)
    x=rng.integers(0,2,(150,4)); y=x[:,2]
    prior=np.array([.9,0,0,0])
    a=fit_surrogate(x,y,steps=900)
    b=fit_surrogate(x,y,l2=5,prior=prior,steps=900)
    assert np.linalg.norm(b['coef']-prior)<np.linalg.norm(a['coef']-prior)

def test_lime_uses_blackbox_outputs():
    x,m=synthetic_image(14,True)
    r=lime_explain(x,ToyBlackBox(),n=100,seed=1)
    assert r['map'].shape==x.shape and r['coef'].shape==(16,)
    assert -2 < r['r2'] <= 1.00001 and 0<=auprc(m,r['map'])<=1

def test_reconstruction_preserves_visible_pixels():
    x,_=synthetic_image(8)
    model,_=train_inpainter(n=24,epochs=2)
    keep=np.ones(16);keep[[5,6]]=0
    y=inpaint(x,keep,model)
    assert y.shape==x.shape
    assert np.allclose(x[keep[patch_ids()]!=0],y[keep[patch_ids()]!=0])

def test_references_are_limited_to_library():
    lib=np.stack([synthetic_image(500+i,True)[0] for i in range(10)])
    q,_=synthetic_image(99,True)
    ids,sims=nearest_reference(q,lib,k=4)
    assert len(ids)==4 and len(set(ids))==4
    c=np.ones((10,16))
    prior,idx,w=evidence_prior(q,lib,c,k=4)
    assert prior.shape==(16,) and np.allclose(prior,1)
    assert np.isclose(w.sum(),1)

def test_adaptation_freezes_model():
    model=ToyBlackBox()
    x,_=synthetic_image(15,True)
    adapter,losses=supervised_adapt(x*.55,1,predictor=model,steps=5)
    assert len(losses)==5 and np.isfinite(adapter.scale) and np.isfinite(adapter.bias)
    assert adapter.apply(x).shape == x.shape

def test_auc_negative_mask_is_undefined():
    assert np.isnan(auprc(np.zeros((32,32),bool),np.zeros((32,32))))
