
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("https://www.python.org/")

# Task 1
# driver.maximize_window()
# print(driver.get_window_size())

# Task 2
# print(driver.title)

# Task 3
# expectedurl = "https://www.python.org/"
# actualUrl = driver.current_url
# if actualUrl == expectedurl:
#     print("Matched URL")
# else: print("Not Matched")

# Task 4
# print(driver.page_source)

# Task 5
# keyword = "Python.org"
# actualTitle = driver.title
# if keyword in actualTitle:
#     print("Keyword Matched")
# else: print("Not Matched")