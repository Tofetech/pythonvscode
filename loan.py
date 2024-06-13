import streamlit as st
import pandas as pd #for helping makeking databases

database = pd.read_csv('loan.csv') 

menu = st.sidebar.selectbox("Menu",["Check loan eligibility","Loan database"])

if menu == 'Check loan eligibility':
  st.title("loan")
  Name = st.text_input("What is you name")
  annual_income= st.number_input("what is your annual income",0)
  credit_score = st.number_input("what is your credit score",0)

 

  if st.button("Submit"):
    if (annual_income < 30000 and credit_score < 600):
     no = 'no'
     st.write("You cant not get a loan")
     
    elif ( annual_income > 29999 and annual_income <= 50000 and credit_score >599 and credit_score <700):
     smallloan = 'smallloan'
     st.write("You can get a small loan")

    elif (annual_income > 49999 and annual_income <= 100000 and credit_score > 699 and credit_score <801):
     medium = 'medium '
     st.write("You can get a medium loan")

    elif (annual_income > 999999 and credit_score > 799):
     large = 'large '
     st.write("You can get a large loan")


    loan_database = pd.DataFrame({'Name':[Name],'annual_income':[annual_income],'credit_score':[credit_score],'no':[no],'smallloan':[smallloan],'medium':[medium],'large':[large]}) 
    new_database = pd.concat([database,loan_database],ignore_index=True) 
    new_database.to_csv("loan.csv",index=False) 

if menu == 'Loan database':
   st.table(database) 
