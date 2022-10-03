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
driver.get("https://www.amazon.com/")

driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Laptops")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()

k=driver.find_elements(By.TAG_NAME, "a")


for i in range (len(k)):
    if i== 59:
        k[i].click()

driver.find_element(By.ID,  "add-to-cart-button").click()

l=driver.find_element(By.XPATH, '//*[@id="sw-all-product-variations"]/ul/li[1]').text
print(l)

assert l== 'Model name: M1502IA-AS51'

driver.close()






