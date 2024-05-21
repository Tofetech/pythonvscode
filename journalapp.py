import streamlit as st

menu = st.sidebar.selectbox("Menu",["Input","inputout"])

st.title("Journal app")


if menu == 'Input':
    tot = st.text_input("Title of topic")
    cot = st.text_input("Content of topic")
    dot = st.text_input("Date or topic")

if menu == 'inputout':
    st.write("The topic of the artical is",tot,"Content of topic is ",cot,"and the date is",dot)
