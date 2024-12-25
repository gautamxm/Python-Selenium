
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

logo = driver.find_element(By.CLASS_NAME,"header-logo")
print("Logo Status: ",logo.is_displayed())

searchBox = driver.find_element(By.ID,"small-searchterms")
print("SearchBox Status: ", searchBox.is_displayed())
print("SearchBox Status: ", searchBox.is_enabled())

maleBox = driver.find_element(By.XPATH,"//input[@id='gender-male']")
femaleBox = driver.find_element(By.XPATH,"//input[@id='gender-female']")

maleBox.click()
print("MaleBox Status: ",maleBox.is_selected())
print("FemaleBox Status: ",femaleBox.is_selected())

femaleBox.click()
print("MaleBox Status: ",maleBox.is_selected())
print("FemaleBox Status: ",femaleBox.is_selected())


