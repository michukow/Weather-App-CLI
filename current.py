import requests, json

def get_localisation(lat,longi):
    params = {
        "lat": lat,
        "lon": longi,
        "format": "json",
        "addressdetails": 1,
        "accept-language": "pl",
        "zoom": 10
    }

    headers = {"User-Agent": "weather-app-michal/1.0"}
    url = "https://nominatim.openstreetmap.org/reverse"

    response = requests.get(url,params=params,headers=headers)
    data = response.json()

    address = data.get("address",{})
    city_name = address.get("city") or address.get("town") or address.get("village")
    country = address.get("country")

    return city_name,country

def data_loading(lat,longi):
    city_name,country=get_localisation(lat,longi)

    params = {
        "latitude": lat,
        "longitude": longi,
        "current_weather": True,
        "timezone": "Europe/Warsaw"
    }

    url = "https://api.open-meteo.com/v1/forecast"
    zapytanie=requests.get(url,params=params)
    content=zapytanie.json()
    return city_name,country,content

def show_weather(lat, longi):
    city_name,country,content=data_loading(lat,longi)
    weather=content["current_weather"]
    date,time=weather["time"].split("T")
    return date,time,weather['temperature'],weather['windspeed'],weather['winddirection']
