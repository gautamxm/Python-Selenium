
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("http://www.automationpractice.pl/index.php")
h1 = driver.find_element(By.TAG_NAME,"h1").text
print(h1) 