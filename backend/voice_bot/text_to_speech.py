import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Optional: speed of speech
    engine.setProperty('volume', 1.0)  # Optional: volume (0.0 to 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can try voices[1] if [0] is silent

    engine.say(text)
    engine.runAndWait()

import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

