import numpy as np
import streamlit as st
from keras.models import load_model
import webbrowser
import app1
import app2
import app4
import app3


PAGES = {
    "PCOS Predictor":app1 ,
    "Breast Cancer Predictor" : app2,
    "Heart Disease Predictor":app3 ,
    "Pre-cancerous Lesions predictor ": app4,



}
st.sidebar.title('Stree++ ')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
st.sidebar.header('About Me & this project')
st.sidebar.write('Hi! I am Uma kadam from IIIT Guwahati and Stree++ won under the category Best Healthtech Hack in Superposition VI. from'
                 ' 523+ attendees from 23+ countries hosted on Devpost and EventBrite.')
url1= 'https://devpost.com/software/stree'
if st.sidebar.button(' Go to Devpost ') :
    webbrowser.open_new_tab(url1)
url2 = 'https://github.com/umak1106'
if st.sidebar.button(' Go to Github ') :
    webbrowser.open_new_tab(url2)
url3 = 'https://www.linkedin.com/in/uma-kadam-7885341b0/'
if st.sidebar.button(' Go to Linkedin ') :
    webbrowser.open_new_tab(url3)
