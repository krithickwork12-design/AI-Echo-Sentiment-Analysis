# AI ECHO - Sentiment Analysis Dashboard

An **end-to-end NLP & Machine Learning project** built using **Streamlit**, designed to analyze and predict the sentiment of textual data in real time. This application demonstrates how a trained ML model can be integrated into an interactive web interface for practical use.

---

## About the Project

The Sentiment Analysis Dashboard allows users to input free-form text (such as reviews or feedback) and instantly receive a sentiment prediction. The project covers the complete NLP lifecycle:

* Text preprocessing
* Feature extraction using TF-IDF
* Machine learning–based sentiment prediction
* Deployment-ready Streamlit interface
* 
---

## Workflow Architecture

1. **User Input** – Text entered via Streamlit UI
2. **Text Cleaning & Preprocessing**

   * Lowercasing
   * Removing special characters
   * Stopword removal
   * Lemmatization
3. **Vectorization** – TF-IDF transformation
4. **Prediction** – Pre-trained ML model inference
5. **Output** – Sentiment result displayed to user

---

## Model Details

* **Vectorizer**: TF-IDF (Term Frequency–Inverse Document Frequency)
* **Model Type**: Supervised Machine Learning Classifier
* **Input**: Cleaned text
* **Output**: Sentiment label (e.g., Positive / Negative)

> Note: Model performance depends on the dataset used during training.

---

## Technology Stack

* **Programming Language**: Python
* **Web Framework**: Streamlit
* **ML & NLP**: Scikit-learn, NLTK
* **Text Processing**: Regex, Lemmatization
* **Model Storage**: Pickle

---

## Features

* Clean and minimal UI
* Real-time sentiment prediction
* Efficient model loading with caching
* Scalable and deployment-ready structure

---

## Use Cases

* Product and service review analysis
* Customer feedback monitoring
* Social media sentiment analysis
* NLP learning and experimentation

---

## Author

**S Krithick**
Data Scientist | NLP | Machine Learning
