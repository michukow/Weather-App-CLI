from current import data_loading, show_weather
from forecast import location_label, chart
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

root = ctk.CTk()

def info():
    try:
        lat=float(lat_entry.get())
        lon=float(lon_entry.get())

        if not (-90<=lat<= 90 and -180<=lon<=180):
            raise ValueError

        city_name,country, _ = data_loading(lat,lon)
        date,time,temperature,wind_sp,wind_dir=show_weather(lat,lon)

        result_label.configure(
            text=(
                f"Date: {date} | Time: {time}\n"
                f"Max. temperature: {temperature} °C\n"
                f"Wind speed: {wind_sp} km/h | Wind direction: {wind_dir}°"
            )
        )

        chart_frame=ctk.CTkFrame(root,fg_color="transparent")
        chart_frame.grid(row=4,column=0,columnspan=2,pady=20)
        chart(chart_frame,lat,lon,city_name,country)

    except ValueError:
        messagebox.showerror("Invalid input","Latitude: -90 to 90\nLongitude: -180 to 180")

def window():

    global lat_entry,lon_entry

    root.title("Weather App")
    root.geometry("1100x700")
    root.grid_columnconfigure((0,1),weight=1)

    title = ctk.CTkLabel(root,text="Weather App",font=ctk.CTkFont(size=28,weight="bold"))
    title.grid(row=0,column=0,columnspan=2,pady=(20,10))

    lat_entry=ctk.CTkEntry(root,placeholder_text="Latitude")
    lat_entry.grid(row=1,column=0,padx=20,pady=10,sticky="ew")

    lon_entry=ctk.CTkEntry(root,placeholder_text="Longitude")
    lon_entry.grid(row=1,column=1,padx=20,pady=10,sticky="ew")

    btn=ctk.CTkButton(root,text="Check current weather",command=info)
    btn.grid(row=2,column=0,columnspan=2,pady=15)

    global result_label
    result_label=ctk.CTkLabel(root,text="",font=ctk.CTkFont(size=16),justify="left")
    result_label.grid(row=3,column=0,columnspan=2,pady=10)


if __name__ == "__main__":
    window()
    root.mainloop()
