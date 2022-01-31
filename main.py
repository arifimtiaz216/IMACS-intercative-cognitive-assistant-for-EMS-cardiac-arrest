import threading
import ctypes
import time
#import datetime

import settings
import writeFile

import audioToText
import checkCondition
import threads
#import cardiac_CPR_BVM
#import defibVIFIB
#import airway_chest
#import vascular_rosc
#import epinephrine
#import flush_med_dilute

import textToAudio
#import time


# =============================================================================
# import tkinterPop
# from Tkinter import *
# =============================================================================
#import string
#from Tkinter import *
#import tkMessageBox
        
#isItCardiac=0
#isItVFIB=0

   
if __name__ == "__main__":
    
    settings.init()
#    textToAudio.test()    
#    time.sleep(6)
        
    strr="What is the name of the Patient?"
    settings.ptName=audioToText.streamToText(strr)
    print("--->>>"+settings.ptName)
    
# =============================================================================
#     fileName="Log for "+str(settings.ptName)+".txt"
#     fileLog=open(fileName,"a")
# =============================================================================
    
    strr="Listening................"
    
    while True:
        line=audioToText.streamToText(strr)
        print("--->>>"+line)

        
        if (line=='stop'):
            bye1="Goodbye!"
            bye2="Thanks For Using The Smart Interaction Module!"
            
            x = threading.Thread(target=threads.thread_func, args=(bye1,bye2))
            x.daemon = True
            x.start()
            
#            writeFile.writeF(fileLog)
#            writeFile.writeS(fileLog)
#            writeFile.writePDF()
#            fileLog.close()
            
            print(bye2)
#            time.sleep(6)
            break
        
        elif(line=='Terminating...'):
            bye1="Too Quiet!"
            bye2="We have not heard anything for a while, so stopped!"
            
            x = threading.Thread(target=threads.thread_func, args=(bye1,bye2))
            x.daemon = True
            x.start()
            
#            writeFile.writeF(fileLog)
#            writeFile.writeS(fileLog)
#            writeFile.writePDF()
#            fileLog.close()
            
            print(bye2)
            break 
#            exit
          
        else:
            flag=checkCondition.check_condition(line)
            
#    print (len(settings.suggestions))

            
    #print(settings.epinephrine_medication_record_list)
    #print(settings.amiodarone_medication_record_list)
        
