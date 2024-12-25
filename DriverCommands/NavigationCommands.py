
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

# driver.get("https://www.amazon.in/")
# driver.get("https://www.flipkart.com/")
#
# print(driver.title)
# driver.back()
#
# print(driver.title)
# driver.forward()
#
# print(driver.title)


# Getting attributes value
driver.get("https://www.flipkart.com/")
Search = driver.find_element(By.NAME,"q")

print(Search.get_attribute("placeholder"))
print(Search.get_attribute("type"))

