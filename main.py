import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3



def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("Hello, what do you want?")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("You said: " + task)

    except sr.UnknownValueError:
        talk("I didn't understand")
        task = command()

    return task

def make_something(task):
    if 'open website' in task:
        talk('I will open')
        url = 'https://btu.edu.ge/'
        webbrowser.open(url)

    elif 'stop' in task:
        talk("Ok, no problem")
        sys.exit()

while True:
    make_something(command())