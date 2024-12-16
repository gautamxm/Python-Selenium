# Open Browser
# Pass Url  -- driver.get()
# Capture the text box
# send values "Selenium"
# Validate

# Service Class
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# approach 1 - drive = webdriver
serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

# approach 2 - this will open the browser
# driver = webdriver.Chrome()
time.sleep(2)
# open the url to the browser
driver.get("https://www.google.com")
time.sleep(2)
searchBox = driver.find_element(By.NAME,"q")
searchBox.send_keys("Selenium")
time.sleep(2)
driver.find_element(By.NAME,"btnK").click()
time.sleep(2)

# Validation
expTitle = "Selenium - Google Search"
actTitle = driver.title
if expTitle == actTitle:
    print("Test Passed")
else: print("Test Failed")