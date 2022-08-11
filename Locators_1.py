import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")

login_username = driver.find_element(By.ID,"username")
login_password = driver.find_element(By.ID,"password")
login_btn = driver.find_element(By.ID,"loginBtn")


'''if name is present in HTML, use name to find element: 
login_password = driver.find_element(By.NAME,"password")'''

login_username.send_keys("vineethac96@gmail.com")
login_password.send_keys("paswhksjdkjk")
login_btn.click()
time.sleep(5)
driver.quit()