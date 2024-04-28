import os
import configparser


from flask import Flask, redirect, url_for, request,jsonify

import requests 
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


config = configparser.ConfigParser()
config.read('config.cfg')
openAikey= str(config['DEFAULT']['openaikey'])
os.environ["OPENAI_API_KEY"] = openAikey


#Select OpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")


#Index reload API
url2="http://127.0.0.1:4000/reloadIndex"

prompt = hub.pull("rlm/rag-prompt")

example_messages = prompt.invoke(
    {"context": "filler context", "question": "filler question"}
).to_messages()


#Configure text splitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2048, chunk_overlap=1024, add_start_index=True
)

#Configure vector db
vectordb = Chroma(persist_directory="embeddings",embedding_function=OpenAIEmbeddings())


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

#Configure retriever
retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 6},similarity = True)

#Configure RAG chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


app = Flask(__name__)

#update OpenAI key in the config file 
@app.route('/updateOpenAIkey', methods=['POST','GET'])
def updateOpenAIkey():
    config.read('config.cfg')
    data = request.form.to_dict(flat=False)
    openAikey= data['apikey'][0]
    config.set('DEFAULT', 'OpenAIKey',str(openAikey))
    with open('config.cfg', 'w') as configfile:
        config.write(configfile)   
    return "ok"    

#Index documents 
@app.route('/index', methods=['POST','GET'])
def index():
        a=request.data
        data = request.form.to_dict(flat=False)
        filename= data['fname'][0]
        loader = PyPDFLoader(filename)
        
        pages = loader.load_and_split()
        docs = loader.load()
        
        all_splits = text_splitter.split_documents(docs)
        try:
            vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings(),persist_directory="embeddings")
        except:
             return "Error"

        #k=vectordb._collection.count()
        x=requests.get(url2)
        return "ok"
        
#Reload VextorDB after indexing
@app.route('/reloadIndex', methods=['POST','GET'])
def reloadIndex():
    global vectordb
    global retriever
    global rag_chain
    vectordb = Chroma(persist_directory="embeddings",embedding_function=OpenAIEmbeddings())

    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 6},similarity = True)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return "Ok"

#Retrive from DB and format using LLMs
@app.route('/retrive', methods=['POST','GET'])
def retrive():
    a=request.data
    data = request.form.to_dict(flat=False)
    inquery= data['inquery'][0]
    responce=""
    for chunk in rag_chain.stream(inquery):
        responce+=chunk
    
    return responce

if __name__ == '__main__':
    app.run(debug=False,port=4000)

