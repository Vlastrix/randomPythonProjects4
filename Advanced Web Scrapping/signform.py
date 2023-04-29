from selenium import webdriver
from selenium.webdriver.common.keys import Keys

FORM_URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver_path = "V:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(FORM_URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Vladi")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Bochkov")

email = driver.find_element_by_name("email")
email.send_keys("YOUR EMAIL")

button = driver.find_element_by_class_name("btn")
button.click()

