Phishing Email Detection

Overview

This project presents an AI-based approach for detecting phishing and legitimate emails using Natural Language Processing (NLP) and Machine Learning techniques.

The project was developed as part of the research study “Phishing E-mail Detection: A Research-Based Analysis.”

Research Objective

The main objective is to analyze how effectively Machine Learning models can classify phishing and legitimate emails and to compare their performance using standard evaluation metrics.

Dataset

The experiment uses multiple email datasets combined to create a binary classification dataset.

Dataset Sources

- Nazario Phishing Corpus
- Nigerian Fraud Dataset
- Enron Email Dataset
- Ling Spam Dataset

After preprocessing and duplicate removal, the dataset contained 23,089 emails.

To create a balanced classification dataset, 4,897 phishing/fraudulent emails and 4,897 legitimate emails were selected.

Final balanced dataset: 9,794 emails

- Phishing: 4,897
- Legitimate: 4,897

Methodology

The experiment followed these steps:

1. Dataset collection
2. Data preprocessing
3. Duplicate removal
4. Email subject and body combination
5. Dataset balancing
6. Stratified train-test splitting
7. TF-IDF feature extraction
8. Machine Learning model training
9. Model evaluation
10. Comparative analysis

The dataset was divided into 80% training data and 20% testing data.

TF-IDF was fitted only on the training data to avoid data leakage.

Machine Learning Models

Three classification algorithms were evaluated:

- Logistic Regression
- Random Forest
- Multinomial Naive Bayes

Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Experimental Results

Model| Accuracy| Precision| Recall| F1-score
Logistic Regression| 99.39%| 99.90%| 98.88%| 99.38%
Random Forest| 99.34%| 99.59%| 99.08%| 99.33%
Multinomial Naive Bayes| 99.13%| 99.18%| 99.08%| 99.13%

Confusion Matrices

Logistic Regression

[[979   1]
 [ 11 968]]

Random Forest

[[976   4]
 [  9 970]]

Multinomial Naive Bayes

[[972   8]
 [  9 970]]

Repository Contents

- "phishing email detection.ipynb" — Experimental notebook containing the implementation and results.
- "README.md" — Project documentation.

Research Paper

Phishing E-mail Detection: A Research-Based Analysis

The research paper presents the methodology, experimental analysis, results, limitations, and findings of this study.

Code Availability

The complete experimental notebook used in this research is publicly available in this repository.
### Live Demo

Temporary demo: https://early-friends-appear.loca.lt

Note: This demo uses a temporary LocalTunnel URL and may become unavailable.
