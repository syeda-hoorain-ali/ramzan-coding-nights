import datetime
import pandas as pd
import streamlit as st
from .style import styles
from .utils import load_mode_data, save_mood_data

st.set_page_config(
    page_title="Mood Tracker - Syeda Hoorain Ali",
    page_icon='😀',
    layout="centered",
)

st.markdown(styles, unsafe_allow_html=True)
st.header("😀 Mood Tracker 😝", anchor='heading')

with st.container(key='container'):
    st.subheader("How are you feeling today")

    mood: str = st.selectbox(
        "Select your mood",
        ["😀 Happy", "😢 Sad", "😡 Angry", "😐 Neutral", "😃 Excited", "😟 Anxious", "😌 Relaxed"]
    )

    if st.button("Log mood", type="primary"):
        today = datetime.date.today()
        save_mood_data(today, mood[2:])
        st.success("Mood Logged Successfully")

    data = load_mode_data()

    if not data.empty:
        st.subheader("Mood Trends Over Time")
        data["Date"] = pd.to_datetime(data["Date"])

        mood_counts = data.groupby(["Mood"]).count()
        col, = st.columns(1)
        col.bar_chart(mood_counts)


footer = st.container(key="footer")
footer.markdown("Made with 💖 by [Syeda Hoorain Ali](https://github.com/syeda-hoorain-ali/)")

