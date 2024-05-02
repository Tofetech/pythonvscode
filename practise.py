#Create a program that accepts user input for their respective age. 

#0 - 12 falls in Children 
#13 - 19 falls in Teens
#20 - 40 falls in Youths
#41 - above falls in Adults

#Using streamlit print age category to user after entering their age.

import streamlit as st
age = st.number_input("What is your age",0)
if age >0 and age <13:
    st.write("You are a child")
elif age >12 and age <20:
    st.write("You are a teen")
elif age >19 and age <41:
    st.write("You are a Youths")
elif age >40:
    st.write("You are a adult")

if st.button('cheak age'):
 st.write("You are ",age)
    




