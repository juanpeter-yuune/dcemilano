from email.mime import image
from email.quoprimime import body_check
from turtle import width
from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="D'Cemilano", page_icon=":hamburger:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>",unsafe_allow_html=True)
local_css("style/style.css")



#sidebar


#Header Section
def header():
    st.header("Welcome to D'Cemilano")
    st.title("D'Cemilano")
    st.write("Street food dengan pilihan cemilan yang beragam", Icon=":fries:")
    st.image("images/gambar4.jpg")
    if st.button('Instagram'):
        st.markdown("[Watch the dirnks?](https://instagram.com/d.cemilano")
    else:
        st.write('Goodbye')
    
header()
