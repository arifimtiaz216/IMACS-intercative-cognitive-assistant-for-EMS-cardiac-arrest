# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:22:40 2020

@author: mir6zw
"""

import threads
import threading

import datetime
import settings

def vascular_access(info):
    
    infoo="1. Vascular access detected.\nTimer started for vascular access protocol\n---------------\n"
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
    vascular_attempt_intraneous ("Attempting intraneous access after 90 seconds of first IV Attempt-",6)

def vascular_attempt_intraneous(info,delay):
    infoo="Checklists for the intraneous access protocols are:\n1.Attempt intraneous access 90 seconds from first IV\n---------------\n"
    x = threading.Thread(target=threads.thread_func2, args=(info,infoo,delay))
    x.daemon = True
    x.start()
    
def vascular_access_intubation(info):
    infoo="1.First intubation attempt detected.\n---------------\n"
    
    settings.suggestions.append(str(datetime.datetime.now())[5:19]+": "+infoo)

    str1=str(datetime.datetime.now())[5:19]+": Time of first intubation attempt."+"\n"
    settings.intubation_list.append(str1)
    settings.sequential_list.append(str1)

# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
    
def ROSC_yes_protocols (info):
    infoo="Checklists for the ROSC protocols are:\n1.Amiodarone drip 150 mg over 10 mins by IV pump\n2.Dilute of 150mg amiodarone in 100ml D5W to yield 1.5mg/mL concentration\n---------------\n"
    #3.Dilute 150mg of amiodarone in 100mL D5W to yield 1.5mg/mL"
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
    str1=str(datetime.datetime.now())[5:19]+": Time of first ROSC found."+"\n"
    settings.rosc_list.append(str1)
    settings.sequential_list.append(str1)    
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================

    
def ROSC_no_protocols(info):
    infoo="No ROSC detected, to do checklists are:\n1.Check resuscitation list\n2.Retsart CPR\n---------------\n"
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
# =============================================================================
# 
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
#     
# =============================================================================
    str1=str(datetime.datetime.now())[5:19]+": No ROSC found."+"\n"
    settings.rosc_list.append(str1)
    settings.sequential_list.append(str1)