"""Regenerate the twelve pedagogical notebooks deterministically."""
from pathlib import Path
import nbformat as nbf

HERE=Path(__file__).parent
OUT=HERE/'notebooks'; OUT.mkdir(parents=True,exist_ok=True)
SETUP = '''from pathlib import Path
import sys
here = Path.cwd()
for candidate in (here, here.parent, here.parent.parent):
    if (candidate / 'medlime_tutorials.py').exists():
        sys.path.insert(0, str(candidate.resolve())); break
else:
    raise FileNotFoundError('Open Jupyter from the MedLIME folder or its notebooks/ subfolder')
import numpy as np
import matplotlib.pyplot as plt
from medlime_tutorials import *
np.set_printoptions(precision=3, suppress=True)
'''

BOOKS=[]
def book(filename, title, weeks, prereq, objective, sections, takeaways, exercises, checkpoint):
    cells=[]
    cells.append(nbf.v4.new_markdown_cell(f'''# {title}

**MedLIME Learning Track — Notebook {len(BOOKS)+1:02d}/12** · Curriculum weeks {weeks} · Suggested time: 60–100 minutes

**Before starting:** {prereq}

**Learning goal:** {objective}

> **Important:** All images below are synthetic visual teaching phantoms, **not real medical images**. The educational implementations are **not** the original MedLIME implementation, are not evaluated for clinical use, and do not establish diagnostic or explanation reliability.
'''))
    cells.append(nbf.v4.new_code_cell(SETUP))
    for kind, text in sections:
        if kind=='md': cells.append(nbf.v4.new_markdown_cell(text))
        else: cells.append(nbf.v4.new_code_cell(text))
    cells.append(nbf.v4.new_markdown_cell('''## What you should now understand
'''+ '\n'.join(f'- {x}' for x in takeaways)+'''\n\n## Try it yourself (do not just read the code)\n'''+ '\n'.join(f'{i+1}. {x}' for i,x in enumerate(exercises))+'''\n\n## Exit ticket
'''+checkpoint+'''\n\nRecord your answers in a new Markdown cell before moving to the next notebook. Many questions have more than one reasonable answer; explain your evidence.'''))
    nb=nbf.v4.new_notebook(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'},'medlime_track':{'module':len(BOOKS)+1,'scope':'educational'}})
    nbf.validate(nb)
    nbf.write(nb,OUT/filename)
    BOOKS.append((filename,title,weeks))

book('01_medical_images_and_labels.ipynb','Medical images, labels, and lesion localization','1–4','No programming or medical-imaging background required.', 'Distinguish image classification from lesion localization and run your first Python image experiment.',[
('md',r'''## Biology question: What does *abnormal* mean?
A radiologist may determine whether an image contains an abnormal finding (**classification**) and may also indicate *where* the finding lies (**localization**). These are different data tasks. Here we create a toy image that vaguely resembles two tissue regions, not a real chest radiograph.

**Mini-math:** An image is a rectangular array of pixel intensities between 0 and 1. A lesion mask is a separate array of `True`/`False` values.'''),
('code',r'''healthy, mask0 = synthetic_image(seed=4, lesion=False)
sick, lesion_mask = synthetic_image(seed=4, lesion=True)
fig=show_images([healthy,sick,lesion_mask.astype(float)],
               ['synthetic normal','synthetic lesion (green = location)','binary lesion mask'],
               masks=[mask0,lesion_mask,lesion_mask])
plt.show()'''),
('md',r'''## Which numbers describe these images?
The classifier will later learn the **label** 0 or 1. The **mask** has one entry for each pixel; it encodes location, not diagnosis by itself. Inspect shapes and summary statistics.'''),
('code',r'''print('Image shape:', sick.shape, 'data type:', sick.dtype)
print('Image intensity range:', float(sick.min()), 'to', float(sick.max()))
print('Number of pixels annotated as lesion:', int(lesion_mask.sum()))
print('Percentage occupied:', round(100*lesion_mask.mean(),2), '%')
assert sick.shape == lesion_mask.shape == (32,32)'''),
('md',r'''## Create a tiny dataset
`dataset` samples images, image-level labels, and masks. Real studies require annotation protocols, privacy review, patient-disjoint splits, and quality assurance.'''),
('code',r'''images, labels, masks = dataset(n=12, seed=11)
print('labels:', labels.tolist(), '| images:', images.shape, '| masks:', masks.shape)
fig=show_images(images[:6], [f'label={y}' for y in labels[:6]], masks=masks[:6], ncols=3)
plt.show()'''),
],["An image-level label does not tell us which pixels caused a prediction.","A lesion mask provides spatial ground truth for a *localization* evaluation.","The educational simulator is not real biological evidence."],
["Change the random seed and identify three ways the toy images differ.","Write one sentence explaining why a false positive can still have a plausible-looking heatmap."],
"**Question:** If a classifier reports 95% accuracy, have we demonstrated that its explanations point to lesions? Why or why not?")

book('02_pixels_filters_and_patches.ipynb','Pixels, filters, and image patches','5–8','Notebook 01 (arrays, masks).','Use NumPy indexing and patch masks to construct image perturbations.',[
('md',r'''## A picture is an array
Use array slices to edit square regions. In a 32×32 image, a 4×4 patch grid has 16 patches, each 8×8 pixels. LIME later treats each patch as an interpretable feature.'''),
('code',r'''image, lesion = synthetic_image(seed=14)
print('Top-left 4x4 pixel values:\n',image[:4,:4])
modified=image.copy(); modified[8:16,8:16]=0
fig=show_images([image,modified,np.abs(image-modified)],['original','edited (rows 8:16)','absolute change'])
plt.show()'''),
('md',r'''## Build a binary patch mask
A one means retain the patch; zero means hide it. Unlike arbitrary pixel deletion, patches help maintain local structure and produce a small interpretable feature set.'''),
('code',r'''identifiers=patch_ids()
print('Distinct patch ids:',np.unique(identifiers))
keep=np.ones(16,np.float32); keep[5]=0; keep[10]=0
masked=patch_mask(image,keep,fill='zero')
fig=show_images([identifiers/15,image,masked],['patch numbers scaled 0..1','original','hide patches 5 and 10'],cmap='gray')
plt.show()'''),
('md',r'''## Compare image processing choices
A Gaussian filter averages pixels nearby, reducing noise but also blurring small findings. A patch mask hides a selected region. Do not confuse *masking* with a true biological intervention.'''),
('code',r'''from scipy.ndimage import gaussian_filter
blurred=gaussian_filter(image, sigma=1.5)
fig=show_images([image,blurred,patch_mask(image,keep,fill='mean'),patch_mask(image,keep,fill='blur')],
 ['original','Gaussian smoothing','mean fill','blur fill'])
plt.show()
print('Mean intensity before/after smoothing:',round(float(image.mean()),3),round(float(blurred.mean()),3))'''),
],["An image pixel is numerical data and masks select subsets of pixels.","A 4x4 patch grid gives 16 binary LIME features.","Filters, missingness, and image perturbation are different operations."],
["Hide four chosen patches by setting their corresponding `keep` values to 0.","Change `sigma` and describe the risk to a very small lesion."],
"**Question:** Why might a black square be unlike anything a medical imaging model saw during training?")

book('03_classification_and_deep_learning.ipynb','Classification, overfitting, and neural networks','9–16','Notebooks 01–02; basic Python arrays.','Train a low-compute classifier and separate predictive accuracy from explanation quality.',[
('md',r'''## From numbers to predictions
A classifier converts image features into a score. We will use a separate train and test set and compare logistic regression with a tiny neural network. We extract the maximum brightness in each 8×8 region; **this engineered feature is part of the teaching setup**, not a clinical biomarker.

**Mini-math:** logistic regression uses \(p(y=1|x)=1/(1+e^{-(w^Tx+b)})\). A loss function penalizes wrong probabilities.'''),
('code',r'''from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
Xtrain,ytrain,_=dataset(220,seed=100)
Xtest,ytest,_=dataset(100,seed=200)
def features(images):
    a=np.asarray(images)
    return a.reshape(len(a),4,8,4,8).max(axis=(2,4)).reshape(len(a),16)
clf=LogisticRegression(max_iter=600).fit(features(Xtrain),ytrain)
probs=clf.predict_proba(features(Xtest))[:,1]
print('Holdout accuracy:',accuracy_score(ytest,probs>=.5))
print('Confusion matrix:\n',confusion_matrix(ytest,probs>=.5))'''),
('md',r'''## A two-layer neural network
Here PyTorch optimizes weights using gradients. In later notebooks we use a fixed deterministic black box instead, because stable examples keep attention on the explanation methods; you may substitute your own trained classifier when ready.'''),
('code',r'''import torch
from torch import nn
torch.manual_seed(4)
net=nn.Sequential(nn.Linear(16,24),nn.ReLU(),nn.Linear(24,1))
optimizer=torch.optim.Adam(net.parameters(),lr=.04)
train_x=torch.tensor(features(Xtrain),dtype=torch.float32)
train_y=torch.tensor(ytrain[:,None],dtype=torch.float32)
for epoch in range(45):
    logits=net(train_x)
    loss=nn.functional.binary_cross_entropy_with_logits(logits,train_y)
    optimizer.zero_grad(); loss.backward(); optimizer.step()
with torch.no_grad():
    test_scores=torch.sigmoid(net(torch.tensor(features(Xtest),dtype=torch.float32))).numpy().ravel()
print('Tiny MLP holdout accuracy:',accuracy_score(ytest,test_scores>=.5))
print('Last training BCE loss:',round(float(loss.detach()),4))'''),
('md',r'''## Is a correct classification enough?
Visualize a correct image, label, and probability. A probability is **not** a saliency map; it contains no location information. Also note that evaluating on the same samples used for training would conceal overfitting.'''),
('code',r'''idx=int(np.flatnonzero(ytest==1)[0])
show_images([Xtest[idx],(Xtest[idx]>.7).astype(float)],
            [f'positive image; p={probs[idx]:.2f}','crude threshold, NOT explanation'])
plt.show()'''),
],["Separate training and test sets before evaluating a model.","Predictive accuracy does not imply correct localization.","Neural network parameters are learned by minimizing a loss using gradients."],
["Reduce the training set to 20 images. What happens to holdout accuracy?", "Compare the engineered max-intensity features with patch-average intensity."],
"**Question:** Why might the 16 engineered features fail on a real mammogram or chest X-ray?")

book('04_lime_from_scratch.ipynb','Implement local interpretable explanations (LIME)','17–20','Notebook 03; binary patch masks and linear regression.','Implement perturbation-based explanation without querying neural-network gradients.',[
('md',r'''## Question: which patch drives the output?
LIME samples masks, asks a black-box predictor for the score of each perturbed image, and fits a local weighted linear surrogate. The coefficients approximate local patch influence, not causal biological effects.

For masks \(z_i\), scores \(f(x(z_i))\), and proximity weights \(\pi_i\), estimate \(w,b\) by minimizing \(\sum_i\pi_i(f(x(z_i)) - b - z_i^\top w)^2\).'''),
('code',r'''x, lesion=synthetic_image(seed=6)
g=ToyBlackBox()  # Fixed detector; explanation only uses predict_proba.
print('Positive class score of original image:',round(float(g.predict_proba(x)[0]),3))
keep=random_patch_masks(n=180,seed=11)
perturbed=masked_examples(x,keep,fill='zero')
response=g.predict_proba(perturbed)
print('Shapes: masks, images, scores', keep.shape, perturbed.shape, response.shape)
show_images([x,perturbed[5],perturbed[10]],['original','sample perturbation','another perturbation'])
plt.show()'''),
('md',r'''## Weighted regression
Masks close to the original image receive a higher weight. Interpret positive regression coefficients as patches whose presence tends to raise the local score under the chosen perturbation rule.'''),
('code',r'''weights=lime_kernel(keep,bandwidth=.75)
fit=fit_surrogate(keep,response,sample_weight=weights)
heatmap=coef_map(fit['coef'])
print('Local surrogate weighted R²:',round(fit['r2'],3))
print('Pixelwise AUPRC (positive class vs lesion mask):',round(auprc(lesion,heatmap),3))
fig=show_images([x,lesion.astype(float),heatmap],['synthetic image','true lesion mask','LIME patch coefficients'],cmap='viridis')
plt.show()'''),
('md',r'''## Why not rely only on R²?
A surrogate can reproduce a model that relies on a scanner artifact instead of a lesion. Good local fitting and faithful medical localization measure different properties.'''),
('code',r'''plt.figure(figsize=(5,3))
plt.scatter(keep.mean(axis=1), response, c=weights, cmap='viridis',s=16)
plt.xlabel('Fraction of visible patches');plt.ylabel('Black-box score')
plt.title('Perturbation neighborhood');plt.colorbar(label='LIME proximity weight');plt.show()'''),
],["LIME is black-box: it needs model outputs but not weights or gradients.","A local linear coefficient measures sensitivity under a chosen perturbation design.","Good surrogate fit is not a guarantee of clinical localization."],
["Try `n=40`, `n=180`, and `n=500`; record saliency stability.","Change `bandwidth` to 0.3 and 1.2. What neighborhood does the regression emphasize?"],
"**Question:** Why does changing the masking operator change the meaning of the LIME explanation?")

book('05_perturbation_and_distribution_shift.ipynb','When naive image masking fails','21–24','Notebook 04: LIME.','Observe how masking can produce unnatural inputs and unstable explanatory coefficients.',[
('md',r'''## In-distribution vs out-of-distribution
Medical classifiers are typically trained on images with tissue structure, not black rectangles. Explaining their responses to implausible perturbations can be misleading. The masking rule is therefore a *scientific assumption*.

We compare three cheap fills: zero (black), global image mean, and Gaussian blur. None is guaranteed to be realistic.'''),
('code',r'''x,m=synthetic_image(21)
keep=np.ones(16);keep[[5,6,9,10]]=0
variants=[patch_mask(x,keep,fill=f) for f in ['zero','mean','blur']]
show_images([x,*variants],['original','black fill','global mean','blur fill'])
plt.show()
for name,z in zip(['original','black','mean','blur'],[x,*variants]):
 print(f'{name:>8}: p(lesion) = {ToyBlackBox().predict_proba(z)[0]:.4f}; mean pixel intensity={z.mean():.3f}')'''),
('md',r'''## Same model, different local explanations
Holding the query, masks, and fitted objective fixed, change only the perturbation operator. Differences are evidence that explanation depends on the data-generation mechanism.'''),
('code',r'''results={fill:lime_explain(x,n=150,seed=4,fill=fill) for fill in ['zero','mean','blur']}
show_images([r['map'] for r in results.values()],list(results),cmap='viridis')
plt.show()
for k,v in results.items(): print(k,'AUPRC',round(auprc(m,v['map']),3),'R²',round(v['r2'],3))'''),
('md',r'''## Explore stability across sampling seeds
A useful explanation should not swing wildly when we change the random masks. Here we use the standard deviation across repeated coefficient maps as a simple stability diagnostic.'''),
('code',r'''heatmaps=[lime_explain(x,n=100,seed=s,fill='zero')['map'] for s in range(3)]
print('Mean pixelwise coefficient standard deviation:',np.std(heatmaps,axis=0).mean().round(4))
show_images([np.std(heatmaps,axis=0)],['explanation instability'],cmap='viridis')
plt.show()'''),
],["Masking can shift image statistics outside a model's training distribution.","Masking rules affect LIME coefficients even with identical random masks.","Explanation stability requires an explicit measurement and is not automatic."],
["Find a seed for which blur-fill and black-fill disagree about the top patch.","Explain why matching simple means/variances does not establish in-distribution samples."],
"**Question:** If reconstructed tissue looks convincing, is it necessarily medically correct?")

book('06_learning_to_reconstruct_masked_images.ipynb','Learned masked-image reconstruction','21–24','Notebook 05; beginner PyTorch experience.','Train a lightweight self-supervised masked-image reconstructor and audit hallucination.',[
('md',r'''## From masking to reconstruction
Generative masking in MedLIME is motivated by avoiding unnatural holes. A masked autoencoder learns to predict missing image content using observed context. Our **tiny convolutional inpainter is NOT a masked-autoencoder transformer**: it teaches the core input/target/loss workflow on CPU before students study MAE papers and implementations.

Training target: original image \(x\); observed input: \(m\odot x\). The target includes no radiologist diagnosis.'''),
('code',r'''model,losses=train_inpainter(n=96,epochs=8,seed=10)
plt.plot(losses,marker='o');plt.xlabel('Epoch');plt.ylabel('Last minibatch weighted MSE');plt.title('Self-supervised reconstruction training');plt.show()
print('Model class:',type(model).__name__)'''),
('md',r'''## Does the model preserve known information?
Observed pixels are copied from the original. Only hidden pixels come from predictions. Compare reconstruction error to simple baselines, not just visual plausibility.'''),
('code',r'''x,m=synthetic_image(seed=40)
keep=np.ones(16);keep[[5,6,9,10]]=0
reconstructed=inpaint(x,keep,model)
black=patch_mask(x,keep,fill='zero')
blur=patch_mask(x,keep,fill='blur')
show_images([x,black,blur,reconstructed],['original','black fill','blur fill','learned reconstruction'])
plt.show()
hidden=(keep[patch_ids()]==0)
for name,z in [('zero',black),('blur',blur),('learned',reconstructed)]:
 print(name,'masked-region MSE:',round(float(np.mean((x[hidden]-z[hidden])**2)),5))
assert np.allclose(x[~hidden],reconstructed[~hidden])'''),
('md',r'''## A critical limitation
A reconstructor may erase a lesion that was present in a masked patch, or hallucinate a bright spot that was absent. Visual naturalness is *not* proof that a generated image preserves pathology. This is central to MedLIME's scientific interpretation.'''),
('code',r'''visible_lesion=np.count_nonzero(m & ~hidden)
hidden_lesion=np.count_nonzero(m & hidden)
print('Lesion pixels still observed:',visible_lesion,'lesion pixels hidden:',hidden_lesion)
print('Average intensity in hidden lesion before/after:',
      round(float(x[m & hidden].mean()),3) if hidden_lesion else 'not hidden',
      round(float(reconstructed[m & hidden].mean()),3) if hidden_lesion else 'not hidden')'''),
],["Self-supervised learning can use images as their own reconstruction targets.","Missing-pixel MSE tests numerical accuracy; realism and pathology preservation need other tests.","A small CNN inpainter teaches mechanics but does not replicate the MedLIME MAE."],
["Use a different mask to hide the complete synthetic lesion and record whether it returns.","Train for 2 versus 12 epochs; compare masked-region error on a held-out image."],
"**Question:** Why can very good reconstruction MSE still correspond to a poor explanation of a rare lesion?")

book('07_generative_masking_in_lime.ipynb','LIME with learned generative masking','21–24','Notebooks 04 and 06.','Replace black masking with learned image reconstruction inside LIME.',[
('md',r'''## Full perturbation pipeline
For each sampled patch mask \(z\), reconstruct a partially hidden query, pass it to the black-box model, then regress its scores on \(z\). This is a **toy analogue** of the paper's Generative Masking (GM), not a replacement for the paper's pretrained MAE.'''),
('code',r'''model,_=train_inpainter(n=96,epochs=8,seed=10)
x,lesion=synthetic_image(seed=13)
black=lime_explain(x,n=140,seed=8,fill='zero')
learned=lime_explain(x,n=140,seed=8,fill='learned',inpainter=model)
show_images([x,lesion.astype(float),black['map'],learned['map']],
 ['original','ground truth','LIME: black mask','LIME: learned mask'],cmap='viridis')
plt.show()'''),
('md',r'''## Quantify both localization and surrogate agreement
AUPRC uses lesion pixels as positives; R² quantifies how well the fitted surrogate predicts the black-box scores of generated perturbations. Neither alone establishes causal faithfulness.'''),
('code',r'''for name,r in [('black',black),('learned',learned)]:
 print(name,'AUPRC=',round(auprc(lesion,r['map']),3),'R²=',round(r['r2'],3),
       'score range=',tuple(np.round([r['scores'].min(),r['scores'].max()],3)))
print('Top patch (black):',int(np.argmax(black['coef'])))
print('Top patch (learned):',int(np.argmax(learned['coef'])))'''),
('md',r'''## Pairwise ablation
Evaluate multiple query seeds, always with the same perturbation masks for each pair. It is possible for the tiny inpainter to **lose** to black masking; the important scientific skill is to report it without hiding failures.'''),
('code',r'''rows=[]
for seed in [2,3,4,5]:
    q,gt=synthetic_image(seed,True)
    a=lime_explain(q,n=96,seed=22,fill='zero')
    b=lime_explain(q,n=96,seed=22,fill='learned',inpainter=model)
    rows.append([seed,auprc(gt,a['map']),auprc(gt,b['map'])])
print('seed | zero-fill AUPRC | learned-fill AUPRC')
for r in rows: print(r[0],round(r[1],3),round(r[2],3))'''),
],["Generative masking changes the perturbation *distribution* before regression.","Identical masks support a controlled comparison of filling strategies.","A teaching reconstructor may not improve localization; report both successes and failures."],
["Compare the learned reconstructor with `fill='blur'` on the same sample.","Choose one sample with worse learned-mask AUPRC and explain a likely cause."],
"**Question:** What does the LIME regression assume about reconstruction consistency as the binary mask changes?")

book('08_distribution_shift_and_transforms.ipynb','Distribution shift and test-time transformations','25–28','Notebooks 03–07.','Diagnose scanner-like appearance changes and understand input transformation families.',[
('md',r'''## A simple distribution shift
A model trained on one acquisition protocol may receive darker or lower-contrast images from another protocol. We simulate that situation numerically without pretending the effect captures real scanner physics.

**Terms:** source distribution = images used to establish a model; target distribution = images encountered after deployment. A transform \(T_\phi(x)=\mathrm{clip}(a x+b)\) changes brightness and contrast.'''),
('code',r'''x,gt=synthetic_image(seed=36,lesion=True)
dark=x*.58
bright=np.clip(x*1.15+.06,0,1)
g=ToyBlackBox()
show_images([x,dark,bright],['source-like','target: darker','target: brighter'])
plt.show()
for name,z in zip(['source','dark','bright'],[x,dark,bright]):
 print(name,'mean',round(float(z.mean()),3),'probability',round(float(g.predict_proba(z)[0]),5))'''),
('md',r'''## Check a population, not only a selected image
Applying a transformation that helps one positive example could harm other patients or healthy images. Measure behavior across both classes.'''),
('code',r'''images,labels,_=dataset(80,seed=82)
scores_source=g.predict_proba(images)
scores_dark=g.predict_proba(images*.58)
print('Fraction called positive at threshold .5:')
for name,s in [('source',scores_source),('dark',scores_dark)]:
 print(name,'true positives',round(np.mean(s[labels==1]>.5),3),
       'false positives',round(np.mean(s[labels==0]>.5),3))
plt.hist(scores_source,bins=12,alpha=.5,label='source');plt.hist(scores_dark,bins=12,alpha=.5,label='dark')
plt.xlabel('Predicted positive probability');plt.ylabel('Count');plt.legend();plt.show()'''),
('md',r'''## Why optimization enters the picture
Instead of selecting brightness by eye, we could choose trainable \(a,b\) using an objective. But which supervision signals are legitimately available at test time? If you use the true label of the query, that creates a supervised setting that differs from label-free deployment.'''),
('code',r'''transforms=[AffineAdapter(scale=s,bias=b) for s,b in [(1,0),(1.2,.0),(1.0,.12),(1.2,.12)]]
for t in transforms:
 print(f'scale={t.scale:.1f}, bias={t.bias:.2f}: p={g.predict_proba(t.apply(dark))[0]:.4f}')'''),
],["Brightness and contrast shifts can change model behavior even if pathology is unchanged.","A transformation family has parameters that can be optimized.","Test-time supervision availability must be stated, not assumed."],
["Plot score changes for darker shifts at factors 0.9, 0.7, 0.5.","Find a global brightness change that helps positives but produces false positives."],
"**Question:** Why would optimizing each test query using its true label create a challenging deployment assumption?")

book('09_supervised_test_time_adaptation.ipynb','Supervised test-time adaptation (teaching analogue)','25–28','Notebook 08; gradients and binary cross-entropy.','Optimize a lightweight input transform with a frozen model and examine the supervision assumptions.',[
('md',r'''## What adaptation means here
We **freeze** the predictor and optimize just scale and bias, using a labeled, darkened *synthetic* query. This uses the predictor's gradient during adaptation even though subsequent LIME explanation queries remain black-box. The label is explicitly provided by the experimenter. This is a **deliberate simplification** of MedLIME STTA, whose architectural and supervision details must be read from the paper before attempting reproduction.

Objective (toy): binary cross entropy \(\ell(g(T_\phi(x)),y) + \eta\lVert\phi-\phi_0\rVert^2\).'''),
('code',r'''q,mask=synthetic_image(seed=18,lesion=True)
target=q*.58
black_box=ToyBlackBox()
print('Original probability',float(black_box.predict_proba(q)[0]))
print('Shifted probability',float(black_box.predict_proba(target)[0]))
adapter,history=supervised_adapt(target,true_label=1,predictor=black_box,steps=55)
print('Adapted transformation:',adapter)
print('Adapted probability',float(black_box.predict_proba(adapter.apply(target))[0]))
plt.plot(history);plt.xlabel('Optimization step');plt.ylabel('BCE + regularizer');plt.title('Toy supervised adaptation');plt.show()'''),
('md',r'''## Can we interpret transformed predictions?
The adapter is fitted on the single query's label. This is optimistic supervision and must never be counted as an independent blind-test localization result. In real experiments, document how each supervised adaptation target becomes available.'''),
('code',r'''baseline=lime_explain(target,black_box,n=130,seed=17,fill='zero')
adapted=lime_explain(target,black_box,n=130,seed=17,fill='zero',adapt=adapter)
show_images([target,adapter.apply(target),baseline['map'],adapted['map']],
 ['dark query','adapted query','LIME before','LIME after adaptation'],cmap='viridis')
plt.show()
print('AUPRC before/after:',round(auprc(mask,baseline['map']),3),round(auprc(mask,adapted['map']),3))'''),
('md',r'''## Stress test on a negative case
Unconstrained supervised adaptation of a positive case can shift all pixels upward, making an unrelated normal image appear positive. Avoid inferring calibration or clinical robustness from one-case training.'''),
('code',r'''normal,_=synthetic_image(seed=19,lesion=False)
print('Normal score without adapter:',round(float(black_box.predict_proba(normal*.58)[0]),5))
print('Normal score with positive-query adapter:',round(float(black_box.predict_proba(adapter.apply(normal*.58))[0]),5))'''),
],["During toy adaptation, model weights stay frozen; only input-transform parameters change.","A differentiable optimization experiment can clarify why an objective changes predictions.","True-label test-time supervision is a major assumption; never conceal it."],
["Try weight_decay=0.2 versus 0.01 and examine changes to transformed intensity.","Optimize with an intentionally incorrect label and report the resulting failure."],
"**Question:** Is a transformed image that increases confidence necessarily more faithful to the original pathology?")

book('10_neighbor_evidence_and_similarity.ipynb','Reference cases, similarity, and evidence priors','29–32','Notebook 04; array distances and averaging.','Build a reference-only evidence library and use weighted neighbor explanations as a prior.',[
('md',r'''## How might past images help?
Evidence-based regularization aims to stabilize explanations by using related reference examples. Here we use cosine similarity on pooled intensities, retrieve top-k library images, calculate their LIME maps, and average the patch coefficients.

Crucially, **reference images must be separate from held-out queries**. This lesson uses no query labels, query lesion masks, or nearest-neighbor ground truth to compute the prior. It is still a simplified approximation of paper EBR.'''),
('code',r'''library=np.stack([synthetic_image(1000+i,True)[0] for i in range(18)])
query,ground_truth=synthetic_image(seed=71,lesion=True)
idx,sims=nearest_reference(query,library,k=4)
print('Selected reference indices:',idx,'similarities:',np.round(sims,4))
show_images([query,*library[idx]],['held-out query']+[f'neighbor {j}' for j in idx])
plt.show()'''),
('md',r'''## Each neighbor has an explanation
Compute local coefficients for the reference images using the same black-box predictor, perturbation budget, and mask strategy.'''),
('code',r'''reference_coef=[]
for ref in library:
    fit=lime_explain(ref,n=75,seed=19)
    reference_coef.append(fit['coef'])
reference_coef=np.asarray(reference_coef)
print('Reference explanations array:',reference_coef.shape)
prior,ids,weights=evidence_prior(query,library,reference_coef,k=4,bandwidth=.05)
print('Neighbor contribution weights:',np.round(weights,3))
show_images([coef_map(reference_coef[j]) for j in ids]+[coef_map(prior)],
 [f'neighbor {j}' for j in ids]+['evidence prior'],cmap='viridis')
plt.show()'''),
('md',r'''## A statistical and ethical caution
A similar *looking* image may have different pathology. Similarity in a pooled intensity space is not clinical equivalence, and using a reference pool with mislabeled or duplicate patients can invalidate the analysis.'''),
('code',r'''print('Prior coefficient spread:',round(float(prior.min()),4),'to',round(float(prior.max()),4))
for bandwidth in [.01,.05,.2]:
    p,_,w=evidence_prior(query,library,reference_coef,k=4,bandwidth=bandwidth)
    print('bandwidth',bandwidth,'effective max neighbor weight',round(float(w.max()),3),
          'prior norm',round(float(np.linalg.norm(p)),3))'''),
],["A similarity metric maps each image to a neighborhood of reference examples.","Neighbor explanations can form a soft prior, not absolute ground truth.","Query/reference separation and provenance matter for valid evaluation."],
["Change the number of neighbors from 2 to 10; plot the evidence prior.","Insert a duplicated query into the reference library; describe why this would be a leakage risk."],
"**Question:** How could systematic differences between scanners make intensity-based nearest neighbors misleading?")

book('11_evidence_based_regularization.ipynb','Evidence-regularized local surrogates','29–32','Notebooks 04 and 10; ridge regression intuition.','Fit a sparse local surrogate with an evidence-derived soft prior and inspect hyperparameters.',[
('md',r'''## Put evidence in the objective
The toy loss is

\[L(w,b)=\frac1N\sum_i \pi_i\,(f(x_i)-b-z_i^Tw)^2+\lambda_1\lVert w\rVert_1+\lambda_2\lVert w-w_{ref}\rVert_2^2.\]

`lambda1` encourages fewer important patches; `lambda2` encourages agreement with the neighbor evidence. Both can also *hurt* if chosen poorly. This mirrors the paper's broad EBR motivation but is **not asserted to reproduce its exact optimization**.'''),
('code',r'''query,lesion=synthetic_image(seed=27,lesion=True)
reference=np.stack([synthetic_image(3000+i,True)[0] for i in range(18)])
reference_coef=np.asarray([lime_explain(ref,n=75,seed=3)['coef'] for ref in reference])
prior,ids,weights=evidence_prior(query,reference,reference_coef,k=5)
base=lime_explain(query,n=170,seed=9)
regularized=lime_explain(query,n=170,seed=9,l1=.003,l2=.15,prior=prior)
show_images([query,lesion.astype(float),base['map'],coef_map(prior),regularized['map']],
 ['query','lesion mask','LIME','evidence prior','regularized LIME'],cmap='viridis',ncols=3)
plt.show()'''),
('md',r'''## Diagnose the trade-off
Increase the prior penalty, and the learned patch weights should approach the reference weights. But an inaccurate prior may degrade lesion localization even as the objective gets smaller.'''),
('code',r'''for strength in [0,.01,.1,.4,2.]:
    r=lime_explain(query,n=170,seed=9,l1=.003,l2=strength,prior=prior)
    print('lambda2=',strength,'local R²=',round(r['r2'],3),
          '||w-prior||=',round(float(np.linalg.norm(r['coef']-prior)),3),
          'AUPRC=',round(auprc(lesion,r['map']),3))'''),
('md',r'''## Why regularize at all?
With limited black-box queries, many patch coefficients can fluctuate. A sparse penalty and a reference-informed penalty trade freedom for constraints. Constraints lower variance when useful, but create bias when wrong.'''),
('code',r'''fig,axs=plt.subplots(1,2,figsize=(9,3))
axs[0].bar(range(16),base['coef']);axs[0].set_title('No evidence penalty')
axs[1].bar(range(16),regularized['coef']);axs[1].set_title('Evidence penalty')
for ax in axs: ax.set_xlabel('Patch id');ax.set_ylabel('Coefficient')
plt.tight_layout();plt.show()'''),
],["The local fit, sparsity, and evidence penalties are distinct competing objectives.","Prior quality determines whether regularization helps or hinders.","Hyperparameters must be selected without tuning against held-out test masks."],
["Sweep `l1` across 0, 0.002, 0.01, and 0.1; count coefficients whose magnitude exceeds 0.01.","Construct an intentionally wrong prior concentrated in a corner and show its effect."],
"**Question:** When could an agreement-with-evidence penalty make a medically important rare lesion *less* visible?")

book('12_medlime_capstone_and_ablations.ipynb','Capstone: integrated MedLIME-inspired explanations','33–40','All previous notebooks.','Compare controlled explanation variants and prepare a critical replication plan.',[
('md',r'''## The four-step research workflow
1. Create a **reference-only** library of positive synthetic cases.
2. Train a lightweight image inpainter on separate synthetic images.
3. For each held-out query, compare black LIME, generative LIME, regularization, adaptation, and combinations.
4. Evaluate AUPRC against known toy lesion masks and inspect failures.

This is an **educational integration exercise, not a numerical reproduction** of the MedLIME CVPR 2026 tables. It substitutes synthetic images, a hand-specified predictor, a small CNN inpainter (not the paper MAE), simplified supervised single-image affine adaptation (using true test label), and a simplified evidence penalty. The *FULL* variant has optimistic test-time label access.'''),
('code',r'''# Partition data by separate seed ranges. No query appears in reference or training pool.
reference=np.stack([synthetic_image(5000+i,True)[0] for i in range(16)])
reference_coef=np.asarray([lime_explain(z,n=75,seed=11)['coef'] for z in reference])
queries=[synthetic_image(7000+i,True) for i in range(6)]
inpainter,losses=train_inpainter(n=96,epochs=8,seed=10)
print('Queries:',len(queries),'reference images:',len(reference),'final inpainter loss:',round(losses[-1],4))'''),
('md',r'''## Run fair paired ablations
Within each query use the *same random mask seed and number of masks* across arms. The local optimization is small; to keep runtime low, we use 100 perturbations and only six held-out toy lesions. These figures are too small for a clinical claim.'''),
('code',r'''arms=['LIME (black)','GM only','GM + EBR','GM + supervised adaptation','ALL (GM+STTA+EBR)']
records=[]
for i,(original,lesion) in enumerate(queries):
    q=original*.82
    prior,_,_=evidence_prior(q,reference,reference_coef,k=4)
    adapter,_=supervised_adapt(q,true_label=1,steps=28)
    configs=[dict(fill='zero'),
             dict(fill='learned',inpainter=inpainter),
             dict(fill='learned',inpainter=inpainter,prior=prior,l1=.002,l2=.1),
             dict(fill='learned',inpainter=inpainter,adapt=adapter),
             dict(fill='learned',inpainter=inpainter,prior=prior,l1=.002,l2=.1,adapt=adapter)]
    scores=[]
    for config in configs:
        explanation=lime_explain(q,n=100,seed=26,**config)
        scores.append(auprc(lesion,explanation['map']))
    records.append(scores)
    print('Query',i+1,dict(zip(arms,np.round(scores,3))))
results=np.asarray(records)
assert results.shape == (6,5)
print('\nMean AUPRC (illustrative only):')
for arm,v in zip(arms,results.mean(axis=0)): print(f'{arm:>28}  {v:.3f}')'''),
('md',r'''## Read an ablation table as a scientist
Ablation asks what changes when one component is removed, **holding other relevant choices fixed**. On this tiny dataset, variation across individual examples is often more informative than a mean. Do not claim the last column is best before inspecting it.'''),
('code',r'''fig,ax=plt.subplots(figsize=(8,3.5))
ax.boxplot([results[:,j] for j in range(len(arms))])
ax.set_xticks(range(1,6),labels=['LIME','GM','GM+EBR','GM+STTA','ALL'])
ax.set_ylabel('Pixel AUPRC');ax.set_title('Synthetic cases — not paper results');ax.set_ylim(0,1)
plt.xticks(rotation=15);plt.tight_layout();plt.show()
print('Top arm by observed mean:',arms[int(np.argmax(results.mean(0)))])
print('Mean is not an unbiased test of tuned methods at n=6.')'''),
('md',r'''## Build your real-paper reproduction plan
Before using real patient images, students should read the paper and supplementary protocol, check dataset licensing and ethical permissions, isolate patients across splits, identify exactly what supervision STTA requires, identify the pretraining corpus/architecture for the actual MAE, implement paper-specific neighbor similarity and EBR terms, match mask counts and hyperparameters, and compare to every relevant baseline on the same test data.

**Read:** [MedLIME CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Magazine_MedLIME_A_Distribution-Aligned_and_Evidence-Supported_Framework_for_Medical_Saliency_Explanations_CVPR_2026_paper.html) and its supplement. **Do not use label-informed adaptation results as label-blind evaluation**.'''),
('code',r'''# Challenge template: document results without inventing successful outcomes.
for arm,mean,std in zip(arms,results.mean(0),results.std(0,ddof=1)):
 print(f'{arm:>28}: mean={mean:.3f}, SD={std:.3f}, n={len(queries)}')
print('Research interpretation: explain failures, do not only rank averages.')'''),
],["The integrated pipeline combines perturbation, reconstruction, adaptation, and evidence priors.","Proper ablations must control masks, queries, supervision, and evaluation metric.","Synthetic demonstrations cannot verify the paper's clinical performance claims."],
["Create a component-ablation matrix and defend every experimental control.","Run three different sets of six held-out queries and report uncertainty.","Write a two-page methods audit of the real MedLIME paper, identifying any toy/paper mismatch and how you would close it."],
"**Final defense:** Explain in your own words why each component exists, which assumptions it makes, and what data could falsify its promised benefit.")

if __name__=='__main__':
    print('Generated',len(BOOKS),'notebooks in',OUT)
    for filename,title,weeks in BOOKS: print(filename, '|', title, '| weeks',weeks)
