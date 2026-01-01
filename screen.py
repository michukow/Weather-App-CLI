from tkinter import *
from current import city, data_loading, show_weather
from forecast import location_label
from main import current_forecast

def window_1(city_name,country,lat,longi):
    local=location_label(city_name,country,lat,longi)

    root=Tk()
    root.title(f"Weather for {local}")
    root.geometry("750x350")

    Label(root,text=f"Location: {local}").pack()
    btn = Button(root,text='Check current weather',command = root.current_forecast())
    btn.pack(side='top')  

    root.mainloop() #execute