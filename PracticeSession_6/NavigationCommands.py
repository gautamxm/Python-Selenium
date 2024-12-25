import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("https://www.selenium.dev/")

# Task 1
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.back()
# time.sleep(2)

# Task 2
# time.sleep(3)
# driver.refresh()
# time.sleep(3)

# Task 3
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)

# Task 4
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.back()
# time.sleep(2)
# driver.forward()
# expectedUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# actualUrl = driver.current_url
# if actualUrl == expectedUrl:
#     print("Validate Pass")
# else: print("Not Validate")

# Task 5
# driver.find_element(By.LINK_TEXT,"Downloads").click()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")