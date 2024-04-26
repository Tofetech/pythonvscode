#TEST 1
#write a python program for house buyers
#Ask them for their name
#ask them for their yearly salary
#If the earn between 100000-500000 they can buy a bungalow
#If the earn between >500000-1000000 they can buy a duplex
#If the earn between >1000000-5000000 they can buy a manshion

import streamlit as st

st.title("Houses For Sale")

Name = st.text_input("What is you name")
salary = st.number_input("What is your yearly salary",0)

if st.button("Which House"):
    if (salary > 100000 and salary <= 500000):
        st.write("You can buy a bungalow")

    elif (salary > 500000 and salary <= 1000000):
        st.write("You can buy a duplex")

    elif (salary > 1000000 and salary <= 5000000):
        st.write("You can buy a manshion")

    