# DiffCAM curriculum — complete tutorial map

Each notebook provides conceptual reading, executable experiments, questions, and an exit ticket. Follow the order below.

| Week(s) | Notebook | Research skill |
|---|---|---|
| 1 | [Biological images as measurements](00_orientation/01_biological_images.ipynb) | What counts as evidence in a biological image? |
| 2 | [The same image, different reference questions](00_orientation/02_reference_questions.ipynb) | Why is a comparison meaningless without a reference? |
| 3 | [Python: variables, loops, and biological measurements](01_python/01_python_basics.ipynb) | How do we express a biological calculation in code? |
| 4 | [NumPy arrays and image pixels](01_python/02_numpy_images.ipynb) | How can an image be represented as a matrix? |
| 5–6 | [Histograms, thresholds, and regions](01_python/03_image_processing.ipynb) | How do numerical operations affect apparent morphology? |
| 7 | [Vectors and distances for cell measurements](02_linear_algebra/01_vectors_distances.ipynb) | What is a biological feature vector? |
| 8–9 | [Projection directions and separability](02_linear_algebra/02_projections.ipynb) | Which direction best distinguishes a target from a population? |
| 10 | [Matrices, linear systems, and stable solutions](02_linear_algebra/03_matrices_solves.ipynb) | How do we compute a direction without explicitly inverting a matrix? |
| 11 | [Distributions and variation among cells](03_statistics/01_probability_distributions.ipynb) | What does a reference population look like statistically? |
| 12–13 | [Covariance and Mahalanobis geometry](03_statistics/02_covariance.ipynb) | Why is diagonal variance not enough? |
| 14 | [Estimating covariance with few references](03_statistics/03_regularization.ipynb) | What happens when we have more features than reference samples? |
| 15–16 | [Logistic regression and decision boundaries](04_machine_learning/01_logistic_classification.ipynb) | How does a classifier choose between cell populations? |
| 17–18 | [Train/test separation, imbalance, and shortcuts](04_machine_learning/02_generalization.ipynb) | When does an impressive accuracy estimate mislead us? |
| 19 | [A tiny neural network and backpropagation](05_deep_learning/01_neural_network_numpy.ipynb) | How do networks learn nonlinear representations? |
| 20 | [Convolutions reveal local image structure](05_deep_learning/02_convolutions.ipynb) | Why are convolutional filters natural for images? |
| 21–22 | [Train a CNN on synthetic cell images](05_deep_learning/03_train_cnn.ipynb) | Can a CNN learn to recognize a known synthetic change? |
| 23 | [From CNN spatial maps to feature embeddings](05_deep_learning/04_feature_embeddings.ipynb) | What are the channels and vectors inside a CNN? |
| 24 | [Class Activation Mapping from classifier weights](06_explainable_ai/01_cam.ipynb) | How can channel importance generate a location map? |
| 25 | [Grad-CAM and gradient-based weights](06_explainable_ai/02_gradcam.ipynb) | How do prediction gradients decide which channels matter? |
| 26 | [Contrastive explanations without a classifier](06_explainable_ai/03_contrastive_explanations.ipynb) | How does the reference group change the explanation? |
| 27 | [Saliency localization, faithfulness, and sanity checks](06_explainable_ai/04_saliency_evaluation.ipynb) | How should we evaluate a heatmap? |
| 28 | [DiffCAM objective: distinctiveness versus reference spread](07_diffcam/01_geometric_objective.ipynb) | Which feature direction makes a target unusually different from references? |
| 29 | [Derive DiffCAM weights from the Rayleigh quotient](07_diffcam/02_derivation.ipynb) | Can we derive the reference-aware optimal direction? |
| 30 | [DiffCAM in NumPy with handcrafted spatial features](07_diffcam/03_numpy_feature_maps.ipynb) | How does a feature-space direction become a spatial saliency map? |
| 31 | [End-to-end DiffCAM with a trained CNN](07_diffcam/04_pytorch_diffcam.ipynb) | Can we implement DiffCAM using learned image features? |
| 32 | [Three reference groups, three scientific questions](08_evaluation/01_reference_selection.ipynb) | Which real examples belong in a defensible reference set? |
| 33 | [Reference sample size and regularization ablations](08_evaluation/02_ridge_and_n.ipynb) | How stable are feature weights under reference resampling? |
| 34 | [Sanity checks and confounded features](08_evaluation/03_saliency_sanity_checks.ipynb) | Can a heatmap highlight an acquisition artifact instead of biology? |
| 35 | [Region localization on simulated medical-like images](09_biomedical_applications/01_localization_metrics.ipynb) | How does a heatmap compare with an annotated abnormality region? |
| 36 | [DiffCAM with a feature extractor and no classifier](09_biomedical_applications/02_self_supervised_features.ipynb) | Why does DiffCAM not need a classifier head? |
| 37 | [Vision Transformer patches and spatial attribution](09_biomedical_applications/03_vit_patches.ipynb) | How can patch tokens become image-region explanations? |
| 38–39 | [Capstone: a controlled DiffCAM versus Grad-CAM experiment](10_capstone/01_reproduction.ipynb) | Can we compare two methods under defensible experimental controls? |
| 40 | [Capstone: critique the paper and design a next experiment](10_capstone/02_research_report.ipynb) | Can we distinguish empirical findings from interpretation? |
