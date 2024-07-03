import streamlit as st

st.set_page_config(layout='wide')

st.title("Gems Winchester")

name = st.text_input("What is the student name")

sub1,sub2,sub3 = st.columns(3)

with sub1:
    math = st.number_input("How much score did the student get in Math",0)
    english = st.number_input("How much score did the student get in English",0)
    humanities = ("How much did the student get in Humanities",0)

with sub2:
    art = st.number_input("How much score did the student get in Art",0)
    non_arabic = ("How much score did the student get on Non arab",0)
    moral = ("How much did the student get in Moral",0)


with sub3:
    science = st.number_input("How much score did the student get in Science",0)
    arabic = ("How much did the student get in arabic")



