
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://www.python.org/")

print(driver.title)

print(driver.current_url)

print(driver.page_source)
