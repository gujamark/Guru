import speech_recognition as sr
import sys, pyttsx3, random, datetime, smtplib, ssl,time, selenium.common, requests, geocoder, os
from smtplib import SMTPAuthenticationError
from btu_scores import get_scores
from selenium import webdriver
from questions import *
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from speech_recognition import UnknownValueError
from exchange_rate import get_exchanges
