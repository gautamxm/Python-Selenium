import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.devtools.v129.fed_cm import click_dialog_button
from selenium.webdriver.support.select import Select

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Select One Checkbox
# driver.find_element(By.XPATH,"//*[@id='monday']").click()
# time.sleep(2)

# Select All Checkbox
all = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
time.sleep(2)

# for i in all:
#     i.click()
# time.sleep(2)

# for i in range(len(all)):
#     all[i].click()
# time.sleep(2)

# To select specific last two
for i in range(len(all)-2,len(all)):
    all[i].click()

time.sleep(2)

# to unselect
for i in all:
    if i.is_selected():
        i.click()

time.sleep(2)