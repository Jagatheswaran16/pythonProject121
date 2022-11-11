


from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
url=driver.find_element(By.XPATH, "//h1[@class='text-size-48 font-bold text-black text-center leading-none text-shadow md:w-full leading-height-70 mx-auto smtablet:text-size-30 smtablet:leading-height-42']").text
assert url=="Simple Form Demo"
s="Welcome to LambdaTest"
driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys(s)
driver.find_element(By.ID, "showInput").click()
v=driver.find_element(By.XPATH,"//p[@id='message']").text
print(v)
assert v == "Welcome to LambdaTest"
driver.quit()