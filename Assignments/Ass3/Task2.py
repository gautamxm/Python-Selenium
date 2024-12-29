
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.maximize_window()
driver.get("https://www.amazon.com/")

# Implicitly Wait
driver.implicitly_wait(5)
driver.find_element(By.ID,"nav-search-keywords").send_keys("Laptops")
driver.find_element(By.XPATH,"//input[@value='Go']").click()

# Explicitly Wait
mywait = WebDriverWait(driver,6)
searchBox = mywait.until(EC.presence_of_element_located((By.NAME,"q")))
searchBox.send_keys("Laptops")
mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@value='Go']"))).click() 