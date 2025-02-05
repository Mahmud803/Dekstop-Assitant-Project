import json
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
import os
import pywhatkit as kit
import smtplib
import sys
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QTimer, QTime, QDate, Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
# from jarvis4 import Ui_MainWindow

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

# print(voices)

engine.setProperty('voice', voices[0].id)
# print(voices[0].id)

author = "Imran"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('almokaddim6@gmail.com', '1234almokaddim1234')
    server.sendmail('almokaddim6@gmail.com', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {author}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {author}")
    else:
        speak(f"Good Evening {author}")

    speak(f"Hello I am Jarvis, Please tell me How may I help You")


def takeCommend():
    '''
    take microphone input from the user and return string
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query} \n")
    except Exception as e:
        print(f"Sorry {author}, Say That again... ")
        return "None"
    return query


if __name__ == "__main__":
    # speak(f"Welcome {author}, I am Jarvis")
    wishMe()
    # takeCommend()
    while True:
        query = takeCommend().lower()
        if 'wikipedia' and 'who' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'news' in query:
            speak("News Headlines")
            query = query.replace("news", "")
            url = "Your News Api url"
            news = requests.get(url).text
            news = json.loads(news)
            art = news['articles']
            for article in art:
                print(article['title'])
                speak(article['title'])

                print(article['description'])
                speak(article['description'])
                speak("Moving on to the next news")
        elif 'open google' in query:
            speak("sir,what should i search on google")
            cm=takeCommend().lower()
            webbrowser.open(f"{cm}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search browser' in query:
            speak("What should i search ?")
            um = takeCommend().lower()
            webbrowser.open(f"{um}")

        elif 'ip address' in query:
            ip = requests.get('http://api.ipify.org').text
            print(f"Your ip is {ip}")
            speak(f"Your ip is {ip}")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open powerpoint' in query:
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codepath)

        elif 'open code block' in query:
            codepath = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(codepath)

        elif 'open vs code' in query:
            codepath = "C:\\Users\\mahmu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open chrome' in query:
            codepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codepath)

        

         
        elif 'play music' in query:
             music_dir = 'C:\\Users\\mahmu\\Desktop\\jarvis my project\\audio'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[0]))  

        elif 'play youtube' in query:
              speak("What should i search in youtube ?")
              cm = takeCommend().lower()
              kit.playonyt(f"{cm}") 

        elif 'send message' in query:
            speak("Who do you want to send the message ?")
            num = input("Enter number : \n")
            speak("what do you want to send?")
            msg = takeCommend().lower()
            speak("Please Enter Time sir.")
            H = int(input("Enter hour ?\n"))
            M = int(input("Enter Minutes ?\n"))
            kit.sendwhatmsg(num, msg, H, M) 

        elif 'email' in query:
            speak("What should i send sir ?")
            content = takeCommend().lower()
            speak("Whom to send the email , enter email address sir ")
            to = input("Enter Email Address : \n ")
            sendEmail(to, content)  

        elif "no thanks" in query:
            speak("thanks sir for using me,have a good day")
            sys.exit()

        elif 'how are you jarvis' in query:
            speak("Sir,i'm fine. what about you,sir")

        elif 'what is your name' in query:
            speak("i'm jarvis,sir")
            speak('sir i really fan of you')

        elif 'do you know asia' in query:
            speak("yes she is your relative")
           # speak('sir i really fan of you')



        speak("sir,do you have any other works")    
                 