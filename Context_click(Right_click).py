import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(3)

'''right/context click'''
act_chain = ActionChains(driver)

ele = driver.find_element(By.CSS_SELECTOR,"span.context-menu-one")
act_chain.context_click(ele).perform()

'''to print all options and click on one of the option'''
rightclick_options = driver.find_elements(By.CSS_SELECTOR,".context-menu-icon")
for ele in rightclick_options:
    print(ele.text)
    if ele.text == "Copy":
        ele.click()
        break


time.sleep(3)


