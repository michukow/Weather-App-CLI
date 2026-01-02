import requests
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def data_load(lat,longi):
    params = {
        "latitude": lat,
        "longitude": longi,
        "daily": [
            "temperature_2m_max",
            "rain_sum"
        ],
        "timezone": "auto"
    }

    url = "https://api.open-meteo.com/v1/forecast"
    response = requests.get(url, params=params)
    data = response.json()["daily"]
    return data

def forecasting(lat,longi,city=None,country=None):
	dates=[]
	temp=[]
	rain=[]
	data=data_load(lat,longi)
	for i in range(len(data["time"])):
		dates.append(data['time'][i])
		temp.append(data['temperature_2m_max'][i])
		rain.append(data['rain_sum'][i])  
	return dates, temp, rain

def location_label(city=None,country=None,lat=None,lon=None):
    if city and country:
        return f"{city}, {country}"
    if city:
        return city
    if country:
        return country
    if lat is not None and lon is not None:
        return f"lat: {lat}, lon: {lon}"
    return "Unknown location"

def chart(parent,lat,longi,city=None,country=None):
    dates,temp,rain=forecasting(lat,longi)
    fig=Figure(figsize=(10,10))
    ax1=fig.add_subplot(111)

    ax1.plot(dates,temp,marker="o",label="Max temperature (°C)",color="red")
    ax1.set_ylabel("Max temperature (°C)")
    ax1.set_ylim(min(temp)-2,max(temp)+2)

    ax2=ax1.twinx()
    ax2.bar(dates,rain,alpha=0.4,label="Rain (mm)")
    ax2.set_ylabel("Rain (mm)")
    ax2.set_ylim(0,max(rain)+1 if max(rain)>0 else 1)

    ax1.set_title(location_label(city, country,lat,longi))
    ax1.tick_params(axis="x",rotation=45)

    canvas=FigureCanvasTkAgg(fig,parent)
    canvas.draw()
    canvas.get_tk_widget().pack()