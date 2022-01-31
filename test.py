# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:21:11 2020

@author: mir6zw
"""

#import time
#import easygui
#import Tkinter
#import tkMessageBox
#import pymsgbox

import threading
import ctypes


def thread_func (info):
    
    print("Inside Thread "+info+"\n")
    
    ctypes.windll.user32.MessageBoxW(None, unicode(info), unicode(info), 0x1000| 0x40)
    
    print(info+" acknowledged!")
    
# =============================================================================
#     easygui.msgbox("This es a message!", title="simple gui")
#     #easygui.msgbox("This is a message!", title="simple gui")
# =============================================================================
# =============================================================================
# #    root = Tk()
#     window = Tkinter.Tk()
#     window.wm_withdraw()
#     tkMessageBox.showinfo("--- MISSING OPTIONAL INFO ---","Yes")
#     time.sleep(5)
#     window.destroy()
# #    root.destroy()
# =============================================================================

    
# =============================================================================
#     import easygui   
#     easygui.msgbox("This is a message!", title="simple gui")
# =============================================================================
    
# =============================================================================
#     import pymsgbox
#     pymsgbox.alert('This is an alert!', 'Title')
#     response = pymsgbox.prompt('What is your name?')
# =============================================================================
    
    
    
if __name__ == "__main__":
    
    x = threading.Thread(target=thread_func, args=("GO AWAY hahahahhahhahahhahhahsadahsjdgagshfdhjsdfghjsdgfdakjsdgfdahjsdgfasd!",))
    x.daemon = True
    
    print("Main: Before Thread Starting\n")    
    x.start()

    print("Main: After Thread Starting\n")
    x.join()
       
    print ("Main : all done")
    
    y = threading.Thread(target=thread_func, args=("HAHAHA!",))
    y.daemon = True
    
    y.start()
#    y.join()
    

    