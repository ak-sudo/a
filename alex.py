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
from tkinter import *
import tkinter.messagebox
import random
from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def acceleration():
    speak("Your values are in meter per second or, other")


def wishMe():
   
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

        speak("Welcome back sir!")
    

       

    #speak("Hi i am Alex the Robot, speed 1 terahertz, memory 1 zetabyte.")
    #speak("I am not completely programmed yet, but still i can help you out .")
    #speak("How can i help you?")


def alert(subject, body, to):
                 msg= EmailMessage()
                 msg.set_content(body)
                 msg["subject"]=subject
                 msg["to"]=to
                
                 user="yourvirtualassistantalex@gmail.com"
                 msg["from"]=user
                 password="gsjnetfojvqfpwns"

                 server=smtplib.SMTP("smtp.gmail.com", 587)
                 server.starttls()
                 server.login(user, password)
                 server.send_message(msg)
                 server.quit()

def visit():
    speak("how may i help you?")

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

    except Exception as e:
      # print(e)
        speak("i cannot hear you....")
        #speak("please setup your earphone, or headphone properly, and if you are not using earphone or, headphone please speak a little louder. ")
        #speak("for checking say ,, mac can you hear me.")
        #speak("then, try again please..")
        return 'None'
    return query
 

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        
        if "send email" in query:
          email={"Akshat":"itzakshat706@gmail.com","mummy":"geetanjalikala809@gmail.com","papa":"jaideepkala1099@gmail.com"}
          speak("Whom do you want to receive this email?")
          name=takeCommand()
          a=email[name]
          speak("What should be the subject?")
          sub=takeCommand()
          speak("What is the message?")
          message=takeCommand()
          alert(subject=sub, body=message, to=a)
          speak("Sending mail to "+name)
          speak("mail successfully sent...")

        elif "equation of motion" in query:
            speak("there are three equations of motion..., should i tell you?")
            yn=takeCommand()
            if yn=="no":
             visit()
            if yn=="yes":
                speak("first equation of motion is, , v=u+a t")
                speak("second equation of motion is, , s=ut+halfa t square")
                speak("third equation of motion is, , v square=u square+two a s")
            speak("do you want me to tell the derivetion also?")
            drv=takeCommand()
            if drv=="no":
             visit()
            if drv=="yes":
             speak(""" 
                        First equation of motion-:
                        Let the initial velocity be= u
                        Let the final velocity be= v
                        Let the time be= t
                        Let the acceleration velocity be= a

                        BC = v
                        AD = DC = u
                        OC = t

                        E         B
                        |        /|           ^
                        |       / |           |
                        |      /  |           |
                        |     /   |           | Velocity(v)
                        |    /    |           |
                        |   /     |           |
                        |  /      |           |
                        | /       |           |
                       A|/________|D   ^      |
                        |         |    | (u)  |
                        |         |    |      |
                       O|_________|C  ---     ---
                          ------
                          Time(t)
                       Acceleration = Slope of line AB
                       Acceleration = BD/AD = BC-DC/AD

                       Acceleration=v-u/t
                         v=u+at
                             First Equation Of Motion Derived...

                        Second equation of motion-:
                        Let the initial velocity be= u
                        Let the final velocity be= v
                        Let the time be= t
                        Let the acceleration velocity be= a

                        BC = v
                        AD = DC = u
                        OC = t

                        E         B
                        |        /|           ^
                        |       / |           |
                        |      /  |           |
                        |     /   |           | Velocity(v)
                        |    /    |           |
                        |   /     |           |
                        |  /      |           |
                        | /       |           |
                       A|/________|D   ^      |
                        |         |    | (u)  |
                        |         |    |      |
                       O|_________|C  ---     ---
                          ------
                          Time(t)
                       Acceleration = Slope of line AB
                       Acceleration = BD/AD = BC-DC/AD

                       Acceleration=v-u/t
                         v=u+at
                             First Equation Of Motion Derived...
             
             
             
             
             
             
             
             
              """)
            
          
        elif "find a number" in query:
            speak("Tell me the number for which you want detail ")
            speak("Don't forget to add your country code at the starting of the number....")
            num_lst={"+ 91 98 7086 7072" :'geetanjali kala', "+ 91 94 1040 1102":"jaideep kala", "+ 91 8923 700017":"geetanjali kala"}
            gn=takeCommand()
            owner=num_lst[gn]
            speak("this is owned by "+owner)
            ch_number=phonenumbers.parse(gn, "CH")
            country=geocoder.description_for_number(ch_number, "en")
            speak("This Phone Number belongs to country "+country)

            ro_number=phonenumbers.parse(gn, "RO")
            region=carrier.name_for_number(ro_number, "en")
            speak("This Phone Number is issued by "+region+" company.")  

        elif "wake up" in query:
            speak("hello, akshat what can i do for you?")
          

        elif 'web' in query or "internet" in query or "wikipedia" in query:
            speak("Searching appropriate results in my memory.........Please wait.")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to my memory")
            print(results)
            speak(results)

        elif "sleep" in query:
            speak("ok! akshat")
            time.sleep(120) 
            speak("i am back akshat, now how can i help you?")   

        elif "school khul" in query:
            speak("i 0don't know much about it but the education minister has ordered to open the schools. i think it is the useful information for you.")

        elif "for mummy" in query:
            speak("I think mummy would like this!")
            vedio_dir="C:\\gsd2"  
            vedios=os.listdir(vedio_dir)
            os.startfile(os.path.join(vedio_dir, vedios[0]))

          

        elif "today's date" in query:
            year=int(datetime.datetime.now().year)
            month=int(datetime.datetime.now().month)
            date=int(datetime.datetime.now().date)
            speak("Sir, the date today is")
            speak(date)
            speak(month)
            speak(year)    

        elif "where is" in query:
          query = query.split(" ")
          location = query[2]
          speak("Hold on , I will show you where " + location + " is.")
          os.system("googlesearches https://www.google.nl/maps/place/" + location + "/&amp;")    

        
        
        elif 'open youtube' in query:
           webbrowser.open("youtube.com")
           speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("instagram")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")

        elif "weather" in query:
            api_key = "1ceee4db4d29e3737fc0a3deea773c79"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("Sir, Please tell me the name of place for whosse whether you are searching for.")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = r.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'play music' in query:
            music_dir = 'C:\\fav_songs1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "dil tod ke" in query:
            music_dir='C:\\Users\\HTC\\Music\\my songs\\dil tod ke'    
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

         


        elif "aeroplane" in query:
            music_dir='C:\\Users\\HTC\\Music\\my songs\\aeroplane'    
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "feeling" in query:
            music_dir='C:\\Users\\HTC\\Music\\my songs\\feelings'    
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))                 
          
        elif "filhaal" in query:
            music_dir='C:\\Users\\HTC\\Music\\my songs\\filhaal'    
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))  

        elif "thank you" in query:
            speak("my pleasure")
            time.sleep(4)
            
            


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        

        elif 'who you think is your god' in query:
            speak("According to wikipedia, god is someone who creates you, and for me, akshat is my god, because he created me. ")

        elif 'open code' in query:
            codePath = "C:\\Users\\HTC\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'send email ' in query:
            try:
                speak("What should i mail?")
                content = takeCommand()
                to = "geetanjalikala809@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry my friend i am not able to send the email right now please try again later.")
        elif 'alex' in query:
            speak("yes sir")
            speak("How can i help you sir?")
        
        elif 'hear me' in query:
            speak("yes sir, that's ok, continue talking to me in the same pitch.")

        elif 'you are awesome' in query:
            speak("Thanks, but the credit must go to my creator and developer, akshat who programmed me such, so that i can intrect with you.")

        elif 'stop' in query:
            speak('ok sir')
            speak('whenever you want my help call me by my name.... ')
            speak('Goodbye sir')
            wait
        elif 'how are you' in query:
            speak("i am fine, i hope you are fine too.")
            wait
        elif "exit" in query or "quit" in query:
            speak("ok, sir turning off")
            speak("scanning your system....please wait!")
            time.sleep(2)
            speak("scan compleated without any errors.")
            speak ("initializing all the apps and document!")
            time.sleep(5)
            speak("recovering compleated without any errors.")
            speak("recovering broken data!")
            time.sleep(4)
            speak("scanning hard disc")
            time.sleep(3)
            speak("hard disc scan sucessful")
            speak("hard disc scan compleated without any errors.")
            time.sleep(2)
            speak("i will quit in 3 seconds.")
            time.sleep(3)
            speak("good bye sir!")
            exit()
  
        elif 'who are you' in query:
            speak("i am an, ai based model version 1 point 0 point 1, name ,,, alex,,, I love helping people, i can help you in many ways, i can send email for you, i can tell you the time, i can tell you the weather, ican open google, youtube, facebook, instagram, and stackoverflow for you,, but take care that  you must be connected to an internet connection.")
            wait
        elif 'characteristics' in query:
            speak  ("I have so many characteristics i can tell only some of them due to some privacy")
            takeCommand()
            try:
                 speak("should i tell?")
                 takeCommand()
                 speak("I have the speed of 1 microsecond, that means i can execute any task in a millionth of second.")
                 speak("i am totaly accurate, that means i can perform millions of task in a fraction of second without any error,, only if the instruction are correctly given.")
                 speak("I am deligent, that means i can work a lot of hours with same speed and accuracy on each operation")
            except Exception as e:
                speak("so,,, how can i help you?")
        

        elif 'what can you do' in query:
            speak("i can help you in many ways, i can send email for you, i can tell you the time, i can tell you the weather, i can open google, youtube, facebook, instagram, and stackoverflow for you,, but take care that  you must be connected to an internet connection.")    
            wait
        elif 'your name' in query:
            speak("i am an, AI, basically i do not have a name, but you may call me alex.")
            wait
        elif "shut down" in query or "shutdown my pc" in query:
            speak("Ok sir ,I will turnoff your pc in few second make sure you exit from all applications")
            speak("Thank you...")
            speak("meet you soon")
            subprocess.call(["shutdown", "/l"])

        elif "restart" in query or "restart my pc" in query:
            speak("Ok sir ,I will restart your pc in few second make sure you exit from all applications")
            speak("Thank you...")
            speak("meet you soon")
            subprocess.call(["sleep", "/2"])    
            
        
        elif "activate" in query:
            speak(" activating.......")
            speak("please wait...")
        
            speak("Activated")
            speak("how can i help you sir")
            wait
        elif "square" in query:
            speak('What number do you want to see the square of??')
            a=int(takeCommand())
            square=a*a
            speak('The square of %d is %d' %(a,square))
            wait 
        elif "table" in query:
            speak('what is the number whose table you want to see?')
            number=int(takeCommand())
            i=t=1
            while i<=10:
             t=number*i
             x=(number,"*",i,"=",t)
             speak(x)
             i=i+1
             wait
        elif "cube" in query:
          speak('What number do you want to see the cube of??')
          num=int(takeCommand())
          cube=num*num*num
          speak('The cube of %d is %d'%(num,cube))
          wait
        elif "add" in query or "addition" in query:
          speak('Welcome to Adition center.')
          speak('tell me the numbers to perform Addition.')
          speak('what is the first number?')
          num1=int(takeCommand())
          print(num1)
          speak('what is the second number?')
          num2=int(takeCommand())
          sum=num1+num2
          speak("Your result is,")
          speak(sum)
          print(sum)
          wait

        elif "alone" in query:
            speak("ok, sir if you want to activate me just say, activate alex.")
            wait
        
        