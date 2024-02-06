#-create a dictionary of 5 cars and their country
#-then convert this dictionary into a dataframe
#no csv file is needed

import streamlit as st
import pandas as pd

#a dictioary is used to store a key and a data

car = {'honda':['Japan','England'],'bmw':['Germany','Nigeria'],'lambo':['UAE','Canada'],'ferari':['England','USE'],'Lexus':["China",'Turkey']}

st.write(car)

dataframe = pd.DataFrame(car)

st.dataframe(dataframe,use_container_width=True)

