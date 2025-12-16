from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "jinewholic@gmail.com"
TWITTER_PASSWORD = "YOI18@nate"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

