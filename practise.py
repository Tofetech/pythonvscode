#Create a program that accepts user input for their respective age. 

#0 - 12 falls in Children 
#13 - 19 falls in Teens
#20 - 40 falls in Youths
#41 - above falls in Adults

#Using streamlit print age category to user after entering their age.

import streamlit as st
age = st.number_input("What is your age",0)
if age >0 and <12:
    st.write("")

