import streamlit as st

ask1 = st.number_input("Write a number",0)

ask2 = st.number_input("Write 1 number",0)

st.write("This is a caculator app where you can caculate any 2 numbers")

if st.button("_+_"):
    total1 = ask1 + ask2
    st.write(total1)


if st.button("_-_"):
    total2 = ask1 - ask2
    st.write(total2)

if st.button("_*_"):
    total3 = ask1 * ask2
    st.write(total3)

if st.button("/"):
    total4 = ask1 / ask2
    st.write(total4)