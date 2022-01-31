# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:36:32 2020

@author: mir6zw
"""

import Tkinter as tk
from PIL import Image, ImageTk
import random

def on_after3():
    text1="Let's say I allow user to change the text type so how to configure that ? how to change it without declaring the variable again labelPryProt = Label()! "
    text1=text1+str(random.random())
    rectangle_3.configure(text=text1)
    rectangle_3.after(3000, on_after3)

def on_after4():
    text1="Let's say I allow user to change the text type so how to configure that ? how to change it without declaring the variable again labelPryProt = Label()! "
    text1=text1+str(random.random())
    rectangle_4.configure(text=text1)
    rectangle_4.after(3000, on_after4)
    
def on_after6():
    text1="Let's say I allow user to change the text type so how to configure that ? how to change it without declaring the variable again labelPryProt = Label()! "
    text1=text1+str(random.random())
    rectangle_6.configure(text=text1)
    rectangle_6.after(3000, on_after6)
    
def hi():
    print "HI"

##########################  
root = tk.Tk()
root.title("SmartEMS: An Interaction Module for Cardiac Arrest Cases in EMS") 
root.config(bg='snow')
root.geometry("1260x1000")

root.columnconfigure(0, weight=5)
root.columnconfigure(1, weight=3)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=7)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=5)
root.rowconfigure(4, weight=5)
########################

wraplength1=650
wraplength2=400

########################
rectangle_1 = tk.Label(root, font="Helvetica 30 bold", text="Live Trasncriptions", bg="snow", fg="black", borderwidth=3, relief="groove", anchor='center', wraplength=wraplength1)
rectangle_1.grid(column=0, row=0, ipadx=10, ipady=10, sticky="NSEW")
########################
rectangle_2 = tk.Label(root, font="Helvetica 18 bold", text="Suggestions", bg="purple", fg="black", borderwidth=3, relief="groove", anchor='center', wraplength=wraplength2)
rectangle_2.grid(column=1, row=0, ipadx=0, ipady=0, sticky="NSEW")
########################
########################
rectangle_3 = tk.Label(root, font=15, text="Hi", bg="snow", fg="black", borderwidth=2, relief="sunken", anchor='n', wraplength=wraplength1)
rectangle_3.grid(column=0, row=1, rowspan=3, ipadx=10, ipady=10, sticky="NSEW")
########################
rectangle_4 = tk.Label(root, font=15, text="Hi", bg="purple", fg="black", borderwidth=2, relief="sunken", anchor='n', wraplength=wraplength2)
rectangle_4.grid(column=1, row=1, ipadx=10, ipady=10, sticky="NSEW")
########################
rectangle_5 = tk.Label(root, font="Helvetica 18 bold", text="Reminders", bg="lightskyblue1", fg="black", borderwidth=3, relief="groove", anchor='center', wraplength=wraplength2)
rectangle_5.grid(column=1, row=2, ipadx=0, ipady=0, sticky="NSEW")
########################
rectangle_6 = tk.Label(root, font=15, text="Yo", bg="lightskyblue1", fg="black", borderwidth=2, relief="sunken", anchor='n', wraplength=wraplength2)
rectangle_6.grid(column=1, row=3, ipadx=0, ipady=0, sticky="NSEW")
########################
################################
rectangle_7 = tk.Label(root, bg="gray94", fg="black",borderwidth=3, relief="sunken", anchor='nw')
rectangle_7.grid(columnspan=2, row=4, ipadx=10, ipady=10, sticky="NSEW")


rectangle_7.rowconfigure(0, weight=2)
rectangle_7.rowconfigure(1, weight=1)
rectangle_7.rowconfigure(2, weight=2)
rectangle_7.columnconfigure(0, weight=1)
rectangle_7.columnconfigure(1, weight=1)
rectangle_7.columnconfigure(2, weight=1)

start_button = tk.Button(rectangle_7, text="Start", font=25, bg='misty rose', fg='black', borderwidth=7, relief="raised", command=hi)
start_button.config(height = 1, width = 20)
start_button.grid(row = 1, column=0, sticky = "NS")

quit_button = tk.Button(rectangle_7, text="Quit", font=25, bg='misty rose', fg='black', borderwidth=7, relief="raised", command=hi)
quit_button.config(height = 1, width = 20)
quit_button.grid(row = 1, column=2, sticky = "NS")


bg_image1 = Image.open("0.jpg")
bg_image=ImageTk.PhotoImage(bg_image1)
rectangle_8 = tk.Label(rectangle_7, image= bg_image)
rectangle_8.place(x=0, y=0, relwidth=2, relheight=2)
rectangle_8.grid(row=1, column=1, ipadx=10, ipady=10, sticky="NSWE")
###################################
###################################
rectangle_3.after(3000, on_after3)
rectangle_4.after(3000, on_after4)
rectangle_6.after(3000, on_after6)
###################################
root.mainloop()