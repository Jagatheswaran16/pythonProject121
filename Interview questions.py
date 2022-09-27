import time
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




driver =webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')

driver.maximize_window()


driver.get("https://www.youtube.com/")

web=driver.title
print(web)

assert "YouTube"== web

k=driver.find_elements(By.TAG_NAME, "a")
for i in k:
    print (i)
time.sleep(1)
driver.save_screenshot("C:/Users/jagatheswaran.m/Desktop/Brunel Project/home.png")

driver.close()









