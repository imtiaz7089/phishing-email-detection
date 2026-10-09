# AI-Based Phishing Email Detector

An AI-based web application that uses Machine Learning and Natural Language Processing techniques to classify emails as legitimate or potentially phishing/fraudulent.

## 🚀 Live Demo

**Try the application:** [AI-Based Phishing Email Detector](https://phishing-email-detection-k5tmgwwhxqpjhj2zjwo2gm.streamlit.app/)

## ✨ Features

* AI-based phishing email classification
* Logistic Regression machine learning model
* TF-IDF text feature extraction
* Email subject and body analysis
* Classification into legitimate and phishing/fraudulent emails
* Interactive web interface built with Streamlit
* Publicly accessible web application

## 🛠️ Technologies Used

* Python
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* Streamlit
* Joblib
* Pandas
* NumPy

## 📊 Model Performance

The Logistic Regression model was evaluated using the CEAS_08 dataset, TF-IDF features, and an 80/20 stratified train-test split.

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 99.45% |
| Precision | 99.43% |
| Recall    | 99.59% |
| F1-score  | 99.51% |

**Note:** These metrics represent the experimental evaluation results. They do not guarantee the same performance on unseen or real-world emails.

## ⚙️ How It Works

1. The user enters an email subject and body.
2. The text is transformed into TF-IDF features.
3. The trained Logistic Regression model analyzes the features.
4. The application predicts whether the email is legitimate or potentially phishing/fraudulent.
5. The prediction is displayed on the web interface.

## 📁 Project Files

* `app.py` — Streamlit web application
* `model.pkl` — Saved machine learning model
* `vectorizer.pkl` — Saved TF-IDF vectorizer
* `phishing_email_detection_updated.ipynb` — Updated research and experimentation notebook
* `requirements.txt` — Python dependencies

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/imtiaz7089/phishing-email-detection.git
cd phishing-email-detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## ⚠️ Limitations

* The model's performance may vary on emails from sources not represented in the training data.
* Experimental test results do not guarantee real-world accuracy.
* The application should be used as a preliminary screening tool, not as the sole basis for security decisions.

## 🔮 Future Improvements

* Evaluate the model on additional independent datasets.
* Test performance against newer and more diverse phishing emails.
* Improve feature engineering and model generalization.
* Explore URL and sender-domain analysis.
* Add more comprehensive security testing.

## 👨‍💻 Author

**Imtiaz Ahmed**

GitHub: [@imtiaz7089](https://github.com/imtiaz7089)

## 📜 Disclaimer

This project is developed for educational and research purposes. Predictions may be incorrect, so users should independently verify suspicious emails and avoid clicking untrusted links or sharing sensitive information.


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
