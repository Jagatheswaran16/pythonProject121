import time
import requests

from select import select
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')
#driver = webdriver.Edge(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/msedgedriver.exe')
driver.maximize_window()

driver.implicitly_wait(4)
driver.get("https://google.com")
k=driver.find_elements(By.TAG_NAME, 'a')
for j in k:
    l=j.get_attribute('href')
    a=requests.get(l)

    if a.status_code==200:
        print("sucess", a)

    else:
        print("not sucess")
