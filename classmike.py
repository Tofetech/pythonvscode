# "OR" OPERATOR
# x = 0
# y = 1
# print(x or y) 

# 0 is FALSE while any other Non-zero value is TRUE.

# x = 1
# y = 3
# # print(x or y)
# print(y or x)

import streamlit as st




age = st.number_input("What is you age",0)


if st.button("Can i vote"):

  if age <18:
    st.write("Sorry you to young to vote")

  else:
    st.write("You are old enough to vote")