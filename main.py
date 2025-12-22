from current import city, show_weather, location
from forecast import data_load, chart

def main():
    lat,longi = city()
    location(lat,longi)
    show_weather(lat,longi)
    data_load(lat,longi)
    chart(lat,longi)

if __name__ == "__main__":
    main()