
import streamlit as st

total = 0
 
st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Menu',['Furnitures','About Us'])

if menu == 'Furnitures':
    st.header(':Orange[Welcome to The Furnitures]')

    st.title("Beds")
    bed1,bed2,bed3 = st.columns(3)

    with bed1:
        st.image("https://cdn.pixabay.com/photo/2021/08/27/01/33/bedroom-6577523_1280.jpg")
        if st.checkbox("**Sweetnight Full Size Mattress :$24**"):
            st.success("Added to cart")
            total += 246

    with bed2:
        st.image("https://cdn.pixabay.com/photo/2020/11/24/11/36/bedroom-5772286_1280.jpg")
        if st.checkbox("**5 Inch Goose Down and Feather Bed : 190**"):
            st.write("Added to cart")
            total += 190

    with bed3:
        st.image("https://cdn.pixabay.com/photo/2020/10/18/09/16/bedroom-5664221_1280.jpg")
        if st.checkbox("**Full Size Metal Bed Frame 14 Inch Black Heavy Duty Mattress Foundation** : 113"):
            st.write("Added to cart")
            total += 113
    
    st.title("Desk")
    desk1,desk2,desk3 = st.columns(3)

    with desk1:
        st.image("https://cdn.pixabay.com/photo/2015/01/21/14/14/apple-606761_1280.jpg")
        if st.checkbox("**Stand up Desk with Splice Board, Electric Adjustable Height Desk, 48 x 24 Inches Sit Stand Home Office Desk** : 177"):
            st.write("Added to cart")
            total +=177
    
    with desk2:
        st.image("https://cdn.pixabay.com/photo/2016/11/29/06/18/home-office-1867761_1280.jpg")
        if st.checkbox(" **ODK 48 inch Computer Desk with Monitor Shelf and Storage Shelves, Writing Desk** : 188"):
            st.write("Added to cart")
            total += 188

    with desk3:
        st.image("https://cdn.pixabay.com/photo/2015/06/24/16/36/home-820389_1280.jpg")
        if st.checkbox("**Monomi Electric Standing Desk, 55 x 28 inches Height Adjustable Desk, Ergonomic Home Office Sit Stand Up Desk**  : 129"):
            st.write("Added to cart")
            total += 129


    st.title("Couch")
    cup1,cup2,cup3 = st.columns(3)

    with cup1:
        st.image("https://cdn.pixabay.com/photo/2017/08/02/01/01/living-room-2569325_1280.jpg")
        if st.checkbox("**Straight Arms, Soft Fabric Upholstery, Tool-Free Assembly, 73, Sofa grey : 351**"):
            st.write("Added to cart")
            total += 351

    with cup2:
        st.image("https://cdn.pixabay.com/photo/2017/08/06/15/44/house-2593570_1280.jpg")
        if st.checkbox("**Vonanda Fabric Sofa, Blue Couch Upholstered Sofa, 72 Inch Blue Sofa : 400**"):
            st.write("Added to cart")
            total += 400

    with cup3:
        st.image("https://cdn.pixabay.com/photo/2013/09/21/14/30/sofa-184551_1280.jpg")
        if st.checkbox("**Jarenie 79 Convertible Sectional Sofa, Modern L Shaped 3-Seater Couches with Reversible Chaise :389 **"):
            st.write("Added to cart")
            total +=389

if menu == 'About Us':
    st.header('This is about us')
    about1,about2 = st.columns(2)

    with about1:
        st.write("**Hello this is about us this shop was made in in 1935 all the was to 2023 me and my workes have been working to make to this store very very good and cheap so you dont have to pay to much i hope you like us thank you**")

    
    
    with about2:
        st.image("https://cdn.pixabay.com/photo/2016/10/04/14/40/about-us-1714489_1280.jpg")

        

           
 



    