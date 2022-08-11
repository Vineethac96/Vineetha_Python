import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
# driver.get('https://www.amazon.in/')
#
# '''using javascript'''
# best_sellers = driver.find_element(By.LINK_TEXT,"Best Sellers") #to click on best sellers
# driver.execute_script("arguments[0].click();", best_sellers)
#
# title = driver.execute_script("return document.title;") #to get title
# print(title)
#
# driver.execute_script("history.go(0);") #to referesh page
#
# #driver.execute_script("alert('vineetha');") #alerts
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)

driver.get('https://classic.crmpro.com/')
frgt_pswd = driver.find_element(By.LINK_TEXT,"Forgot Password?")
driver.execute_script("arguments[0].scrollIntoView(true);", frgt_pswd)
time.sleep(3)