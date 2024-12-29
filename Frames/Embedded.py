
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH,"//div[@class='tabpane']/ul/li[2]/a").click()
time.sleep(3)
frame1 = driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
driver.switch_to.frame(frame1)
frame2 = driver.find_element(By.XPATH,"//html/body/section/div/div/iframe")
driver.switch_to.frame(frame2)
driver.find_element(By.TAG_NAME,"input").send_keys("gautam")
time.sleep(3)