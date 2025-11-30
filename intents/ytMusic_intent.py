import yt_dlp
import vlc
import time
from rapidfuzz import fuzz

player = None

def handle_ytMusic(command: str):
    global player
    raw_song = command.replace("play", "").strip().lower()

    # add context improves accuracy
    search_query = f"{raw_song} official song lyrics audio"

    print("Searching exact match for:", raw_song)

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True,
        "default_search": "ytsearch5",  # fetch top 10 results
    }

    best_match = None
    best_score = -1

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        results = ydl.extract_info(search_query, download=False)

        for entry in results["entries"]:
            title = entry["title"].lower()

            # give a similarity score
            score = fuzz.token_set_ratio(raw_song, title)

            # bonus points for keywords
            keywords = ["lyrics", "audio", "official", "video"]
            for key in keywords:
                if key in title:
                    score += 5

            # avoid remixes/covers
            bad_words = ["remix", "lofi", "slowed", "reverb", "cover", "8d"]
            for bad in bad_words:
                if bad in title:
                    score -= 20

            if score > best_score:
                best_score = score
                best_match = entry

    if not best_match:
        print("No match found.")
        return

    url = best_match["url"]
    title = best_match["title"]

    print(f"Matched: {title}  (score={best_score})")

    # stop existing song
    if player:
        player.stop()

    # play new song
    player = vlc.MediaPlayer(url)
    player.play()

    time.sleep(1)
