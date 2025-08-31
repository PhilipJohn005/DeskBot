import time
import pyautogui
import os


def handle_spotify(command:str):
    os.system("start spotify:")
    time.sleep(15)
    song_name=command.replace("play","").strip()
    
    pyautogui.hotkey("ctrl","l")
    time.sleep(2)
    
    pyautogui.write(song_name)
    pyautogui.press("enter")
    time.sleep(3)
    
    pyautogui.press("tab",presses=0,interval=0.1)
    pyautogui.press("enter")
    
    print(f"Playing the song {song_name}")
    