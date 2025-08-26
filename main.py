import speech_recognition as sr
import pyautogui
import os
import time
from intents.chrome_intent import handle_chrome
from intents.spotify_intent import handle_spotify

recognizer= sr.Recognizer()

with sr.Microphone() as source:
    print("Listening.....")
    audio=recognizer.listen(source)
    command=recognizer.recognize_google(audio)
    print("You said: ",command)

    # Parse the command ( Intent Detection )
    
if "play" in command.lower():
    # play song
    handle_spotify(command)
elif "search" in command.lower():
    handle_chrome(command)
elif "opera gx" in command.lower():
    # open opera gx
    pass

