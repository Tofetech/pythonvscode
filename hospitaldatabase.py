import streamlit as st

st.set_page_config(layout='wide')

st.title("Hospital Paient Registratoin")

subt,subt2 = st.columns(2)

with subt:
    select = st.radio("select Title",["Mr","Ms","Miss","Mrs"],horizontal=True)

with subt2:
    regdate = st.date_input("Data of registration")

st1,st2 = st.columns(2)

with st1:
    st.text_input("First name")

with st2:
    st.text_input("Second name")

p1,p2 = st.columns(2)

with p1:
    st.text_input("Last name")

with p2:
    st.text_input("Nick name")

dat1,dat2 = st.columns(2)

with dat1:
       birth = st.date_input("Date of Birth")

with dat2:
     gender = st.radio("select ",["Male","Female"],horizontal=True)

st.title("PATIENT CONTACT DETAILS")

mpa1,mpa2 = st.columns(2)

with mpa1:
     st.text_input("Mobile Phone")

with mpa2:
     st.text_input("Address")

hpe1,hpe2 = st.columns(2)

with hpe1:
     st.text_input("Home Phone")

with hpe2:
     st.text_input("Email")

ctpc1,ctpc2 = st.columns(2)

with ctpc1:
     st.text_input("City]]Town")

with ctpc2:
     st.text_input("Postcode")


