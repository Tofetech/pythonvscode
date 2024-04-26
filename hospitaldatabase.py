import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('menu', ["Hospital painent Registration", "PATIENT CONTACT DETAILS" ])

database = pd.read_csv('hospital.csv')

st.dataframe(database,use_container_width=True)

st.title("Hospital Paient Registration")

subt,subt2 = st.columns(2)

with subt:
    select = st.radio("select Title",["Mr","Ms","Miss","Mrs"],horizontal=True)

with subt2:
    regdate = st.date_input("Data of registration")

st1,st2 = st.columns(2)

with st1:
    firstname = st.text_input("First name")

with st2:
    seconname = st.text_input("Second name")

p1,p2 = st.columns(2)

with p1:
    lastname = st.text_input("Last name")

with p2:
    nickname = st.text_input("Nick name")

dat1,dat2 = st.columns(2)

with dat1:
       birth = st.date_input("Date of Birth")

with dat2:
     gender = st.radio("select ",["Male","Female"],horizontal=True)

st.title("PATIENT CONTACT DETAILS")

mpa1,mpa2 = st.columns(2)

with mpa1:
     phone = st.text_input("Mobile Phone")

with mpa2:
     address = st.text_input("Address")

hpe1,hpe2 = st.columns(2)

with hpe1:
     homephone = st.text_input("Home Phone")

with hpe2:
     email = st.text_input("Email")

ctpc1,ctpc2 = st.columns(2)

with ctpc1:
     city = st.text_input("City]]Town")

with ctpc2:
     postcode = st.text_input("Postcode")

if st.button("Register patient"):
     st.success(f"The patient detal has been submited we will get back to you soon")
     student_database = pd.DataFrame()
     


