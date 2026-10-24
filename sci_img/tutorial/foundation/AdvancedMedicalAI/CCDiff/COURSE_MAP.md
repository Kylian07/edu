# CCDiff learning map

Each notebook has a `.md` reading companion. Start with T01 and advance numerically. The full trajectory is 30 weeks; longer tutorials deliberately span two weeks.


## A. Biological data and Python

- **T01 (Week(s) 1):** [From biological observations to datasets](notebooks/T01_from_biological_observations_to_datasets.ipynb) · [read-only Markdown](notebooks/T01_from_biological_observations_to_datasets.md)
- **T02 (Week(s) 2):** [Python for biological data analysis](notebooks/T02_python_for_biological_data_analysis.ipynb) · [read-only Markdown](notebooks/T02_python_for_biological_data_analysis.md)
- **T03 (Week(s) 3):** [NumPy, matrices, and visualization](notebooks/T03_numpy_matrices_and_visualization.ipynb) · [read-only Markdown](notebooks/T03_numpy_matrices_and_visualization.md)
- **T04 (Week(s) 4):** [Digital images as measurable biological data](notebooks/T04_digital_images_as_measurable_biological_data.ipynb) · [read-only Markdown](notebooks/T04_digital_images_as_measurable_biological_data.md)

## B. Mathematical foundations

- **T05 (Week(s) 5–6):** [Probability, sampling, and dataset distributions](notebooks/T05_probability_sampling_and_dataset_distributions.ipynb) · [read-only Markdown](notebooks/T05_probability_sampling_and_dataset_distributions.md)
- **T06 (Week(s) 7):** [Vectors, dot products, and projections](notebooks/T06_vectors_dot_products_and_projections.ipynb) · [read-only Markdown](notebooks/T06_vectors_dot_products_and_projections.md)
- **T07 (Week(s) 8–9):** [Cosine similarity, covariance, and correlation](notebooks/T07_cosine_similarity_covariance_and_correlation.ipynb) · [read-only Markdown](notebooks/T07_cosine_similarity_covariance_and_correlation.md)
- **T08 (Week(s) 10):** [Standardization, PCA, and singular value decomposition](notebooks/T08_standardization_pca_and_singular_value_decomposition.ipynb) · [read-only Markdown](notebooks/T08_standardization_pca_and_singular_value_decomposition.md)

## C. ML and vision–language models

- **T09 (Week(s) 11):** [Machine learning, generalization, and distribution shift](notebooks/T09_machine_learning_generalization_and_distribution_shift.ipynb) · [read-only Markdown](notebooks/T09_machine_learning_generalization_and_distribution_shift.md)
- **T10 (Week(s) 12):** [Neural networks and pretrained visual features](notebooks/T10_neural_networks_and_pretrained_visual_features.ipynb) · [read-only Markdown](notebooks/T10_neural_networks_and_pretrained_visual_features.md)
- **T11 (Week(s) 13–14):** [CLIP, contrastive learning, and image–text embeddings](notebooks/T11_clip_contrastive_learning_and_image_text_embeddings.ipynb) · [read-only Markdown](notebooks/T11_clip_contrastive_learning_and_image_text_embeddings.md)
- **T12 (Week(s) 15):** [Caption generators and candidate concept banks](notebooks/T12_caption_generators_and_candidate_concept_banks.ipynb) · [read-only Markdown](notebooks/T12_caption_generators_and_candidate_concept_banks.md)

## D. Canonical correlation analysis

- **T13 (Week(s) 16):** [Paired biological views and cross-covariance](notebooks/T13_paired_biological_views_and_cross_covariance.ipynb) · [read-only Markdown](notebooks/T13_paired_biological_views_and_cross_covariance.md)
- **T14 (Week(s) 17–18):** [Canonical correlation analysis: geometry and objective](notebooks/T14_canonical_correlation_analysis_geometry_and_objective.ipynb) · [read-only Markdown](notebooks/T14_canonical_correlation_analysis_geometry_and_objective.md)
- **T15 (Week(s) 19–20):** [CCA computation, rank, regularization, and stability](notebooks/T15_cca_computation_rank_regularization_and_stability.ipynb) · [read-only Markdown](notebooks/T15_cca_computation_rank_regularization_and_stability.md)
- **T16 (Week(s) 21):** [Low-correlation components and inverse CCA](notebooks/T16_low_correlation_components_and_inverse_cca.ipynb) · [read-only Markdown](notebooks/T16_low_correlation_components_and_inverse_cca.md)

## E. CCDiff implementation

- **T17 (Week(s) 22):** [Candidate selection from average image–text similarity](notebooks/T17_candidate_selection_from_average_image_text_similarity.ipynb) · [read-only Markdown](notebooks/T17_candidate_selection_from_average_image_text_similarity.md)
- **T18 (Week(s) 23):** [Cross-set pairing, inverse-CCA components, and concept matching](notebooks/T18_cross_set_pairing_inverse_cca_components_and_concept_matching.ipynb) · [read-only Markdown](notebooks/T18_cross_set_pairing_inverse_cca_components_and_concept_matching.md)
- **T19 (Week(s) 24):** [Combining inverse correlation and within-set relevance](notebooks/T19_combining_inverse_correlation_and_within_set_relevance.ipynb) · [read-only Markdown](notebooks/T19_combining_inverse_correlation_and_within_set_relevance.md)
- **T20 (Week(s) 25–26):** [Build the complete pedagogical CCDiff pipeline](notebooks/T20_build_the_complete_pedagogical_ccdiff_pipeline.ipynb) · [read-only Markdown](notebooks/T20_build_the_complete_pedagogical_ccdiff_pipeline.md)

## F. Evaluation and biological research

- **T21 (Week(s) 27):** [Benchmark metrics, baselines, and reproducibility](notebooks/T21_benchmark_metrics_baselines_and_reproducibility.ipynb) · [read-only Markdown](notebooks/T21_benchmark_metrics_baselines_and_reproducibility.md)
- **T22 (Week(s) 28):** [Ablations, pairing stability, and scientifically meaningful controls](notebooks/T22_ablations_pairing_stability_and_scientifically_meaningful_controls.ipynb) · [read-only Markdown](notebooks/T22_ablations_pairing_stability_and_scientifically_meaningful_controls.md)
- **T23 (Week(s) 29):** [Biomedical case study: microscopy and medical claims](notebooks/T23_biomedical_case_study_microscopy_and_medical_claims.ipynb) · [read-only Markdown](notebooks/T23_biomedical_case_study_microscopy_and_medical_claims.md)
- **T24 (Week(s) 30):** [Read, reproduce, and critically defend the paper](notebooks/T24_read_reproduce_and_critically_defend_the_paper.ipynb) · [read-only Markdown](notebooks/T24_read_reproduce_and_critically_defend_the_paper.md)

## End-of-course deliverables

1. An annotated, shape-checked implementation of the five steps in CCDiff Algorithm 1.
2. A direct cosine-difference baseline and an inverse-CCA comparison.
3. At least one null (identical-set) control, twenty shuffled pairing trials, and written uncertainty considerations.
4. A 15-minute paper presentation and a two-page reproducibility/limitations review.
