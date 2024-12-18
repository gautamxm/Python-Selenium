
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://www.facebook.com/")

driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("gautam@123")
time.sleep(3)