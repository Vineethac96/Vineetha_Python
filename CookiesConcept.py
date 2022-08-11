import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
print(driver.get_cookies())

'''to add cookies in the form of dict'''
driver.add_cookie({"name":"vineetha","domain":"reddit.com","value":"python"})
print(driver.get_cookies())

'''delete cookies'''
driver.delete_cookie("vineetha")
print(driver.get_cookies())


