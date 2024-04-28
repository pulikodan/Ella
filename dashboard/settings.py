import streamlit as st
import requests
#Set tab name
st.set_page_config(page_title='Ella-Settings')
#Set page title
st.title("Settings")

#LLM selections
genre = st.radio(
    "Language models (LLMS)",
    ["GPT-3.5", "Llama 2 7B", "Llama 3 8B", "Claude 3 Opus","Gemini 1.5 Pro"],
    disabled=True)

#Embedding Models selections
genre = st.radio(
    "Embedding Models",
    ["OpenAI Ada", "OpenAI Large","E5-Mistral","SFR-Embedding-Mistral","GritLM-7B","Cohere-embed-multilingual-v3.0"],
    disabled=True)

#Accept openkey token from users
user_input = st.text_input("OpenAI Key", "Please enter your key",disabled=True)
#if user_input:
if 0:
    url1="http://127.0.0.1:4000/updateOpenAIkey"
    fobject={}
    fobject['apikey']=user_input
    x=requests.get(url1, data=fobject)
    print(x.text)

#Chunk size and overlap
user_input = st.text_input("Chunk Size", 4096,disabled=True)
user_input = st.text_input("Text Overlap", 1024,disabled=True)