#5 things kids can do on python with an example each

import streamlit as st

#1 Display texts on python

st.title("Things kids can do in python")

st.title("Submit your score")

#2 Ask user text question

st.text_input("What is your name")

#3 Ask user number questions

Math = st.number_input("What is your math score",0)

english = st.number_input("What is your english score",0)

#4 Add variables together

total = Math + english

#5 Create a button 

if st.button("Total score"):
    st.success(f"Your total score is {total}")

    7 **2




 