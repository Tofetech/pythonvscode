# SIMPLE TYPE
#create a simple church age range database

#This will get the name, age, gender of the church member


#Make sure you group members in different category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )

import streamlit as st

st.set_page_config(layout='wide')

Name,Age,Gender = st.columns(3)
with Name:
    name = st.text_input("Enter your name")
with Age:
    age = st.number_input("Enter your age",0)
with Gender:
    gender = st.selectbox('Gender',('Male','Female'))

submit = st.button("Submit")

if submit:
    if age >2 and age <13:
        st.success(f"Please go to the Kids class")
    elif age >12 and age <20:
        st.success(f"Please go to the Teens class")
    elif age >19 and age <36:
        st.success(f"Please go to the Youth class")
    elif age >35 and age <65:
        st.success(f"Please go to the Adults class")
    elif age >64:
        st.success(f"Please got to the Elders class")



