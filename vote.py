#Create a voting application with python using streamlit.

#Requirements:
#- Add an image
#- Minimum age is 18 years.
#- Age entered less than minimum should get “You are not eligible to vote” response.
#- Age entered greater than or equal to minimum should get “You are eligible to vote” response.

import streamlit as st
st.image('https://cdn.pixabay.com/photo/2016/11/07/00/49/vote-1804596_1280.jpg')
st.subheader("Voting app")
st.write("This is a voting app for 18 and above can only vote")

vote = st.number_input("How old are you ",0)

if st.button("Vote"):
    if vote > 17:
        st.write("You are eligible to vote")

    else: 
        st.write("You are to young to vote")
