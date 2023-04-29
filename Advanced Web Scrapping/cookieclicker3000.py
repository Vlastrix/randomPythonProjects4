from selenium import webdriver
from selenium.webdriver.common.keys import Keys

COOKIE_URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "V:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(COOKIE_URL)

cookie = driver.find_element("#cookie")
while True:
    cookie.click()
