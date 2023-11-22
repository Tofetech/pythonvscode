#Create a menu for Registration and Database
#Design a blood donation database that can get donor input
#-Name of donor -Contact Number (use text)
#-Blood group A, B, AB, O(use radio or selectbox) -Disease/Infection (use radio or selectbox)

#-Submit donor details

#Next, save these in a csv file and show the database in a Database page in the menu

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

database = pd.read_csv('donor.csv')



menu = st.sidebar.selectbox("Menu",["Registration","Database"])

if menu == 'Registration':
    don1,don2 = st.columns(2)

    with don1:
        Name = st.text_input("What is your name")

    with don2:
        number = st.text_input("Contact number")

    rad1,rad2 = st.columns(2)
    with rad1:
       bloodgroup = st.radio("Blood group",["A","B","AB","O"])

    with rad2:
        disease_or_infection = st.radio("Do you have a disease or infection",["Disease","Infection","None "])

    save1,save2 = st.columns(2)
    with save1:
      if st.button("Submit donor details"):
        st.success(f"Ok Thank you")
        student_dict = {'Name':[Name],'Number':[number],'Bloodgroup':[bloodgroup],"Disease_or_infection":[disease_or_infection]}
        student_database = pd.DataFrame(student_dict)
        new_database = pd.concat([database,student_database],ignore_index=True)
        new_database.to_csv('donor.csv',index=False)



if menu == 'Database':
   
    st.dataframe(database,use_container_width=True)


 

    
