import sys
import os
import tkinter as tk
from imdb import IMDb
from tkinter import *
from PIL import ImageTk


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1500, height = 900)
canvas1.config(bg = 'black')

image = ImageTk.PhotoImage(file = "Images/Moviex.png")
canvas1.create_image(10, 10, image = image, anchor = NW)

canvas1.pack(padx = 10, pady = 10)

root.attributes("-fullscreen", True)


promptL = tk.Label(text = "Input favorite movie")
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


x = IMDb()

def reStart ():
    python = sys.executable
    os.execl(python, python, * sys.argv)
      

def getDetails(mName):
    canvas1.delete("all")
    button2 = tk.Button(text = 'Start Over', command = reStart, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1140, 40, window=button2)
    button2 = tk.Button(text = 'Exit', command = quit, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1000, 40, window=button2)
    label1 = tk.Label(text="Movies similar to: '{}' in genre".format(mName), bg = 'light blue', fg = 'black')
    label1.config(font = ("Courier", 15, 'bold'))
    canvas1.create_window(400, 20, window=label1)
    name = mName
    id = name.movieID
    movie = x.get_movie(id)
    genre = movie.data['genres']
    year = movie.data['year']
    rating = movie.data['rating']
    directors = movie.data['director']
    cast = movie.data['cast']
    
    label2 = tk.Label(text="Movie ID: {0}                        Movie Genres: {1}".format(id, genre), bg = 'light blue', fg = 'black')
    label2.config(font = ("Courier", 15, 'bold'))
    canvas1.create_window(600, 300, window=label2)
    label4 = tk.Label(text="Movie Year: {0}                         Movie Rating: {1}".format(year, rating), bg = 'light blue', fg = 'black')
    label4.config(font = ("Courier", 15, 'bold'))
    canvas1.create_window(450, 400, window=label4)
    label5 = tk.Label(text="Directors: {0}".format(directors), bg = 'light blue', fg = 'black')
    label5.config(font = ("Courier", 15, 'bold'))
    canvas1.create_window(700, 500, window=label5)
def getEntry ():  
    canvas1.delete("all")
    canvas1.config(bg = 'light blue')

    button2 = tk.Button(text = 'Exit', command = quit, bg = 'white', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1000, 40, window=button2)
    button2 = tk.Button(text = 'Start Over', command = reStart, bg = 'white', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1140, 40, window=button2)
    x1 = entry1.get()
    x2 = x.search_movie(x1) 
    y = 200
    z = 150
    index = 0
    for i in x2:
        index = index+1
    b = [0 for x in range(index)]
    tempI = 0
    for i in x2:
        b[tempI] = tk.Button(text=i, command = lambda i=i: getDetails(i), bg = 'white', fg = 'black')
        b[tempI].pack()
        tempI = tempI + 1
    for i in range(index):
        if z > 800:
            y = y+200
            z = 150
        if y > 1300:
            break
        canvas1.create_window(y, z, window = b[i])
        z = z+50
button1 = tk.Button(text='Enter', command=getEntry, bg = 'white', fg = 'black')
button1.config(font = (1))
canvas1.create_window(950, 430, window=button1)


root.mainloop()