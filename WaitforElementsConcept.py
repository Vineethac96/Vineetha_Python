import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #giving ec as an alias name for expected conditions a sit is a big name

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.freshworks.com/')

wait = WebDriverWait(driver,10)
footer_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,"ul.footer-nav li")))
print(len(footer_links))

for ele in footer_links:
    print(ele.text)
