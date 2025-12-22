import requests
import matplotlib.pyplot as plt

def data_load(lat, longi):
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

def forecasting(lat,longi):
	dates=[]
	temp=[]
	rain=[]
	data=data_load(lat,longi)
	for i in range(len(data["time"])):
		dates.append(data['time'][i])
		temp.append(data['temperature_2m_max'][i])
		rain.append(data['rain_sum'][i])  
	return dates, temp, rain

def chart(lat,longi):
	dates,temp,rain=forecasting(lat, longi)

	fig, ax1 = plt.subplots(figsize=(10, 5))
	ax1.plot(dates, temp, marker="o", label="Max temperature (°C)",color="red")
	ax1.set_ylabel("Max temperature (°C)")
	ax1.set_ylim(min(temp)-2, max(temp)+2)

	ax2 = ax1.twinx()
	ax2.bar(dates,rain,alpha=0.4,label="Rain (mm)")
	ax2.set_ylabel("Rain (mm)")
	ax2.set_ylim(0,max(rain)+1)

	plt.title("7-day weather forecast")
	plt.xlabel("Date")

	plt.show()