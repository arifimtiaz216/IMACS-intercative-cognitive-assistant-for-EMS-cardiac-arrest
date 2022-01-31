# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:28:28 2020

@author: mir6zw
"""
#import nltk
#nltk.download()
#from nltk import sent_tokenize
from nltk import word_tokenize

# threads
#import threading

import settings
import datetime

def post_medication_flush(info):
    infoo="Post medication flush detected.\nChecking medication name, dosage, route and time of administration\n---------------\n"
    
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
 
def dilute_amiodarone(info):
    infoo="Dilute 150mg of amiodarone in 100mL D5W to yield 1.5mg/mL\n---------------\n"
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)

    
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
def med_details(infoOfMed):
#    print("The line is: "+infoOfMed)
#    print("Extract Details of Medication!")

#    info="Listing medication details"
    infoo="Checklists for the medication cross check are:\n1.Check medication name \n2.Check dosage\n3.Check route of administration\n6.Check time of administration\n---------------\n"   

    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": "+infoo)
# =============================================================================
#     x = threading.Thread(target=threads.thread_func, args=(info,infoo))
#     x.daemon = True
#     x.start()
# =============================================================================
    
def med_details_epinephrine(line):
    
#    global ptName
    #global epinephrine_medication_record_list
    str1=str(datetime.datetime.now())[5:19]+": Patient name = "+settings.ptName+", Medication name = Epinephrine, Dosage = 1:10,00 1mg, Route of administration = IVP, Time of administration = "+str(datetime.datetime.now())[5:19]+"\n"
    settings.epinephrine_medication_record_list.append(str1)
    settings.sequential_list.append(str1)
    
    #print("DIMIDMIDMIDMIDMIDMIDMDIMDIDMIDMDIMDIDMDIMDIDMIDMDIMD")
    #print(settings.epinephrine_medication_record_list)
    
    
def med_details_amiodarone(line):

#    print("The line is: "+line)
    dosageGiven=''
    routeGiven=''
    
    words=word_tokenize(line)
    
    if('mg' in words):
        indexOf=int(words.index('mg'))
        dosageGiven=str(words[indexOf-1])
        
    if('drip' in line):
        routeGiven='IV drip '
        if('minutes' in line):
            indexOff=int(words.index('minutes'))
            routeGiven='IV drip over '+str(words[indexOff-1])+' minutes'
    elif('iv push' in line):
        routeGiven='IV push'
                
    str1=str(datetime.datetime.now())[5:19]+": Patient name = "+settings.ptName+", Medication name = Amiodarone, Dosage = "+dosageGiven+"mg, Route of administration = "+routeGiven+", Time of administration = "+str(datetime.datetime.now())[5:19]+"\n"
    settings.amiodarone_medication_record_list.append(str1)
    settings.sequential_list.append(str1)
    #print(routeGiven,dosageGiven)

    
#print(datetime.datetime.now())
# =============================================================================
# settings.init() 
# haha= "Giving the post medication flush and an iv push of Amiodarone 300 mg now"
# hahaha= "I’m administering amiodarone drip 150 mg over 10 minutes via IV pump"
# med_details_amiodarone(haha)
# =============================================================================
