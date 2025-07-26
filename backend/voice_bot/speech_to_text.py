# scripts/test_voice_bot.py
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak a welcome message
engine.say("Say something. I am listening...")
engine.runAndWait()

with sr.Microphone() as source:
    print("🎤 Listening...")
    audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)


try:
    # Convert speech to text
    text = recognizer.recognize_google(audio)
    print(f"🗣️ You said: {text}")
    engine.say(f"You said: {text}")
    engine.runAndWait()
except sr.UnknownValueError:
    print("❌ Could not understand audio")
    engine.say("Sorry, I could not understand that.")
    engine.runAndWait()
except sr.RequestError as e:
    print(f"⚠️ Could not request results; {e}")

import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"❌ Request error: {e}")
        return ""
