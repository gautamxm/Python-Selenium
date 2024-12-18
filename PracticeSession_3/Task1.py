
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get(r"https://www.wikipedia.org/")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='searchInput']").send_keys("Automation Testing")
time.sleep(3)
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(2)