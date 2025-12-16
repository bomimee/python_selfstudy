from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = (
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # 브라우저 닫히지 않도록
# 필요하면 headless 등 옵션 추가: chrome_options.add_argument("--headless=new")

# Chrome 드라이버 생성 시 options= 로 전달
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)


time.sleep(5)
sign_in = driver.find_element(By.CSS_SELECTOR, value='.sign-in-modal button')
sign_in.click()

# 이메일 입력 필드 대기
email_field = driver.find_element(By.NAME, value="session_key")
password_field = driver.find_element(By.NAME, value="session_password")

# 값 입력 (민감정보 주의)
email_field.clear()
email_field.send_keys("jinewholic@gmail.com")

password_field.clear()
password_field.send_keys("Iamfine2020.")  # 실제 비밀번호 넣지 말고 안전하게 관리하세요
password_field.send_keys(Keys.ENTER)
   
time.sleep(5)

job_lists = driver.find_elements(By.CLASS_NAME, value='job-card-list')
job_lists[0].click()
time.sleep(5)

apply_button = driver.find_element(By.ID, value='jobs-apply-button-id')
apply_button.click()

next_btn = driver.find_element(By.CSS_SELECTOR, value='footer .display-flex .artdeco-button')
next_btn.click()

recheck_btns = driver.find_elements(By.CSS_SELECTOR, value='footer .display-flex .artdeco-button')
recheck_btns[1].click()
send_btns = driver.find_elements(By.CSS_SELECTOR, value='footer .display-flex .artdeco-button')
send_btns[1].click()


    # 로그인 후 프로필 로딩 또는 캡차/2FA 대기
    # 2FA/캡차가 있으면 여기서 수동으로 처리해야 합니다.
time.sleep(2)


