from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROOQ_API_KEY"),
               model="llama3-70b-8192")
llm2 = Ollama(model="llama3:latest ")

app=FastAPI(
    title="Langchain server",
    version="1.0",
    description="API Server"
)

add_routes(
    app,
    llm,
    path="/Groq"
)
               
prompt1 = ChatPromptTemplate.from_template("Write me a essay about {topic}")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} make it short and concise , make sure it rhymes")
prompt3 = ChatPromptTemplate.from_template("Write me a story about {topic}")

add_routes(
    app,
    prompt1|llm,
    path="/essay"   
)
add_routes(
    app,
    prompt1|llm2,
    path="/poem" 
)  
add_routes(
    app,
    prompt3|llm,
    path="/story"   
)
if __name__ =="__main__":
    uvicorn.run(app,host="localhost",port=8000)
