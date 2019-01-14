import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'C:\workspace\ykim\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(drvPath)
UserId = "youngmozzang"
UserPw = "RLAdudah1!"

driver.get("https://www.daum.net")
time.sleep(2)

ifr = driver.find_element_by_id('loginForm')
driver.switch_to.frame(ifr)

id = driver.find_element_by_id('id')
id.send_keys(UserId)
pw = driver.find_element_by_id('inputPwd')
pw.send_keys(UserPw)
pw.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()