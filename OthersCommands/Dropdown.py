import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

# approach 1 - drive = webdriver
serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drpdwn = Select(driver.find_element(By.XPATH,"//*[@id='country']"))

# Select By VisibleText
# drpdwn.select_by_visible_text("India")
# time.sleep(3)

# Select By Value
# drpdwn.select_by_value("uk")
# time.sleep(3)

# Select By Index
# drpdwn.select_by_index(3)
# time.sleep(3)

# allOptions = drpdwn.options
# print(len(allOptions))
# for i in allOptions:
#     print(i.text)

