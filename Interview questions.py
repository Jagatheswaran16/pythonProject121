import time
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




driver =webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')

driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.yatra.com/")

driver.find_element(By.XPATH, "//a[@id='booking_engine_visa']").click()
par=driver.current_window_handle


child= driver.window_handles

for i in child:
    if i !=par:
        driver.switch_to.window(i)
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Dubai Visa").click()


driver.switch_to.window(par)
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit()









