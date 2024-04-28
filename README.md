# Ella- An Information Retrival System
This is a straightforward information retrieval application developed with Retrieval Augmented Generation technology, utilizing LangChain.

Key features of the application include:

 1 The ability to index new documents individually. 
 2 A chat interface that enables user queries.


## Getting Started Guide


### Prerequisites 
This application is built using LangChain and Streamlit. To run this solution, you will need to install the following packages:
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
There are two services you need to operate in order to use this application: one for the user interface and another for the backend.

To run the backend service, please navigate to the 'src' folder and execute it from the terminal.
```pyhton
python3 indexAndRetrive.py
```
To run the UI service, please go to the 'dashboard' folder and run it from the terminal.
```pyhton
streamlit run dashboard.py
```
After starting these two services, you will be able to access the application using the  link http://localhost:8501.

## Todo
    1 Integrate support for additional large language models (LLMs) and embedding models.
    2 Implement a reranking feature to enhance result accuracy.
    3 Enhance the user interface for better usability.
    4 Implement functionality to delete files from the knowledge base.
    5 Introduce additional models to improve retrieval from charts, tables, and mathematical expressions.
    6 Add Optical Character Recognition (OCR) support to process text from images.
