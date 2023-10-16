#HOMEWORK
#A church asks members of their age:
#if the member is less than 13, please go to the kids class
#if the member is from 13 to 19, please go to the teens class
#if the member is older than 20, you can go to the adult class
#Any age between 0 - 2 is not not allowed yet in church
#Any age below 0 is an error, not acceptable

import streamlit as st

st.title("Church classes")

age = st.number_input("How old are you:",value=3,step= 1,format="%d")



if (age <  13):
  st.write("Please go to the kids class")


elif (age > 12) and (age <20):
  st.write("Please go to the teens class")


elif (age > 19):
  st.write("Please go to the adult class") 



