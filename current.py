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

def get_localisation(lat, longi):
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

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    address = data.get("address", {})
    city_name = address.get("city") or address.get("town") or address.get("village")
    country = address.get("country")

    return city_name, country

def data_loading(lat,longi):
    city_name, country = get_localisation(lat,longi)

    params = {
        "latitude": lat,
        "longitude": longi,
        "current_weather": True
    }

    url = "https://api.open-meteo.com/v1/forecast"
    zapytanie=requests.get(url,params=params)
    content=zapytanie.json()
    return city_name, country, content

def location(lat,longi):
    try:
        response=requests.get(...)
        response.raise_for_status()
        data=response.json()

        address=data.get("address",{})
        city=address.get("city") or address.get("town") or address.get("village")
        country=address.get("country")

        return city,country

    except requests.RequestException:
        return None,None

def show_weather(lat,longi):
    city_name,country,content=data_loading(lat,longi)
    weather=content["current_weather"]
    data,czas=weather["time"].split("T")
    city_name,country=location(lat,longi)

    if city_name is None or country is None:
        print("Could not related coordinate to any city or country")
    elif city_name is None:
        print(f"{country}")
    elif country is None:
        print(f"{city_name}")
    else:
        print(f"{country}, {city_name}")

    print(f"Date: {data}")
    print(f"Time: {czas}")
    print(f"Temperature: {weather['temperature']} °C.")
    print(f"Wind speed: {weather['windspeed']} km/h.")
    print(f"Wind direction: {weather['winddirection']}°.")