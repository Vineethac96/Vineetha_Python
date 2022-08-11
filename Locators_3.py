import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")

list = driver.find_element(By.CLASS_NAME,'nav-search-dropdown').text
print(list)
time.sleep(3)

driver.find_element(By.XPATH,"//img[@alt='Keyboards']").click()
driver.find_element(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']").click()


driver.find_element(By.CLASS_NAME,'icp-nav-flag').click()
time.sleep(2)




driver.quit()