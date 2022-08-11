import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://amazon.com")
driver.get_screenshot_as_file("Screenshot1.png")
driver.get_screenshot_as_png()

