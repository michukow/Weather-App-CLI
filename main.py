from current import data_loading, show_weather
from forecast import location_label
from tkinter import *

def current_forecast():
    try:
        lat=float(lat_entry.get())
        longi=float(lon_entry.get())

        if not(-90<=lat<= 90 and -180<=longi<= 180):
            raise ValueError("Coordinates out of range")

        city_name, country, _ = data_loading(lat, longi)
        show_weather(lat, longi)

        label.config(
            text=f"Location: {location_label(city_name,country,lat,longi)}",fg="black")

    except ValueError:
        messagebox.showerror("Invalid input","Latitude must be between -90 and 90\nLongitude must be between -180 and 180")

def window():
    global lat_entry, lon_entry, label

    root=Tk()
    root.title("Weather App")
    root.geometry("750x350")

    Label(root,text="Latitude:").pack()
    lat_entry=Entry(root,width=20)
    lat_entry.pack()

    Label(root,text="Longitude:").pack()
    lon_entry = Entry(root, width=20)
    lon_entry.pack()

    btn = Button(root, text="Check current weather", command=current_forecast)
    btn.pack(pady=10)

    label=Label(root,text="Enter coordinates and click the button")
    label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    window()
