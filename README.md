# Ella- An Information Retrival System
It ia a very basic information retrival systems based of Retrival Augemented Generation and it is built using LangChain.
  
This are the main fetures of the system 

  1) Ability to index new documnts in fifle by file mode 
  2) A chat interface where user can query    



## Getting Started guide


### Prerequisites 
This applications built suning  Langchain and streamlit, and you need to install following packages to run this solution
```pyhton
Flask==2.2.5
langchain==0.1.16
langchain_chroma==0.1.0
langchain_community==0.0.34
langchain_core==0.1.46
langchain_openai==0.1.4
langchain_text_splitters==0.0.1
numpy==1.26.4
pandas==2.2.2
Requests==2.31.0
st_pages==0.4.5
streamlit==1.32.0
```
Ther are two services you need to run to use this, one for UI and other for the backend.

Inoder to run the backed service, please go to 'src' folder and run it from the terminal
```pyhton
python3 indexAndRetrive.py
```
Inoder to run the UI service, plese go to 'dashboared' folder and run it from the terminal
```pyhton
streamlit run dashboard.py
```
After starting this two services, you will be able to use the application using the link 

## Todo
1) Add support for other LLMs and embedding models
2) Add reranker
3) Improve the UI
4) Add suport for deleting the files from the knowledgebase
5) Add additional models to support effective retrivel from charts, tables and mathematicl expressions
6) Add OCR support 
