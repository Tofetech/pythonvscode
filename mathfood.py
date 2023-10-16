import streamlit as st
st.set_page_config(layout="wide") #makes your page full width 


score = 0

st.title("Welcome to Math food with Ms. Moji")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-VAh9tCknxopzTSttxwoaOvr2vjrAHdcvfubdvX43kw&s",500,500)




Food1 = st.number_input("2+2=?",value=0)
   
if (Food1 == 4):
   st.success("Good job you did it we will add 4 points to your score")

elif (Food1 > 4):
   st.error("try again next time")

elif (Food1 < 4):
   st.error("try again next time")
