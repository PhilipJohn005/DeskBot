import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.pause_threshold =2.0       
recognizer.phrase_threshold = 2.0    
recognizer.energy_threshold = 200        
recognizer.dynamic_energy_threshold = True

def listen_once():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.8)
        audio = recognizer.listen(source, phrase_time_limit=None)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except Exception as e:
        print("Recognition error:", e)
        return ""
