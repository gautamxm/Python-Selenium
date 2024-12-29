

import time
import requests as request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("http://www.deadlinkcity.com/")

all = driver.find_elements(By.TAG_NAME,"a")
time.sleep(3)
print("Total No. of links: ",len(all))
count = 0
for link in all:
    url = link.get_attribute("href")
    try:
        res = request.head(url)
    except:
        None

    if res.status_code >= 400:
        count+=1

print("Broken Links: ",count)