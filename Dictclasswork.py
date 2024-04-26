#-create a dictionary of 5 cars and their country
#-then convert this dictionary into a dataframe
#no csv file is needed

import streamlit as st
import pandas as pd

#a dictioary is used to store a key and a data

car = {'honda':['Japan','England'],'bmw':['Germany','Nigeria'],'lambo':['UAE','Canada'],'ferari':['England','USE'],'Lexus':["China",'Turkey']}

st.write(car)

dataframe = pd.DataFrame(car)

st.table(dataframe)

#create a dictionary of messi and Ronaldo with the following attributes:
#the country they play for
#the clubs they play for
#how many games played
#how many goals scored
#how many assist made

#then convert to a table

football = {'Name':['Ronaldo'],'Country': ['portugal'],'clubs': ["21"],'Games': ['673'],'Goals': ['1100'],'Assist': ['800'], 'Name': ['Messi'],'Country': ['Argentina'], 'clubs': ["61"],'Games': ['519'], 'Goal': ["1000"], 'Assist': ['600']}

st.write(football)

dataframe = pd.DataFrame(football)

st.table(dataframe)