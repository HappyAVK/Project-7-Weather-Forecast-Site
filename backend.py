import requests


def get_data(place, forecast_days, forecast_type):
    api_key = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid=d65ec62fc756db4c55b20c412c4c24c1"

    r = requests.get(api_key)
    cont = r.json()
    data = cont["list"]  # #"list" contains dictionaries for each day's temperature
    # There is a temperature reading every 3 hours, so to get data for all the requested days we times the amount by 3
    value = 8 * forecast_days
    new_data = data[:value]

    if forecast_type == "Temperature":

        new_data = [i["main"]["temp"] for i in new_data]
    elif forecast_type == "Forecast":

        new_data = [i["weather"][0]['main'] for i in new_data]

    return new_data


if __name__ == "__main__":
    print(get_data(place="tokyo", forecast_days=4, forecast_type="Temperature"))