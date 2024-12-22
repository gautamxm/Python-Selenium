import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://www.facebook.com/login/")

beforemail = driver.find_elements(By.XPATH,"//input[@name='email']/parent::div/preceding::*")
aftermail = driver.find_elements(By.XPATH,"//input[@name='email']/parent::div/following::*")
time.sleep(5)

print(len(beforemail))   # 71
print(len(aftermail))    # 142

# for i in beforemail:
#     print(i.tag_name,end=",")
#
# for i in aftermail:
#     print(i.tag_name,end=",")


