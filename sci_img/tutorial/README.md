
# Medical & Biological Imaging AI — Tutorial Series

A four-phase, hands-on curriculum that takes you from first principles in signal processing all the way to clinical 3-D segmentation, generative synthesis, vision-language models, and real cryo-electron tomography. Every notebook runs on Google Colab (free T4 GPU), and each phase builds deliberately on the one before it.Besides, you are encouraged to pull a issue in this repo.

---

## Who this is for

| Background | Where to start |
|------------|----------------|
| Python user curious about medical AI | Phase 01 → Phase 02 → Phase 03 |
| Biologist wanting to understand cryoEM computation | Phase 01 (Module 02) → Phase 04 |
| ML practitioner new to medical imaging | Phase 02 → Phase 03 |
| Structural biology researcher / cryo-ET newcomer | Phase 04 (after Phase 01 Module 02) |

---

## 🗺️ Full Roadmap

```
Phase 01 — Computational Signal Base
  ├─ 01 PyTorch Tensor Basics & Image I/O
  ├─ 02 Frequency Filtering & Image Pyramids
  ├─ 03 Classical Feature Extraction (Edges, Lines, Curves)
  ├─ 04 Geometry-Based Classification of Bio-Images
  ├─ 05 Corner Detection & Feature Descriptors
  └─ 06 Spatial Transformations & Image Warping

Phase 02 — Spatial Perception & Analysis
  ├─ 01 Dimensionality Reduction & Latent Space (PCA)
  ├─ 02 Object Detection & Tracking (YOLOv5 + LAP)
  ├─ 03 Image Segmentation (Watershed → U-Net)
  ├─ 04 Image Alignment & Registration (SimpleITK + Pix2Pix)
  └─ 05 Stereo Vision & Depth Estimation (DLT + Block Matching)

Phase 03 — Advanced Medical AI
  ├─ 01 3-D Volumetric Segmentation with MONAI
  ├─ 02 Multimodal Image Registration
  ├─ 03 Medical Generative Models (Schrödinger Bridge CFM)
  ├─ 04 Medical Vision-Language Models (BiomedCLIP, BLIP-2, LLaVA)
  └─ 05 Clinical Diagnostic Assistant Case Study

Phase 04 — CryoEM & Structural Biology
  ├─ 01 Low-SNR Noise Processing & Particle Picking
  ├─ 02 3-D CryoEM Reconstruction
  └─ 03 Build & Diagnose a Real Cryo-ET Tomogram (EMPIAR-10164)

Phase 05 — Robotic Lab Automation & VLA Models
  ├─ 01 AutoBio Simulator & Benchmark Tasks
  └─ 02 AutoBio Computer Vision & Closed-Loop Control
```

### 📅 Suggested 8-Week Timeline
To help you pace your learning, we have organized the 5 phases into a suggested **8-week schedule**:

