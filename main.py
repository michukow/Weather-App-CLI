from current import city, data_loading, show_weather
from forecast import location_label
from screen import window

def main():
    lat,longi=city()
    city_name,country,_ = data_loading(lat,longi)
    show_weather(lat,longi)
    window(city_name,country,lat,longi)

if __name__ == "__main__":
    main()