
import time
from unittest import expectedFailure

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
# serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service = serviceObj)
#
# driver.get("https://www.facebook.com/login/")

# X-Path with and
# driver.find_element(By.XPATH,"//input[@name='email' and @id='email']").send_keys("gautamxm")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='pass' and @id='pass']").send_keys("Gautam@123")
# time.sleep(2)

# X-Path with or
# driver.find_element(By.XPATH,"//input[@name='email' or @id='gautam']").send_keys("gautamxm")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@name='gautam' or @id='pass']").send_keys("Gautam@123")
# time.sleep(2)

# X-Path with contains()
# driver.find_element(By.XPATH,"//input[contains(@id,'email')]").send_keys("gautamxm")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[contains(@id,'pass')]").send_keys("Gautam@123")
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[text()='Log in']").click()
# time.sleep(2)

# X-Path with start-with()
# driver.find_element(By.XPATH,"//input[starts-with(@id,'em')]").send_keys("gautamxm")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[starts-with(@id,'pa')]").send_keys("Gautam@123")
# time.sleep(2)

# X-Path with axes
# driver.get("https://money.rediff.com/gainers/bse")

# Child
# child = driver.find_elements(By.XPATH,"//td[text()='62.72']/parent::tr/child::td")
# print(len(child))

# Parent
# Parent = driver.find_elements(By.XPATH,"//td[text()='62.72']/parent::tr")
# print(len(Parent))

# Following
# following = driver.find_elements(By.XPATH,"//td[text()='62.72']/parent::tr/following::tr")
# print(len(following))

# Preceding
# preceding = driver.find_elements(By.XPATH,"//td[text()='62.72']/parent::tr/preceding::tr")
# print(len(preceding))

# Following-Sibling
# follSib = driver.find_elements(By.XPATH,"//td[text()='62.72']/following-sibling::td")
# print(len(follSib))

# Preceding-Sibling
# precSib = driver.find_elements(By.XPATH,"//td[text()='62.72']/preceding-sibling::td")
# print(len(precSib))

