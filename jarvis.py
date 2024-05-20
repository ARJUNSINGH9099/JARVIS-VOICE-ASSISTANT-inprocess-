import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
from ecapture import ecapture as ec
import wikipedia
import webbrowser
import pyjokes
import pywhatkit as kit
import pyautogui
import time
import requests
import smtplib
import sys
import ctypes
from b import process_query, listen_for_command






engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# text to speech
def speak(audio):
    engine.setProperty('rate', 150)  # Speed of speech
    # engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    engine.say(audio)

    print(audio)
    engine.runAndWait()
# convert voice to texxt
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recogning...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}")
    except Exception as e:
        speak("Say that again please...")
        return None
    return query
#  for wish
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak('i am jarvis 3 point o please tell me hoe can i help you')
# to send email
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("arjunrana9099@gmail.com","MANSICHAUHAN")
    server.sendmail("2022mcaaidsarjun10854@poornima.edu.in",to,content)
    server.close()
    # tell joke

def get_joke():
    # """Fetches and returns a joke using the pyjokes library."""
    try:
        joke = pyjokes.get_joke()
        return joke
    except Exception as e:
        return f"Error fetching joke: {e}"
        

    



if __name__== "__main__":

    wish()
    while True:
    # if 1:
        query=takecommand().lower()
        command = listen_for_command()
        process_query(command)

    # logic building for task
        if 'open notepad'  in query:
            npath="C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(npath)

        elif "who are you" in query:
            speak("i am jarvis three point o createtd by arjun")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "will you be my gf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")

        elif "wikipedia" in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            result= wikipedia.summary(query,sentences=4)
            speak("According to wikipedia")
            speak(result)
            # print(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "search on google" in query:
             speak("What do you want to search on Google?")
             search_query = takecommand().lower()
             search_url = "https://www.google.com/search?q=" + search_query
             webbrowser.open(search_url)
        
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")
       
        elif "send message" in query:
            phone_number = "+919045647246"
            message = "hi abhisek."
            kit.sendwhatmsg_instantly(phone_number,message,wait_time=10,tab_close=True)
             # Wait a bit longer to ensure the message is typed
            time.sleep(15)
            # Press the "Enter" key to send the message
            pyautogui.press('enter')

        elif "play song on youtube" in query:
            speak("what you want to play")
            song_name=takecommand().lower()
            kit.playonyt(song_name)
 
        elif "open stackoverflow" in query:
            webbrowser.open("")

        elif 'open adobe reader'  in query:
            apath="C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(apath)

        elif 'open command prompt'  in query:
            os.system("start cmd")

        elif  "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "no thanks" or "no" or "exit" in query:
            speak("thanks for using me sir ,have a good day")
            sys.exit()

        speak("sir do you have any other work")




        
        

        


        



        
        
       

        


       


