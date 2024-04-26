import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

database = pd.read_csv('scores.csv')




menu= st.sidebar.selectbox('menu',['Submit scores','Database'])

if menu == 'Database':
   st.table(database)






if menu  == 'Submit scores':
  
  name = st.text_input("Enter name")

  sub1,sub2 = st.columns(2)

  
  with sub1:
   Math = st.number_input("Enter the student`s score for math",0,100)
   English = st.number_input("Enter the students score for english",0,100)

  with sub2:
   Art = st.number_input("Enter the student`s score for art",0,100)
   History = st.number_input("Enter the student`s score for history",0,100)

  total = Art+History+Math+English

  average = total/4


  if average >=90:
   grade = "A+"
  elif average >=80 and average <=89:
   grade = "A"
  elif average >=65 and average <=88:
   grade = "B"
  elif average >=55 and average <=87:
   grade = "C"
  elif average >=35 and average <=86:
   grade = "D"
  elif average >=0 and average <=85:
   grade = "F"

  su1,su2 = st.columns(2)
  with su1:
   if st.button("Submit Student score"):
    st.success(f"{name} your total score is {total}. The average is {average}. And the grade is {grade}")
    student_dict = {'Name':[name],'Art':[Art],'History':[History],
    'Math':[Math],"English":[English], 'Total':[total],'Average':[average],'Grade':[grade]}
    student_database = pd.DataFrame(student_dict)
    new_database = pd.concat([database,student_database],ignore_index=True)
    new_database.to_csv('scores.csv',index=False)

 



 

 






