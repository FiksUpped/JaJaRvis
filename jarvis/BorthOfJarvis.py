import speech_recognition as sr
import os
import sys
import webbrowser
import vlc
import time
from gtts import gTTS
from googletrans import Translator



from WebsiteJarvis import *


def main():

    cinema_pack = CinemaList()

    for i in cinema_pack:

        VoiceActing(i)





def VoiceActing(text):


    speach = gTTS(text=text, lang='ru')

    print(text)

    file = "to_voice.mp3"
    speach.save(file)
    voice_file_path = os.path.realpath(file)
    player = vlc.MediaPlayer(f"file:///{voice_file_path}")
    player.play()
    time.sleep(7)


def ParseWeather():


 current_weather_in_minsk = GetWeather()

 translator = Translator()

 for key, value in current_weather_in_minsk.items():


    if (len(value) == 4):


        russian_text = translator.translate(str(value[3]), dest='ru')

        value[3] = russian_text.text

    else:

        russian_text = translator.translate(str(value[3]), dest='ru')

        value[3] = russian_text.text

        russian_text_2 = translator.translate(str(value[4]), dest='ru')

        value[4] = russian_text_2.text

    full_weather = ' '.join(value)

    say_hello_babe(full_weather)






def IncomingCommand(command):

    print('test')





def LatestNews():

    news_dict = GetNews()

    for key, value in news_dict.items():

        VoiceActing(value[0])

main()