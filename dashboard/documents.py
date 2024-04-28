import streamlit as st
import pandas as pd
import numpy as np
import os
import requests
import datetime
import sqlite3
import pandas as pd
import streamlit.components.v1 as components
#set tab name
st.set_page_config(page_title='Ella-Update')


#doument db 
con = sqlite3.connect("doclibrary.db")
cur = con.cursor()

#page title
st.title('Update my knowledge')

#indexing service 
url1="http://127.0.0.1:4000/index"
dataDir="../data/"

#update status flag
uploadedStatus=0

uploaded_file = st.file_uploader('Upload a Pdf document', type="pdf")

if uploaded_file is not None:

    df = pd.read_sql_query("SELECT * FROM docList", con)

    if uploaded_file.name in df['docName'].values:
        uploadedStatus=1
    else:
        with open(os.path.join(dataDir,uploaded_file.name),"wb") as f:
            f.write(uploaded_file.getbuffer())
        fobject={}
        fobject['fname']='../data/'+uploaded_file.name
        x=requests.get(url1, data=fobject)
        uploadedStatus=2
        current_time = datetime.datetime.now()
        date=str(current_time.day)+"-"+str(current_time.month)+"-"+str(current_time.year)
        time=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
        insertCmd="INSERT INTO docList (docName, uploadedDate, uploadedTime) VALUES ('"+uploaded_file.name+"', '"+date+"', '"+time+"'); "
        cur.execute(insertCmd)
        con.commit()



#Response and warnings        
if uploadedStatus==1:
    mycode = "<script>alert('Document with this name is already present in the knowledge base!')</script>"
    components.html(mycode, height=0, width=0)
    uploadedStatus=0
if uploadedStatus==2:
    mycode = "<script>alert('Successfully indexed the docuemnt!')</script>"
    components.html(mycode, height=0, width=0)
    user_table = pd.read_sql_query("SELECT * FROM docList", con)
    uploadedStatus=0


#Session headings
st.write(' ')
st.write('Uploaded documents')

# Show document list
colms = st.columns((1, 2, 2, 1, 1))
fields = ["Document #", 'Document Name', 'Upload Date', 'Upload time']


for col, field_name in zip(colms, fields):
    col.write(field_name)

 
# Get doc list from table
user_table1 = pd.read_sql_query("SELECT * FROM docList", con)

# Reverse doc list
user_table=user_table1.reindex(index=user_table1.index[::-1])



count_row = user_table.shape[0]
for x in range(count_row-1,-1,-1):
    col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
    col1.write(x+1)  # index
    col2.write(user_table['docName'][x])  # Document data
    col3.write(user_table['uploadedDate'][x])  # uploaded date
    col4.write(user_table['uploadedTime'][x])  # uploaded time 
