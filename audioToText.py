# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:51:41 2020

@author: mir6zw
"""

import speech_recognition as sr
import settings
import threads
import threading
import time


def streamToText(strr):
    r=sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        
        if (settings.GUI_var==1):
            settings.GUI_var=0
            x = threading.Thread(target=threads.thread_func_GUI, args=(strr,))
            x.daemon = True
            x.start()
            time.sleep(10)

        
        print(strr)        
        audio=r.listen(source,timeout=500)
        
        try:
            sentence=r.recognize_google(audio)
            line=str(sentence).lower().strip()
            
            settings.narrative.append(line)       

            print("--------------->>>>>>>>> "+r.recognize_google(audio))
            
            return line
            
        except Exception as e:
            print("Error: "+ str(e))
            settings.narrative.append("Did not hear anything, Goodbye!")
            return "Terminating..."
    
            
# =============================================================================
# if __name__=="__main__":
# 
#     import nltk
#     #nltk.download()
#     from nltk import sent_tokenize
#     from nltk import word_tokenize
# 
#     i=0
#     for i in range(5):
#         i=i+1
#         sent=streamToText("SAY IT------------>>>>>>>>>>")
#         if (sent=='Terminating...'):
#             print("Terminating...")
#             break
#         words=nltk.word_tokenize(sent)
#         print i
#         print sent
#         print words
#         print("---------------------")
#         print("---------------------")
# =============================================================================
