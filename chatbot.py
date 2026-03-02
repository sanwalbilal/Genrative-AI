# lets build a chat app using streamlit and langchain
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("groq_api_key")

model = ChatGroq(api_key=api_key, model="llama-3.1-8b-instant")

genral_prompt = """
  Act as a cybersecurity instructor. anwer the questions about attacks like SQL injection,
  XSS, brute force, and phishing work conceptually. 
  Then provide defensive Python examples to detect, prevent, 
  and log such attacks in a controlled lab environment. Do not generate exploit code.
  Focus on mitigation and secure coding practices"""

prompt = ChatPromptTemplate.from_messages([("system", genral_prompt), ("user", "{input}")])

# creating the outputparser
parser = StrOutputParser()

# creating the chain
chain = prompt | model | parser
# creating the streamlit app
st.title("Chatbot with Langchain and Streamlit")
user_input = st.text_input("Enter your message:")
if user_input:
    response = chain.invoke(input=user_input)
    st.write("Response:", response)

