# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:51:41 2020

@author: mir6zw
"""

import speech_recognition as sr

def streamToText():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please Say Something!")
        
        audio=r.listen(source)
        
        try:
            print("You have said \n"+r.recognize_google(audio))
            
        except Exception as e:
            print("Error--->>>> "+ str(e))
            
#if __name__=="__main__":
#    streamToText()