from langchain_core.prompts import  ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="True"

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpfull assistant. Please respond to the queries"),
        ("user","Question:{question}")
    ]
)
st.title('Ollama Chatbot')
input_text= st.text_input("Search the topic")

llm = Ollama(model="llama2:latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text})) 