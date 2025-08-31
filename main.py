import speech_recognition as sr
from intents.chrome_intent import handle_chrome
from intents.ytMusic_intent import handle_ytMusic
import asyncio
import edge_tts
import tempfile
import os
import pygame 

recognizer = sr.Recognizer()

async def speak(text: str):
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp_file.close()  # Close immediately so TTS can write

    # Generate TTS audio
    communicate = edge_tts.Communicate(text, voice="en-IN-PrabhatNeural")
    await communicate.save(tmp_file.name)

    # Play audio with pygame
    pygame.mixer.init()
    pygame.mixer.music.load(tmp_file.name)
    pygame.mixer.music.play()

    # 🔑 Wait until playback is done
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    # Stop and cleanup
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # Now safe to delete
    os.remove(tmp_file.name)

def main():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        # Speak "Listening" immediately
        asyncio.run(speak("Listening"))

        print("Speak now...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            asyncio.run(speak("The command you said is " + command))
        except sr.UnknownValueError:
            print("Could not understand audio")
            asyncio.run(speak("Sorry, I did not understand that."))
            return
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return

        # Intent handling
        if "play" in command.lower():
            #handle_spotify(command)
            handle_ytMusic(command)
        elif "search" in command.lower():
            handle_chrome(command)
        elif "opera gx" in command.lower():
            asyncio.run(speak("Opening Opera GX"))


if __name__ == "__main__":
    main()
