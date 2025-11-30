import subprocess

CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
PROFILE = "Default"

def handle_chrome(command: str):
    query = command.replace("search", "").strip()

    if query.endswith((".com", ".in", ".org", ".io", ".net")):
        url = "https://" + query
    else:
        url = f"https://www.google.com/search?q={query}"

    subprocess.Popen([
        CHROME_PATH,
        f"--profile-directory={PROFILE}",
        url
    ])
