import requests
import tkinter as tk
from tkinter import ttk, StringVar, W, E, Listbox, Button

root = tk.Tk()
root.title("Weather App")
root.configure(background="light green")
root.geometry("500x400")
root.resizable(width=False, height=False)

canvas1 = tk.Canvas(root, width=400, height=300, background="light blue")
canvas1.pack()

label = ttk.Label(root, text="Enter City Name", background="light green", font=("TkDefaultFont", 16))
canvas1.create_window(200, 100, window=label)

IP = tk.Entry()
canvas1.create_window(200, 140, window=IP, width="170")

def weather():
    city = IP.get()
    lst = []
    Api_Add = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=f93e3c7d58b9511d289eab42e14c7f3c'.format(city)
    jsonData = requests.get(Api_Add).json()
    format1 = jsonData['weather'][0]['main']
    format2 = jsonData['weather'][0]['description']
    lst.append(format1)
    lst.append(format2)
    for i in lst:
        listbox.insert('end', i)

listbox = Listbox(root, height=5, width=20, font="helvetica 13")
canvas1.create_window(200, 230, window=listbox)

add_btn = Button(root, text="Click Here", bg="blue", fg="white", font="helvetica 10 bold", command=weather)
add_btn.place(x=200, y=340)

root.mainloop()

"""__________________________________________________________________________________________________________________"""
# def weather():
#     city = input("Enter your city name :")
#
#     #Formating Api key
#     Api_Add = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=f93e3c7d58b9511d289eab42e14c7f3c'.format(city)
#     jsonData = requests.get(Api_Add).json()
#     format1 = jsonData['weather'][0]['main']
#     format2 = jsonData['weather'][0]['description']
#
#     print(jsonData)
#     print(format1)
#     print(format2)
#
# weather()