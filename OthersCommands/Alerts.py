# https://the-internet.herokuapp.com/javascript_alerts
# Switch_To - alerts, frames, windows
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)


driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Confirm Alert
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[2]/button").click()
# time.sleep(2)
# confirm = driver.switch_to.alert
# confirm.accept()

# Prompt Alert
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
# time.sleep(2)
# prompt = driver.switch_to.alert
# time.sleep(2)
# prompt.send_keys("Heyy Gautam!")
# time.sleep(2)
# prompt.accept()
# time.sleep(2)
