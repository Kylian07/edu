import numpy as np
from diffcam_edu import make_cell_images, reference_scatter, diffcam_weights, diffcam_map
from diffcam_edu.evaluation import mask_iou, pointing_game, area_under_precision_recall
from diffcam_edu.models import build_cnn, fit_cnn, feature_maps, embeddings_from_maps, gradcam


def test_images_reproducible():
    im,y,m=make_cell_images(n=20,seed=4)
    im2,y2,m2=make_cell_images(n=20,seed=4)
    assert im.shape==(20,32,32)
    assert np.array_equal(im,im2) and np.array_equal(y,y2)
    assert m[y==1].sum()>0 and not m[y==0].any()


def test_analytic_weights():
    refs=np.array([[0.,0.],[1.,0.],[0.,1.],[1.,1.]])
    target=np.array([2.,0.])
    mu,S=reference_scatter(refs)
    w=diffcam_weights(target,refs,ridge=.3)
    np.testing.assert_allclose((S+.3*np.eye(2))@w,target-mu,rtol=1e-9)
    assert np.isfinite(w).all()
    sal=diffcam_map(np.ones((2,3,3)),w)
    assert sal.shape==(3,3)


def test_singular_ridge():
    refs=np.ones((3,4))
    w=diffcam_weights(np.array([2.,1.,3.,0.]),refs,ridge=.5)
    assert np.isfinite(w).all()


def test_metrics():
    m=np.eye(4,dtype=bool)
    assert mask_iou(m,m)==1.
    assert pointing_game(m.astype(float),m)==1
    assert area_under_precision_recall(m.astype(float),m)>.99


def test_torch_shapes():
    images, labels, masks=make_cell_images(n=48,seed=4)
    model,history=fit_cnn(images,labels,epochs=2)
    maps=feature_maps(model,images[:3]); em=embeddings_from_maps(maps)
    assert maps.shape==(3,24,8,8) and em.shape==(3,24)
    sal,w=gradcam(model,images[0]); assert sal.shape==(8,8) and len(w)==24
