
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://www.selenium.dev/documentation/")

driver.find_element(By.PARTIAL_LINK_TEXT,"WebDriver").click()
time.sleep(2)