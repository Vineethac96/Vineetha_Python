import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #giving ec as an alias name for expected conditions a sit is a big name

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')

'''wait'''
wait = WebDriverWait(driver,10)
#wait.until(ec.title_is("HubSpot Login")) #or
wait.until(ec.title_contains("Login"))
print(driver.title)
email_id = wait.until(ec.presence_of_element_located((By.ID,"username")))

email_id.send_keys("test@gmail.com")




