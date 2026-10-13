# Xu lab cryo-ET and cryo-EM paper atlas

**Purpose.** This is the bridge from the beginner notebooks to the lab's research literature. It covers the cryo-ET, cryo-EM, molecular-density-map, and directly supporting image-analysis papers listed in the [published CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub), the [lab publication page](https://xulabs.github.io/publication/), and the lab [BibTeX list](https://raw.githubusercontent.com/xulabs/xulabs.github.io/master/doc/reference_xulab.bib), checked 2026-10-13. The CV includes papers absent from the selected-publications page. Conference and online dates may differ, and some 2026 entries have no linked manuscript yet. Verify final citation details against the publisher before citing. This atlas does not cover unrelated genomics, optical microscopy, general medical imaging, autonomous laboratory, or video papers.

**How to use it.** Complete the named notebook(s), then read the paper's abstract, figures, methods, and limitations. For each paper write: (1) biological or computational question, (2) input data and independent split unit, (3) output, (4) supervision and assumptions, (5) strongest baseline and metric, (6) failure case, (7) one test that could falsify the central claim. Where a link leads to the CV rather than the full manuscript, search the exact title there or through the publisher.

## A. Measurement, reconstruction, resolution, and structural interpretation

| Paper | Prepare with | Reading lens |
|---|---|---|
| Xu, Zhang & Alber, **3D rotation invariant features for characterization of molecular density map images** (2009), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 02, 06, 15 | Which information is preserved when orientation is removed? |
| Zhang et al., **Simultaneous fitting of assembly components into cryo-EM density maps** (2010), [paper](https://doi.org/10.1093/bioinformatics/btq201) | 02, 16 | What makes a fit distinguishable from alternatives? |
| Beck et al., **Exploring the spatial and temporal organization of a cell's proteome** (2011), [paper](https://doi.org/10.1016/j.jsb.2010.11.011) | 00, 01, 16 | Which in-cell structural questions are accessible? |
| Thalassinos et al., **Conformational states of macromolecular assemblies explored by integrative structure calculation** (2013), [paper](https://doi.org/10.1016/j.str.2013.08.006) | 08, 15, 16 | How are conformational alternatives and other data integrated? |
| Shi et al., **Resolution-guided homogeneous cryo-EM image selection** (2020), [paper](https://doi.org/10.1007/s40484-019-0191-8) | 07, 08, 10 | How does selection change dataset composition and validation? |
| Lu et al., **Parallel 3D Fourier shell correlation for local resolution** (2020), [paper](https://doi.org/10.1186/s12859-020-03680-6) | 04, 08 | Why can a single global resolution number mislead? |
| Jiang et al., **Molecular landscape of the fungal plasma membrane and implications for antifungal action** (2025), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 00, 01, 16 | Trace one biological conclusion back to map, localization, and controls. |

## B. Tomography, alignment, averaging, and software

| Paper | Prepare with | Reading lens |
|---|---|---|
| Xu & Alber, **Gradient-based high precision alignment of cryo-electron subtomograms** (2011 conference), [BibTeX](https://raw.githubusercontent.com/xulabs/xulabs.github.io/master/doc/reference_xulab.bib) | 05, 06 | What objective is optimized, and from what initialization? |
| Xu & Alber, **High precision alignment through gradient-based parallel optimization** (2012), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 06 | What improves precision and what costs computation? |
| Xu, Beck & Alber, **High-throughput subtomogram alignment and classification by Fourier-space constrained fast volumetric matching** (2012), [paper](https://doi.org/10.1016/j.jsb.2012.02.014) | 04, 06, 08 | Why constrain matching in Fourier space? |
| Xu & Alber, **Automated target segmentation and real-space fast alignment of crowded subtomograms** (2013), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 06, 08, 09 | How is the target separated from neighboring density? |
| Frazier, Xu & Alber, **TomoMiner and TomoMinerCloud** (2017), [paper](https://doi.org/10.1016/j.str.2017.04.016) | 01, 06–09 | Which analysis steps does the platform make reproducible? |
| Zhao et al., **Integration of fast alignment and maximum-likelihood methods for subtomogram averaging and classification** (2018), [paper](https://doi.org/10.1093/bioinformatics/bty267) | 06, 08, 12 | What is traded between search speed and statistical refinement? |
| Han et al., **Joint marker-free alignment of tilt series in electron tomography** (2019), [paper](https://doi.org/10.1093/bioinformatics/btz323) | 05, 06 | How is tilt geometry estimated without fiducials? |
| Lü et al., **Fine-grained alignment of cryo-electron subtomograms based on MPI parallel optimization** (2019), [paper](https://doi.org/10.1186/s12859-019-3003-2) | 06, 08 | What computation is parallelized, and how is alignment assessed? |
| Zeng & Xu, **Gum-Net: unsupervised geometric matching for 3D subtomogram alignment and averaging** (2020), [paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Zeng_Gum-Net_Unsupervised_Geometric_Matching_for_Fast_and_Accurate_3D_Subtomogram_CVPR_2020_paper.html) | 06, 08, 14 | How is geometric correspondence learned without pose labels? |
| Zeng, Howe & Xu, **End-to-end robust joint unsupervised image alignment and clustering** (2021), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 06, 12, 15 | Why solve alignment and grouping together? |
| Zhu et al., **Unsupervised multi-task learning for 3D subtomogram alignment, clustering and segmentation** (2022), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 06, 09, 12, 15 | Which tasks share information and which can conflict? |
| Jiang et al., **BOE-ViT: equivariant self-supervised 3D subtomogram orientation estimation** (2025), [lab list](https://xulabs.github.io/publication/) | 06, 14, 15 | What equivariance is enforced and how is pose error tested? |
| Zhan et al., **AITom: AI-guided cryo-ET image analyses toolkit** (2025), [paper](https://doi.org/10.1016/j.jsb.2025.108207) | 01, 06–15 | Which modules correspond to a full analysis workflow? |

## C. Template-free discovery, structural pattern mining, and identity

| Paper | Prepare with | Reading lens |
|---|---|---|
| Xu, Beck & Alber, **Template-free detection of macromolecular complexes in cryo-electron tomograms** (2011), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 07, 12 | What is detected when no template is supplied? |
| Xu et al., **De novo visual proteomics in single cells through pattern mining** (2015 preprint), [arXiv](https://arxiv.org/abs/1512.09347) | 00, 12, 16 | What claim was proposed before the later journal study? |
| Xu et al., **De novo structural pattern mining in cellular electron cryo-tomograms** (2019), [paper](https://doi.org/10.1016/j.str.2019.01.005) | 07–09, 12, 16 | How do discovery, average, and molecular interpretation connect? |
| Wu et al., **Template-based and template-free approaches in cellular cryo-ET structural pattern mining** (2019 chapter), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 07, 12 | When does each discovery approach have an advantage? |
| Zeng & Xu, **AITom open-source AI platform** (2019 preprint), [arXiv](https://arxiv.org/abs/1911.03044) | 01, 12 | Compare the proposed platform with the 2025 toolkit paper. |
| Zeng et al., **High-throughput cryo-ET structural pattern mining by deep unsupervised clustering** (2023), [paper](https://doi.org/10.1073/pnas.2213149120) | 08, 12, 16 | What evidence turns an unsupervised cluster into a structural pattern? |
| Kim et al., **Computational methods toward unbiased pattern mining and structure determination in cryo-ET** (2023 review), [paper](https://doi.org/10.1016/j.jmb.2023.168068) | 01–16 | Draw the field's full pipeline and unresolved bottlenecks. |
| Nair et al., **Molecular structure discovery via auxiliary semantic prototypes** (2025), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 11, 12, 15 | What does a prototype represent and how is novelty checked? |
| Uddin, Armouti & Xu, **Unsupervised identification of protein compositions and conformations via content–transformation disentanglement** (2025), [lab list](https://xulabs.github.io/publication/) | 12, 15, 16 | Which factors are composition, conformation, and pose? |
| Uddin et al., **DUIL: deep unsupervised inverse learning for in situ macromolecular morphology identification** (2026), [lab list](https://xulabs.github.io/publication/) | 12–16 | What inverse model and validation are needed for identification? |

## D. Simulation, synthetic data, denoising, and transfer

| Paper | Prepare with | Reading lens |
|---|---|---|
| Pei et al., **Simulating crowded cryo-electron tomograms for particle-picking assessment** (2016), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 05, 07, 13 | Which nuisance factors are simulated and which omitted? |
| Wang et al., **Image-derived generative modeling of pseudo-macromolecular structures for template-matching assessment** (2018), [arXiv](https://arxiv.org/abs/1805.04634) | 07, 13–14 | What is the null model for a significant match? |
| Liu et al., **Unified packing of deformable and non-deformable structures in crowded tomogram simulation** (2020), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 00, 13 | How is biological crowding modeled? |
| Liu et al., **Efficient cryo-electron tomogram simulation of macromolecular crowding with SARS-CoV-2 application** (2020), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 05, 13 | How does application-specific context alter simulation? |
| Che et al., **Domain randomization for macromolecule classification and segmentation** (2019), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 10, 13 | Which shifts are randomized? |
| Lin et al., **Adversarial domain adaptation for cross-source in situ classification** (2019), [paper](https://doi.org/10.1093/bioinformatics/btz364) | 10, 13 | What aligns across data sources, and what could fail to align? |
| Yu et al., **Few-shot domain adaptation for in situ structural classification** (2020), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 11, 13 | How many target-domain labels are needed? |
| Wu et al., **CryoETGAN: cryo-ET image synthesis via unpaired image translation** (2022), [paper](https://doi.org/10.3389/fphys.2022.760404) | 13–14 | How is biological content preserved during style translation? |
| Bandyopadhyay et al., **Cryo-shift: reducing domain shift with unsupervised adaptation and randomization** (2021), [paper](https://doi.org/10.1093/bioinformatics/btab794) | 10, 13 | What is the target domain and what is unlabeled? |
| Jain, Li & Xu, **Knowledge transfer from macro-world to micro-world for 3D cryo-ET classification** (2024), [paper](https://doi.org/10.1093/bioinformatics/btae368) | 10, 13, 15 | Which video features transfer to volumes, and which do not? |
| Uddin et al., **DUAL: deep unsupervised simultaneous simulation and denoising for cryo-ET** (2024 preprint), [preprint](https://doi.org/10.1101/2024.03.02.583135) | 03, 13–14 | How are the simulator and denoiser coupled? |
| Liu et al., **J-Invariant Volume Shuffle for self-supervised tomogram denoising** (2025), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 03, 14 | How is target leakage prevented with one noisy volume? |
| Wu et al., **Score-Based Matching with Target Guidance for Cryo-EM Denoising** (2026), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 04, 14 | How are generated details constrained by measured data? |

## E. Classification, scarce labels, robustness, and interpretability

| Paper | Prepare with | Reading lens |
|---|---|---|
| Che et al., **Improved deep-learning classification from electron cryo-tomograms** (2018), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 09–10 | What is the unit of train/test separation? |
| Zhao et al., **Respond-CAM: visualizing deep models for 3D imaging** (2018), [arXiv](https://arxiv.org/abs/1806.00102) | 10, 16 | Does the explanation localize relevant biological structure? |
| Guo et al., **Model compression for faster structural separation** (2018), [arXiv](https://arxiv.org/abs/1801.10597) | 10, 13 | What accuracy–speed tradeoff is measured? |
| Luo et al., **Classification with imbalanced cryo-ET data** (2019), [arXiv](https://arxiv.org/abs/1908.09993) | 10–11 | What is reported beyond overall accuracy? |
| Du et al., **Open-set recognition of unseen macromolecules** (2019), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 11–12 | How is “unknown” separated from low-confidence known classes? |
| Liu et al., **Semi-supervised classification with a 3D autoencoding classifier** (2019), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 10–12 | What do unlabeled examples contribute? |
| Wu et al., **Regularized adversarial training for robust cryo-tomogram classification** (2019), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 10, 13 | Is robustness evaluated on meaningful image variation? |
| Gao et al., **Dilated-DenseNet for cryo-ET macromolecule classification** (2020), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 09–10 | What receptive field is needed for the target structures? |
| Gao et al., **3D dilated dense network structural classification** (2021 journal), [paper](https://doi.org/10.1109/TCBB.2021.3065986) | 09–10 | Compare with the 2020 version and note changed evaluation. |
| Li et al., **Few-shot learning for novel macromolecular structures** (2020), [paper](https://doi.org/10.1371/journal.pcbi.1008227) | 10–11 | Which classes are novel and how are episodes constructed? |
| Du et al., **Active learning to classify macromolecular structures in situ** (2021), [paper](https://doi.org/10.1093/bioinformatics/btab123) | 10–11 | Does it beat random labeling for the same budget? |
| Wang et al., **Deep active learning for cryo-ET classification** (2022), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 10–11 | What selection rule and annotation budget are used? |
| Gao et al., **FSCC: few-shot classification with contrastive learning and distribution calibration** (2022), [paper](https://doi.org/10.3389/fmolb.2022.931949) | 11, 14 | How are few examples supplemented or calibrated? |
| Gupta et al., **Self-supervised learning for macromolecular structure classification** (2022), [paper](https://doi.org/10.3389/fphys.2022.957484) | 10, 14 | What pretext task learns a reusable representation? |
| Uddin et al., **Practical analysis of macromolecule identity with deep learning** (2021), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 09–11, 16 | Which practical constraints determine method choice? |
| Zeng et al., **Unsupervised domain alignment based open-set recognition** (2021), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 11, 13 | How are domain shift and unknown classes handled together? |
| Uddin et al., **Localization from extremely sparse labels** (2025), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 07, 11 | What is the label unit and localization tolerance? |
| Hosseini et al., **RobPicker: meta learning for robust macromolecule identification** (2026), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 07, 11, 13 | Across which specimens or domains is robustness demonstrated? |

## F. Segmentation, detection, and foundation models

| Paper | Prepare with | Reading lens |
|---|---|---|
| Xu et al., **Deep-learning subdivision for large-scale structure recovery** (2017), [paper](https://doi.org/10.1093/bioinformatics/btx230) | 09–10, 12 | Why subdivide the large-scale recovery problem? |
| Zeng et al., **Convolutional autoencoder for feature mining and weakly supervised coarse segmentation** (2018), [paper](https://doi.org/10.1016/j.jsb.2017.12.015) | 09–10, 12 | What are the labels, and what is only coarse? |
| Liu et al., **Supervised semantic segmentation of electron cryo-subtomograms** (2018), [arXiv](https://arxiv.org/abs/1802.04087) | 09–10 | How is voxel-level quality measured? |
| Liu et al., **Multi-task classification, segmentation, and coarse structural recovery** (2018), [arXiv](https://arxiv.org/abs/1805.06332) | 09–10, 12 | Which outputs share a representation? |
| Li et al., **Mitochondria localization and identification with Faster R-CNN** (2019), [paper](https://doi.org/10.1186/s12859-019-2650-7) | 07, 09–10 | What is an object detector's target and evaluation unit? |
| Zhou et al., **One-shot attention-guided segmentation in cryo-ET** (2020), [paper](https://doi.org/10.3389/fmolb.2020.613347) | 09, 11 | What changes with one labeled example? |
| Zeng et al., **Structure detection by reconstructing 2D annotated tilt series** (2022), [paper](https://doi.org/10.1089/cmb.2021.0606) | 05, 07, 09 | How are 2D annotations transferred into 3D? |
| Zhu et al., **Weakly supervised 3D semantic segmentation with cross-image consensus and inter-voxel affinity** (2021), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 09, 11 | What replaces dense labels? |
| Zhao et al., **CryoSAM: training-free cryo-ET segmentation with foundation models** (2024), [preprint](https://arxiv.org/abs/2407.06833) | 09, 14 | What is prompted, and how are 3D consistency errors corrected? |
| Li et al., **Vox-UDA: voxel-wise unsupervised domain adaptation for subtomogram segmentation** (2025), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 09, 13–14 | What pseudo-label noise is expected? |
| Li et al., **MVGFormer: multi-view graph-guided transformer for cryo-ET segmentation** (2025), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 09, 15 | How are views and spatial relations combined? |
| Uddin et al., **Unsupervised multi-scale segmentation of the 3D subcellular world with a stable-diffusion foundation model** (2026), [lab list](https://xulabs.github.io/publication/) | 09, 14 | How are different object scales handled without labels? |
| Salla et al., **TopoFuse: topology-aware tri-planar fusion for 3D cryo-ET segmentation** (2026), [lab list](https://xulabs.github.io/publication/) | 09, 15 | Which topological errors are reduced by fusing three planes? |
| Xu, Zhan & Xu, **CryoMAE: few-shot cryo-EM particle picking with masked autoencoders** (2025), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 07, 11, 14 | How do few labels and pretraining interact? |

## G. Benchmarks and supporting methods

| Paper | Prepare with | Reading lens |
|---|---|---|
| Gubins et al., **Classification in cryo-electron tomograms** (2019 benchmark), [paper](https://doi.org/10.2312/3dor.20191061) | 09–10 | Are teams compared on the same data and metric? |
| Gubins et al., **SHREC’20 benchmark: classification in cryo-electron tomograms** (2020), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 09–10, 13 | What shifts between benchmark data and real cells? |
| Uddin et al., **Harmony: disentangling semantic content from parameterized transformations** (2022), [paper](https://openaccess.thecvf.com/content/CVPR2022/html/Uddin_Harmony_A_Generic_Unsupervised_Approach_for_Disentangling_Semantic_Content_From_CVPR_2022_paper.html) | 06, 12, 15 | Which transformation factors are learned separately? |
| Yi et al., **Disentangling semantic features of macromolecules in cryo-ET** (2021 preprint), [arXiv](https://arxiv.org/abs/2106.14192) | 12, 15 | Which variation is semantic rather than nuisance? |
| Uddin et al., **Feature detection in cryo-ET image analysis** (2025 chapter), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 07, 09 | Summarize the detection taxonomy. |
| Han & Xu, **Advance of computational methods in cryo-ET** (2024 chapter), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 01–16 | Use it as a review of the full workflow. |
| Cai et al., **3D macromolecule localization with deep reinforcement learning** (2019 workshop), [CV](https://docs.google.com/document/d/e/2PACX-1vQOw1_7_1a6HuyyvcwmtOzfliOmyz4L7giYkp3-i0MOxh-ASU0ZCjNtdYZZ4KC3UlFHdC9Gb-gzXMsi/pub) | 07, 10 | What is the agent's state, action, and reward? |
| Zhou et al., **Feature decomposition based saliency detection in electron cryo-tomograms** (2018 workshop), [arXiv](https://arxiv.org/abs/1801.10562) | 09, 16 | What is “salient” and is it biological? |

## Recommended paper-reading spiral

1. **First pass, biological purpose:** 2019 *De novo structural pattern mining* and 2023 PNAS pattern mining. Read figures and conclusions; no method derivation yet.
2. **Second pass, measurement:** 2012 Fourier-space matching, 2019 marker-free tilt alignment, 2020 local FSC.
3. **Third pass, classic analysis:** 2011 template-free detection, 2018 averaging/classification, 2020 Gum-Net.
4. **Fourth pass, AI and scarce labels:** 2018 autoencoder, 2020 few-shot, 2021 active learning, 2022 self-supervised classification, 2024 CryoSAM.
5. **Fifth pass, current frontier:** 2023 PNAS, 2025 AITom/BOE-ViT/ICCV composition–conformation, and 2026 DUIL/TopoFuse/multiscale segmentation. For papers without a full public manuscript, use the title and abstract as a provisional map and revisit when the manuscript appears.

**Completion standard:** a student should be able to explain one paper from each section without slides, reproduce a central conceptual figure or computation, identify its strongest alternative explanation, and design a discriminating experiment. The final notebook gives the audit form.
