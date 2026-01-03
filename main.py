from current import data_loading, show_weather
from forecast import location_label, chart
from tkinter import *

root=Tk()

def info():
    try:
        lat=float(lat_entry.get())
        longi=float(lon_entry.get())

        if not(-90<=lat<= 90 and -180<=longi<= 180):
            raise ValueError("Coordinates out of range")

        city_name,country, _ = data_loading(lat,longi)
        date,time,temperature,wind_sp,wind_dir=show_weather(lat,longi)
        chart_frame=Frame(root)
        chart_frame.pack()

        label.config(
        text=(
        f"Location: {location_label(city_name,country,lat,longi)}\n"
        f"Date: {date}, Time: {time}\n"
        f"Temperature: {temperature} °C\n"
        f"Wind: {wind_sp} km/h, {wind_dir}°"
        ),
        fg="black",justify="left")
        chart(chart_frame,lat,longi,city_name,country)

    except ValueError:
        messagebox.showerror("Invalid input","Latitude must be between -90 and 90\nLongitude must be between -180 and 180")

def window():
    global lat_entry,lon_entry,label

    root.title("Weather App")
    root.geometry("1250x750")

    Label(root,text="Latitude:").pack()
    lat_entry=Entry(root,width=20)
    lat_entry.pack()

    Label(root,text="Longitude:").pack()
    lon_entry=Entry(root,width=20)
    lon_entry.pack()

    btn=Button(root,text="Check current weather",command=info)
    btn.pack(pady=10)

    label=Label(root,text="Enter coordinates and click the button")
    label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    window()