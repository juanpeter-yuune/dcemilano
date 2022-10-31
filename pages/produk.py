from email.mime import image
from email.quoprimime import body_check
from turtle import width
from PIL import Image
import requests
import streamlit as st

#Assets
img_download = Image.open("images/download.png")

st.set_page_config(page_title="Contact Us", page_icon=":freis:", layout="wide")
#What D'Cemilano do
def middle():
    st.write("...")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Menu")
        st.write("##")
        st.write(
            """
            D'Ceminalo menyediakan beragam menu:
            - Burger
            - Salad Buah
            """
        )
        
        st.write("[Instagram>](https://instagram.com/d.cemilano)")
    with right_column:
        st.header("Menu")
        st.write("##")
        st.write(
            """
            D'Ceminalo menyediakan beragam menu:
            - Burger
            - Salad Buah
            """
        )
    st.write("...")
    st.header("Drinks")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_download)
    with text_column:
        st.subheader("Minuman baru")
        st.write("""
                 Harga terjangkau dong
                 """
        )
        
middle()