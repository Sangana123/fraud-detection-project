# Fraud Detection using Machine Learning and IP Reputation Intelligence

## Overview

This project was developed as part of a Master's thesis focused on fraud detection in e-commerce transactions using Machine Learning techniques.

The objective of this research is to evaluate the impact of integrating external IP reputation scores into fraud detection models and measure the resulting performance improvements.

In real-world environments, financial institutions and e-commerce platforms increasingly rely on IP Risk Intelligence services such as IPQualityScore, MaxMind minFraud, ThreatMetrix and Sift to identify potentially fraudulent network activity.

This project investigates whether enriching transactional data with IP reputation information can improve the detection of fraudulent transactions.

---

## Research Question

**What is the impact of IP reputation scores on the performance of Machine Learning models applied to banking fraud detection?**

---

## Dataset

The dataset contains approximately 100,000 e-commerce transactions.

### Target Variable

* `is_fraud = 0` → Legitimate transaction
* `is_fraud = 1` → Fraudulent transaction

### Transaction Features

* transactions_last_24h
* transactions_last_1h
* amount_aed
* items_count
* hour
* day_of_week
* avg_item_price

### Payment Features

* payment_method_bank_transfer
* payment_method_card
* payment_method_google_pay
* payment_method_paypal

### External Feature

* ip_risk_score

The IP reputation score represents the estimated fraud risk associated with a customer's IP address.

---

## Project Architecture

### Baseline Model

The baseline version uses only:

* Transactional features
* Payment-related features

### Enriched Model

The enriched version includes:

* Transactional features
* Payment-related features
* IP reputation score

The objective is to quantify the contribution of external IP intelligence to fraud detection performance.

---

## Machine Learning Models Evaluated

The following supervised learning algorithms were implemented and compared:

### Logistic Regression

A linear classification model used as a baseline reference.

### Decision Tree

A tree-based model capable of capturing non-linear relationships.

### Random Forest

An ensemble learning algorithm combining multiple decision trees.

### Gradient Boosting

A boosting technique that sequentially improves model performance.

### K-Nearest Neighbors (KNN)

A distance-based classification algorithm.

---

## Evaluation Metrics

Models were evaluated using the following metrics:

### Precision

Measures the proportion of predicted frauds that are actually fraudulent.

### Recall

Measures the ability to identify fraudulent transactions.

Recall is considered the most important metric in fraud detection because missing a fraud may result in significant financial losses.

### F1-Score

Harmonic mean of Precision and Recall.

### ROC-AUC

Measures the model's ability to discriminate between legitimate and fraudulent transactions.

---

## Technology Stack

### Programming Language

* Python

### Data Science Libraries

* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

### Web Application

* Flask

### Version Control

* Git
* GitHub

### Development Environment

* Jupyter Notebook
* Anaconda

---

## Web Application

A Flask application was developed to demonstrate real-time fraud prediction.

Users can:

* Enter transaction information
* Select a Machine Learning model
* Obtain a fraud prediction
* View the estimated fraud probability

The application supports:

* Baseline Random Forest model
* IP-Enriched Random Forest model

---

## Key Findings

Experimental results indicate that integrating IP reputation scores improves fraud detection performance.

The enriched models consistently achieved higher Recall and F1-Score values compared to their baseline counterparts.

These findings highlight the value of combining transactional data with external cybersecurity intelligence sources.

---

## Project Structure

```text
fraud-detection-project/

├── notebooks/
│   └── fraud_detection.ipynb
│
├── templates/
│   └── index.html
│
├── app.py
│
├── model_baseline.pkl
├── model_enriched.pkl
│
├── requirements.txt
│
└── README.md
```

## Future Improvements

* Hyperparameter optimization
* Threshold optimization for fraud detection
* Integration of real IP Risk Intelligence APIs
* Explainable AI using SHAP values
* Deployment to cloud platforms
* Real-time fraud scoring API

---

## Academic Context

This project was carried out as part of a Master's thesis in Data Science and Machine Learning.

The work combines concepts from:

* Fraud Detection
* Machine Learning
* Cybersecurity Intelligence
* Data Engineering
* Predictive Analytics

---

## Author

Sangana

Master's Thesis Project

Machine Learning • Data Science • Fraud Detection • Python • Flask
