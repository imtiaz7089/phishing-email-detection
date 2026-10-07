# Phishing Email Detection

## Overview

This project presents an AI-based approach for detecting phishing and legitimate emails using Natural Language Processing (NLP) and Machine Learning techniques.

The project was developed as part of the research study **“Phishing E-mail Detection: A Research-Based Analysis.”**

## Research Objective

The main objective is to analyze how effectively Machine Learning models can classify emails and to compare their performance using standard evaluation metrics.

## Dataset

The experiment uses the **CEAS_08 email dataset**.

The dataset contains **39,154 email records** used for the experiment.

## Methodology

The following steps were performed:

1. Data preprocessing
2. Email subject and body text preparation
3. TF-IDF feature extraction
4. Train-test splitting
5. Machine Learning model training
6. Model evaluation
7. Comparative analysis

## Machine Learning Models

Three classification algorithms were evaluated:

- Logistic Regression
- Random Forest
- Multinomial Naive Bayes

## Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score

## Experimental Results

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Logistic Regression | 99.45% | 99.43% | 99.59% | 99.51% |
| Random Forest | 99.63% | 99.68% | 99.66% | 99.67% |
| Multinomial Naive Bayes | 98.66% | 99.70% | 97.89% | 98.79% |

Random Forest achieved the highest overall Accuracy, Recall, and F1-score among the three evaluated models.

## Repository Contents

- `phishing email detection.ipynb` — Experimental notebook containing the code and results.
- `README.md` — Project documentation.

## Research Paper

**Phishing E-mail Detection: A Research-Based Analysis**

The research paper is based on the methodology and experimental results presented in this repository.

## Code Availability

The complete experimental notebook used in this research is publicly available in this repository.
