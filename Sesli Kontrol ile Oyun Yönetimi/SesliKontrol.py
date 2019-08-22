#from pynput.keyboard import Key, Controller
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import selenium
from selenium import webdriver
#keyboard = Controller()
import keyboard

def recordAudio():
    print("Komut Ver")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
    data = ""
    try:
        data = r.recognize_google(audio, language='tr-tr')
        data = data.lower()
        print("Şu Komutu Verdin: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data
 

sag = ["sa","sağ"]
sol = ["sol","son"]
yukari = ["yukarı"]
asagi = ["aşağı","asağı","aşçı","ayşe"]
def jarvis(data):
    if data in sag:
        keyboard.press('d')
        time.sleep(1)
        keyboard.release('d')
    if data in sol:
        keyboard.press('a')
        time.sleep(1)
        keyboard.release('a')
    if data in yukari:
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')
    if data in asagi:
        keyboard.press('s')
        time.sleep(1)
        keyboard.release('s')

time.sleep(2)
while 1:
    data = recordAudio()
    jarvis(data)

