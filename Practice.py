import time


from select import select
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests





driver = webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')
#driver = webdriver.Edge(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/msedgedriver.exe')
driver.maximize_window()
driver.get("https://www.amazon.in")
driver.implicitly_wait(5)
k=driver.find_elements(By.TAG_NAME, "a")
l=len(k)
for i in range(l):
    u=driver.find_element(By.LINK_TEXT, i).text
    print(u)



for i in k:
    url=i.get_attribute('href')
    r=requests.head(url)
    if r.status_code!=200:
        print(url,r.status_code)