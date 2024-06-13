import streamlit as st

st.text_input("What is your name")
st.number_input("How old are you ",0)

st.radio('What is your favorite type of food',['Mexican','Italian','Fat','Nuts and seeds','Seafood'])

st.selectbox('what hobbie do you like',  ['Hiking','Cooking','Football','Basketbal','Reading','Gaming','Painting'])

st.text_input("Why do you like the hobbie")

st.number_input('how familiarity are you with technology',0,5)

st.text_input("Now you can write any comments or suggestion you have")

if st.button('Submit'):
    st.text_input("Thank you for your comment have a nice day")
