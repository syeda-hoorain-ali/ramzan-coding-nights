import time
import streamlit as st
from utils import fetch_money_quote, fetch_side_hustle, generate_bitcoin


st.set_page_config(
    page_title="Money Making Machine", 
    page_icon="💰",
    layout="centered",
)


st.title("Money Making Machine")
st.text("Welcome to the Money Making Machine!")

st.markdown("---")


st.subheader("Instant Cash Generator")
if st.button("Mine bitcoins", type="primary", key="bitcoin"):
   
    with st.spinner("Mining bitcoins...", show_time=True):
        time.sleep(2)
   
    amount = generate_bitcoin()
    st.success(f"You've mined {amount} bitcoins!")
    st.balloons()


st.markdown("---")


st.subheader("Side Hustle Ideas")
if st.button("Generate hustle", type="primary", key="hustle"):
    idea = fetch_side_hustle()

    if not idea:
        st.error("Failed to generate a side hustle idea.")
    else:
        st.success(idea)


st.markdown("---")


st.subheader("Money-Making Motivation")
if st.button("Get Inspired", type="primary", key="quote"):
    quote = fetch_money_quote()

    if not quote:
        st.error("Failed to generate a money quote.")
    else:
        st.success(quote)

