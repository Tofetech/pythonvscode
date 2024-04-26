#TEST 1
#write a python program for house buyers
#create a menu for the buy house page and the house database page
#Ask them for their name
#ask them for their yearly salary
#if they earn below 100000 they can buy or rent an apartment
#If the earn between 100000-500,000 they can buy a bungalow
#If the earn between >500,000-1,000,000 they can buy a duplex
#If the earn between >1,000,000-5,000,000 they can buy a manshion
#if the earn above 5000000 they can buy an estate
#create a database to to store and view their answers and display in another customer section

import streamlit as st
import pandas as pd

database = pd.read_csv('buyhouse.csv')


menu = st.sidebar.selectbox("Menu",["Houses for sale","store"])

if menu == 'Houses for sale':
  st.title("Houses For Sale")
  Name = st.text_input("What is you name")
  salary = st.number_input("What is your yearly salary",0)

  if st.button("Submit"):
    if (salary > 100000 and salary <= 500000):
        st.write("You can buy a bungalow")

    elif (salary > 500000 and salary <= 1000000):
        st.write("You can buy a duplex")

    elif (salary > 1000000 and salary <= 5000000):
        st.write("You can buy a manshion")


     
    student_database = pd.DataFrame({'name':[Name],'salary':[salary]})
    new_database = pd.concat([database,student_database],ignore_index=True)
    new_database.to_csv('buyhouse.csv',index=False)
    st.success(f"House bought")

if menu == 'store':
   st.table(database)
   
