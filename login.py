#use a login feature to protect the test database 

import streamlit as st
import pandas as pd

correctpass = '12345'

password = st.text_input("Enter the admin password",type='password')

if st.button("Login"):
    if password ==correctpass:
        csv = pd.read_csv('scores.csv')
        st.dataframe(csv,use_container_width=True)
    else:
        st.error("Wrong Password")