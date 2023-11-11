import streamlit as st
from PIL import Image

st.subheader('Конвертер цветного в серый')

uploaded_img = st.file_uploader("Добавить изображение")

with st.expander("Сделать снимок"):
    camera_image = st.camera_input("Camera")

if uploaded_img:
    up_img = Image.open(uploaded_img)
    gray_img = up_img.convert("L")
    st.image(gray_img)

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")

    st.image(gray_img)