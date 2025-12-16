from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

FB_EMAIL = "jinewholic@gmail.com"
FB_PASSWORD = ""


driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="u-1445010807"]/div/div[1]/div/div/div/main/div/div[2]/div[1]/div[3]/div/div/button[2]/div[2]/div[2]/div')

sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]  #Selenium이 현재 열려 있는 모든 창(탭)의 ID 목록을 리스트로 반환-> 저장
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.Enter)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)

    try:
        print("called")
        like_button = driver.file_detector(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_elemnt(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        
        except NoSuchElementException:
            sleep(2)

driver.quit()
