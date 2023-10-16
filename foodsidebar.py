import streamlit as st
st.set_page_config(layout='wide')

bill = 0

mean = st.sidebar.subheader("food ordred")

meal1,meal2,meal3,meal4 = st.columns(4)

with meal1:
    st.image("https://cdn.pixabay.com/photo/2017/03/31/10/56/waffles-2190961_1280.jpg")
    if st.checkbox("Waffles : $20"):
        st.sidebar.image("https://cdn.pixabay.com/photo/2017/03/31/10/56/waffles-2190961_1280.jpg",width= 200)
        bill +=20

    
with meal2:
    st.image("https://cdn.pixabay.com/photo/2014/08/14/14/21/shish-kebab-417994_1280.jpg")
    if st.checkbox("Shish kebab : $25"):
        st.sidebar.image("https://cdn.pixabay.com/photo/2014/08/14/14/21/shish-kebab-417994_1280.jpg",width= 200)
        bill += 25


with meal3:
    st.image("https://cdn.pixabay.com/photo/2017/01/30/13/49/pancakes-2020863_1280.jpg")
    if st.checkbox("Pancakes : $15"):
        st.sidebar.image("https://cdn.pixabay.com/photo/2017/01/30/13/49/pancakes-2020863_1280.jpg",width= 200)
        bill += 15


with meal4:
    st.image("https://cdn.pixabay.com/photo/2018/04/13/17/14/vegetable-skewer-3317060_1280.jpg")
    if st.checkbox("Vegetable skewer : 15"):
       st.sidebar.image("https://cdn.pixabay.com/photo/2018/04/13/17/14/vegetable-skewer-3317060_1280.jpg", width= 200)
       bill += 15



if st.button("Check my bill"):
    st.sidebar.success(f"Total bill is ${bill}")