#A school charges 50,000 for elementary students. Ask how many kids the parent has, 
#if a parent has 2 kids or more, the school will deduct 10,000 as a discount, 
#and also ask if a parent's child is in year 1, the school will deduct 5,000 as a discount

#Create a program for the school to the calculate school fees for new parents 
#hint: there should be a button to check fees once
#The school feee is -----
#you recieved a discountof ... for having more than 1 kids
#you recieved a discount of ... for having a chind in year 1

import streamlit as st

st.title("school")

fee = 50000

st.write("Welcome to Tofetech School")

kids = st.number_input("Deer perent before we stat with the prosses of enrolling you kids please state if you have more than 2 kids if :",value=0,step= 1,format="%d")
year = st.number_input("What year is your child",value=0,step= 1,format="%d")

if st.button("show fees"):
   st.write("you total school fise is ",fee,"dollars:")

   if (kids > 1):
      fee -=10000
      st.write("you have gotten a discount  of 10000  dollars for having more than 1 kid")
      st.write("you total school fise is ",fee,"dollars:")



   if (year ==1):
      fee -=5000
      st.write ("you have gotten a discount of 5000 dollars for your children bieng in year 1")

      st.write("The total amount you spent is",fee)

      st.write("Thank you for enrolling in this school we will keep in touch with you")



