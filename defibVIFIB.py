# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:09:41 2020

@author: mir6zw
"""
import datetime
import settings

import threads
import threading
import sys


def defibrillation_pads(info):
    infoo="Checklists for the defibrillation protocols are:\n1.Record EKG Waveform\n---------------\n"
    
    str1=str(datetime.datetime.now())[5:19]+": Time of attachment of Defibrillation Pads."+"\n"
    settings.defib_pad.append(str1)
    settings.sequential_list.append(str1)   
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
def defibrillation_protocols120 (info):
    #infoo="Reminders for VFIB Protocol Are:\n1.Start VFIB Protocol"
    infoo="1. First defibrillation 120 joules detected.\n---------------\n"
    str1=str(datetime.datetime.now())[5:19]+": Time of First Defibrillation. Defibrillation energy 120 Joules."+"\n"
    settings.defib_pad.append(str1)
    settings.sequential_list.append(str1)
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
#    defibrillation_protocols150_1 ("Second defibrillation starting",120)

def defibrillation_protocols150(info):
    infoo="1. Second defibrillation 150 joules detected.\n---------------\n"
    
    str1=str(datetime.datetime.now())[5:19]+": Time of second defibrillation. Defibrillation energy 150 Joules."+"\n"
    settings.defib_pad.append(str1)
    settings.sequential_list.append(str1)
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
def defibrillation_protocols200(info):
    infoo="1. This defibrillation 200 joules detected. \n---------------\n"
    
    str1=str(datetime.datetime.now())[5:19]+": Time of this defibrillation. Defibrillation energy 200 Joules."+"\n"
    settings.defib_pad.append(str1)
    settings.sequential_list.append(str1)
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================

def VFIB (info):
    #global isItVFIB
    #isItVFIB=1
    #print("Patient is in VFIB Protocol!")
    #infoo="Reminders for VFIB Protocol Are:\n1.Start VFIB Protocol"
    infoo="1. Detected: VFIB Protocol.\n---------------\n"
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
    defibrillation_timer("First DEFIB", "Defibriilate at 120 Joules",15)       
    defibrillation_timer("Second DEFIB", "Defibriilate at 150 Joules",30)
    defibrillation_timer("Next DEFIB", "Defibriilate at 200 Joules",45)       
    defibrillation_timer("Next DEFIB", "Defibriilate at 200 Joules",60)

def defibrillation_timer (info,infoo,delay):

    #infoo="Reminders for VFIB Protocol Are:\n1.Start VFIB Protocol"
    #infoo="1.Second defibrillation at 150 joules"
    
    x = threading.Thread(target=threads.thread_func2, args=(info,infoo,delay))
    x.daemon = True
    x.start()

def not_cardiac (info):
    infoo="STOP Here! Not a Cardiac Arrest Protocol! Protocol Missmatch."+"\n"
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    sys.exit()
    
def not_VFIB (info):
    infoo="STOP Here! Not a VFIB Protocol! Protocol Missmatch."+"\n"
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    sys.exit()