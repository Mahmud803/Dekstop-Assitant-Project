import json
from json.tool import main
from pickle import TRUE
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
import os
import sys
import pywhatkit as kit
import smtplib
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis4 import Ui_MainWindow

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
    if hour >= 0 and hour < 4:
        speak(f"Good deep night {author}")
    elif hour >= 4 and hour < 10:
        speak(f"Good morning {author}")
    elif hour >= 10 and hour < 12:
        speak(f"Good noon {author}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {author}")
    else:
        speak(f"Good Evening {author}")

    speak(f"Hello {author} I am your voice assistant, Please tell me How may I help You")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()


    def takeCommend(self):
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

    def TaskExecution(self):

     # if __name__ == "__main__":
        # speak(f"Welcome {author}, I am Jarvis")
        wishMe()
        # takeCommend()
        while TRUE:
            self.query = self.takeCommend().lower()

            if 'wikipedia' and 'who' in self.query:
                speak("Searching Wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'news' in self.query:
                speak("News Headlines")
                self.query = self.query.replace("news", "")
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
            elif 'open google' in self.query:
             speak("sir,what should i search on google")
             cm=self.takeCommend().lower()
             webbrowser.open(f"{cm}")

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")

            elif 'search browser' in self.query:
                speak("What should i search ?")
                um = self.takeCommend().lower()
                webbrowser.open(f"{um}")

            elif 'ip address' in self.query:
                ip = requests.get('http://api.ipify.org').text
                print(f"Your ip is {ip}")
                speak(f"Your ip is {ip}")

            elif 'open command prompt' in self.query:
                os.system("start cmd")

            elif 'open powerpoint' in self.query:
                codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(codepath)

            elif 'open code block' in self.query:
                codepath = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
                os.startfile(codepath)

            elif 'open vs code' in self.query:
                codepath = "C:\\Users\\mahmu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

            elif 'chrome' in self.query:
                codepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(codepath)

            
            elif 'play music' in self.query:
                music_dir = 'C:\\Users\\mahmu\\Desktop\\jarvis my project\\audio'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))  

            elif 'play youtube' in self.query:
                speak("What should i search in youtube ?")
                cm = self.takeCommend().lower()
                kit.playonyt(f"{cm}") 

            elif 'send message' in self.query:
                speak("Who do you want to send the message ?")
                num = input("Enter number : \n")
                speak("what do you want to send?")
                msg = self.takeCommend().lower()
                speak("Please Enter Time sir.")
                H = int(input("Enter hour ?\n"))
                M = int(input("Enter Minutes ?\n"))
                kit.sendwhatmsg(num, msg, H, M) 

            elif 'email' in self.query:
                speak("What should i send sir ?")
                content = self.takeCommend().lower()
                speak("Whom to send the email , enter email address sir ")
                to = input("Enter Email Address : \n ")
                sendEmail(to, content) 

            elif "no thanks" in self.query:
               speak("thanks sir for using me,have a good day")
               sys.exit()      

            # elif "no thanks" in self.query:
            #     speak("thanks sir for using me,have a good day")
            #     sys.exit()

            speak("sir,do you have any other works")   


startExecution = MainThread()


class Main(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.startTask)
            self.ui.pushButton_2.clicked.connect(self.close)

        def startTask(self):
            self.ui.movie = QtGui.QMovie("../picture/7LP8.gif")
            self.ui.jarvis.setMovie(self.ui.movie)
            self.ui.movie.start()
            self.ui.movie = QtGui.QMovie("../picture/T8bahf.gif")
            self.ui.label_2.setMovie(self.ui.movie)
            self.ui.movie.start() 
            timer = QTimer(self)
            timer.timeout.connect(self.showtime) 
            timer.start(10000)  
            startExecution.start()

        def showtime(self):
            current_time = QTime.currentTime()
            current_date = QDate.currentDate()
            jarvis_time = current_time.toString('hh:mm:ss')
            jarvis_date = current_date.toString(Qt.ISODate)
            self.ui.textBrowser.setText(jarvis_date) 
            self.ui.textBrowser_2.setText(jarvis_time) 


app = QApplication (sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())         



