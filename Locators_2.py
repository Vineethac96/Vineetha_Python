import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.amazon.com/")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Sell").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"Returns").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input.a-input-text.a-span12.auth-autofocus.auth-required-field").send_keys("vineethac96@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input.a-button-input").click()

driver.find_element(By.NAME,"password").send_keys("tesst@12335")

loginBtn = driver.find_element(By.CSS_SELECTOR,"input.a-button-input")
loginBtn.click()




time.sleep(5)
driver.quit()