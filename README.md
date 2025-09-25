# Human-Centered Design Evaluation & Synthetic Data Generation
This repository contains two Python mini-sub-projects that demontrate data analysis and data augmentation workflows.
1. **Human Centered Design Evaluation (Video Ratings Analysis)** provides analysis of real Instagram videos using human evaluation rubric scores (appeal, clarity, creativity) and engagement metrics (likes, comments, number of savings, sharings and views).
2. **Synthetic Data Generation** provides creation of augmented image datasets using Pytorch/Torchvision package for machine learning experiments.


## 1. Human Centered Design Evaluation (Video Ratings Analysis)

This sub-project analyzes three Instagram videos based on:
1. Rubric scores of two real subjective human ratings.
2. Real engagement metrics (normalized by number of views values of likes, comments, sharings, savings)

### Goal
1. Checking inter-rate reliability of human ratings using Cohen's kappa.
2. Comparing scores between human judgment and user behavior.
3. Computing correlations of different metrics.
4. Vizualizing average human ratings. 

### Features:
1. Loads video engagement metrics and a rubric for human feedback from Pandas DataFrame.
2. Supports inter-rater agreement metrics (Cohen’s kappa).
3. Normalizes engagement metrics.
4. Computes metrics correlations.
5. Generates visualization of rubric for analysis.


## 2. Synthetic Data Gemeration

This sub-project generates synthetic images by applying transformations to 3 existing Instagram video-thumbnails. 
The synthetic dataset can be used to:
- Train machine learning models with more diverse samples.
- Simulate different real-world conditions (lighting, quality of camera, etc.).

### Techniques Used
- Brightness adjustment
- Contrast adjustment
- Saturation adjustment
- Sharpness adjustment

### Vizualization
Row 1: 5 variations of brightness, contrast and saturation. 
Row 2: 5 variations of sharpness.


## Required Installations:
This project requires Python 3.12. 
Installation of the following packages:
- Pandas
- sklearn 
- Matplotlib (Pyplot)
- PyTorch (Torchvision)