import time
# import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'C:\Workspace\ykim\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(drvPath)
UserId = "youngmo87"
UserPw = "2uppvw"

driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")
time.sleep(1)
driver.execute_script("document.getElementById('id').value='youngmo87';")
driver.execute_script("document.getElementById('pw').value='2uppvw';")

driver.find_element_by_class_name('btn_global').click()

# id = driver.find_element_by_id('id')

# for i in UserId:
#     time.sleep( random.randrange(1, 5) / 10 )
# id.send_keys(UserId)

# id.send_keys(Keys.TAB)
# time.sleep(1)
# pw = driver.find_element_by_id('pw')
# driver.find_element_by_id('pw').click()
# for i in UserPw:
#     time.sleep(random.randrange(1, 5) / 10)
# pw.send_keys(UserPw)



# time.sleep(0.5)
# pw.send_keys(Keys.CONTROL, 'a')
# time.sleep(1)
# pw.send_keys(Keys.DELETE)
# time.sleep(1)
# pw.send_keys(Keys.CONTROL, 'v')
# pw.send_keys(Keys.RETURN)

time.sleep(1)


time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit() # driver.close()