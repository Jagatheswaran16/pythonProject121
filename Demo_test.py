from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.lambdatest.com/selenium-playground/input-form-demo")


driver.find_element(By.XPATH, "//p[normalize-space()='Progress Bar & Sliders']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Drag & Drop Sliders']").click()
ele=driver.find_element(By.XPATH, "//input[@value='15']")
ActionChains(driver).drag_and_drop_by_offset(ele, 118, 0).perform()
k=driver.find_element(By.XPATH, "//output[@id='rangeSuccess']").get_attribute("value")
print(k)
assert k== "95"
