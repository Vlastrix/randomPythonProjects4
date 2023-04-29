import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

SIGN_IN_LINK = "https://www.linkedin.com/checkpoint/lg/sign-in-another-account"
EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASS"
counter = -1

with open("Empleados.csv") as data_file:
    data = pd.read_csv(data_file)
    links = data["ï»¿ProfileLinkedIn"]
    employees = data["Nombre"].to_list()
    employees_id = data["idEmpleado"].to_list()

chrome_driver_path = "V:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(SIGN_IN_LINK)

email = driver.find_element_by_name("session_key")
email.send_keys(EMAIL)

password = driver.find_element_by_name("session_password")
password.send_keys(PASSWORD)

sign_in_button = driver.find_element_by_class_name("btn__primary--large")
sign_in_button.click()

for link in links:
    counter += 1
    driver.get(link)
    current_employee = employees[counter]
    current_employee_id = employees_id[counter]
    try:
        company = driver.find_element_by_link_text("BairesDev")
        print(f"The employee '{current_employee}' with id '{current_employee_id}' has a BairesDev mention")
    except NoSuchElementException:
        print(f"The employee '{current_employee}' with id '{current_employee_id}' has *NO* BairesDev mention or does "
              f"not exists")

    sleep(2)

driver.quit()
