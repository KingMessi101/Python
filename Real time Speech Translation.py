import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Speak in English...")
            audio = r.listen(source)

        text = r.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None

    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def translate(text, lang):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=lang)
        return translated.text

    except Exception as e:
        print(f"Translation error: {e}")
        return None
        result = translator.translate(text, dest=lang)
        return result.text

languages = {
    "1": "hi",
    "2": "ta",
    "3": "te"
}

print("1. Hindi")
print("2. Tamil")
print("3. Telugu")

choice = input("Choose language: ")

text = listen()
translated = translate(text, languages[choice])

print("Translated:", translated)

speak(translated)