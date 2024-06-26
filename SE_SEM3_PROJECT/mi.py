import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("I hope u were having a great day,Good Morning!")
    elif hour>=12 and hour<18:
        speak("I hope u were having a great day,Good Afternoon!")

    else :
        speak("I hope u were having a great day, Good Evening!")

    speak("Hi User, I'm  kenny, your personal assistant how can i help you?")
        
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening.....")
       r.pause_threshold = 1
       audio = r.listen(source)

    try:
       print("Recognizing....") 
       query = r.recognize_google(audio, language = 'en-in')  
       print(f"User said:{query}\n")

    except Exception as e:
       print ("Say that again please.....")
       return "None"
    return query


if __name__ == "__main__":
   wishMe()
   while True:
        query = takeCommand().lower()

        # Logic 
        if 'wikipedia' in query:
           speak('Searching wikipedia....')
           query = query.replace('wikipedia','')
           results= wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")      
            
        elif 'how are you' in query:
            print("im fine")    
            speak("im fine")