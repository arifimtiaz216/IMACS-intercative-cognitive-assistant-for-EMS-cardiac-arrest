# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:00:54 2020

@author: mir6zw
"""
#import nltk
#nltk.download()
#from nltk import sent_tokenize
from nltk import word_tokenize


import threads
import threading
import datetime
import settings

def cardiac_arrest_found(info):
    #global isItCardiac
    #isItCardiac=1
#    print("Caridiac Arrest Case Detected!")
    
    infoo="Cardiac arrest case detected!\n---------------\n"

# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
def CPR_protocols(info):
    infoo="Checklists for CPR are:\n1. Swicth CPR provider every 5 minutes\n---------------\n"
    
    str1=str(datetime.datetime.now())[:19]+": Time of Compression Start."+"\n"
    settings.compression_time.append(str1)
    settings.sequential_list.append(str1)
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    i=0
    for i in range(3):
        i=i+1
        CPR_protocols_5min("Swtich CPR Provider alert!", 10*i)
#    print("CPR Protocols")
#    print("------------------------------")
    
def CPR_protocols_5min(info,delay):
    infoo="Times up! Switch CPR provider now!\n---------------\n"
    x = threading.Thread(target=threads.thread_func3, args=(info,infoo,delay,"dummy"))
    x.daemon = True
    x.start()

#    print("CPR Protocols")
#    print("------------------------------")
    
    
def start_CPR_BVM_DX(info,line):
    infoo="Checklists for the CPR/BVM/DX are:\n1. Check for chest rise\n---------------\n"
    
    words=word_tokenize(line)
    
    indexOff=int(words.index('bvm'))
    length=len(words)
    
    str2=''
#    i=indexOff
    for i in range(indexOff,length):
        str2=str2+" "+words[i]
        i=i+1    
 
    str1=str(datetime.datetime.now())[:19]+": Time of BVM start "+str2+"\n"
    settings.bvm_list.append(str1)
    settings.sequential_list.append(str1)

    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
#    print(str2)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================

# =============================================================================
# settings.init()
# start_CPR_BVM_DX("nothing","start bvm with yeheh hoho ahahha")
# =============================================================================
