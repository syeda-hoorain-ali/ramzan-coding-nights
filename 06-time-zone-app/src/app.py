import pandas as pd
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
from styles import style_dataframe, styles

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]


st.set_page_config(
    page_title="Time Zone App - Syeda Hoorain Ali", 
    page_icon="🕰️", 
    layout="centered"
)

st.markdown(styles, unsafe_allow_html=True)
st.title("Time Zone App")


with st.container(key="container"):

    time_zone, convert = st.tabs(["**Time Zone**", "**Convert Time**"])

    with time_zone:
        selected_time_zone = st.multiselect("Select time zones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

        st.subheader("Selected Time Zones")
        
        table: list[dict[str, str]] = []

        for tz in selected_time_zone:
            current_time = datetime.now(ZoneInfo(tz)).strftime('%Y-%m-%d  %I:%M:%S %p')
            table.append({"Time Zone": tz, "Current Time": current_time})

        dataframe = pd.DataFrame(table, index=None)
       
        styled_df = style_dataframe(dataframe)
        st.table(styled_df)


    with convert:
        st.subheader("Convert Time Between Time Zone")
        current_time = st.time_input("Current Time")
        col1, col2 = st.columns(2)

        from_tz = col1.selectbox("From Time Zone", TIME_ZONES, index=0)
        to_tz = col2.selectbox("To Time Zone", TIME_ZONES, index=1)

        if st.button("Convert Time", type="primary"):

            dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
            converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime('%Y-%m-%d  %I:%M:%S %p')

            st.success(f"Converted Time in {to_tz}: {converted_time}")


