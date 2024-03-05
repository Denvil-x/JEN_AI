
# Solely coded by Harsh 
# AI which can do many works
# More functions are to be added

import pyttsx3
import wikipedia as wp
import datetime
import webbrowser as wb
import speech_recognition as sr
import os
import random
# using microsoft speech api
jenny = pyttsx3.init("sapi5")
voices = jenny.getProperty("voices")
jenny.setProperty('voice', voices[1].id)

def speak(audio):
    # Speaker
    jenny.say(audio)
    jenny.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak(" Good Morning !")
    elif hour>12 and hour<18:
        speak(" Good Afternoon !")
    else :
      speak("Good Evening !") 
    print(" Started !")

    speak(" I am Jennny Sir , Please tell how can i help you !")

def command():     # Command Taker
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print(" Listening")
         r.pause_threshold = 1
         r.energy_threshold = 400
         audio = r.listen(source)

         try:
           print(" Recognizing....")
           # using google recognizer
           query = r.recognize_google(audio, language='en-in')
           print(f"User said : {query} \n")

         except Exception as e :
            #print(e)
            gh = " Can you say that again please...."
            print(gh)
            speak(gh)
            return "None"
     return query

if __name__ == "__main__" :
    wish_me()

    while True:
        query = command().lower()


        # Final functions 
        a =  True
        #if quit in query :
           # a = False


        if 'wikipedia' in query:
            speak(" Searching Wikipedia")
            query = query.replace("wikipedia", "")
            info = wp.summary(query,sentences=1)
            print(info)
            speak (" According to wikipedia ")  
            speak(info)
        elif 'open youtube' in query:

            speak(" Do you want me to sarch anything on youtube ?")
            ans = command().lower()
            if 'yes'or"yash" in ans:
                speak(" What do you want to search in google ?")
                qu = command()
                li =  f'https://www.youtube.com/results?search_query={qu}'
                wb.open(li)
            else:
                wb.open('youtube.com')

        elif 'open google' in query:
            wb.open("google.com")
            speak(" What do you want to search on google ?")
            search = command()
            site = f"/www.google.com/search?q={search}"
            wb.open(site)
        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")

        elif 'play music' in query:
            dir = "D:\Movies\harsh\AI JEN\music"
            songs = os.listdir(dir)
            r = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(dir,songs[r]))
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            st = f" Sir , the time is {time}"
            speak(st)
            print(st)

        elif 'open vs code' in query:
            path = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif " quit" in query:
            exit()

