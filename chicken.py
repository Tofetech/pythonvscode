#Classwork 1:
#A poultry farm sells a chicken for 10$. Create a program in Python to ask how many chickens people want to get and then tell them the total price

import streamlit as st

st.title("Selling chickens For 10 dollars")

chicken = 10

ask = st.number_input("How many chicken do you want to buy",value=0,step=1,format='%d')

total = chicken * ask

st.write("Your total price is",total,"Dollars")

