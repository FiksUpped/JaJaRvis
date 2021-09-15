import speech_recognition as sr
import os
import sys
import webbrowser
import vlc
import time
from gtts import gTTS


def say_hello_babe(text):
    speach = gTTS(text=text, lang='en')
    file = "chech.mp3"
    speach.save(file)
    player = vlc.MediaPlayer("file:///C:/Python34/%s" % file)
    player.play()
    time.sleep(10)

say_hello_babe("Test")



