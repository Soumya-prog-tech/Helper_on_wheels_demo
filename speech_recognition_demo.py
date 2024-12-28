import speech_recognition as sr
import pyttsx3

def speak(text) :
    engine = pyttsx3.init()
    engine.say(text)

    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout = 15)
            command = recognizer.recognize_google(audio)   # I am using Google's Speech Recognition API
            print(f"Command recognized : {command}")
            return command.lower()
        except sr.UnknownValueError:

            print(
                "Make sure you are speaking clearly and try again"
            )
            speak("Sorry, I didn't get that")
            return None
        except sr.WaitTimeoutError:
            print("No command heard")
            speak("No command heard")
            return None

command = listen_command()
if command:
    speak(command)