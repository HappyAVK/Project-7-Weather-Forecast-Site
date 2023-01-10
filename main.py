import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast")
place = st.text_input("Place: ")

sky_dict = {"Clear": "images/clear.png", "Clouds" : "images/clouds.png", "Rain" : "images/rain.png", "Snow" : "images/snow.png"}

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Look at the forecast five days ahead from the current date")
option = st.selectbox("Select data to view", ("Temperature", "Forecast"))


st.subheader(f"{option} for DATES in {place}")


if place:
    try:
        new_data = get_data(place, days)
        Error_msg = ""




        if option == "Temperature":
            Temp = [i["main"]["temp"] for i in new_data]
            Temp = [int(x/10) for x in Temp]
            Dates = [i["dt_txt"] for i in new_data]
            figure = px.line(x=Dates, y=Temp, labels={"x": "dates", "y": "temperatures(C)"})

            st.plotly_chart(figure)
        elif option == "Forecast":
            Sky_cond = [i["weather"][0]['main'] for i in new_data]

            current_sky = [sky_dict[condition] for condition in Sky_cond]
            st.image(current_sky, width=200)

    except LookupError:
        Error_msg = st.info("Enter a real world city")

