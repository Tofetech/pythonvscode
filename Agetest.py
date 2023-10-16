
import streamlit as st

st.title("Welcome to my age caculator")


name = st.text_input("Enter your name")
yearofbirth = st.number_input("Enter your year of birth",value=1995)
currentyear = st.number_input("Enter the current year ",value=2023)

age = currentyear - yearofbirth

internet = st.checkbox("Are you allowed to use internet")

if st.button("Show my age"):
 st.write("You are",age,"years old in year",currentyear)
