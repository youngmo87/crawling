import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Workspace\ykim\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver')  # mac or linux

driver.get("https://www.daum.net")
time.sleep(2)

ifr = driver.find_element_by_id('loginForm')
driver.switch_to.frame(ifr)


id = driver.find_element_by_id('id')
pw = driver.find_element_by_id('inputPwd')


inputElement = driver.find_element_by_name("q")
inputElement.send_keys(Keys.DELETE)

inputElement.submit()        # cf.  inputElement.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()
