import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
time.sleep(3)

source = driver.find_element(By.ID,"draggable")
target = driver.find_element(By.ID,"droppable")

act_chain = ActionChains(driver)
act_chain.drag_and_drop(source,target).perform()
'''to drap and drop without using above method-QA'''
#act_chain.click_and_hold(source).move_to_element(target).release().perform()
time.sleep(3)
