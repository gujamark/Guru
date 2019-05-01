import speech_recognition as sr
import sys
import webbrowser
import pyttsx3
import random
import datetime
import smtplib, ssl



greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['how are you', 'ow are you doing']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I was created by Zhana right in her computer.', ' Zhana', 'Some girl whom i never got to know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
cmd1 = ['open website', 'open google']
cmd2 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.',
         'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.',
         'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd3 = ['exit', 'close', 'goodbye', 'nothing']
cmd4 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd5 = ['what is you favourite colour', 'what is your favourite colour']
cmd6 = ['thank you']

repfr6 = ['youre welcome', 'glad i could help you']
fav_color = ['blue','pink','green','white']





def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("I'm ready sir!")
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
    global r

    if task in greetings:
            random_greeting = random.choice(greetings)
            talk(random_greeting)
            print(random_greeting)

    elif task in question:
        random_responses = random.choice(responses)
        talk(random_responses)
        print(random_responses)

    elif task in var1:
        random_answer=random.choice(var2)
        talk(random_answer)
        print(random_answer)

    elif task in var3:
        talk(datetime.datetime.now())
        print(datetime.datetime.now())

    elif task in var4:
        talk('I am GURU')

    elif task in cmd1:
        talk('Which web do you want?')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            search = r.recognize_google(audio).lower()
            url = 'https://www.google.com/search?q=' + search
            webbrowser.open(url)
            talk("I opened sir")

    elif task in cmd2:
        random_joke = random.choice(jokes)
        talk(random_joke)
        print(random_joke)

    elif task in cmd3:
        talk('see you later')
        print('see you later')
        sys.exit()

    elif task in cmd4:
        random_color = random.choice(colrep)
        talk(random_color)
        print(random_color)

    elif task in cmd5:
        favorite_color = random.choice(fav_color)
        talk(favorite_color)
        print(favorite_color)

    elif task in cmd6:
        answer = random.choice(repfr6)
        talk(answer)
        print(answer)
        sys.exit()

    elif task == 'gmail':
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        talk('Enter your address sir')
        sender_email = input('Enter your address: ')
        talk('Enter receiver address sir')
        receiver_email = input('Enter receiver address: ')
        talk('Type your password and press enter')
        password = input("Type your password and press enter: ")
        talk('tell me message sir')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak ")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            text = r.recognize_google(audio).lower()
            print(text)

        message = """\
        Subject: Hi there

        This message is sent from Python.
        {}""" .format(text)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            talk('Message sent sir')
            print("Message sent.")

    else:
        talk("I'm not as smart as you think, sorry")
        make_something(command())


while True:
    make_something(command())



