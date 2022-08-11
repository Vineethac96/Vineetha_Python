import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.reddit.com/login")

# driver.find_element(By.ID, "loginUsername").send_keys("vin_eetha")
# time.sleep(2)
# driver.find_element(By.ID, "loginPassword").send_keys("BLESSy@20")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ".AnimatedForm__submitButton.m-full-width").click()
# time.sleep(4)

driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH, "//a[@class='BottomLink']").click()

