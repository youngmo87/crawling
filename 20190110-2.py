import timeit
import time
from selenium import webdriver
start = timeit.default_timer()

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--window-size=1920x1080')
options.add_argument("disable-gpu")    # or.   options.add_argument("--disable-gpu")
# UserAgent값을 바꿔줍시다!
# options.add_argument("user-agent=Mozilla/5.0 ...")

driver = webdriver.Chrome('C:\Workspace\ykim\chromedriver.exe', chrome_options=options)
# driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver', options=options)

driver.implicitly_wait(3)

driver.get("https://www.daum.net/")
time.sleep(2)

driver.save_screenshot("eee.png")   # or.  driver.get_screenshot_as_file('bbb.png')
driver.implicitly_wait(5)
driver.quit()
end = timeit.default_timer()
print("Elapsed time is", (end - start), "ms.")
