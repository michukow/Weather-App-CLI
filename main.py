from current import city, data_loading, show_weather
from forecast import chart

def main():
    lat,longi=city()
    city_name,country, _ =data_loading(lat,longi)
    show_weather(lat,longi)
    chart(lat,longi,city_name,country)

if __name__ == "__main__":
    main()