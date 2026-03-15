# PhageLytic-ESM: Deep Learning for Bacteriophage Enzyme Classification

## Overview
Antimicrobial Resistance (AMR) is a rapidly escalating global health crisis. Bacteriophage lytic proteins (endolysins) present a highly targeted, programmable alternative to broad-spectrum antibiotics. 

**PhageLytic-ESM** is a machine learning pipeline designed to classify phage lytic proteins into three distinct functional classes: Amidases, Glycosylases (Lysozymes), and Peptidases (M15/M23 domains). By leveraging transfer learning through the **ESM-2 Protein Language Model**, this project extracts high-dimensional structural embeddings from raw amino acid sequences to train lightweight, highly accurate downstream classifiers.

## Dataset
Data is curated from the **PhaLP 2.0 Database** and strictly filtered by Enzyme Commission (EC) numbers and structural domains to ensure biological validity:
* **Amidase:** EC `3.5.1.28`
* **Glycosylase (Lysozyme):** EC `3.2.1.17`
* **Peptidase:** `M15` and `M23` metalloendopeptidase domains

*(Note: Raw sequence data is stored locally in the `data/raw` directory. The processed data is also in the directory. Moreover, the features extracted by the ESM-2 model are in the `X_esm_features.npy` and `y_labels.npy` file. There is a code block to load the files instead of needing to extract the features yourself.).*

## Tech Stack & Architecture
* **Feature Extraction:** Pre-trained ESM-2 (Evolutionary Scale Modeling) Transformer.
* **Hardware Acceleration:** PyTorch utilizing Apple Metal Performance Shaders (MPS) for local M-series compute.
* **Data Processing:** Pandas, NumPy.
* **Classification Models:** Scikit-learn (MLP, Random Forest, XGBoost, Logistic Regression, K-Nearest Neighbors, Naive Bayes).

## Methodology 
1. **Data Preprocessing:** Aggregation, sequence length validation, and droping of duplicates.
2. **Embedding Generation:** Transforming variable-length biological text sequences into fixed-length numerical vectors using ESM-2.
3. **Cluster-Aware Splitting:** Grouping training and test sets by Cluster Name to prevent sequence data leakage and artificially inflated accuracy metrics.
4. **Supervised Classification:** Training and hyperparameter tuning of downstream classifiers to achieve maximum predictive performance.