from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select






driver =webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")


def test_firstname():
    firstname = driver.find_element(By.XPATH, "//input[@type='text']")
    firstname.send_keys("jaga")
def test_skills():
    dropdown = Select(driver.find_element(By.XPATH, "//select[@id='Skills']"))
    dropdown.select_by_visible_text('c')
def test_Gend():
    gen=driver.find_element(By.XPATH, "//input[@value='Male'] ")
    gen.click()
def test_Hobb():
    driver.find_element(By.XPATH, "//input[@value='Cricket'] ").click()
    driver.find_element(By.XPATH, "//input[@value='Movies'] ").click()
    driver.find_element(By.XPATH, "//input[@value='Hockey'] ").click()
def test_Lang():
    driver.find_element(By.XPATH, "//*[@id='msdd']").click()
    driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[7]/div/multi-select/div[2]/ul/li[8]/a").click()

def test_year():
    yr=Select(driver.find_element(By.XPATH, "//select[@id='yearbox']"))
    yr.select_by_visible_text("2000")



test_firstname()