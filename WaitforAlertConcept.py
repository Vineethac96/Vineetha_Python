import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #giving ec as an alias name for expected conditions a sit is a big name

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

'''wait for alert- no need to swtich to alert while using this webdriverwait'''
driver.find_element(By.NAME,"proceed").click()
wait = WebDriverWait(driver,10)
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()




