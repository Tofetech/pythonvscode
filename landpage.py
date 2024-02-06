import streamlit as st

st.set_page_config(layout='wide')

menu = ["ABOUT Me","CONTACT","WHERE I LIVE"]
choice = st.sidebar.selectbox('menu',menu)

st.image('https://assets.telegraphindia.com/telegraph/2022/Mar/1647575151_resized-pic23.jpg')

if choice == 'ABOUT Me':
      st.title("Hello my name is Tofe i am 11 years old i like school,Games my favourite subject is Math and i am very good at it and i am in year 8 and i like Tech")

    
if choice == 'CONTACT':
      st.title("My number is 05098437612")

if choice == 'WHERE I LIVE':
      st.title("I live in UAE gate towers reem island")