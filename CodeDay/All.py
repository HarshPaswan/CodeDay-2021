import tkinter as tk
import cgitb 

from tkinter import *
import os

from PIL import ImageTk
import MultiPurpose
import Weather

cgitb.enable()
root2= tk.Tk()

canvas2 = tk.Canvas(root2, width = 500, height = 400)
root2.title("MultiPurpose Catalog")
#canvas2.config(bg = 'white')

image = ImageTk.PhotoImage(file = "Images/Cave.png")
canvas2.create_image(0, 0, image = image, anchor = NW)


canvas2.pack(padx = 0, pady = 0)


def open():
    os.system('python MultiPurpose.py')
    
def open2():
    os.system('python Weather.py')


button2 = tk.Button(text = 'Movie APP', command=open, bg = 'orange', fg = 'black', width = 40, height = 5)
button2.config(font = (10))
canvas2.create_window(250, 100, window=button2)

button3 = tk.Button(text = 'Weather APP', command=open2, bg = 'sky blue', fg = 'black', width = 40, height = 5)
button3.config(font = (10))
canvas2.create_window(250, 300, window=button3)



root2.mainloop()