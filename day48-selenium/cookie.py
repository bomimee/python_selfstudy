from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'http://orteil.dashnet.org/experiments/cookie/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
cookie = driver.find_element(By.ID, value='cookie')

timeout = time.time() + 5

while True:
    cookie.click()

if time.time() > timeout:
    money = driver.find_element(By.ID, value='money')
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    for item in reversed(items):  # 가장 비싼 것부터 시도
            try:
                price = int(item.text.split("-")[-1].strip().replace(",", ""))
                if money >= price:
                    item.click()
                    break
            except:
                pass
    timeout = time.time() + 5


