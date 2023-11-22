# write a program for a use
# -ask for the name and -age - use a radio to ask for gender
# -use a selectbox to ask to choose best color - use a selectbox to ask best game
# -use a text to ask to enter best movie - use a text to ask their best friend
# create a submit button and show this in a success bar
# Jeida (F), your best game is: Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe


import streamlit as st

age1,age2,age3 = st.columns(3)

with age1:
    name = st.text_input("What is your name")

with age2:
    age = st.number_input("What is your age",0)

with age3:
    gender = st.radio("What is your gender",["Male","Female"])

sele1,sele2 = st.columns(2)

with sele1:
    color = st.selectbox("What is your best color",["Blue","Red","Purple","Yellow"])

with sele2:
    bestgame = st.selectbox("What is your best Game",["Minecraft","Roblox"])

text1,text2 = st.columns(2)

with text1:
    movie = st.text_input("What is your best movie")

with text2:
    bestfriend = st.text_input("Who is your best friend")

if st.button("Check"):
    st.success(f"{name} age is: {age} best game is: {bestgame} color: {color} movie: {movie} friend: {bestfriend}")