```mermaid
flowchart TD
    %% Define Styles
    classDef phase1 fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px,color:#01579b;
    classDef phase2 fill:#e8f5e9,stroke:#4caf50,stroke-width:2px,color:#1b5e20;
    classDef phase3 fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px,color:#4a148c;
    classDef phase4 fill:#fff3e0,stroke:#ff9800,stroke-width:2px,color:#e65100;
    classDef phase5 fill:#efebe9,stroke:#795548,stroke-width:2px,color:#3e2723;

    subgraph P1 [Phase 01: Computational Signal Base]
        W1["<b>Week 1: Foundations I</b><br/>• Tensor Basics & I/O (M01)<br/>• Frequency Filtering (M02)<br/>• Edges & Curves (M03)"]:::phase1
        W2["<b>Week 2: Foundations II</b><br/>• Geometric Classification (M04)<br/>• Corner Detection (M05)<br/>• Coordinate Transforms (M06)"]:::phase1
    end

    subgraph P2 [Phase 02: Spatial Perception & Analysis]
        W3["<b>Week 3: Perception I</b><br/>• Dimensionality Reduction (M01)<br/>• YOLOv5 Object Detection (M02)<br/>• Cell Tracking (M02)"]:::phase2
        W4["<b>Week 4: Perception II</b><br/>• U-Net Segmentation (M03)<br/>• SimpleITK Registration (M04)<br/>• Pix2Pix GAN Translation (M04)"]:::phase2
        W5_1["<b>Week 5: Stereo Depth</b><br/>• Stereo Vision (M05)<br/>• Triangulation & Matching (M05)"]:::phase2
    end

    subgraph P3 [Phase 03: Advanced Medical AI]
        W5["<b>Week 6: Clinical Systems I</b><br/>• 3-D MONAI Segmentation (M01)<br/>• Multimodal Registration (M02)"]:::phase3
        W6["<b>Week 7: Clinical Systems II</b><br/>• Schrödinger Bridge CFM (M03)<br/>• Medical VLMs (M04)<br/>• Diagnostic Assistant (M05)"]:::phase3
    end

    subgraph P4 [Phase 04: Cryo-EM Specialisation]
        W7["<b>Week 8: Cryo-EM / Cryo-ET</b><br/>• Low-SNR Denoising (M01)<br/>• 3-D Reconstruction (M02)<br/>• Practical IMOD Tomogram Build (M03)"]:::phase4
    end

    subgraph P5 [Phase 05: Robotic Lab Automation]
        W8["<b>Week 9: Lab Robotics & VLA</b><br/>• AutoBio Simulator (M01)<br/>• AutoBio Computer Vision (M02)"]:::phase5
    end

    %% Flow connections
    W1 --> W2
    W2 --> W3
    W3 --> W4
    W4 --> W5_1
    W5_1 --> W5
    W5 --> W6
    
    %% Alternative Learning Paths
    W1 -.->|Biologist / Cryo-EM Track| W7
    W5_1 -.->|Full Curriculum| W7
    W6 -.->|Robotics Track| W8
```
```

### 🔗 Concept Connection Workflow
The curriculum is designed so that early mathematical foundations directly prepare you for later deep learning architectures and domain-specific applications. The diagram below illustrates how concepts and methods flow between modules:

```mermaid
graph TD
    %% Node definitions
    Tensors["PyTorch Tensors<br/>(Ph01-M01)"]
    Fourier["Fourier Transform / FFT<br/>(Ph01-M02)"]
    Conv["Spatial Convolutions<br/>(Ph01-M02)"]
    Edges["Edge & Line Detection<br/>(Ph01-M03)"]
    Geometry["GLCM & RegionProps<br/>(Ph01-M04)"]
    Corners["Corner Descriptors<br/>(Ph01-M05)"]
    Transforms["Spatial Transforms & Warping<br/>(Ph01-M06)"]

    PCA["PCA & Latent Space<br/>(Ph02-M01)"]
    YOLO["YOLOv5 & LapTrack<br/>(Ph02-M02)"]
    UNet["U-Net Segmentation<br/>(Ph02-M03)"]
    RegClassical["SimpleITK Registration<br/>(Ph02-M04)"]
    Pix2Pix["Pix2Pix Translation GAN<br/>(Ph02-M04)"]

    Monai3D["3-D MONAI Segmentation<br/>(Ph03-M01)"]
    RegDeep["Deep Reg (VoxelMorph)<br/>(Ph03-M02)"]
    CFM["Schrödinger Bridge CFM<br/>(Ph03-M03)"]
    VLM["Vision-Language Models<br/>(Ph03-M04)"]
    Clinical["Clinical Assistant Case Study<br/>(Ph03-M05)"]

    CTF["CTF Wiener Filtering<br/>(Ph04-M01)"]
    Recon3D["3-D Reconstruction & EM<br/>(Ph04-M02)"]
    Tomogram["Tomogram Stack & Align<br/>(Ph04-M03)"]

    %% Class assignment for colors
    classDef phase1 fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px,color:#01579b;
    classDef phase2 fill:#e8f5e9,stroke:#4caf50,stroke-width:2px,color:#1b5e20;
    classDef phase3 fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px,color:#4a148c;
    classDef phase4 fill:#fff3e0,stroke:#ff9800,stroke-width:2px,color:#e65100;

    class Tensors,Fourier,Conv,Edges,Geometry,Corners,Transforms phase1;
    class PCA,YOLO,UNet,RegClassical,Pix2Pix phase2;
    class Monai3D,RegDeep,CFM,VLM,Clinical phase3;
    class CTF,Recon3D,Tomogram phase4;

    %% Dependencies and flow
    Tensors --> Conv
    Tensors --> Transforms
    
    Fourier --> CTF
    Fourier --> Recon3D
    Conv --> Edges
    
    Edges --> YOLO
    Edges --> UNet
    Geometry --> PCA
    Corners --> Transforms
    
    Transforms --> RegClassical
    Transforms --> RegDeep
    
    PCA --> CFM
    PCA --> Recon3D
    UNet --> Monai3D
    UNet --> Pix2Pix
    RegClassical --> RegDeep
    
    CFM --> RegDeep
    VLM --> Clinical
    UNet -.->|Masks as centroids| YOLO
    
    CTF --> Recon3D
    Recon3D --> Tomogram
