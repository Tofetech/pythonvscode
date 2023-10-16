import streamlit as st
st.set_page_config(layout="wide") #makes your page full width 


total = 0

st.title("Welcome to Tofes Barbershop")
st.image("https://cdn.pixabay.com/photo/2014/04/02/10/21/moustache-303571_1280.png")





st.title("Hair styles")
styles1,styles2,styles3,styles4 = st.columns(4)


with styles1:
    if st.checkbox("This fine boy cut : $50"):
     st.write("Ok sir")
     total += 39
    if st.checkbox("This big daddy hairstyle: $30"):
     st.write("Ok sir")
     total += 30


with styles2:
    if st.checkbox("Low cut: $20"):
     st.write("Ok sir")
     total += 20
    if st.checkbox("Travis Scott: $40"):
     st.write("Ok sir")
     total += 40

with styles3:
    if st.checkbox(" Dreads: $35"):
     st.write("Ok sir")
     total += 35
    if st.checkbox("High fade: $42"):
     st.write("Ok sir")
     total += 42


with styles4:
    if st.checkbox("Curls: $20"):
     st.write("Ok sir")
     total += 20
    if st.checkbox("Coloured hair: $20"):
     st.write("Ok sir")
     total += 20
    
 

