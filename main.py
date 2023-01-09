import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast")
place = st.text_input("Place: ")


days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Look at the forecast five days ahead from the current date")
option = st.selectbox("Select data to view", ("Temperature", "Forecast"))


st.subheader(f"{option} for DATES in {place}")


def heat_up_the_sun(days):

    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]

    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = heat_up_the_sun(days)

figure = px.line(x=d, y=t, labels={"x": "dates", "y": "temperatures(C)"})

st.plotly_chart(figure)

