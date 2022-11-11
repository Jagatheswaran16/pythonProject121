import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.lambdatest.com/selenium-playground/")
driver.find_element(By.LINK_TEXT, "Input Form Submit").click()


#driver.execute_script("window.scrollBy (0, 500)", "")
driver.find_element(By.ID, "inputZip").send_keys("123")
k=driver.find_element(By.XPATH, "//button[@type='submit']")
k.click()

driver.quit()

