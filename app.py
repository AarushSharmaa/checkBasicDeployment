import streamlit as st
import requests

st.title("Hello World with Streamlit and Flask")

# Make a request to the Flask API
response = requests.get("http://localhost:5000/hello")

# Display the response from the API
if response.status_code == 200:
    api_message = response.json().get("message", "No message found")
    st.write(f"Flask API says: {api_message}")
else:
    st.write("Failed to connect to the Flask API")