```

### 💡 Why Learn in This Order?
Understanding *why* the curriculum is structured this way helps contextualize how simpler models build into clinical-grade applications:

* **Tensors & Warping to Deep Registration**: In Phase 01 Module 06, you build coordinate transformations and image warping from mathematical first principles. This exact logic is scaled in Phase 03 Module 02 (VoxelMorph), where a U-Net outputs a dense deformation field which is applied to a clinical scan using PyTorch's differentiable `grid_sample` (acting as a spatial transformer).
* **Fourier Transforms to Cryo-EM**: Frequency-domain filtering (Phase 01 Module 02) introduces the Fourier Transform. This is the direct prerequisite for Phase 04 (Cryo-EM), where you simulate the microscope's Contrast Transfer Function (CTF), denoise extremely low SNR micrographs, and reconstruct 3-D volumes using the Fourier Slice Theorem.
* **Classical Convolutions to Deep U-Nets**: Implementing Sobel and Canny edge detection by hand (Phase 01 Module 03) demystifies what convolutional neural network layers are actually doing. When training a U-Net for yeast cell segmentation (Phase 02 Module 03), you will realize the network learns these edge and feature kernels automatically via backpropagation.
* **Dimensionality Reduction to Generative Models**: Retinal image compression via PCA (Phase 02 Module 01) introduces the concept of a low-dimensional latent space. This prepares you to understand how modern generative models (Phase 03 Module 03 Schrödinger Bridge CFM) learn mapping trajectories between source and target latent representations.

---

## Phase Overview

### Phase 01 — Computational Signal Base
**Level: Beginner** · No prior PyTorch or image-processing experience required.

The foundation everything else rests on. You will leave Phase 01 fluent in PyTorch tensors, comfortable loading DICOM and TIFF medical images, and able to design and apply filters in both the spatial and frequency domains. The final module introduces hand-crafted geometric features and classical classifiers — still the right choice whenever labelled data is scarce.

➜ [`ComputationalSignalBase/`](ComputationalSignalBase/)

---

### Phase 02 — Spatial Perception & Analysis
**Level: Intermediate** · Requires Phase 01 or equivalent PyTorch familiarity.

Phase 02 is about understanding *where things are* and *what shape they have*. You will compress high-dimensional images with PCA, train a YOLOv5 object detector on a custom dataset, track cells across 3-D time-lapse volumes, segment structures with both classical algorithms and U-Net, and align image pairs using both iterative optimisation and a conditional GAN.

➜ [`SpatialPerceptionAnalysis/`](SpatialPerceptionAnalysis/)

---

### Phase 03 — Advanced Medical AI
**Level: Advanced** · Requires Phases 01 and 02.

The phase where individual building blocks converge into complete clinical-grade systems. You will train a 3-D U-Net on the Medical Segmentation Decathlon spleen benchmark, work through the full spectrum of multimodal registration from classical SimpleITK to deep VoxelMorph-style networks, synthesise missing imaging modalities using Schrödinger Bridge Conditional Flow Matching, and probe state-of-the-art foundation models (BiomedCLIP, BLIP-2, LLaVA-1.5) with real medical images.

➜ [`AdvancedMedicalAI/`](AdvancedMedicalAI/)

---

### Phase 04 — CryoEM & Structural Biology
**Level: Specialist** · Requires Phase 01 Module 02 (Fourier analysis) + NumPy/SciPy fluency.

An end-to-end computational treatment of cryo-electron microscopy. Module 01 builds the 2-D signal-processing intuition (CTF simulation, denoising, particle picking, class averaging, FRC resolution). Module 02 extends everything to 3-D: the Fourier Slice Theorem, trilinear back-projection, and expectation-maximisation pose estimation. Module 03 is a full hands-on practical using IMOD/Etomo on a real published tilt series from EMPIAR.

➜ [`cryoem/`](../../cryoem/readme.md)

---

### Phase 05 — Robotic Lab Automation & VLA Models
**Level: Advanced / Specialist** · Requires Phase 01 and Phase 02.

An end-to-end treatment of robotic lab automation. Module 01 covers the AutoBio simulation framework (Lan et al., 2025), physics plugins for detents and screw-caps, success metrics, and baseline VLA model evaluations. Module 02 builds computer vision tasks inspired by AutoBio (tube localization, slot symmetry indexing, liquid-level estimation, closed-loop dial panel control) using synthetic toy data.

➜ [`RoboticLabAutomation/`](RoboticLabAutomation/)

---

## Prerequisites

| Tool | Phase needed | Notes |
|------|-------------|-------|
| Python 3.9+ | All | |
| NumPy, Matplotlib | All | |
| PyTorch | 01–04 | Covered from scratch in Phase 01 |
| Google Colab or local GPU | 02–04 | T4 (16 GB VRAM) sufficient for all notebooks |
| IMOD/Etomo | Phase 04 Module 03 only | Linux / macOS; install locally |

---

## How to Run

**Option A — Google Colab (recommended)**

Open any notebook directly in Colab by replacing `github.com` in the URL with
`colab.research.google.com/github`. Each notebook installs its own dependencies in the first cell.

**Option B — Local Jupyter**

```bash
git clone https://github.com/pastretender/edu.git
cd edu/Tutorials
pip install torch torchvision jupyterlab
jupyter lab
```

---

## Curriculum Map: Concepts and Their Modules

| Concept | First introduced | Used again in |
|---------|-----------------|--------------|
| PyTorch tensors | Ph01-M01 | Every subsequent module |
| Convolution / kernels | Ph01-M02 | Ph01-M03, Ph02-M03, Ph03-M01 |
| Fourier Transform | Ph01-M02 | Ph04-M01, Ph04-M02 |
| Edge & feature detection | Ph01-M03 | Ph02-M02, Ph02-M03 |
| GLCM / geometric features | Ph01-M04 | Ph02-M01 (motivation for PCA) |
| PCA / latent space | Ph02-M01 | Ph03-M03, Ph04-M02 |
| U-Net architecture | Ph02-M03 | Ph02-M04, Ph03-M01, Ph03-M02 |
| Similarity metrics (MI) | Ph02-M04 | Ph03-M02 |
| Dice loss | Ph02-M03 | Ph03-M01 |
| CTF | Ph04-M01 | Ph04-M02, Ph04-M03 |
| Expectation-Maximisation | Ph04-M02 | Ph04-M03 (production software) |

---

## Folder Structure

```
tutorial/
├── README.md                          ← You are here
├── ComputationalSignalBase/
│   ├── README.md
│   ├── PyTorchTensorBasic/
│   ├── FrequencyFiltering/
│   ├── ClassicalFeatureExtract/
│   ├── GeometryBasedClassification/
│   ├── CornerDetection/
│   └── SpatialTransformations/
├── SpatialPerceptionAnalysis/
│   ├── README.md
│   ├── DimensionReductionLatentSpace/
│   ├── ObjectDetectTracking/
│   ├── ImageSegmentation/
│   ├── ImageAlignmentRegister/
│   └── StereoVision/
├── AdvancedMedicalAI/
│   ├── README.md
│   ├── Volume3DSegmentation/
│   ├── MultimodalRegistration/
│   ├── MedicalGenerativeModel/
│   ├── MedicalVisionLanguage/
│   └── ClinicalDiagnosticAssistant/
└── RoboticLabAutomation/
    ├── README.md
    ├── AutoBioBenchmark/
    └── AutoBioComputerVision/
```

---

## Suggested Learning Paths

**"I want to work in medical imaging AI"**
Phase 01 (all) → Phase 02 (M01, M03, M04) → Phase 03 (M01, M02, M04)

**"I want to understand generative models for medical data"**
Phase 01 (M01, M02) → Phase 02 (M03, M04) → Phase 03 (M03)

**"I'm joining a cryoEM lab"**
Phase 01 (M01, M02) → Phase 04 (all, in order)

**"I want the full curriculum"**
Phase 01 → Phase 02 → Phase 03 → Phase 04
