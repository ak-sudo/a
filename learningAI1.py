from instapy import InstaPy
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib as s0
import sys
import json
import requests
import time
import subprocess
from email.message import EmailMessage
import wait
import selenium
import AMP
from googlesearch import search
from getpass import getpass
import ctypes
from twilio.rest import Client
import smtplib
import tkinter
import tkinter.messagebox
import random
from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
   
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")    

       

    #speak("Hi i am Alex the Robot, speed 1 terahertz, memory 1 zetabyte.")
    #speak("I am not completely programmed yet, but still i can help you out .")
    #speak("How can i help you?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 90
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")

    except Exception:
      # print(e)
        speak("i cannot hear you....")
        #speak("please setup your earphone, or headphone properly, and if you are not using earphone or, headphone please speak a little louder. ")
        #speak("for checking say ,, mac can you hear me.")
        #speak("then, try again please..")
        return 'None'
    return query
 

if __name__ == "__main__":
    wishMe()
    speak("how can i help you sir?")
    while True:
        query = takeCommand().lower()

        if "what is your name" in query:
            speak("i am aisha your virtual assistant.")

        elif "who is your creator" in query:
            speak("akshat is my creator and my god!")

        elif "something about you" in query:
            speak("Hey there, i am aisha a self learning A I")

        elif "hey" in query:
            speak("hi, nice to meet you")

        elif "who is" in query:
            speak("ok, Please wait.")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to me.")
            print(results)
            speak(results)

        else:
            speak("indeed!")
            speak ("i dont't know about this please tell me about this!")

        

        

        

        
