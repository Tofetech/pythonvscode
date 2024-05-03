import streamlit as st

correctpass = '12345'

password = st.text_input("Enter the admin password",type='password')

if st.button("Tofflix"):
    if password == correctpass:
        st.image("https://cdn.pixabay.com/photo/2016/03/23/16/23/minecraft-1275065_1280.jpg")
        st.image("https://cdn.pixabay.com/photo/2018/03/12/04/00/mammal-3218712_1280.jpg")
    else:
        st.write("Wrong password")

