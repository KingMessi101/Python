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
        print(" Speak in English...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text

    except:
        print("Sorry, could not understand.")
        return ""

def translate(text, lang):
    t = Translator()
    result = t.translate(text, dest=lang)
    print("Translation:", result.text)

print("Choose language:")
print("1. Hindi")
print("2. Tamil")
print("3. Telugu")

choice = input("Enter 1/2/3: ")

languages = {
    "1": "hi",
    "2": "ta",
    "3": "te"
}

target = languages.get(choice, "hi")
target = languages.get(choice, "hi")

text = listen()

if text:
    translated = translate(text, target)
    speak(translated)

print("Done!")