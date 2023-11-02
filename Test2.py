import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

database = pd.read_csv('Test2.csv')

st.dataframe(database,use_container_width=True)



st1,st2 = st.columns(2)

with st1:
    name = st.text_input("What is your name",0,100)

with st2:
    age = st.number_input("How old are you",0,100)

sub1,sub2 = st.columns(2)

with sub1:
    if st.button("Check my name and age"):
        st.success(f"Your name is {name} and you are {age} years old")
        your_database = pd.DataFrame({'Name':[name] ,'Age':[age]})
        new_database = pd.concat([database,your_database],ignore_index=True)
        new_database.to_csv('test2.csv',index=False)