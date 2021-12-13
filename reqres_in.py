from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://reqres.in/')

janet=driver.find_element_by_xpath('//*[@id="console"]/div[1]/ul/li[2]')
janet.click

time.sleep(3)
driver.quit