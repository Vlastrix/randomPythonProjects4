from selenium import webdriver

PYTHON_URL = "https://www.python.org/"

chrome_driver_path = "V:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(PYTHON_URL)

events = driver.find_elements_by_css_selector(".event-widget li a")
# events = {event.text for event in events}

events_dates = driver.find_elements_by_css_selector(".event-widget li time")
# events_dates = {date.text for date in events_dates}

events_dic = {}

for n in range(len(events_dates)):
    events_dic[n] = {
        "time": events_dates[n].text,
        "name": events[n].text,
    }

print(events_dic)

driver.quit()
