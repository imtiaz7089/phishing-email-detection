import streamlit as st
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="AI Phishing Email Detector", page_icon="🛡️")
st.title("AI-Based Phishing Email Detector")
st.write("Enter an email subject and body to check the email.")

subject = st.text_input("Email Subject")
body = st.text_area("Email Body")

if st.button("Detect"):
    email_text = subject + " " + body
    features = vectorizer.transform([email_text])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("Phishing / Fraudulent Email")
    else:
        st.success("Legitimate Email")
