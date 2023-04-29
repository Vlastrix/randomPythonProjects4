from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_driver_path = "V:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=WIKIPEDIA_URL)

counter = driver.find_element_by_css_selector("#articlecount a")
# counter.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
all_portals.get_attribute("name")

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
