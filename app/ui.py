import streamlit as st
import requests


API_URL = "http://localhost:8001/demo"

st.title("🚦 Traffic Sign Demo UI")

# Call FastAPI dummy server
if st.button("Run Demo"):
    response = requests.get(API_URL)
    data = response.json()

    st.write("Demo Video:", data["video"])
    st.write("Detections:")
    for item in data["detections"]:
        st.json(item)