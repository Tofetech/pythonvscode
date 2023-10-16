#A lecturer in the university wants you as programmer to create a software to mark students scores
#Ask the students for their scores in english, maths and science
#If the total score is above 90, give the student A+
#If the total score is between 80-89, give the student A
#If the total score is between 70-79, give the student B
#If the total score is between 60-69, give the student C
#If the total score is between 50-59, give the student D
#If the total score is below 50, give the student F

import streamlit as st

st.title("Math score")

math = st.number_input("what is your score in math :",0,100,value=50,step= 1,format="%d")

if (math > 90):
  st.write("A+")

elif (math < 90)  and  (math > 80):
  st.write("A") 

elif (math < 80)  and  (math > 70):
  st.write("b") 

  
elif (math < 70)  and  (math > 60):
  st.write("c") 

  
elif (math < 60)  and  (math > 50):
  st.write("d") 

  
elif (math < 50):
  st.write("f") 



