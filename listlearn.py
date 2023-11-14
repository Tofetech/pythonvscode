import streamlit as st

#List
#A list is when you what to put more than 1 data in a variable
#Bestcolours

bestcolour = ["Yellow","Red","Green"]

st.write(bestcolour)

bestbooks = st.selectbox("Bestbook",['The dog','The cat'])

bestfruit = st.radio("Bestfruits",['Apples','Banana','Grapes'])