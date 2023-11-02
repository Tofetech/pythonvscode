import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Menu', ['Save Now', 'View Savings'])

database = pd.read_csv('saving.csv')

saving1,saving2 = st.columns(2)

with saving1:
    monday = st.number_input("How much do you wont to save on Monday",value=0)
    tuesday = st.number_input("How much do you wont to save on Tuesday",value=0)

with saving2:
    wednesday = st.number_input("How much do you wont to save on Wednesday",value=0)
    thursday = st.number_input("How much do you wont to save on Thursady",value=0)

