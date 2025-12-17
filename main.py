import requests, json

def city():
    while True:
        try:
            lat = float(input("Insert the latitude: "))
            longi = float(input("Insert the longitude: "))
            if -90 <= lat <= 90 and -180 <= longi <= 180:
                return round(lat, 2), round(longi, 2)
            else:
                print("Invalid range. Try again.")
        except ValueError:
            print("Insert valid latitude or longitude")

def get_localisation(lat,longi):

    params={
    "lat":lat,
    "lon": longi,
    "format": "json",
    "addressdetails": 1,
    "accept-language": "pl",
    "zoom": 10
    }

    headers = {
    "User-Agent": "weather-app-michal/1.0"
    }

    url = "https://nominatim.openstreetmap.org/reverse?"
    localisation=requests.get(url,params=params,headers=headers)
    data=localisation.json()
    address = data.get("address", {})
    city = address.get("city") or address.get("town") or address.get("village")
    country = address.get("country")
    return city, country

coordinates=city()
lat=coordinates[0]
longi=coordinates[1]

def data_loading():
    city_name, country = get_localisation(lat,longi)
    print(f"Looking for latitude: {lat} and longitude: {longi}")

    if city_name == None or country==None:
        print("Coordinates could not be related to any place")
    elif city_name==None:
        print(f"Showing weather for {country}")
    elif country==None:
        print(f"Showing weather for {city_name}")
    else:
        print(f"Showing weather for {city_name}, {country}")

    params = {
        "latitude": lat,
        "longitude": longi,
        "current_weather": True
    }

    url = "https://api.open-meteo.com/v1/forecast"
    zapytanie=requests.get(url,params=params)

    content=zapytanie.json()
    return content

def show_weather():
        content=data_loading()
        weather = content["current_weather"]
        data,czas=weather["time"].split("T")
        print(f"Weather for {lat}, {longi}: ")
        print(f"Date: {data}")
        print(f"Time: {czas}")
        print(f"Temperature: {weather["temperature"]} °C.")
        print(f"Wind speed: {weather["windspeed"]} km/h.")
        print(f"Wind direction: {weather["winddirection"]}°.")

show_weather()