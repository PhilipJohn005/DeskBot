import speech_recognition as sr
import pyautogui
import os
import time


recognizer= sr.Recognizer()

with sr.Microphone() as source:
    print("Listening.....")
    audio=recognizer.listen(source)
    command=recognizer.recognize_google(audio)
    print("You said: ",command)

    # Parse the command ( Intent Detection )
    
if "spotify" in command.lower():
    # play song
    pass
elif "chrome" in command.lower():
    # open chrome and search
    pass
elif "search" in command.lower():
    query=command.replace("search","").strip()
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    time.sleep(3)
    pyautogui.write("https://www.google.com/search?q="+query)
    pyautogui.press("enter")
    
elif "opera gx" in command.lower():
    # open opera gx
    pass

