import asyncio
from stt import listen_once
from tts import speak
from intents.chrome_intent import handle_chrome
from intents.ytMusic_intent import handle_ytMusic

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
    asyncio.run(bot_loop())
