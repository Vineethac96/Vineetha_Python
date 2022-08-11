import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#timeout = 10
#dynamic wait
#global wait
#implicit wait will be applied for all web elements
#find element, find elements
#only for web elements
#not for non -web elements like title, alerts,url
driver.get('https://app.hubspot.com/login')
print(driver.title) # this is a non-web element , therefore 10 sec impliict wait wont be applied to it and it may give wrong title like "chceking browser"

driver.implicitly_wait(2) # we can override this wait and this becomes global now

driver.find_element(By.ID,"username").send_keys("test@123")
driver.find_element(By.ID,"password").send_keys("ftregjj")

driver.implicitly_wait() #nullify of implicit wait (defualt value is 0)
