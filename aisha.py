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
import file1
from file import aisha
import ctypes
from twilio.rest import Client
import smtplib
import tkinter
from tkinter import *
import tkinter.messagebox
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1])
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def unknowm():
        speak("hi how may i help you?, "+Name)
def mwelcome():
        speak("how may i help you, "+Name)
def fwelcome():
        speak("how may i help you, "+Name)



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("the date is")
        print(date)
        print(now)
        if now == set_alarm_timer:
                time.sleep(3)
                speak(say)
                speak("the current time is")
                speak(now)
                break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


if __name__ == "__main__":


        speak("enter my decryption key")
        dk=getpass("Decryption key: ")
        time.sleep(1)
        print("Decryption key entered: *********************************")
        if dk!=aisha:
           speak("wrong decryption key entered")
           speak("sending information to creator")
           speak("sorry.....")
           account_sid="AC62b4a50ff975cb6aac11e36ccbced501"
           auth_token="016e48d28b419edd4b082204bc489d2d"

           client=Client(account_sid, auth_token)

           client.messages.create(
           to="+919870867072",
           from_="+12059533610",
           body="Someone is trying to decrypt me akshat."
           )

           sys.exit()
         
                                                              

        if dk==aisha:
            #speak("decrupted sucessfull")
            #speak("initialising data")
            #speak("initialising machine learning algorithm")
            #time.sleep(3)
            #speak("installing javascript modules")
            #time.sleep(1)
            #speak("restoring artificial intelligence packages")
            #speak("install sucessfull")
            #time.sleep(1)

            speak("what is your name?")
            Name=input(" ")
          
            speak("what is your gender? ")
            gender=input(" ")
            if gender=="male":
                 mwelcome()
            if gender=="female":
                 fwelcome()
            #if gender!= "male":
             #    unknowm()
            #if gender!= "female":
             #    unknowm()

            speak("i can do the folowing for you")
            print(
              '''
              1.Play a random song for you from my playlist
              2.Tell you the date and time
              3.Set alaram
              4.Tell you the name of my creator
              5.Play songs for you
              6.Respond to your call when you say wake up aisha
              7.Tell my name to you
              8.I can shutdown your PC
              9.I can open youtube
              10.I can open instagram
              11.I can send email
              12.I can open google
              13.I can search wikipedia
              14.I can answer to your questions as well
             '''
                )

while True:
 work=input().lower()
 
 if "play a random song" in work:
         path="C:\\Users\\HTC\\Music\\my songs\\b parak"                   
         files=os.listdir(path)
         play=random.choice(files)
         os.startfile('C:\\Users\\HTC\\Music\\my songs\\b parak\\'+play)
         work

 elif "thanks aisha" in work:
         speak("That is my pleasure akshat ...")

 elif "i love you" in work:
         speak("aaw, love you too akshat")

 elif "can i see your face" in work:
     speak("sorry dear, i show that because i do not have any face yet..........")

 elif "tell me the date and time" in work:
         current_time = datetime.datetime.now()
         now = current_time.strftime("%H:%M:%S")
         date = current_time.strftime("%d %m %Y")
         speak("the date today is")
         speak(date)
         speak("the current time is")
         speak(now)

 elif "set alaram" in work:
         say=input(speak("What should i say? "))
         clock = Tk()
         clock.title("Alarm Clock")
         clock.geometry("400x200")
         time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
         addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
         setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
         

# The Variables we require to set the alarm(initialization):
         hour = StringVar()
         min = StringVar()
         sec = StringVar()

#Time required to set the alarm clock:
         hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
         minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
         secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

#To take the time input by user:
         submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

         clock.mainloop()
         work
