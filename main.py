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

#Assets
img_download = Image.open("images/download.png")

#Header Section
with st.container():
    st.subheader("Welcome to D'Cemilano")
    st.title("D'Cemilano")
    st.write("Tempat tepat untuk beragam cemilan enak")

#What D'Cemilano do
with st.container():
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

with st.container():
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
        st.markdown("[Watch the dirnks?](https://instagram.com/d.cemilano")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_download)
    with text_column:
        st.subheader("Minuman baru")
        st.write("""
                 Harga terjangkau dong
                 """
        )
        st.markdown("[Watch the dirnks?](https://instagram.com/d.cemilano")

#CONTACT
with st.container():
    st.write("...")
    st.header("Get In Touch With Us")
    st.write("##")
    
    contact_form= """
    <form action="https://formsubmit.co/the.tangkorok@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">     
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder ="Your Email" required>
        <textarea name="message" placeholder="Your Message Here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column= st.columns(2)
    with left_column:
         st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
     
