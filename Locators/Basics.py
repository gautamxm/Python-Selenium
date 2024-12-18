import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get(r"http://www.automationpractice.pl/index.php")

# driver.find_element(By.ID,"search_query_top").send_keys("Tshirt")
# driver.find_element(By.NAME,"submit_search").click()
# driver.find_element(By.LINK_TEXT,"Faded Short Sleeve T-shirts").click()
# time.sleep(5)
# expectedTitle = "Faded Short Sleeve T-shirts - My Shop"
# actualTitle = driver.title
# if expectedTitle == actualTitle:
#     print("Test Passed")
# else: print("Test Failed")

# Printing names of category
# Category = driver.find_elements(By.CLASS_NAME,"sf-menu")
# for i in Category:
#     print(i.text)
# print(len(Category))

# No. of sliders
# slider = driver.find_elements(By.CLASS_NAME,"homeslider-container")   # List return
# print(len(slider))

# No. of images
# images = driver.find_elements(By.TAG_NAME,"img")
# print(len(images))

# No. of Links
# links = driver.find_elements(By.TAG_NAME,"a")
# print(len(links))

