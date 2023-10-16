
import streamlit as st

st.title("Welcome to the age caculator app")

name = st.text_input("What is your name")
yearofbirth = st.number_input("What is your year of birth",value=1995)
currentyear = st.number_input("What is the current year",value=2023)

age = currentyear - yearofbirth

Internet = st.checkbox("Are you allowed to use internet")

if st.button("Show my age"):
    st.write("You are",age,"years old in year",currentyear)