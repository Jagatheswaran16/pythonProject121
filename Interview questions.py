import time

from select import select
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class amazon:
    def test(self):


        #driver = webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/chromedriver.exe')
        driver = webdriver.Edge(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/msedgedriver.exe')
        driver.maximize_window()



        driver.get("https://www.amazon.in/")

        driver.find_element(By.ID, "twotabsearchtextbox").send_keys('macbook pro')
        driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        p=driver.current_window_handle
        print(p)

        k = driver.find_element(By.XPATH, "//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_3']//div[@class='a-section a-spacing-none puis-padding-right-small s-title-instructions-style']//span[1]")
        k.click()
        l=driver.window_handles
        print(l)
        if l!=p:
            driver.switch_to.window(p)
            print("changed to parent window")


o=amazon()
o.test()


















