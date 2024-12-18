# CSS Selector
# X-Path
import time
from unittest import expectedFailure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

# driver.get("https://www.facebook.com/login/")

# By Tag ID
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Gautam")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("12345")
# time.sleep(2)

# By Tag Class
# driver.find_element(By.CSS_SELECTOR,"input._1kbt").send_keys("Gautam")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input._9npi").send_keys("12345")
# time.sleep(2)

# By Tag And Attribute
# driver.find_element(By.CSS_SELECTOR,"input[name=email]").send_keys("Gautam")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input[name=pass]").send_keys("12345")
# time.sleep(2)

# By Tag Class n Attribute
# driver.find_element(By.CSS_SELECTOR,"input._1kbt#email[name=email]").send_keys("Gautam")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input._9npi#pass[name=pass]").send_keys("12345")
# time.sleep(2)

# X-Path  - realtive //tagname[@attribute="value"]
driver.get("https://online.btes.co.in/login/index.php")

driver.find_element(By.XPATH,"//input[@id='username']").send_keys("gautam@123")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Gautam@123")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='loginbtn']").click()
time.sleep(5)
# actual = driver.find_element(By.XPATH,"//*[@id='action-menu-toggle-1']/span/span[1]").text
# expected = "Gautam Gautam"
# if actual == expected:
#     print("Test Passed")
# else: print("Test Failed")
driver.find_element(By.CLASS_NAME,"aalink").click()
time.sleep(2)

actual = driver.find_element(By.XPATH,"//*[@id='page-header']/div/div/div/div[1]/div[1]/div/div/h1").text
expected = "SDET with Python-AI for IT&R"
if actual == expected:
    print("Test Passed")
else: print("Test Failed")





