
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

# approach 1 - drive = webdriver
serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
time.sleep(2)
driver.find_element(By.ID,"name").send_keys("Gautam")
time.sleep(2)
frame1 = driver.find_element(By.ID,"frm1")
frame2 = driver.find_element(By.ID,"frm2")

driver.switch_to.frame(frame1)
drpdwn = Select(driver.find_element(By.ID,"course"))
drpdwn.select_by_visible_text("Java")
time.sleep(4)

driver.switch_to.default_content()

driver.switch_to.frame(frame2)
driver.find_element(By.ID,"firstName").send_keys("Gautam")
time.sleep(2)
driver.find_element(By.ID,"lastName").send_keys("Rajput")
time.sleep(2)
driver.find_element(By.ID,"malerb").click()
time.sleep(2)