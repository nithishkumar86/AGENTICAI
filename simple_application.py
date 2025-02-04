import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv('GROQ_API_KEY')

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=ChatGroq(model="gemma2-9b-it")

prompt=ChatPromptTemplate.from_messages([
    ("system","As yor are an ai expert please provide me answer based on the question"),
    ("user","{question}")
])

chain=prompt|llm|StrOutputParser()

input=st.text_input("tell me what's your doubt")

if input:
    response=chain.invoke({"question":input})
    st.write(response)