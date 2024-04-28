'''
For onboarding documents in bulk
'''

import os
import sqlite3
import requests
import pandas as pd
import datetime

con = sqlite3.connect("doclibrary.db")
cur = con.cursor()

#indexing service 
url1="http://127.0.0.1:4000/index"
dataDir="../data/"


# assign directory
directory = './llm_papers'
directory2= '../dashboard/llm_papers'
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory2, filename)
    # checking if it is a file
    if os.path.isfile(f):
        df = pd.read_sql_query("SELECT * FROM docList", con)
        if filename not in df['docName'].values:
            print(f)
            fobject={}
            fobject['fname']=f
            x=requests.get(url1, data=fobject)
            uploadedStatus=2
            current_time = datetime.datetime.now()
            date=str(current_time.day)+"-"+str(current_time.month)+"-"+str(current_time.year)
            time=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            insertCmd="INSERT INTO docList (docName, uploadedDate, uploadedTime) VALUES ('"+filename+"', '"+date+"', '"+time+"'); "
            cur.execute(insertCmd)
            con.commit()