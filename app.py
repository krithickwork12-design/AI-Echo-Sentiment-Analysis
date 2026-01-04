import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('wordnet')

st.set_page_config(
    page_title="Sentiment Analysis Dashboard",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Sentiment Analysis Dashboard")

@st.cache_resource
def load_artifacts():
    with open("tfidf_vectorizer.pkl", "rb") as f:
        tfidf = pickle.load(f)
    with open("sentiment_model.pkl", "rb") as f:
        model = pickle.load(f)
    return tfidf, model

tfidf, model = load_artifacts()

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)

# =========================
# User Input
# =========================
text = st.text_area("Enter Review Text", height=150)

# =========================
# Prediction
# =========================
if st.button("Predict Sentiment"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        clean = clean_text(text)
        vec = tfidf.transform([clean])
        pred = model.predict(vec)[0]

        st.success(f"✅ Predicted Sentiment: **{pred.upper()}**")