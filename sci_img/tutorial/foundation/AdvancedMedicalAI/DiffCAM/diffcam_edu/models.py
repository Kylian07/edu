"""Small CPU-compatible CNN used in advanced tutorials.
Imports torch lazily; early notebooks work without it.
"""
import numpy as np


def require_torch():
    try:
        import torch
        from torch import nn
        return torch, nn
    except ImportError as exc:
        raise ImportError('Install extras: pip install -r requirements-torch.txt') from exc


def build_cnn(seed=13):
    torch, nn = require_torch()
    torch.manual_seed(seed)
    class TinyCNN(nn.Module):
        def __init__(self):
            super().__init__()
            self.features = nn.Sequential(
                nn.Conv2d(1, 8, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
                nn.Conv2d(8, 16, 3, padding=1), nn.ReLU(),
                nn.Conv2d(16, 24, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2))
            self.classifier = nn.Linear(24, 2)
        def forward(self, x):
            maps = self.features(x)
            return self.classifier(maps.mean(dim=(-2,-1)))
    return TinyCNN()


def fit_cnn(images, labels, epochs=6, seed=13, batch_size=64, lr=0.01):
    torch, nn = require_torch()
    torch.set_num_threads(min(2, torch.get_num_threads()))
    torch.manual_seed(seed)
    model = build_cnn(seed)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    x = torch.tensor(np.asarray(images), dtype=torch.float32)[:,None]
    y = torch.tensor(np.asarray(labels), dtype=torch.long)
    rng = np.random.default_rng(seed)
    history=[]
    for epoch in range(epochs):
        model.train()
        inds=rng.permutation(len(x))
        total=0.
        for chunk in np.array_split(inds, max(1,int(np.ceil(len(inds)/batch_size)))):
            opt.zero_grad()
            loss=nn.functional.cross_entropy(model(x[chunk]),y[chunk])
            loss.backward()
            opt.step()
            total+=float(loss.detach())*len(chunk)
        history.append(total/len(x))
    model.eval()
    return model, history


def feature_maps(model, images):
    torch, _ = require_torch()
    x=torch.tensor(np.asarray(images),dtype=torch.float32)
    if x.ndim==2: x=x[None,None]
    elif x.ndim==3: x=x[:,None]
    with torch.no_grad():
        maps=model.features(x)
    return maps.numpy()


def embeddings_from_maps(maps):
    return np.asarray(maps).mean(axis=(-2,-1))


def gradcam(model, image, class_index=1):
    torch,_=require_torch()
    x=torch.tensor(np.asarray(image),dtype=torch.float32)[None,None]
    maps=model.features(x)
    maps.retain_grad()
    logits=model.classifier(maps.mean(dim=(-2,-1)))
    model.zero_grad(set_to_none=True)
    logits[0,class_index].backward()
    grads=maps.grad[0].mean(dim=(-2,-1))
    weights=grads.detach().numpy()
    heat=(maps[0].detach().numpy()*weights[:,None,None]).sum(axis=0)
    return np.maximum(heat,0), weights
