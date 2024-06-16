import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie_spinner

def get_groq_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']['content']


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']

def get_groq_responseST(input_text):
    response = requests.post("http://localhost:8000/story/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']['content']

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Enhanced UI
st.set_page_config(
    page_title="LangChain API Demo",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('📚 LangChain API Demo')
st.subheader('Generate text content using LangChain models')

# Sidebar options
st.sidebar.title("Options")
text_type = st.sidebar.selectbox(
    "Select type of text",
    ("Essay", "Poem", "Story")
)

# Input fields
st.markdown(f"### Write a {text_type.lower()} on")
input_text = st.text_area(f"Enter the topic for the {text_type.lower()}", height=100, max_chars=100)

# Button to submit request
if st.button(f"Generate {text_type}", key='generate_button', help=f'Click to generate a {text_type.lower()} based on the input topic'):
    if input_text:
        with st.spinner('Fetching response, please wait...'):
            if text_type == "Essay":
                response = get_groq_response(input_text)
            elif text_type == "Poem":
                response = get_ollama_response(input_text)
            elif text_type == "Story":
                response = get_groq_responseST(input_text) 
            st.markdown(f"### Generated {text_type}")
            st.write(response)
    else:
        st.error("Please enter a topic.")
