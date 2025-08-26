import subprocess

CHROME_PATH="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
PROFILE_DIR = "Default"


def handle_chrome(command:str):
    query=command.replace("search","").strip()
    #os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    #time.sleep(3)
    # pyautogui.write("https://www.google.com/search?q="+query)
    # pyautogui.press("enter")
    
    # If user said "youtube.com" or something ending with .com/.org/.net, treat it as a site
    if query.endswith((".com", ".org", ".net", ".in", ".io")):
        url=query 
    else:
         url=f"https://www.google.com/search?q={query}"
    
    subprocess.Popen([
        CHROME_PATH,
        f"--profile-directory={PROFILE_DIR}",
        url
    ])