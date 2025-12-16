from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
# driver.get("https://www.python.org/")
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
# driver.find_element(By.XPATH, value='//*[@id="accordion-panel-title--443"]/span/span')


# event_times = driver.find_elements(By.CSS_SELECTOR, value='.menu li time')
# event_titles = driver.find_elements(By.CSS_SELECTOR, value='.menu li a')
# events = {}

# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_titles[n].text
#     }

# print(events)
# get_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[1]/a').text


# all_portals = driver.find_element_by_link_text("All protals")
# all_portals.click()
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# driver.quit()

first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
button = driver.find_element(By.TAG_NAME, value='button')
first_name.send_keys("Bomi")
last_name.send_keys("Kim")
email.send_keys("bomi.kim@sobetec.com")
button.click()
