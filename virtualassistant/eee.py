from email import message
from os import name
from tkinter.constants import S
import pywhatkit
import pyttsx3
from pywhatkit import main
import speech_recognition as sr
import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from newgui import Ui_MainWindow
import sys
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

def engine_speak(audio):
    engine.say(audio)
    engine.runAndWait()





r=sr.Recognizer()
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.0
        audio = r.listen(source ,5 ,5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        engine_speak("Say that again please...")
        return "None" 
    return query





        


  
if __name__== "__main__":

    query=takeCommand().lower()

    if query=="send a whatsapp message":
        engine_speak("enter the number")
        a=str(input("enter the number: "))
        time=datetime.time

        engine_speak("whats the message")
        b=str(input("type your message: "))
        pywhatkit.sendwhatmsg_instantly(a,b)
        print("message sent")
