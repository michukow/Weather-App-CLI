from tkinter import *
from current import city, data_loading, show_weather
from forecast import location_label

def window(city_name,country,lat,longi):
    local = location_label(city_name,country,lat,longi)

    root=Tk()
    root.title(f"Weather for {local}")
    root.geometry("750x350")

    Label(root,text=f"Location: {local}").pack()
    Label(root,text=f"{weather}").pack()

    root.mainloop()