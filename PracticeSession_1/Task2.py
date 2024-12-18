
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
username = driver.find_element(By.NAME,"username")
username.send_keys("Admin")
time.sleep(2)
password = driver.find_element(By.NAME,"password")
password.send_keys("admin123")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
time.sleep(2)