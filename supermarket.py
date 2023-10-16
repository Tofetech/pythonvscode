# A supermarket sells fruits. Apples cost 20 dollars while oranges cost 15 dollars.
# Anytime you buy a dozen of orange you get 10 dollars deducted from your fee, anytime you also buy a dozen of apples you get 8 dollars deducted from your fee.A supermarket sells fruits. 
# Apples cost 20 dollars while oranges cost 15 dollars. Anytime you buy a dozen of orange you get 10 dollars deducted from your fee,  
# anytime you also buy a dozen of apples you get 8 dollars deducted from your fee.

import streamlit as st

st.title("Super store")
orangescost = 0
applescost = 0
apples = 20
oranges = 15

#apples
buyapples = st.number_input ("How many apple did you want to buy:",0,100)

if (buyapples > 11): 
   st.write("Ok you shall get an 8 dollar discount for over a dozen apples")
   applescost = (buyapples * apples) - 8
   st.write("Your total amount for",buyapples,"apples with discounts is",applescost)



#oranges
buyoranges = st.number_input("How many oranges did you want to buy: ",0,100)

if (buyoranges > 11): 
   st.write("Ok you shall get an 10 dollar discount a dozen oranges")
   orangescost = (buyoranges * oranges) - 10
   st.write("Your total amount for",buyoranges,"orange is",orangescost)

if st.button("Show the bill"):
  st.write("Your total is",applescost + orangescost,"dollars")





