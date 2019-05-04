import requests
from bs4 import BeautifulSoup
import pyttsx3

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


def get_scores():
    talk("Enter Your Email or ID Number")
    username = input("Enter Your Email/ID Number: ")
    talk("Enter Your Password: ")
    password = input("Enter Your Password: ")
    payload = {
        "username" : username,
        "password" : password
    }

    with requests.Session() as session:
        connect = session.post("https://classroom.btu.edu.ge/ge/login/trylogin",data=payload)
        source = session.get("https://classroom.btu.edu.ge/ge/student/me/courses")
        soup = BeautifulSoup(source.content,"html.parser")
        courses = soup.find_all("tr")
        courses = courses[1:len(courses) - 1]
        scores = { }
        for course in courses:
            tds = course.find_all("td")
            scores[tds[2].text.replace("\t","").replace("\n","")] = tds[3].text.replace("\t","").replace("\n","")

    if scores == {}:
        return "Wrong Email/Password"
    else:
        return scores

