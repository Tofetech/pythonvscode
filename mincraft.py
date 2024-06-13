# Mia is excited to explore the Minecraft store and purchase some exciting items for her gameplay.
# She wants to download the game itself, choose a world to play in, buy some costumes, and maybe even get a farm! Additionally, she’s eyeing some gems to enhance her gameplay.
# Write a Python program to help Mia calculate the total cost of her Minecraft adventure.


# Mia’s journey through the Minecraft store involves several steps:


# First, she needs to download the game itself, which costs $200.
# Mia will then enter her username and password to access the store.
# Next, she can choose between two worlds: the Survival world for $20 or the Creative world for $100.
# Mia can also browse through three different costume options, each with its own price tag.
# Additionally, Mia has the option to add a farm to her gameplay for an additional $25.
# Finally, she can purchase gems: diamonds for $45, silver for $20, or gold for $30.
# After making her selections, Mia wants to see the total cost of her Minecraft adventure. Let’s create a Python program to help her out.


import streamlit as st

cost = 0


download = st.selectbox("Download Minecraft",["Choose",'No',"Yes $200"])

if download == "Yes $200":
    cost += 200
    st.write("Congratulations you got Minecraft")
    st.write("Now time for you to set up your Username and Password")
    username = st.text_input("What do you want your Username to be")
    password = st.number_input("What do you want you Password to be",0)
    world = st.selectbox("Choose your world",["Choose","creative_world : $100","survival_world : $20"])

    if world == "creative_world : $100":
     cost += 100
     st.write ("You have successfully purchased Creative_World")

    elif world == 'survival_world : $20':
     cost += 20
     st.write ("You have successfully purchased Survival_World")
    # Finally, she can purchase gems: diamonds for $45, silver for $20, or gold for $30.
    
    gems = st.selectbox ("Choose your gem",["Choose",'diamonds : $45','Silver : $20','Gold : $30'])
    if gems == 'diamonds : $45':
      cost += 45

    elif gems == 'Silver : $20':
      cost += 20

    elif gems == 'Gold : $30':
      cost += 30

    if st.button("Total"):
     st.write("Total",cost)
