import streamlit as st
import time

date = time.strftime("%d-%m-%y")

st.title("Weather Forecast")
place = st.text_input("Place: ")

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Look at the forecast five days ahead from the current date")
option = st.selectbox("Select data to view", ("Temperature", "Forecast"))


st.subheader(f"{option} for {date} in {place}")

