from current import city, show_weather
from forecast import data_load, chart

def main():
    lat, longi = city()
    show_weather(lat, longi)
    data_load(lat, longi)
    chart(lat,longi)

if __name__ == "__main__":
    main()