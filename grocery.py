
  
import streamlit as st
st.set_page_config(layout="wide") #makes your page full width 


total = 0

st.title("Lulu")
st.image("https://cdn.pixabay.com/photo/2019/07/03/20/04/store-4315394_1280.jpg")


st.subheader("Welcome to lulu")


st.title("Rice")
rice1,rice2,rice3 = st.columns(3)


with rice1:
    if st.checkbox("Ofada rice: $20"):
     st.write("You have added Ofada rice")
     total += 20
    if st.checkbox("Jollof rice: $20"):
     st.write("You have added  Jollof Rice")
     total += 20


with rice2:
    if st.checkbox("Rice and beans: $20"):
     st.write("You have added Rice and beans")
     total += 20
    if st.checkbox("Fried rice: $20"):
     st.write("You have added Fried rice")
     total += 20

with rice3:
    if st.checkbox("Basmati Rice: $20"):
     st.write("You have added Basmati Rice")
     total += 20
    if st.checkbox("Biryani: $20"):
     st.write("You have added Biryani")
     total += 20



    
 




st.title("Fruits")
fruits1,fruits2,fruit3 = st.columns(3)
with fruits1:
    if st.checkbox("Apple: $9"):
     st.write("You have added Apple")
     total += 9
    if st.checkbox("Banana: $9"):
     st.write("You have added Banana")
     total += 9

with fruits2:
    if st.checkbox("Dragonfruit: $9"):
     st.write("You have added Dragonfruit")
     total += 9
    if st.checkbox("Raspberries: $9"):
     st.write("You have added Raspberries")
     total += 9



with fruit3:
    if st.checkbox("Broccol: $10"):
     st.write("You have added Broccol")
     total += 10
    if st.checkbox("Pineapple: $10"):
     st.write("You have added Pineapple")
     total += 10







st.title("Drinks")
drink1,drink2,drink3 = st.columns(3)


with drink1: 
    if st.checkbox("Fanta: $10"):
     st.write("You have added Fanta")
     total += 10
    if st.checkbox("cola: $10"):
     st.write("You have added cola")
     total += 10

with drink2:
    if st.checkbox("pepsi: $10"):
     st.write("You have added pepsi")
     total += 10
    if st.checkbox("7 Up: $10"):
     st.write("You have added 7 Up")
     total += 10

with drink3:
    if st.checkbox("sprit: $10"):
     st.write("You have added sprit")
     total += 10
    if st.checkbox("Mirinda: $10"):
     st.write("You have added Mirinda cb")
     total += 10



st.title("Chips")
chips1,chips2,chips3 = st.columns(3)
with chips1:
    if st.checkbox("FRITOS: $70"):
     st.write("You have added FRITOS")
     total += 70
    if st.checkbox("Beet chips: $12"):
     st.write("You have added Beet chips")
     total += 12



with chips2:
    if st.checkbox("lay's: $12"):
     st.write("You have added lay's")
     total += 12
    if st.checkbox("Doritos: $12"):
     st.write("You have added Doritos")
     total += 12

with chips3:
    if st.checkbox("Pringles: $12"):
     st.write("You have added Pringles")
     total += 12
    if st.checkbox("Munchos: $12"):
     st.write("You have added Munchos")
     total += 12


st.title("Icecream")
cream1,cream2,cream3 = st.columns(3)
with cream1:
    if st.checkbox("Sundae: $5"):
     st.write("You have added Sundae")
     total += 5
    if st.checkbox("Mint chocolate chip ice cream: $5"):
     st.write("You have added Mint chocolate chip ice cream")
     total += 5


with cream2:
    if st.checkbox("strawberry ice cream: $5"):
     st.write("You have added strawberry ice cream")
     total += 5
    if st.checkbox("chocolate chip cookie dough ice cream: $5"):
     st.write("You have added chocolate chip cookie dough ice cream")
     total += 5

with cream3:
    if st.checkbox("Vanilla ice cream: $5"):
     st.write("You have added Vanilla ice cream")
     total += 5
    if st.checkbox("Chocolate ice cream: $5"):
     st.write("You have added Chocolate ice cream")
     total += 5


st.title("candy")
candy1,candy2,candy3 = st.columns(3)
with candy1:
    if st.checkbox("Gummies: $10"):
     st.write("You have added Gummies")
     total += 10
    if st.checkbox("Snickers: $9"):
     st.write("You have added Snickers")
     total += 9


with candy2:
    if st.checkbox("Lollipop: $10"):
     st.write("You have added b Lollipop")
     total += 10
    if st.checkbox("Cotton candy: $10"):
     st.write("You have added Cotton candy")
     total += 10

with candy3:
    if st.checkbox("Skittles.: $9"):
     st.write("You have added Skittles.")
     total += 9
    if st.checkbox("Sour Patch Kids.: $10"):
     st.write("You have added Pizza with Sour Patch Kids.")
     total += 10


if st.button("Show the bill"):
  st.write("Your total is",total,"dollars")