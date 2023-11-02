import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

database = pd.read_csv('testscore.csv')

st.dataframe(database,use_container_width=True)

name = st.text_input("Name")

sub1,sub2 = st.columns(2)

with sub1:
    math = st.number_input("Enter math score",0,100)
    science = st.number_input("Enter science score",0,100)

with sub2:
    art = st.number_input("Enter art score",0,100)
    english = st.number_input("Enter english score",0,100)

total = art+english+science+math

average = total/4


if average >90:
    grade = "A+"
elif average >80 and average<89:
    grade = "A"
elif average>60 and average<88:
    grade = "B"
elif average>55 and average<87:
    grade = "C"
elif average>40 and average<86:
    grade = "D"
elif average>25 and average<85:
    grade = "F"


su1,su2 = st.columns(2)

with su1:
    if st.button("Submit student score"):
        st.success(f"{name}.Got a total score of {total}and the average is {average} and grade is {grade}")
        student_database = pd.DataFrame({'Name':[name],'Math':[math],'Art':[art],
                                         'Science':[science],'English':[english],'Total':[total],'Average':[average],'Grade':[grade]})
        new_database = pd.concat([database,student_database],ignore_index=True)
        new_database.to_csv('testscore.csv',index=False)
    