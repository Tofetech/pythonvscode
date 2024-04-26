# SIMPLE TYPE
#create a simple church age range database
#This will get the name, age, gender of the church member

#Make sure you group members in different category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )


import streamlit as st

st.title("Church")

name = st.text_input("What is your name")

gender = st.radio(" What is you gender",["Boy","Girl"],horizontal=True)

age = st.number_input("How old are you",0)

if st.button("Which group"):
  if (age < 13):
   st.write("Go to the Kids group")

  if (age < 20):
    st.write("Go to the teens group")

  if (age < 36):
    st.write("Go to the Youth group")

  if (age < 65):
    st.write("Go to the Adult group")

  if (age > 64):
    st.write("Go to the Elders group")


