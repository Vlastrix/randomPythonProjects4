from selenium import webdriver
from time import sleep

TINDER_URL = "https://tinder.com/app/recs"

chrome_driver_path = "V:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(TINDER_URL)
driver.maximize_window()

while True:
    sleep(1.6)
    noup_button = driver.find_element_by_class_name("D(b) Expand")
    noup_button.click()


