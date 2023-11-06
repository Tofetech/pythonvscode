import streamlit as st

#simple classwork
#what is a list?
#mention 2 uses of a list
# give an example of a list and display it on streamlit
#give 3 ways of using a list in streamlit and tell us the function of each method you use

# A list is when you want to but more than 1 data in a varable
# When you want to display bestsubjects you use a list 
# when you want to talk about bestshow you use a list because a () wont let you but more than 1 data

bestshows = ["Spongbob","Tofetech","Mathquiz"]

st.write(bestshows)

bestcolor = st.selectbox("Pick you best color",["Blue","Red","Green"])

bestsubjects = st.radio("Bestsubjects",["Math","Science","English"])

menu = st.sidebar.selectbox("Bestshows",["Spongbob","Tofetech","Mathquiz"])