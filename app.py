# Q&A Chatbot
#from langchain.llms import openai
from dotenv import load_dotenv
import os
from langchain_community.llms import HuggingFaceHub

import streamlit as st

# function to load OpenAI model and get response
def get_openai_response(question):
    os.environ["HUGGINGFACEHUB_API_TOKEN"]
    llm=HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0, "max_length":64})
    response=llm(question)
    return response
    
# initialize streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input:", key="input")
response = get_openai_response(input)

submit = st.button("Ask the question")

# if ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)


#llm_huggingface=HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0, "max_length":64})

load_dotenv() # take environment variables from .env.