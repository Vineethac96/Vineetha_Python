import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options_headless = webdriver.ChromeOptions()
#options_headless.headless = True
'''or'''
options_headless.add_argument("--headless")
'''to run in incognito'''
#options_headless.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options_headless)
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
print(driver.title)