
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Task 1
# button = driver.find_element(By.XPATH,"//input[@value='Submit']")
# print(button.is_enabled())

# Task 2
# bike = driver.find_element(By.XPATH,"//input[@id='vehicle1']")
# bike.click()
# car = driver.find_element(By.XPATH,"//input[@id='vehicle2']")
# car.click()
# print(bike.is_selected())
# print(car.is_selected())

# Task 3
# logo = driver.find_element(By.CSS_SELECTOR,"a#w3-logo")
# print(logo.is_displayed())

# Task 4
# expectedHeading = "HTML Forms"
# actualHeading = driver.find_element(By.TAG_NAME, "h1").text
# if actualHeading == expectedHeading:
#     print("Heading Matched")
# else: print("Not Matched")