import requests, json
import tkinter as tk
import sys
import os

from tkinter import *


api_key = "1987b31fcf1da3359611b45c4db65153"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1500, height = 900)
canvas1.config(bg = 'light grey')


canvas1.pack(padx = 10, pady = 10)

root.attributes("-fullscreen", True)


promptL = tk.Label(text = "Input name of your city")
promptL.config(font = (5))
canvas1.create_window(680, 400, window = promptL)
entry1 = tk.Entry (root, width = 40)
entry1.config(font = (3))
canvas1.create_window(690, 430, window = entry1)

def quit():
    root.destroy()

button2 = tk.Button(text = 'Exit', command = quit, bg = 'white', fg = 'black')
button2.config(font = (10))
canvas1.create_window(1400, 40, window=button2)


def reStart ():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
    
root.mainloop()