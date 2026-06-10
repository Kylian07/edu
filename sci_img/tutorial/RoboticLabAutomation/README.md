# Phase 05 — Robotic Lab Automation & VLA Models

**Level: Advanced / Specialist** · Completion of Phase 01 and Phase 02 (or equivalent experience with PyTorch, basic computer vision, and physical simulation concepts) is recommended.

Phase 05 moves beyond static medical scans and image-processing pipelines to focus on **robotic lab automation**. In modern digital biology laboratories, general-purpose robotic systems must execute precise, long-horizon biological protocols (e.g. pipetting, centrifuging, mixing) using visual observations. This phase introduces the challenges of robotic manipulation in labs, physical simulation pipelines, and the evaluation of Vision-Language-Action (VLA) foundation models on custom benchmarks.

---

## Contents

| # | Subfolder | Core topic | Notebooks | GPU needed? |
|---|-----------|-----------|-----------|-------------|
| 1 | [`AutoBioBenchmark`](AutoBioBenchmark/) | AutoBio simulator architecture, detent/thread physics plugins, SR/SSR metrics, VLA baselines | `AutoBio_Tutorial.ipynb` | No |
| 2 | [`AutoBioComputerVision`](AutoBioComputerVision/) | Multi-view reasoning, tube localization, slot symmetry, liquid-level sensing, closed-loop UI control | `autobio_cv.ipynb` | No |

---

## Module Summaries

### Module 01 — AutoBio Simulator & Benchmark

Robotic manipulation in biology labs presents unique challenges: sub-millimeter precision requirements, transparent materials, and long-horizon protocol sequences where errors compound. This module introduces **AutoBio** (Lan et al., 2025), a custom MuJoCo-based framework designed to digitize real-world lab instruments, simulate helical screw-caps and detent dials, and benchmark state-of-the-art VLA models (e.g., OpenVLA, RDT-1B).

You will study the three-layer pipeline (Assets → Physics → Rendering), explore the math behind screw-thread helix geometry and detent snap potentials, and analyze why task-level Success Rate (SR) and Sub-Task Success Rate (SSR) are used together to diagnose VLA model failures.

**Key skills:** Simulation pipeline design, helical thread physics, detent potential modeling, SR vs. SSR metric evaluation, bimanual VLA baseline analysis.

---

### Module 02 — AutoBio Computer Vision & Closed-Loop Control

Every physical robotic action in the lab relies on first understanding the visual state of the workspace. This module translates the biological protocols of AutoBio into core computer vision tasks, providing a self-learning guide using synthetic toy datasets.

You will implement color-based tube localization and evaluate its robustness to sensor noise, perform circular-symmetry reasoning for rotor slot alignment, estimate the fill ratio of transparent tubes by boundary detection, and construct closed-loop visual control loops to actuate digital dials and panels on thermal mixers.

**Key skills:** Multi-camera visual reasoning, color-based object localization, circular symmetry slot assignment, liquid level estimation, closed-loop panel UI reading.

---

## Learning Goals

After completing Phase 05 you will be able to:

- Identify the main bottlenecks in robotic lab automation (precision limits, transparent glass/liquids, compounding errors)
- Describe the design of physics plugins for helical screw-caps, detents, and orbital mixers
- Evaluate robotic policies using Success Rate (SR) and Sub-Task Success Rate (SSR)
- Build synthetic lab scenes and implement localization, slot assignment, and liquid-level estimation pipelines
- Explain the difference between open-loop and closed-loop visual feedback control for digital instrument displays
- Walk through the evaluation of foundation VLA models on multi-step experimental protocols

---

## Setup

```bash
pip install numpy matplotlib scipy opencv-python Pillow
```
