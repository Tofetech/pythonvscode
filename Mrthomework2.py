#Homework 2:
#Create a python program to ask the user to enter 2 numbers
#Then create a dictionary to show the numbers the user entered, show the addition and the multiplication of the numbers also in the dictionary
#Convert the dictionary to a table

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

Number1 = st.number_input("Enter 1 number",0)

Number2 = st.number_input('Enter a number',0)

add1 = Number1 + Number2

multiplication = Number1 * Number2

Numberinput = {'Number1':[Number1],'add':[add1],'Number2':[Number2],'Multiplication':[multiplication ]}

if st.button("Database"):
    
    st.write("Thank you")

    dataframe = pd.DataFrame(Numberinput)

    st.table(dataframe)











