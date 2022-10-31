from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="Contact Us", page_icon=":calling:", layout="wide")

#Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>",unsafe_allow_html=True)
local_css("style/style.css")

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
