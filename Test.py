#1.What is streamlit used for?
#2.show 8 ways to display text on streamlit
#3.show how to ask for a text on streamlit
#4.show how to ask for a number on streamlit
#5.create a button on the left column but show the output on the right column
#6.create a radio button with a horizontal orientation
#7.import an image with a 150*150 size
#8. read and dispay a CSV file in python
#9.create a toggle option to display any database/dataframe
#10.create a dictionary of 5 different cars with 5 attributes (without using a CSV file)
#and convert it to a dataframe/table

import streamlit as st
import pandas as pd

database = pd.read_csv("test.csv")

#1 Streamlit is used to make apps for types of things like hospital app

#2
st.title("Hi")
st.text_input("Sup")
st.number_input("11")
st.write("I am smart")
st.success(f"WOW NICE")
st.error("WRONG")
st.subheader("UMMM")
if st.button("Hi"):
    st.write("Nice to meet you")

#3
WHY = st.text_input("LIE")

#4
st.number_input("22")

#5



#6
st.radio("Sup",["Yes","No"],horizontal=True)

#7
st.image("https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg")

#8

if st.button("Nice"):
    st.write("Nice")
    mine = pd.DataFrame({'wHY':[WHY]})
    new = pd.concat([database,mine],ignore_index=True)
    new.to_csv('test.csv',index=False)

#9


#10
yes1,yes2,yes3 = st.columns(3)

with yes1: 
    hi = {"Bannan":'Blue,'}
    st.write(hi)



car_dict {
    'Car Model' : ['Toyota', 'Mazda', 'Roland', 'BMW', 'Lamboughini']
    'Year' : ['2022',"" ]
}