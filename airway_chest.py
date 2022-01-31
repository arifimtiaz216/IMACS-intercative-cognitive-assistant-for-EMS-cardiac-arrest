# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:21:07 2020

@author: mir6zw
"""
import nltk
#nltk.download()
from nltk import sent_tokenize
from nltk import word_tokenize

import threads
import threading

import datetime
import settings

def airway_breathing_protocols(info,line):
    infoo="Checklists for the airway breathing protocols are:\n1.Ausculate lungs, check chest rise, check ETCO2\n---------------\n"
    
    words=word_tokenize(line)
    
    indexOff=int(words.index('with'))
    length=len(words)
    
    str2=''
#    i=indexOff
    for i in range(indexOff,length):
        str2=str2+" "+words[i]
        i=i+1      
    
    str1=str(datetime.datetime.now())[5:19]+": Time airway was achieved"+". Type and Size of airway: "+str(str2)+"\n"
    settings.airway_list.append(str1)
    settings.sequential_list.append(str1)
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
def chest_rise_airway_breathing(info,line):
    infoo="Checklists for the chest rise condition are:\n1.Check the condition of chest rise and bilateral lung sound\n---------------\n"
    
    str1=str(datetime.datetime.now())[5:19]+": "+line+".\n"
    settings.chest_rise.append(str1)
    settings.sequential_list.append(str1)   

    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo) 
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================

def circulation_IO_protocols(info,line):
    infoo="Checklists for the circulation protocols are:\n1.Start epinephrine sequence protocols\n2. Administer epinephrine 1:10,000 1mg IVP\n---------------\n"
    
    loc='unknown'
    if('right' in line):
        loc='right humerus'
    elif('left' in line):
        loc='left humerus'
        
    fluid='unknown'
    if('saline' in line):
        fluid='normal saline'
    elif('glucose' in line):
        fluid='glucose solution'

    str1=str(datetime.datetime.now())[5:19]+": Time IO access was achieved. "+"Type of fluid: "+str(fluid)+". Location: "+str(loc)+"\n"
    settings.io_list.append(str1)
    settings.sequential_list.append(str1)   
      
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================