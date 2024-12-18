
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://www.selenium.dev/")
links = driver.find_elements(By.CLASS_NAME,"nav-item")
links[3].click()
time.sleep(4)