#-title
#-image
#-categories
#Men's Fashion

#Women's Fashion

#Children's Fashion

#(each category must have different types of unique items and the prices like shirts(long sleeves,short, round nexk, polo etc), boxers, trousers, shoes, bags etc)

import streamlit as st
st.set_page_config(layout="wide")

price = 0

st.title("Welcome to Tofes fashion store")
st.image("https://cdn.pixabay.com/photo/2019/03/21/15/18/shop-4071232_1280.png")

st.subheader("The best clothing store around")

st.title("Mens section")

st.title("Mens polos")
polo1,polo2,polo3 = st.columns(3)

with polo1:
 if st.checkbox("Red polo: 34"):
  st.write("You have added Red polo to your cart")
  price += 34
 if st.checkbox("yellow polo: 27"):
  st.write("You have added Yellow polo to your cart")
  price += 27

with polo2:
 if st.checkbox("Green polo: 31"):
  st.write("Added to cart")
  price += 31
 if st.checkbox("Brown polo: 25"):
  st.write("Added to cart")
  price += 25

with polo3:
 if st.checkbox("White polo: 36"):
  st.write("Added to cart")
  price += 36
 if st.checkbox("Dark blue polo: 33"): 
  st.write("Added to cart")
  price += 33

st.title("Boxers")
boxer1,boxer2,boxer3 = st.columns(3)

with boxer1:
 if st.checkbox("Dark blue and grey boxer: 16"):
  st.write("Added to cart")
  price += 16
 if st.checkbox("Brown boxer: 18"):
  st.write("Added to cart")
  price += 18

with boxer2:
 if st.checkbox("Red boxer: 15"):
  st.write("Added to cart")
  price += 15
 if st.checkbox("Dark blue boxer: 19"):
  st.write("Added to cart")
  price += 19

with boxer3:
 if st.checkbox("Red and blue boxer: 20"):
  st.write("Added to cart")
  price += 20
 if st.checkbox("Grey and black boxer: 14"):
  st.write("Added to cart")
  price += 14

st.title("Trousers")
trous1,trous2,trous3 = st.columns(3)

with trous1:
 if st.checkbox("Autumn black jogger men cargo pants: 52"):
  st.write("Added to cart")
  price += 52
 if st.checkbox("Mens Multi-pocket Harem Pant: 40"):
  st.write("Added to cart")
  price += 40

with trous2:
 if st.checkbox("Long Pants For Men MenS Cargo Trousers Work Wear Combat Safety: 39"):
  st.write("Added to cart")
  price += 39
 if st.checkbox(" Men's Trousers Casual Pants: 45"):
  st.write("Added to cart")
  price += 45

with trous3:
 if st.checkbox("Blue men Striped Trousers: 44"):
  st.write("Added to cart")
  price += 44
 if st.checkbox("Green and white Men Striped Trousers: 49"):
  st.write("Added to cart")
  price += 49

st.title("Shoes")
shoes1,shoes2,shoes3 = st.columns(3)

with shoes1:
 if st.checkbox(" Light blue Jordan Max Aura 4: 290"):
  st.write("Added to cart")
  price += 290
 if st.checkbox(" Red Air Jordan 3 Retro: 270"):
  st.write("Added to cart")
  price += 270

with shoes2:
 if st.checkbox(" Orange Men's Rincon 3 Lightweight Running Shoe: 345"):
  st.write("Added to cart")
  price += 345
 if st.checkbox(" Black Chuck Taylor All Star Core High-Top Unisex Shoe: 300"):
  st.write("Added to cart")
  price += 300

with shoes3:
 if st.checkbox(" White Men's Bondi 8 Shoe: 399"):
  st.write("Added to cart")
  price += 96
 if st.checkbox("White Men's Court Vision Low Shoe: 415"):
  st.write("Added to cart")
  price += 103

st.title("Womens section")

st.tittle("Womens shirts")
shirt1,shirt2,shirt3 = st.columns(3)

with shirt1:
 if st.checkbox("Red and white CEASIKERY Women's 3/4 Sleeve V Neck Tops Casual Tunic Blouse Loose Shirt: 27"):
  st.write("Added to cart")
  price += 27
 if st.checkbox(" White and black Anyally Womens Summer Puff Short Sleeve Tops Dressy Casual V-Neck T-Shirts Cute Blouse for Work: 25"):
  st.write("Added to cart")
  price += 25

with shirt2:
 if st.checkbox("Red flowers Ficerd Women's Puff Short Sleeve Tunic Tops Pleated Crew Neck Blouses Dressy Casual Loose Spring and Summer T-Shirts: 23 "):
  st.write("Added to cart")
  price += 25
 if st.checkbox("Blackberry Heather Carhartt Women's Heavyweight Short-Sleeve Pocket T-Shirt: 19"):
  st.write("Added to cart")
  price += 19

