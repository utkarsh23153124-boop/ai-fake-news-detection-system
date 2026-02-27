import streamlit as st
import tensorflow as tf
import pickle
import re
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model
model = tf.keras.models.load_model("fake_news_model.h5")

# Load tokenizer
with open("token.pkl", "rb") as f:
    token = pickle.load(f)

max_len = 500

# Cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text

# Prediction
def predict_news(text):
    text = clean_text(text)
    seq = token.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len)

    pred = model.predict(padded)[0][0]

    if pred > 0.5:
        return "🟢 Real News"
    else:
        return "🔴 Fake News"

# UI
st.title("📰 Fake News Detection")

user_input = st.text_area("Enter News Text")

if st.button("Predict"):
    if user_input.strip() != "":
        result = predict_news(user_input)
        st.success(result)
    else:
        st.warning("Please enter text")