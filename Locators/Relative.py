import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.relative_locator import locate_with

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://automationbookstore.dev/")

# left = driver.find_element(locate_with(By.TAG_NAME,"h2").to_left_of({By.ID: "pid2_title"}))
# time.sleep(2)
# print(left.text)

# right = driver.find_element(locate_with(By.TAG_NAME,"h2").to_right_of({By.ID: "pid2_title"}))
# time.sleep(2)
# print(right.text)

# below = driver.find_element(locate_with(By.TAG_NAME,"h2").below({By.ID: "pid2_title"}))
# time.sleep(2)
# print(below.text)