from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import json
import pytz


root = Tk()
root.title("Weather Application")
root.geometry("900x500+300+200")
root.resizable(False,False)


def getweather():

    try:

        city = textfied.get()

        geolocator = Nominatim(user_agent="myGeouser")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng = location.longitude, lat= location.latitude)
        # print(result)

        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather 
        api_key = "b96f823c2b43dba5add384e3b1675a17"
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text = (temp,"°"))
        c.config(text= (condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text= humidity)
        p.config(text=pressure)
        d.config(text=description)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!!")



#Search Bar 
image = PhotoImage(file="Weathe App\search.png")
myimage = Label(root, image=image)
myimage.place(x = 20, y= 20)

textfied = tk.Entry(root, justify="left", width=17, font=("poppins", 25,"bold"), bg="#404040", border=0, fg="white")
textfied.place(x=50, y=40)
textfied.focus()

search_icon = PhotoImage(file="Weathe App\search_icon.png")
image_icon = Button(image=search_icon, borderwidth=0, cursor="hand2",bg="#404040", command=getweather )
image_icon.place(x=400, y= 34)

#logo 
logo = PhotoImage(file="Weathe App\logo.png")
Logo = Label(image=logo)
Logo.place(x=150,y=100)

#bottom box
box = PhotoImage(file="Weathe App\Box.png")
Box = Label(image=box)
Box.pack(padx = 5 , pady = 5, side = BOTTOM)

#time 
name = Label(root, font=("arial",15, "bold"))
name.place(x= 30, y= 100)
clock = Label(root, font=("Helvetica",20))
clock.place(x=30, y=130)


#lable 
lable1 = Label(root, text="WIND", font=("Helvetica",15,"bold"), fg="White", bg="#1ab5ef")
lable1.place(x=120,y=400)

lable2 = Label(root, text="HUMIDITY", font=("Helvetica",15,"bold"), fg="White", bg="#1ab5ef")
lable2.place(x=250,y=400)

lable3 = Label(root, text="DESCRIPTION", font=("Helvetica",15,"bold"), fg="White", bg="#1ab5ef")
lable3.place(x=430,y=400)

lable4 = Label(root, text="PRESSURE", font=("Helvetica",15,"bold"), fg="White", bg="#1ab5ef")
lable4.place(x=650,y=400)

t = Label(font=("arial", 70,"bold"), fg="#ee666d")
t.place(x=400, y=150)

c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="....", font=("arial", 15, "bold"), bg="#1ab5ef")
w.place(x=130, y= 430)

h = Label(text="....", font=("arial", 15, "bold"), bg="#1ab5ef")
h.place(x=280, y= 430)

d = Label(text="....", font=("arial", 15, "bold"), bg="#1ab5ef")
d.place(x=460, y= 430)

p = Label(text="....", font=("arial", 15, "bold"), bg="#1ab5ef")
p.place(x=690, y= 430)

root.mainloop()