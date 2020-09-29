import tkinter as tk 

import os 
#import speech2text.py

root = tk.Tk()
from PIL import Image, ImageTk
height = 600 #size of main box
width = 800

def showImg():
 
    pic = Image.open("car2.png")  
    picture = ImageTk.PhotoImage(pic) 

    image = tk.Button(frame1, width=100, height=200, image=picture) #creating a button on which image can be uploded!!
    image.place(relx=0.2, rely=0.5)

def button1():


    frame2 = tk.Frame(root,bg = 'gray',bd=5) # make frame inside the above box
    frame2.place(relx = 0.19,rely=0.4,relwidth=0.65,relheight=0.2)# positionin the color box 

    frame1 = tk.Frame(root,bg = 'green',bd=5) # make frame inside the above box
    frame1.place(relx = 0.21,rely=0.4,relwidth=0.15,relheight=0.2)# positionin the color box

    frame4 = tk.Frame(root,bg = 'black',bd=5) #black line 1
    frame4.place(relx = 0.4,rely=0.168,relwidth=0.01,relheight=0.7)# positionin the color box
    frame4 = tk.Frame(root,bg = 'black',bd=5) #black line2
    frame4.place(relx = 0.61,rely=0.168,relwidth=0.01,relheight=0.7)# positionin the color box
def button2():
    frame2 = tk.Frame(root,bg = 'gray',bd=5) # make frame inside the above box
    frame2.place(relx = 0.19,rely=0.4,relwidth=0.65,relheight=0.2)# positionin the color box 
    frame1 = tk.Frame(root,bg = 'green',bd=5) # make frame inside the above box
    frame1.place(relx = 0.43,rely=0.4,relwidth=0.15,relheight=0.2)# positionin the color box
    frame4 = tk.Frame(root,bg = 'black',bd=5) #black line 1
    frame4.place(relx = 0.4,rely=0.168,relwidth=0.01,relheight=0.7)# positionin the color box
    frame4 = tk.Frame(root,bg = 'black',bd=5) #black line2
    frame4.place(relx = 0.61,rely=0.168,relwidth=0.01,relheight=0.7)# positionin the color box
def button3():
    frame2 = tk.Frame(root,bg = 'gray',bd=5) # make frame inside the above box
    frame2.place(relx = 0.19,rely=0.4,relwidth=0.65,relheight=0.2)# positionin the color box 
    frame1 = tk.Frame(root,bg = 'green',bd=5) # make frame inside the above box
    frame1.place(relx = 0.64,rely=0.4,relwidth=0.15,relheight=0.2)# positionin the color box
    frame4 = tk.Frame(root,bg = 'black',bd=5) #black line 1
    frame4.place(relx = 0.4,rely=0.168,relwidth=0.01,relheight=0.7)# positionin the color box
    frame4 = tk.Frame(root,bg = 'black',bd=5) #black line2
    frame4.place(relx = 0.61,rely=0.168,relwidth=0.01,relheight=0.7)# positionin the color box

canvas = tk.Canvas(root,height=height,width = width) # apply main box
canvas.pack()

frame = tk.Frame(root,bg = 'silver') # make frame inside the above box
frame.place(relx = 0.1,rely=0.1,relwidth=0.8,relheight=0.8)# positionin the color box 

frame1 = tk.Frame(root,bg = 'gray',bd=5) # make frame inside the above box
frame1.place(relx = 0.15,rely=0.16,relwidth=0.7,relheight=0.7)# positionin the color box 

frame4 = tk.Frame(root,bg = 'black',bd=5) #black line 1
frame4.place(relx = 0.4,rely=0.168,relwidth=0.01,relheight=0.7)# positionin the color box
frame4 = tk.Frame(root,bg = 'black',bd=5) #black line2
frame4.place(relx = 0.61,rely=0.168,relwidth=0.01,relheight=0.7)# positionin the color box

'''background_image = tk.PhotoImage(file='car.png')
background_label1 = tk.Label(root,image=background_image)
background_label1.place(relx=1,rely=1,relheight=100)'''

label = tk.Label(frame,text ="Highway",bg = 'silver')
label.place(relx=0.38,rely=0.01)

button1 = tk.Button(frame1, text="left" , bg='gray', fg = 'gray',command = showImg) #button # here if instead of frame writing root buttom go to top of this box (out of color one)
button1.place(relx=0.1,rely=0.1)

button2 = tk.Button(frame1, text="middle" , bg='gray', fg = 'gray',command = button2) #button # here if instead of frame writing root buttom go to top of this box (out of color one)
button2.place(relx=0.4,rely=0.1)

button3 = tk.Button(frame1, text="right" , bg='gray', fg = 'gray',command = button3) #button # here if instead of frame writing root buttom go to top of this box (out of color one)
button3.place(relx=0.75,rely=0.1)

root.mainloop()





