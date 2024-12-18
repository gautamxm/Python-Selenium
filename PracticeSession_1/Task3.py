
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Edge(service = serviceObj)

driver.get("https://www.google.com")
time.sleep(2)
driver.find_element(By.NAME,"q").send_keys("Selenium")
time.sleep(2)
driver.find_element(By.NAME,"btnK").click()
time.sleep(2)