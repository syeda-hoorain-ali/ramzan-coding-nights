import streamlit as st
import requests
from style import styles


st.set_page_config(
    page_title="Random Joke Generator - Syeda Hoorain Ali",
    page_icon="🎭",
    layout="centered",
)


st.markdown(styles, unsafe_allow_html=True)
st.header("✨ Random Joke Generator ✨")


def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later."

    except:
        return "Why did programmers prefer dark mode? Because light attracts bugs!"


container = st.container(key="container")

with container:

    st.write("Click the button below to get a random joke!")
    if st.button("Get Random Joke", type="primary"):
        joke = get_random_joke()
        st.success(joke)

    st.write("If you want to see more jokes, just click the button again!")


footer = st.container(key="footer")
footer.write("Made with 💖 by Syeda Hoorain Ali")
