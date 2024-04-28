# Ella- An Information Retrival System
It ia a very basic information retrival systems with following features 
  1)Index the douments 
  2)A basic Chat interface for question aswering 


```
## Getting Started guide


### Prerequisites 
This applications mainly use Langchain and streamlit 
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
Ther are two services you have to run to use this, one for UI and other for the backend.
Inoder to run the backed service, plese go to src folder and run it from the terminal
```pyhton
python3 indexAndRetrive.py
```
Inoder to run the UI service, plese go to dashboared folder and run it from the terminal
```pyhton
streamlit run dashboard.py
```
## Todo
streamlit run dashboard.py
python3 indexAndRetrive.py
