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
st.sidebar.write('Hi! I am Uma kadam from IIIT Guwahati.')

st.sidebar.write("[Linkedin](https://www.linkedin.com/in/uma-kadam-7885341b0/)")
st.sidebar.write("[Github](https://github.com/umak1106)")


