import tkinter as tk
from tkinter import *
import requests 
import json 
import datetime 
from PIL import ImageTk, Image 
 
root = tk.Tk() 
root.title("Weather App") 
root.geometry("500x800") 
root['background'] = "sky blue"
  

name = StringVar() 
city_entry = Entry(root, textvariable=name, width=30)
city_entry.config(font = ('Times New Roman', 15)) 
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S) 
  
def city_name(): 
  
    dt = datetime.datetime.now() 
    date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15)) 
    date.place(x=5, y=130) 
    month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15)) 
    month.place(x=100, y=130) 
    
    label_citi = Label(root, text="...", width=0,
                   bg='white', font=("bold", 15)) 
    label_citi.place(x=10, y=63) 
  
    label_country = Label(root, text="...", width=0,bg='white', font=("bold", 15)) 
    label_country.place(x=135, y=63) 
  
    label_lon = Label(root, text="...", width=0,bg='white', font=("Helvetica", 15)) 
    label_lon.place(x=25, y=95) 
    label_lat = Label(root, text="...", width=0,bg='white', font=("Helvetica", 15)) 
    label_lat.place(x=95, y=95)  
  
    label_temp = Label(root, text="...", width=0, bg='white', font=("Helvetica", 110), fg='black') 
    label_temp.place(x=18, y=220) 

    humi = Label(root, text="Humidity: ", width=0,bg='white', font=("bold", 15)) 
    humi.place(x=3, y=400) 
  
    label_humidity = Label(root, text="...", width=0, bg='white', font=("bold", 15)) 
    label_humidity.place(x=107, y=400) 
  
    maxi = Label(root, text="Max. Temp.: ", width=0,bg='white', font=("bold", 15)) 
    maxi.place(x=3, y=430) 
    max_temp = Label(root, text="...", width=0,bg='white', font=("bold", 15)) 
    max_temp.place(x=128, y=430) 
  
    mini = Label(root, text="Min. Temp.: ", width=0, bg='white', font=("bold", 15)) 
    mini.place(x=3, y=460) 
  
    min_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15)) 
    min_temp.place(x=128, y=460) 
    note = Label(root, text="All temperatures are in degree celsius",bg='white', font=("italic", 10)) 
    note.place(x=95, y=495)  
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_entry.get() + "&units=metric&appid=" + "1987b31fcf1da3359611b45c4db65153") 
  
    api = json.loads(api_request.content) 
  
    # Temperatures 
    y = api['main'] 
    current_temprature = y['temp'] 
    humidity = y['humidity'] 
    tempmin = y['temp_min'] 
    tempmax = y['temp_max'] 
  
    # Coordinates 
    x = api['coord'] 
    longtitude = x['lon'] 
    latitude = x['lat'] 
  
    # Country 
    z = api['sys'] 
    country = z['country'] 
    citi = api['name'] 
  
    # Adding the received info into the screen 
    label_temp.configure(text=current_temprature) 
    label_humidity.configure(text=humidity) 
    max_temp.configure(text=tempmax) 
    min_temp.configure(text=tempmin) 
    label_lon.configure(text=longtitude) 
    label_lat.configure(text=latitude) 
    label_country.configure(text=country) 
    label_citi.configure(text=citi) 
city_nameButton = Button(root, text="Search", command=city_name) 
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S) 
root.mainloop() 
