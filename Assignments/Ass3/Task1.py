
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

# Locating Name
driver.find_element(By.ID,"name").send_keys("Gautam")
time.sleep(2)

# Locating Gender Radio Button
driver.find_element(By.ID,"gender").click()
time.sleep(2)

# Locating DOB
driver.find_element(By.ID,"dob").send_keys("10/16/2002")
time.sleep(2)

# Locating CheckBoxes
driver.find_element(By.XPATH,"//*[@id='hobbies']").click()
driver.find_element(By.XPATH,"//*[@id='practiceForm']/div[7]/div/div/div[3]/input").click()
time.sleep(2)

# Locating States
state = Select(driver.find_element(By.ID,"state"))
state.select_by_visible_text("Haryana")
time.sleep(2)
