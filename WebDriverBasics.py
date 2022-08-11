import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\sumanth\\Documents\\drivers\\chromedriver.exe")
print(driver.title)
driver.implicitly_wait(5)
driver.get("http://www.google.com")
driver.find_element(By.NAME, 'q').send_keys("naveen")
optionsList = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(optionsList))

for ele in optionsList:
    print(ele.text)
    if ele.text == "Naveen Polishetty":
        ele.click()
        break
time.sleep(3)
driver.quit()


