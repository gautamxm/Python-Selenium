
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://demoqa.com/automation-practice-form")
placeholder = driver.find_elements(By.TAG_NAME,"input")
print(len(placeholder))


