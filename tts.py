import asyncio
import edge_tts
import tempfile
import os
import vlc
import time

async def speak(text: str):
    
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp_path = tmp.name
    tmp.close()
    tts = edge_tts.Communicate(text, voice="en-IN-PrabhatNeural")
    await tts.save(tmp_path)

    player = vlc.MediaPlayer(tmp_path)
    player.play()
 
    time.sleep(0.4)

    while True:
        state = player.get_state()

        if state in (vlc.State.Ended, vlc.State.Stopped, vlc.State.Error):
            break

        time.sleep(0.1)

    player.stop()
    os.remove(tmp_path)
