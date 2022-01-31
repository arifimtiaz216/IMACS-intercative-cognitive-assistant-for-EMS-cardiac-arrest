# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:13:10 2020

@author: mir6zw
"""

from Tkinter import *
import tkMessageBox
from time import sleep
import threading
from Queue import Queue

# Thread-safe version.
# Tkinter functions are put into queue and called by tkloop in the main thread.

q = Queue()

def button1():
    sleep(2)
    q.put(( tkMessageBox.showinfo, ('title', 'button 1'), {} ))

def button2():
    sleep(2)
    q.put(( tkMessageBox.showinfo, ('title', 'button 2'), {} ))

def start_thread(fun, a=(), k={}):
    threading.Thread(target=fun, args=a, kwargs=k).start()

def tkloop():
    try:
        while True:
            f, a, k = q.get_nowait()
            f(*a, **k)
    except:
        pass

    root.after(100, tkloop)


root = Tk()
frame = Frame(root)
frame.pack()

Frame(root).pack( side = BOTTOM )
Button(frame, command=lambda: start_thread(button1), text="Button 1").pack( side = LEFT)
Button(frame, command=lambda: start_thread(button2), text="Button 2").pack( side = LEFT )
tkloop() # tkloop is launched here
root.mainloop()