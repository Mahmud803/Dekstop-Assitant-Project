import json
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import requests
import json
import webbrowser
import os
#import pywhatkit as kit
import smtplib
engine = pyttsx3.init('sapi5')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


#print(voices)
engine.setProperty('voice', voices[0].id)
#print(voices[0].id)
engine.setProperty('rate',160)

author = "Imran"
def speak(audio):
 engine.say(audio)
 engine.runAndWait()

       

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {author} ")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {author} ")
    else:
        speak(f"Good Evening {author} ")

    speak(f"I am Jarvis, Please tell me How may I help You")

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
    if 1:
        query = takeCommend().lower()
        if 'wikipedia' and 'who' and 'what' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'news' in query:
            speak("News Headlines")
            query = query.replace("news", "")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b4fd19b4ccca4b4db7dac7b35ba95ec4"
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
            webbrowser.open("google.com") 

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
           
              
