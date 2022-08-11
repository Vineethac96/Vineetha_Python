import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
'''we need Action class to perform mouse hover actions
and whatever method we use from action class, we should use *perform* method along with it'''


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")
time.sleep(3)

'''move to element-mouse hovering action'''
login_ele = driver.find_element(By.CLASS_NAME,"nav_item_name")
act_chains = ActionChains(driver) #we have to pass driver in actionchain class, wheras for select we pass WebElement
act_chains.move_to_element(login_ele).perform()
login_ele_1 = driver.find_element(By.LINK_TEXT,"Events")
login_ele_1.click()
'''if multiple hover options are there, repeat the same action again by finding the element and applying move to elememt on it'''

time.sleep(3)

