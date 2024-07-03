import streamlit as st 

import pandas as pd 

 

# Hardcoded login credentials 

HARDCODED_PASSWORD = '12345'

 

movies_df = pd.read_csv('netflix.csv') 

 



st.write('Browse Movies') 

         

genre = st.sidebar.selectbox('Select Genre', ['All'] + list(movies_df['Genre'].unique())) 
filtered_df = movies_df if genre == 'All' else movies_df[movies_df['Genre'] == genre] 

         

for index, row in filtered_df.iterrows(): 

         if st.button(row['Title']): 

                st.image(row['Image'], width=200) 

                st.subheader(row['Title']) 

                st.write(f"**Genre:**{row['Genre']}") 

                st.write(row['Description']) 

                st.video(row['YouTube'])  



 


 










































# import streamlit as st
# import pandas as pd

# movies_df = pd.read_csv("netflix.csv")

# menu = st.sidebar.selectbox("Menu",['Login','Register'])
# movi1,movi2,movi3,movi4 = st.columns(4)

# st.sidebar.header("Login")

#if menu == 'Login':
    #correctpass = '12345'

    #password = st.text_input("Enter the admin password",type='password')

    #if st.button("Netflix"):
     #if password == correctpass:
# st.title("Movies.com")
# genre = st.sidebar.selectbox("Select Genre",['all'] + list (movies_df["Genre"].unique()))
# filtered_df = movies_df if genre == "all" else movies_df[movies_df["Genre"] == genre]  

# for _, row in filtered_df.iterrows():
#            st.image(row['Image'], width=200)
#            st.subheader(row['Title'])
#            st.write(f"**Genre:** {row['Genre']}")
#            st.write(row['Description'])
#            st.video(['YouTube'])
        

      #   with movi1:
      #     st.image("https://m.media-amazon.com/images/M/MV5BOTVkYTBlZDEtZmUxNS00ZjgzLWFjOGItNDdlMjdkYzg1ZmQ4XkEyXkFqcGdeQXVyMTU3NDg0OTgx._V1_.jpg")
      #     st.image('https://images.sr.roku.com/idType/roku/context/global/id/e7f88e252dcb596eae405f16ca00c097/images/gracenote/assets/p23050571_b_v8_ac.jpg/magic/396x0/filters:quality(70)')
      #   with movi2:
      #     st.image("https://upload.wikimedia.org/wikipedia/en/d/de/WishMoviePoster.jpg")
      #     st.image('https://m.media-amazon.com/images/M/MV5BZjFkODAxZjEtMTYzMy00NzNmLWJhNjItOWFmNmY1NThjYzgwXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg')
      #   with movi3:
      #      st.image("https://m.media-amazon.com/images/M/MV5BNDg0N2NiZTAtZWVjNy00YmJlLWI0NDktMjFkMmRiZGIyNzRmXkEyXkFqcGdeQXVyMTA1OTcyNDQ4._V1_.jpg")
      #      st.image("https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p18709634_p_v8_aa.jpg")
      #   with movi4:
      #      st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8Dn2ssofQm4NE6r8ICx2ViroD586blO9pAg&s")
      #      st.image("https://m.media-amazon.com/images/M/MV5BMDMzYzM3MGMtZWFlZC00ODI5LTg5YjgtODI2NzI3ZTZmMGQ4XkEyXkFqcGdeQXVyMTA1NjE5MTAz._V1_QL75_UX190_CR0,2,190,281_.jpg")
           
     #else:
        #st.write("Wrong password")
        
      #   


 