import streamlit as st
import tensorflow as tf
import pickle
import os
import gdown
from tensorflow.keras.preprocessing.sequence import pad_sequences

# =========================
# GOOGLE DRIVE LINKS
# =========================

MODEL_URL = "https://drive.google.com/uc?id=1ccaYOnuSjoatF9FFk0PI3mcV9MNG-78y"
TOKEN_URL = "https://drive.google.com/uc?id=1uiRj-Xc5yKEv6ELe8lhRhCyP0kp8nTCh"

# =========================
# DOWNLOAD FILES
# =========================

# Download model
if not os.path.exists("fake_news_model.h5"):
    gdown.download(MODEL_URL, "fake_news_model.h5", quiet=False)

# Download tokenizer
if not os.path.exists("token.pkl"):
    gdown.download(TOKEN_URL, "token.pkl", quiet=False)

# =========================
# LOAD MODEL & TOKENIZER
# =========================

model = tf.keras.models.load_model("fake_news_model.h5")

with open("token.pkl", "rb") as f:
    tokenizer = pickle.load(f)

max_length = 100

# =========================
# STREAMLIT UI
# =========================

st.title("📰 Fake News Detection")

user_input = st.text_area("Enter News Text:")

if st.button("Predict"):
    seq = tokenizer.texts_to_sequences([user_input])
    padded = pad_sequences(seq, maxlen=max_length)

    prediction = model.predict(padded)[0][0]

    if prediction > 0.5:
        st.error("🚨 Fake News")
    else:
        st.success("✅ Real News")