with shirt3:
 if st.checkbox("Yellow and grey Minthunter Women's Half Sleeve T Shirts Casual Color Block Round Neck Spring Tops: 21"):
  st.write("Added to cart")
  price += 21
 if st.checkbox("Grey Minthunter Women's Half Sleeve T Shirts Casual Color Block Round Neck Spring Tops: 18 "):
  st.write("Added to cart")
  price += 21


st.title("Pants")
pants1,pants2,pants3 = st.columns("3")

with pants1:
 if st.checkbox("Green ZMPSIISA Women High Waisted Cargo Pants Wide Leg Casual Pants 6 Pockets Combat Military Trousers: 31"):
  st.write("Added to cart")
  price += 31
 if st.checkbox(" Black RBX Active Women's Relaxed Fit Lightweight Quick Drying Stretch Woven Pants with Pockets: 33"):
  st.write("Added to cart")
  price += 33

with pants2:
 if st.checkbox("White Lee Women's Relaxed Fit All Day Straight Leg Pant: 36"):
  st.write("Added to cart")
  price += 36
 if st.checkbox("Red NIMIN Womens Casual Loose Pants Comfy Cropped Work Pants with Pockets Elastic High Waist Paper Bag Pants: 35"):
  st.write('Added to cart')
  price += 35

with pants3:
 if st.checkbox("Indigo Daze Levi's Women's 720 High Rise Super Skinny Jeans: 18"):
  st.write("Added to cart")
  price += 18
 if st.checkbox(" Black Bamans Work Pants for Women Yoga Dress Pants Straight Leg Stretch Work Pant with Pockets: 36"):
  st.write("Added to cart")
  price += 36

st.title("Shoes")
shoe1,shoe2,shoe3 = st.columns(3)

with shoe1:
 if st.checkbox("White adidas Women's Puremotion Adapt Running Shoe: 55"):
  st.write("Added to cart")
  price += 55
 if st.checkbox("brown and black The Drop Women's Paulina Pointed Toe Two-Tone Mule: 49"):
  st.write("Added to cart")
  price += 49



with shoe2:
 if st.checkbox("Black Rocket Dog Women's Cheery Sneaker: 24"):
  st.write("Added to cart")
  price += 24
 if st.checkbox("Brown BABUDOG Women's PU Leather Flats Shoes Black Dress Flats Crimping Faux Suede Pointed-Toe Work Shoes: 23"):
  st.write("Added to cart")
  price += 23


with shoe3:
 if st.checkbox("Black and white Canvas Shoes for Women White Canvas Sneakers Womens Casual Shoes Low Top Black Sneakers Comfortable Tennis Shoes: 22"):
  st.write("Added to cart")
  price += 22
 if st.checkbox("Grey blue SHULOOK Hiking Shoes Women Womens Hiking Shoes Non Slip Lightweight Comfortable Breathable Walking Trekking Oudoor Sneaker: 54"):
  st.write("Added to cart")
  price += 54

st.title("Children")
child1,child2,child3 = st.columns(3)

with child1:
 if st.checkbox("mikey mouse shirt: 31"):
  price += 31
  st.write("Added to cart")
 if st.checkbox("mini mouse: 23"):
  price += 23
  st.write("Added to cart")

with child2:
 if st.checkbox("STAR WARS The Mandalorian Darth Vader Chewbacca Stormtrooper 3 Pack T-Shirts Infant to Big Kid: 28"):
  price += 28
  st.write("Added to cart")

 if st.checkbox("The Children's Place Girls' Short Sleeve Graphic High Low Top 5 Pack: 29"):
  price += 29
  st.write("Added to cart")

with child3:
 if st.checkbox("Amazon Essentials Boys' Long-Sleeve T-Shirts (Previously Spotted Zebra), Multipacks : 24"):
  price += 24
  st.write("Added to cart")
 if st.checkbox("Simple Joys by Carter's Babies, Toddlers, and Girls' Short-Sleeve Shirts, Pack of 3 : 23"):
  price += 23
  st.write("Added to cart")


st.title("Pants")
short1,short2,short3 = st.columns(3)

with short1:
 if st.checkbox("Resinta 4 Pack Boys Athletic Sweatpants Fleece Jogger Sweatpants with Pockets Drawstring Active Sweatpants : 31"):
  price += 31
  st.write("Added to cart")
 if st.checkbox("Real Essentials 3 Pack: Boys' Tricot Open Bottom Fleece-Lined Sweatpants with Pockets: 35"):
  price += 35
  st.write("Added to cart")

with short2:
 if st.checkbox("The Children's Place Boys Chino Pants : 75"):
  price += 75
  st.write("Added to cart")
 if st.checkbox("Simple Joys by Carter's Baby Girls' Pant, Pack of 4 : 16"):
  price += 16
  st.write("Added to cart")

with short3:
 if st.checkbox("Fruitsunchen Toddler Boys Jogger Active Athletic Pants Dinosaur Sweatpants (1-Pack 2-Pack) : 41"):
  price += 41
  st.write("Added to cart")
 #if st.checkbox("Amazon Essentials Babies, Toddlers, and Girls' Leggings (Previously Spotted Zebra), Multipacks: 24")


 









