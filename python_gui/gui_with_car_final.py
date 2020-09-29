import tkinter as tk
from tkinter import *
import os # for importing the image from the path
from PIL import Image, ImageTk  #module to put image in tkinter

import time
from time import sleep


app = tk.Tk() #creating a window
app.title('Highway')
app.geometry('600x600')
pic = Image.open("car2.png")  
picture = ImageTk.PhotoImage(pic)
def left_car():
    image = tk.Button(app, width=100, height=200, image=picture) #creating a button on which image can be uploded!!
    image.place(relx=0.1, rely=0.5, anchor=CENTER) 

    pic = Image.open("white.png")  
    picture2 = ImageTk.PhotoImage(pic)

    image = tk.Button(app, width=100, height=200, image=picture2) #making white center
    image.place(relx=0.5, rely=0.5, anchor=CENTER)

    image = tk.Button(app, width=100, height=200, image=picture2) #making white right
    image.place(relx=0.83, rely=0.5, anchor=CENTER)


    app.update()
def center_car():
    image = tk.Button(app, width=100, height=200, image=picture) #creating a button on which image can be uploded!!
    image.place(relx=0.5, rely=0.5, anchor=CENTER)

    pic = Image.open("white.png")  
    picture2 = ImageTk.PhotoImage(pic)

    image = tk.Button(app, width=100, height=200, image=picture2) #making white center
    image.place(relx=0.1, rely=0.5, anchor=CENTER)

    image = tk.Button(app, width=100, height=200, image=picture2) #making white right
    image.place(relx=0.83, rely=0.5, anchor=CENTER)



    app.update()
def right_car():
    image = tk.Button(app, width=100, height=200, image=picture) #creating a button on which image can be uploded!!
    image.place(relx=0.83, rely=0.5, anchor=CENTER) 

    pic = Image.open("white.png")  
    picture2 = ImageTk.PhotoImage(pic)

    image = tk.Button(app, width=100, height=200, image=picture2) #making white center
    image.place(relx=0.1, rely=0.5, anchor=CENTER)

    image = tk.Button(app, width=100, height=200, image=picture2) #making white right
    image.place(relx=0.5, rely=0.5, anchor=CENTER)


    app.update()

pic = Image.open("car2.png")  
picture = ImageTk.PhotoImage(pic)

frame = tk.Frame(app,bg = 'black',bd=5) #black line 1
frame.place(relx = 0.3,rely=0.168,relwidth=0.01,relheight=0.8)# positionin the color box

frame2 = tk.Frame(app,bg = 'black',bd=5) #black line 2
frame2.place(relx = 0.67,rely=0.168,relwidth=0.01,relheight=0.8)# positionin the color box


stop= tk.Button(app, width=10,height= 1,text="stop", activebackground="red", command=app.destroy)
stop.place(relx=0.5,rely=0.9, anchor=CENTER)

#test = open("rep.txt" , "r+") # now readingb the value frome the file
#reading = test.read()

fh = open('rep.txt')
for line in fh:
    if line.strip()== 'right':
        right_car()

    if line.strip()== 'left':
        left_car()

    if line.strip()== 'center':
        center_car()


    print(line)
    sleep(1)
fh.close()


app.mainloop()