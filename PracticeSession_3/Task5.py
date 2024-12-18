
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://www.amazon.in/")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@role='searchbox']").send_keys("Laptops")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@type='submit']").click()
time.sleep(2)
