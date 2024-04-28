#Homework 1
#Create an python app
#-Ask for the user name on the left column and their email on the right column
#next create an age calculator to find out their age
#-create a submit button
#show their name, email and age after submit button is clicked
#-create a csv and a table
#PUBLISH THIS ONE AND SHARE THE LINK

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

database2 = pd.read_csv('mrt1.csv')



menu= st.sidebar.selectbox('menu',['Submit scores','Database2'])

if menu == 'Database2':
   st.table(database2)






if menu  == 'Submit scores':
  ne1,ne2 = st.columns(2)

  with ne1:
        Name = st.text_input("What is your name")

  with ne2:
        Email = st.text_input("what is your email number")
  yearofbirth = st.number_input("What is your year of birth",value=1995)
  currentyear = st.number_input("What is the current year",value=2023)

  Age = currentyear - yearofbirth

  if st.button("Submit Student score"):
    st.success(f"Your name is{Name} you are {Age} years old and your email is {Email}")
               
    Homework1_dict = {'Name':[Name],'Age':[Age],'Email':[Email],'yearofbirth':[yearofbirth],'currentyear':[currentyear]}
    age_database = pd.DataFrame(Homework1_dict)
    new_database = pd.concat([database2,age_database],ignore_index=True)
    new_database.to_csv('mrt1.csv',index=False)
   
   
