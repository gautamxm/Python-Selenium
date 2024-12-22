
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("http://www.automationpractice.pl/index.php")
parent = driver.find_element(By.CSS_SELECTOR,"div.contact-link")
child = parent.find_element(By.XPATH,"//a[@title='Contact us']")
child.click()