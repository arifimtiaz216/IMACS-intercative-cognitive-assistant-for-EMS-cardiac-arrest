# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:55:04 2020

@author: mir6zw
"""
import datetime
from gtts import gTTS
import os

def test():
    # The text that you want to convert to audio 
    mytext = 'Welcome to the cardiac arrest smart interaction module! What is the name of the Patient?'
      
    # Language in which you want to convert 
    language = 'en'
      
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 
      
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 
      
    # Playing the converted file 
    os.system("welcome.mp3")
    
if __name__=="__main__":    
    #test()
    print str(datetime.datetime.now())[11:19]