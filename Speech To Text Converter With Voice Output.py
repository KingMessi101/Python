import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak something..")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You Said:", text)
        return text
    except:
        print("Sorry I didn't Understand")
        return ""
def translate(text, lang):
    t = Translator()
    result = t.translate(text, dest=lang)
    print("translated:", result.text)
    return result.text

print("Choose language: hi(hindi), ta(Tamil), te(Telugu)")
lang = input("Enter code:")
text = listen()
if text:
    translated = translate(text, lang)
    speak(translated)