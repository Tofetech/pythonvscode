import streamlit as st
import pandas as pd #for helping makeking databases

database = pd.read_csv('buycar.csv') #This is so it can read what you put in you csv file 

menu = st.sidebar.selectbox("Menu",["Buy cars","Car database"])

if menu == 'Buy cars':
  st.title("Cars for sale")
  Name = st.text_input("What is you name")
  salary = st.number_input("What is your yearly salary",0)

  if st.button("Submit"):
    if (salary < 30000):
     carused ='Used car'
     st.write("You can buy a used car")
     
    elif (salary > 29999 and salary <= 60000):
     econmycar = 'economy'
     st.write("You can buy a economy car")

    elif (salary > 59999 and salary <= 100000):
     midcar = 'mid_range car '
     st.write("You can buy a mid-range car")

    elif (salary > 999999 and salary <= 2000000):
     luxurycar = 'luxury car'
     st.write("You can buy a luxury car")

    elif (salary > 2000000):
     supercar = 'Super car'
     st.write("You can buy a Super car")




    buycar_database = pd.DataFrame({'name':[Name],'salary':[salary],
                                    'econmy':[econmycar],'mid_range car':[midcar],'luxury car':[luxurycar],'Super car':[supercar]}) #To make the dataframe know the labels like 1 is name 1 is age
    new_database = pd.concat([database,buycar_database],ignore_index=True) # to merge the new database with the old one
    new_database.to_csv("buycar.csv",index=False) #

if menu == 'Car database':
   st.table(database) #So when they open the menu car database they see the database 



     