
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://demo.guru99.com/test/newtours/")
driver.find_element(By.NAME,"userName").send_keys("gautam123")
driver.find_element(By.NAME,"password").send_keys("Gautam@123")
driver.find_element(By.NAME,"submit").click()