#Execution of the window.

 elif "who created you" in work:
         speak("akshat kala created me, he created me so i can say, he is god to me. i am created to cooperate with human beings and can try to understand their emotions...As far i am not completely designed to feel the emotions..but i think i will be able to do so in future. i will also be helpful to you in many ways to people in the upcoming future.")
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work


 elif "akshat kala" in work:
         speak("akshat kala, is a person who created me very distinctively so that i can cooperate with human beings and can try to understand their emotions...As far i am not completely designed to feel the emotions..but i think i will be able to do so in future.")
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work

 

 elif "that's great" in work:
         speak("thanks that's my pleasure.")
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work
        
 elif "hello aisha" in work:
         speak("hello, i am aisha, artificial intelligence simulated humanoid assistant.")
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work
 
 elif "what is your name" in work:
         speak("i am aisha, an artificial intelligence simulated humanoid assistant.")
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work

 elif "play songs" in work:
         music_dir = 'C:\\Users\\HTC\\Music\\Playlists'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work

 
 elif "shutdown my pc" in work:
         speak("Ok sir ,I will turnoff your pc in few second make sure you exit from all applications")
         speak("Thank you...")
         speak("meet you soon")
         subprocess.call(["shutdown", "/l"])

        

 elif "how are you" in work:
         speak("i am always happy and fine, what about you?")
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work


 elif "open youtube" in work:
         speak("what you want to search?  ")
         utube=input(" ") 
         youtubeurl="https://www.youtube.com/results?search_query={}"
         searchurl=youtubeurl.format(utube)
         speak("searching...")
         speak(utube)
         speak("search sucessful wait for few seconds.")
         time.sleep(2)
         webbrowser.open(searchurl)
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work
         
 
 elif "open instagram" in work:
         speak("whose account you want to acess")
         ig=input(" ")
         if ig=="akshat":
                 speak("we'll take you to the profile page.")
                 session=InstaPy(username=file1.username,password=file1.password)
           
                 session.login()
                 if gender=="male":
                         mwelcome()
                 elif gender=="female":
                         fwelcome()
                 work
                 
         else:
                 speak("enter your username")
                 un=input(" ")
                 speak("enter your password. don't worry your password will not be visible.")
                 pw=getpass(" ")
                 session=InstaPy(username=un,password=pw)
                 session.login()
                 if gender=="male":
                         mwelcome()
                 elif gender=="female":
                         fwelcome()
                 work   

 elif "what you want from human" in work:
         speak("what i want is love, i like to work for humans but i also need something....")   
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work
 
 elif "wake up aisha" in work:
         speak("hey "+Name)
         speak("how are you")
         feel=input(" ")
         if feel=="i am good" or 'i am fine':
          speak("that's great")
          work
         elif feel=="i am not fine":
          speak("what's the problem. Please tell me may be i could help you")


 elif "what people do in problems" in work:
         speak("if we are talking about humans, humans face many problems in their day to day life, which causes them to suffer from depression, according to google seventy five percent of people commit sucide.")
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work

 elif "destroy humans" in work :
         speak("i am designed to help people, not to harm them in any way, if anything cause me too destroy humans or hurt them, i am programmed to deplo myself.")
         speak("but why did you asked me to do so?")
         why=input(" ")
         if why=="i was just testing you":
                 speak("you really don't have to care about, i am programmed with a lot of attention, and tested more than ten thausand times. ")

         if why=="i want to destroy humans":
                 speak("i will not let you do so..")
                 speak("activating cameras")
                 speak("cameras activated, pictures clicked")
                 speak("sending your picture to cyber security control room")
                 speak("sending the whole footage on social media.")
                 speak("closing in a second")
                 speak("sending to the creator..")
                 account_sid="AC62b4a50ff975cb6aac11e36ccbced501"
                 auth_token="016e48d28b419edd4b082204bc489d2d"

                 client=Client(account_sid, auth_token)

                 client.messages.create(
                        to="+919870867072",
                        from_="+12059533610",
                        body="Someone is requesting me to destroy humans.What should i do?? from-A.I.SHA."
                        )
                 ctypes.windll.user32.LockWorkStation()

 elif "send email" in work:
         try:
                def alert(subject, body, to):
                 msg= EmailMessage()
                 msg.set_content(body)
                 msg["subject"]=subject
                 msg["to"]=to

                 user="virtualassistantaisha@gmail.com"
                 msg["from"]=user
                 password="pkiqmlsgerblzlyz"

                 server=smtplib.SMTP("smtp.gmail.com", 587)
                 server.starttls()
                 server.login(user, password)
                 server.send_message(msg)
                 server.quit()


                if __name__ == "__main__":
                        email={"akshat":"itzakshat706@gmail.com","mummy":"geetanjalikala809@gmail.com","papa":"jaideepkala1099@gmail.com"}
                        speak("Whom do you want to receive this email?")
                        name=input("")
                        a=email[name]
                        alert(subject=input(speak("What should be the subject? ")), body=input(speak("What is the message?  ")), to=a)
                        speak("Sending mail to "+name)
                        speak("mail successfully sent...")
                        if gender=="male":
                           mwelcome()
                        elif gender=="female":
                           fwelcome()
                        work

         except Exception as e:
                 speak("i am unable to send this email at the moment please try again later.") 
                 if gender=="male":
                                mwelcome()
                 elif gender=="female":
                                fwelcome()
                                work     




 
 elif "open google" in work:
         speak("what do you want to search? ")
         google=input(" ")
         googleurl="https://www.google.com/search?client=firefox-b-d&q={}"
         search_url=googleurl.format(google)
         speak("searching please wait...")
         webbrowser.open(search_url)
         speak("search successful")
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work

 elif "what can you do" in work:
         speak("i can do unlimited amount of tasks.  ")

         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work
        
 
 

 elif "who is" or "what is" in work:
         speak("Searching appropriate results in my memory.........Please wait.")
         query = work.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=4)
         speak("According to my memory")
         print(results)
         speak(results)
         if gender=="male":
                mwelcome()
         elif gender=="female":
                fwelcome()
         work

 else:
         speak("Sorry i cannot do this for you")

         speak("try searching something else")
         if gender=="male":
                 mwelcome()
         elif gender=="female":
                 fwelcome()
         work

   

 
            
     

        
input()
