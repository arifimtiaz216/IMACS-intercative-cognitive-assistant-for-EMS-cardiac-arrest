
import speech_recognition as sr

import os
import os.path

    

audio = '10.wav'
    
    #print(nameOfFile)
    #print(audio)
    

with sr.AudioFile(audio) as source:
        #print('Hello There !')
   r = sr.Recognizer()
   audio = r.listen(source)
   print('Started !')
        
try:
   text = r.recognize_google(audio)
   #os.chdir(folderN)
   file = open("Ttt.txt", "w")
   file.write(text)
   print(text)
   print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
   file.close()
except Exception as e:
   print("Exception is :"+str(e))



