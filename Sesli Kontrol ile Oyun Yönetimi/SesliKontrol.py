#from pynput.keyboard import Key, Controller
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
#keyboard = Controller()
import keyboard


# Etraftaki sesleri dinleyerek algılayan fonksiyon. 
def recordAudio():
    print("Komut Ver")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
    data = ""
    try:
        # Google ses algılama kütüphanesinin ayarları
        data = r.recognize_google(audio, language='tr-tr')
        data = data.lower()
        print("Şu Komutu Verdin: " + data)
        
    # Herhangi bir kelime algılayamazsa, döneceği hata
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    # İnternet yoksa döneceği hata
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data
 

# Algılayabileceği kelimeler ve algıladığında alacağı aksiyonlar
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
# Bu kısımdada uygulamanın sürekli çalışmasını sağlıyoruz.
while 1:
    data = recordAudio()
    jarvis(data)

