# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:25:02 2020

@author: mir6zw
"""
import datetime
import settings

import threads
import threading

def epinephrine_sequence_protocols(info):
    infoo="Checklists for the epinephrine sequence protocol are:\n1.Timer set: epinephrine sequence every 3 minutes\n2.Perform post-medication flush and Amiodarone 300 mg IVP\n---------------\n"
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
    i=0
    for i in range(3):
        i=i+1
        epinephrine_sequence_protocols_3mins("Epinephrine sequence protocol reminder-",6*i)
#    print("Epinephrine Sequence Protocols")
#    print("------------------------------")
    
def epinephrine_sequence_protocols_3mins(info,delay):
    infoo="1. Time up! Administer another dosage \nfor the Epinephrine Sequence Protocol now!"+"\n"
    x = threading.Thread(target=threads.thread_func2, args=(info,infoo,delay))
    x.daemon = True
    x.start()
#    print("Epinephrine Sequence Protocols")
#    print("------------------------------")