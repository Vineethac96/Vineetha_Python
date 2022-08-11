import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #giving ec as an alias name for expected conditions a sit is a big name

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')

wait = WebDriverWait(driver,10)
signup_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT,"Sign up"))) #clcikable such as links
print(signup_link.text)
signup_link.click()

first_name = wait.until(ec.visibility_of_element_located((By.ID,"UIFormControl-2")))
first_name.send_keys("vineetha")

time.sleep(2)




