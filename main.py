import asyncio
from stt import listen_once
from tts import speak
from intents.chrome_intent import handle_chrome
from intents.ytMusic_intent import handle_ytMusic
import subprocess
import atexit
import time


UNITY_EXE_PATH=r"E:\Storage\Projects\Game Dev\Unity\Deskbot\DeskbotRunning.exe"

unity_process=None

def start_overlay():
    global unity_process
    unity_process=subprocess.Popen(
        [UNITY_EXE_PATH],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def stop_overlay():
    if unity_process:
        unity_process.terminate()
        
        
atexit.register(stop_overlay)

async def bot_loop():
    await speak("Bot is now listening continuously")

    while True:
        command = listen_once()
        if not command:
            continue

        print("You said:", command)
        cmd = command.lower()

        # Stop the bot
        if "quit" in cmd or "stop bot" in cmd or "exit" in cmd:
            await speak("Goodbye")
            break

        if "play" in cmd:
            handle_ytMusic(command)
            await speak("Playing your song.")

        elif "search" in cmd:
            handle_chrome(command)
            await speak("Searching")

        else:
            await speak("I did not understand")

if __name__ == "__main__":
    start_overlay()
    time.sleep(1)
    asyncio.run(bot_loop())
