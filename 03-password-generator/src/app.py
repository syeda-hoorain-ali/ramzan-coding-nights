import time
import clipboard
import streamlit as st
from style import styles
from utils import generate_password

st.set_page_config(
    page_icon="assets/logo.png",
    layout="centered",
    page_title="Password Generator - Syeda Hoorain Ali"
)


st.markdown(styles, unsafe_allow_html=True)
st.header("🔑 Password Generator")


container = st.container(key="container")

with container:
    length = st.slider('Select password length:', min_value=8, max_value=32, value=12)
    uppercase = st.checkbox('Uppercase letters: ')
    lowercase = st.checkbox('Lowercase letters: ')
    digits = st.checkbox('Digits: ')
    specialChars = st.checkbox('Special Charactors: ')

    if st.button('Generate Password', type="primary"):

        if not (uppercase or lowercase or digits or specialChars):
            st.toast('Please select at least one character type.')
            time.sleep(3)
            st.rerun()

        password = generate_password(length, uppercase, lowercase, digits, specialChars)
        st.success(f"Generated Password:  {password}")
        clipboard.copy(password)
        st.toast('Password copied to clipboard')


footer = st.container(key="footer")
footer.write("Made with 💖 by Syeda Hoorain Ali")
