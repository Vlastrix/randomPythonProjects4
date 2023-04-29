from selenium import webdriver

# Closes all
# driver.quit()
# Closes a single tab
# driver.close()

PRODUCT_URL = "https://www.amazon.com/dp/B087H24T6G/ref=cm_sw_r_tw_dp_R5239MXN844T34GG4FF6?_encoding=UTF8&psc=1"
PYTHON_URL = "https://www.python.org/"

chrome_driver_path = "V:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=PYTHON_URL)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_form = driver.find_element_by_name("q")
# print(search_form)

# print(search_form.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# You can give multiple classes no a single tag in html
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

bug_report = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_report.text)

driver.quit()