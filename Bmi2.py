import streamlit as st

st.set_page_config(layout='wide')

st.header("Body mass Index")
st.subheader("MI (Body mass index) is a measure that use you height and weight to work out if your weight is healthy")
st.write("")

st.subheader("Enter you height")
h1,h2,h3 = st.columns(3)
with h1:
    meters = st.number_input("Enter your height in meters")
with h2:
    inches = st.number_input("Enter your height in inches")

st.write("")
st.subheader("Enter your weight")
w1,w2,w3 = st.columns(3)
with w1:
    kg = st.number_input("Enter weight in kg")
with w2:
    pounds = st.number_input("Enter weight in pounds")

submit = st.button("Check my Mass")
if submit:
    if kg and meters:
        mass=kg/(meters**2)


        if mass < 18.5:
            st.warning("Your Bmi is {mass} and you are **UNDERWEIGHT**")
        elif mass >= 18.5 and mass < 25:
            st.success("Your Bmi is {mass} and you have a **HEALTHY WEIGHT**")
        elif mass >= 25 and mass <30:
            st.warning("Your Bmi is {mass} and you are **OVERWEIGHT**")
        elif mass >= 30:
            st.error("Your Bmi is {mass} and you are**OBESE**")