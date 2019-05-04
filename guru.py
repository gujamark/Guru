
from imports import *


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("I'm ready sir!")


# task
def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("You said: " + task)

    except sr.UnknownValueError:
        print("I didn't understand")
        task = command()

    return task


def make_something(task):
    global r

    # greetings
    if task in greetings:
        random_greeting = random.choice(greetings)
        talk(random_greeting)
        print(random_greeting)

    # how_is_guru
    elif task in question:
        random_responses = random.choice(responses)
        talk(random_responses)
        print(random_responses)

    # makers
    elif task in var1:
        random_answer = random.choice(var2)
        talk(random_answer)
        print(random_answer)

    # time
    elif task in var3:
        talk(datetime.datetime.now())
        print(datetime.datetime.now())

    # name
    elif task in var4:
        talk('I am GURU')
        with open("guru.txt", "r") as f:
            robot = f.read()
            print(robot)



    # where_is_guru?
    elif task in var5:
        g = geocoder.ip("me")
        city = g.geojson["features"][0]["properties"]["city"]
        print(city)

    # open website
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
            session = HTMLSession()
            r = session.get(url)
            r.html.render(wait=3)
            soup = BeautifulSoup(r.html.html, "html.parser")
            h3 = soup.find("h3")
            a_link = h3.find_parent("a")["href"]
            driver = webdriver.Chrome()
            driver.get(a_link)
            talk("I opened sir")

    # joke
    elif task in cmd2:
        random_joke = random.choice(jokes)
        talk(random_joke)
        print(random_joke)

    # youtube
    elif task in cmd3:
        talk('What do you want to see?')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            search = r.recognize_google(audio).lower()
            url = 'https://www.youtube.com/results?search_query=' + search
            driver = webdriver.Chrome()
            driver.get(url)
            driver.find_element_by_id("video-title").click()
            talk("I opened sir")

    # spotify
    elif task in cmd8:
        talk("Enter Your Email: ")
        email = input("Enter Your Email: ")
        talk("Enter Your Password: ")
        password = input("Enter Your Password: ")
        talk('What do you want to listen?')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                print("Speak")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                search = r.recognize_google(audio).lower()
                driver = webdriver.Chrome()
                driver.get("https://accounts.spotify.com/en/login/")
                driver.find_element_by_id("login-username").send_keys(email)
                driver.find_element_by_id("login-password").send_keys(password)
                driver.find_element_by_id("login-button").click()
                time.sleep(2)
                driver.get(f"https://open.spotify.com/search/results/{search}")
                driver.find_element_by_class_name("spoticon-track-16").click()
                talk("I opened sir")
            except selenium.common.exceptions.NoSuchElementException:
                print("Wrong Email/Password")
                talk("Wrong Email or Password")
            except UnknownValueError:
                talk("I didn't Understand")
                print("I didn't Understand")

    # color
    elif task in cmd4:
        random_color = random.choice(colrep)
        talk(random_color)
        print(random_color)

    # fav_color
    elif task in cmd5:
        favorite_color = random.choice(fav_color)
        talk(favorite_color)
        print(favorite_color)

    # bye_bye
    elif task in cmd6:
        answer = random.choice(repfr6)
        talk(answer)
        print(answer)
        sys.exit()

    # weather
    elif task in cmd7:
        session = HTMLSession()
        r = session.get("https://www.google.com/search?q=weather")
        r.html.render(wait=4)
        soup = BeautifulSoup(r.html.html, "html.parser")
        celsius = soup.find("span", attrs={"id": "wob_tm", "class": "wob_t"})
        talk(celsius.text + "°C")
        print(celsius.text + "°C")

    # send_via_gmail
    elif task == 'gmail':
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        talk('Enter your address sir')
        sender_email = input('Enter your address: ')
        talk('Enter receiver address sir')
        receiver_email = input('Enter receiver address: ').split(",")
        talk('Type your password and press enter')
        password = input("Type your password and press enter: ")
        r = sr.Recognizer()
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                with sr.Microphone() as source:
                    print("Speak ")
                    talk('tell me message sir')
                    r.pause_threshold = 1
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)
                    text = r.recognize_google(audio).lower()
                    print(text)

                    message = """\
                                Subject: Hi there

                                This message is sent from Python.
                                {}""".format(text)

                server.sendmail(sender_email, receiver_email, message)
                talk('Message sent sir')
                print("Message sent.")
        except SMTPAuthenticationError:
            print("Wrong Email/Password")
            talk("Wrong Email or Password")
        except UnknownValueError:
            talk("I didn't Understand")
            print("I didn't Understand")

    # btu_personal_scores
    elif task in btu_questions:
        print(get_scores())

    # fb
    elif task in cmd9:
        talk("Enter Your Email or Nickname: ")
        email = input("Enter Your Email/Nickname: ")
        talk("Enter Your Password: ")
        password = input("Enter Your Password: ")
        try:
            driver = webdriver.Chrome()
            driver.get('https://www.facebook.com/login')
            driver.find_element_by_id("email").send_keys(email)
            driver.find_element_by_id("pass").send_keys(password)
            driver.find_element_by_id("loginbutton").click()
            driver.find_element_by_id("u_0_d")
            talk("welcome to Facebook")
        except selenium.common.exceptions.NoSuchElementException:
            print("Wrong Email/Password")
            talk("Wrong Email or Password")

    # classroom
    elif task in cmd10:
        talk("Enter Your Email or ID Number")
        email = input("Enter Your Email/ID: ")
        talk("Enter Your Password: ")
        password = input("Enter Your Password: ")

        driver = webdriver.Chrome()
        driver.get('https://classroom.btu.edu.ge/ge/login')
        driver.find_element_by_id("username").send_keys(email)
        driver.find_element_by_id("password").send_keys(password)
        time.sleep(1)
        driver.find_element_by_class_name("btn").click()
        time.sleep(1)
        error = driver.find_element_by_class_name("alert-message")
        if not error:
            talk("welcome to Classroom")
        else:
            print("Wrong Email/Password")
            talk("Wrong Email or Password")


    # instagram
    elif task in cmd11:
        talk("Enter Your Nickname: ")
        email = input("Enter Your Nickname: ")
        talk("Enter Your Password: ")
        password = input("Enter Your Password: ")
        driver = webdriver.Chrome()
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        driver.find_element_by_name("username").send_keys(email)
        driver.find_element_by_name("password").send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        wrong_pass = driver.find_element_by_id("slfErrorAlert")
        if not wrong_pass:
            talk("welcome to Instagram")
        else:
            print("Wrong Nickname or Password")
            talk("Wrong Nickname or Password")

    # exchange_rates
    elif task in cmd12:
        print(get_exchanges())
    elif task in cmd13:
        os.system("start birthday_song.mp3")


    # when_guru_is_not_smart
    else:
        talk("I'm not as smart as you think, sorry")
        make_something(command())


while True:
    make_something(command())

# ქრისტე აღდგა და ჩვენ მაინც ამას ვწერდით!