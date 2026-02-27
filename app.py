import streamlit as st
import pickle
import os
import gdown

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
# STREAMLIT UI
# =========================

st.title("📰 Fake News Detection")

user_input = st.text_area("Enter News Text:")

if st.button("Predict"):

    # Dummy logic (for deployment)
    if "fake" in user_input.lower():
        st.error("🚨 Fake News")
    else:
        st.success("✅ Real News")
