# Optional extension: replacing synthetic vectors with real CLIP embeddings

**This is optional and may require a network connection, model download, more RAM, and appropriate usage rights.** The 24 core notebooks intentionally run without it.

## When to attempt

After finishing T11–T12, and preferably after completing T20. The aim is to confirm that genuine image and text embeddings can be put into the same feature space. A full benchmark replication requires the paper's exact backbone, generation model, preprocessing, samples, seeds, and evaluation pipeline; this extension uses a smaller model to introduce the interface only.

## Setup

```bash
pip install 'torch>=2.0' 'transformers>=4.40' 'Pillow>=9'
```

Obtain an image you have the right to use and save it as `my_cell.jpg`. Then run the following code in a separate notebook or script:

```python
from PIL import Image
from transformers import CLIPModel, CLIPProcessor
import torch

checkpoint = 'openai/clip-vit-base-patch32'  # introductory; NOT the paper's ViT-bigG-14
model = CLIPModel.from_pretrained(checkpoint).eval()
processor = CLIPProcessor.from_pretrained(checkpoint)
texts = [
    'a microscope image of elongated cells',
    'a microscope image of round cells',
    'a bright field microscopy image of a tissue section',
]
image = Image.open('my_cell.jpg').convert('RGB')
inputs = processor(text=texts, images=image, return_tensors='pt', padding=True)
with torch.inference_mode():
    out = model(**inputs)
    image_features = out.image_embeds
    text_features = out.text_embeds
    image_features = torch.nn.functional.normalize(image_features, dim=-1)
    text_features = torch.nn.functional.normalize(text_features, dim=-1)
    cosine_scores = image_features @ text_features.T
print(dict(zip(texts, cosine_scores[0].tolist())))
```

**Interpretation:** Values are relative embedding cosine similarities, not calibrated probabilities and not evidence of clinical diagnoses. Examine whether the model is appropriate for your biological image modality. Medical imaging may need specialized encoders and trained reviewers.

## Bridge to CCDiff

For a complete dataset: (1) encode every image into an `N x d` array; (2) encode each shared candidate phrase into a `K x d` array; (3) pass `X_A`, `X_B`, `Y_K` and labels to `ccdiff_bidirectional`. Observe how changing captions, embeddings, or per-set normalization changes the results. More realistic text encoders should be validated on the target domain.

## Paper-vs-lesson differences

| Item | Paper | Optional introductory extension |
|---|---|---|
| Image/text backbone (general benchmark) | CLIP ViT-bigG-14 | CLIP ViT-B/32 (smaller) |
| Captioning | BLIP-2 or domain vocabulary | Manually written list |
| Concepts retained | Top-k=20 | Student-chosen top-k |
| Candidate score | Alpha=0.3 | Alpha=0.3 by default |
| Evaluation | GPT-4-based semantic judge on named benchmarks | Manual exploratory inspection only |
| Medical data | Credentialed MIMIC-CXR experiment | No patient images provided |

Do not report demonstration outputs as the NeurIPS paper's replicated results.
