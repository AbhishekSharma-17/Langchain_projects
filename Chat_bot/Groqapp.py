from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

 
os.environ["LANGCHAIN_TRACING_V2"] = "True" 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") 

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpfull assistant. Please respond to the queries"),
        ("user","Question:{question}")
    ]
)
st.title('langchain chatbot')
input_text= st.text_input("Search the topic")



llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),
               model="llama3-70b-8192",
               )
output_parser= StrOutputParser()
chain= prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))