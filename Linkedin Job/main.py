from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&f_WT=2&keywords=python%20developer"

chrome_driver_path = "V:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=LINKEDIN_URL)
driver.maximize_window()

sleep(2)

sign_in_button = driver.find_element_by_class_name("nav__button-secondary")
sign_in_button.click()

email = driver.find_element_by_name("session_key")
email.send_keys("YOUR EMAIL")

password = driver.find_element_by_name("session_password")
password.send_keys("YOUR PASS")

sign_in_button = driver.find_element_by_class_name("btn__primary--large")
sign_in_button.click()


def save():
    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()


save()
jobs = driver.find_elements_by_class_name("job-card-container")

for job in jobs:
    job.click()
    sleep(3)
    save()
