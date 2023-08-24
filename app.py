import streamlit as st
from PIL import Image 

st.write("Mi primera aplicación")

image = Image.open('TVU VS. CLUBMERC.jpg')

st.image(image, caption = 'Hola Soy Lasso')

texto = st.text_input('Escribe algo','Este es mi texto')
st.write('El texto escrito es', texto)
