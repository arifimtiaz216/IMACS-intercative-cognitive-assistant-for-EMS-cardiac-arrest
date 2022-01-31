# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 01:58:36 2020

@author: mir6zw
"""

import time
import Tkinter as tk
from PIL import Image, ImageTk
import writeFile

import datetime
import settings

def thread_func_GUI (info):
    
    def on_after3():
        narrative2="Welcome to the SmartEMS!\nWhat is the name of the patient?..."
        length=len(settings.narrative)
        i=0
        for i in range(length):
            if(settings.narrative[i]=='stop'):
                narrative2=narrative2+str(settings.narrative[i])+"ed. Goodbye!\n\n"
            else:
                narrative2=narrative2+str(settings.narrative[i])+".  "    
        rectangle_3.config(text=str(narrative2))
        #root.after(1300, on_after3)
        root.after(100, on_after3)
    
    def on_after4():
        suggestion2="Time- "+str(datetime.datetime.now())[11:19]+"\n"
        length=len(settings.suggestions)

        i=0
        for i in range(length):
            suggestion2=suggestion2+str(settings.suggestions[length-i-1])
            if (i>1):
                break

        rectangle_4.config(text=str(suggestion2))
        rectangle_4.after(100, on_after4)
        
    def on_after6():
        reminder2="Time- "+str(datetime.datetime.now())[11:19]+"\n"
        length=len(settings.reminders)

        i=0
        for i in range(length):
            reminder2=reminder2+str(settings.reminders[length-i-1])
            if (i>0):
                break

        rectangle_6.config(text=str(reminder2))
        rectangle_6.after(100, on_after6)
        
    def writeF():
        writeFile.writePDF()
        
    def hi():
        print "HI"
    
    ##########################  
    root = tk.Tk()
    root.title("SmartEMS Demo") 
    root.config(bg='snow')
    root.geometry("1920x1080")
    
    root.columnconfigure(0, weight=5)
    root.columnconfigure(1, weight=3)
    
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=5)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=5)
    root.rowconfigure(4, weight=2)
    root.rowconfigure(5, weight=3)
    ########################
    
    wraplength1=650
    wraplength11=700
    wraplength2=400
    
    ########################
    rectangle_1 = tk.Label(root, font="Helvetica 30 bold", text="Live Transcription", bg="snow", fg="black", borderwidth=3, relief="groove", anchor='center', wraplength=wraplength1)
    rectangle_1.grid(column=0, row=0, ipadx=10, ipady=10, sticky="NSEW")
    ########################
    rectangle_2 = tk.Label(root, font="Helvetica 18 bold", text="Feedback/Checklists", bg="lavender", fg="black", borderwidth=3, relief="groove", anchor='center', wraplength=wraplength2)
    rectangle_2.grid(column=1, row=0, ipadx=0, ipady=0, sticky="NSEW")
    ########################
    ########################
    rectangle_3 = tk.Label(root, font="Helvetica 14 bold", text="Welcome to the SmartEMS!", bg="snow", fg="black", borderwidth=2, relief="sunken", anchor='n', wraplength=wraplength11)
    rectangle_3.grid(column=0, row=1, rowspan=3, ipadx=10, ipady=10, sticky="NSEW")
    ########################
    rectangle_4 = tk.Label(root, font="Helvetica 14 bold", text="Time- "+str(datetime.datetime.now())[11:19], bg="lavender blush", fg="black", borderwidth=2, relief="sunken", anchor='n', wraplength=wraplength2)
    rectangle_4.grid(column=1, row=1, ipadx=10, ipady=10, sticky="NSEW")
    ########################
    rectangle_5 = tk.Label(root, font="Helvetica 18 bold", text="Reminders", bg="IndianRed3", fg="black", borderwidth=3, relief="groove", anchor='center', wraplength=wraplength2)
    rectangle_5.grid(column=1, row=2, ipadx=0, ipady=0, sticky="NSEW")
    ########################
    rectangle_6 = tk.Label(root, font="Helvetica 14 bold", text="Time- "+str(datetime.datetime.now())[11:19], bg="IndianRed1", fg="black", borderwidth=2, relief="sunken", anchor='n', wraplength=wraplength2)
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
    
    start_button = tk.Button(rectangle_7, text="Start/Restart", font=25, bg='snow3', fg='black', borderwidth=7, relief="raised", command=hi)
    start_button.config(height = 1, width = 20)
    start_button.grid(row = 1, column=0, sticky = "NS")

    
    quit_button = tk.Button(rectangle_7, text="Stop/Quit", font=25, bg='snow3', fg='black', borderwidth=7, relief="raised", command=root.destroy)
    quit_button.config(height = 1, width = 20)
    quit_button.grid(row = 1, column=1, sticky = "NS")
    
    
    start_button = tk.Button(rectangle_7, text="Generate Form", font=25, bg='snow3', fg='black', borderwidth=7, relief="raised", command=writeF)
    start_button.config(height = 1, width = 20)
    start_button.grid(row = 1, column=2, sticky = "NS")
    
    

    ###################################
    rectangle_8 = tk.Label(root, bg="snow", fg="black",borderwidth=3, relief="sunken", anchor='nw')
    rectangle_8.grid(columnspan=2, row=5, ipadx=10, ipady=10, sticky="NSEW")
    
    rectangle_8.columnconfigure(0, weight=1)
    rectangle_8.columnconfigure(1, weight=1)
    rectangle_8.columnconfigure(2, weight=1)
    
    bg_image1 = Image.open("000.jpg")
    bg_image=ImageTk.PhotoImage(bg_image1)
    rectangle_88 = tk.Label(rectangle_8, image= bg_image)
    rectangle_88.place(x=0, y=-20, relwidth=1, relheight=1)
    rectangle_88.grid(row=1, column=1, ipadx=0, ipady=0, sticky="NSWE")
    ###################################
    rectangle_3.after(5000, on_after3)
    rectangle_4.after(5000, on_after4)
    rectangle_6.after(5000, on_after6)
    ###################################
    root.mainloop()
        
# =============================================================================
# def thread_func_GUI2 (info):
#     
#     def update():
#         narrative2='What is the name of the patient?...\n'
#         length=len(settings.narrative)
#         i=0
#         for i in range(length):
#             if(settings.narrative[i]=='stop'):
#                 narrative2=narrative2+str(settings.narrative[i])+"ed. Goodbye!\n\n"
#             else:
#                 narrative2=narrative2+str(settings.narrative[i])+"...\n "    
#         l.config(text=str(narrative2))
#         root.after(1300, update)
# 
#     root = tk.Tk()
#     root.geometry("800x800")
#     l = tk.Label(text='Welcome to Cardiac Arrest Smart Interaction Module.\n')
#     l.pack()
#     root.after(5000, update)
#     root.mainloop()
# =============================================================================


def thread_func (info1,info2):
    
#    ctypes.windll.user32.MessageBoxW(None, unicode(info2), unicode(info1), 0x1000| 0x40)
    
    print("...")
    
def thread_func2 (info1,info2,delay):
    time.sleep(delay)
#    time.sleep(6)    
    settings.reminders.append(str(datetime.datetime.now())[5:19]+": "+info2)
        
#    ctypes.windll.user32.MessageBoxW(None, unicode(info2), unicode(info1), 0x1000| 0x40)    
#    print(info1+" acknowledged in thread_func2!")
    
def thread_func3 (info1,info2,delay,x):
    time.sleep(delay)
#    time.sleep(6)
    
    str1=str(datetime.datetime.now())[:19]+": Time of provider switch."
    settings.compression_time.append(str1)
    settings.sequential_list.append(str1)
    
    settings.reminders.append(str(datetime.datetime.now())[5:19]+": "+info2)
   
#    ctypes.windll.user32.MessageBoxW(None, unicode(info2), unicode(info1), 0x1000| 0x40)    
#    print(info1+" acknowledged in thread_func3!")