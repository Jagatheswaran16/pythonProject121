import time
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




driver =webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')

driver.maximize_window()

time.sleep(2)
driver.get("https://www.flipkart.com/")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Jaga@gmail.com")
driver.find_element(By.XPATH,"//input[@name='br_pwd']").send_keys("ABC1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()





