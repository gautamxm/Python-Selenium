import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)

expect = "Congratulations! You must have the proper credentials."
actual = driver.find_element(By.XPATH,"//*[@id='content']/div/p").text
if actual == expect:
    print("Pass")
else: print("Fail")

