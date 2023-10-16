import streamlit as st
from PIL import Image

menu = st.sidebar.selectbox('menu',['Upload files','About us'])

if menu == 'Upload Files':
 st.header('Upload Files here')

image_file = st.file_uploader('Upload image file',type=['png','jpg','jpeg'])

if image_file is not None:
 st.image(Image.open(image_file))

