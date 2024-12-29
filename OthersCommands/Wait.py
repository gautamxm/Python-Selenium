import time

# Implicitly wait
# Explicitly wait
# Fluent wait

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.implicitly_wait(5)
# username = driver.find_element(By.NAME,"username")
# username.send_keys("Admin")
#
# password = driver.find_element(By.NAME,"password")
# password.send_keys("admin123")
#
# driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()

driver.get("https://www.google.com/")

mywait = WebDriverWait(driver,6,poll_frequency=2,ignored_exceptions=[NoSuchElementException ])
searchBox = mywait.until(EC.presence_of_element_located((By.NAME,"q")))
searchBox.send_keys("selenium")
mywait.until(EC.presence_of_element_located((By.NAME,"btnK"))).click()
time.sleep(4)