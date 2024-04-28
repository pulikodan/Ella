import streamlit as st
import random
import time
import requests

#Set tab name
st.set_page_config(page_title='Ella-Chat')

#Set page title
st.title("Hi, I am Ella, How can I assist you? ")

#Retrival service endpoints 
url2="http://127.0.0.1:4000/retrive"

#Chat UI template
st.markdown(
    """
<style>
    .st-emotion-cache-4oy321 {
        flex-direction: row-reverse;
        text-align: right;
    }
</style>
""",
    unsafe_allow_html=True,
)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
inquery=""
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        inquery=prompt
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Generate and display assistant response
if len(inquery)>0:
    with st.chat_message("assistant"):
        fobject={}
        fobject['inquery']=prompt
        x=requests.get(url2, data=fobject)
        chatresponse=x.text
        response = st.write(chatresponse)


    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": chatresponse})



