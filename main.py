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

coordinates=city()
lat=coordinates[0]
longi=coordinates[1]

def data_loading():
    print(f"Looking for latitude: {lat} and longitude: {longi}")

    params = {
        "latitude": lat,
        "longitude": longi,
        "current_weather": True
    }

    url = "https://api.open-meteo.com/v1/forecast"
    zapytanie=requests.get(url,params=params)

    content=zapytanie.json()
    print("Content from page was loaded successfully")

    with open('weather.json','w',encoding='utf-8') as file:
        json.dump(content,file,ensure_ascii=False,indent=4)

def show_temp():
    with open('weather.json', 'r', encoding='utf-8') as file:
        dane = json.load(file)
    weather = dane["current_weather"]
    czas=weather["time"].split("T")
    print(f"Weather for {lat}, {longi}: ")
    print(f"Date: {czas[0]}")
    print(f"Time: {czas[1]}")
    print(f"Temperature: {weather["temperature"]}")
    print(f"Wind speed: {weather["windspeed"]}")
    print(f"Wind direction: {weather["winddirection"]}")

show_temp()