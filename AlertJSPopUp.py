import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoSliders():
    def AlertPopUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
        driver.find_element(By.NAME,"proceed").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept() #accept alert pop-up, click OK
        #alert.dismiss() #cancel pop-up
        #alert.send_keys("username") #if some data is needed to mentioned
        
        driver.switch_to.default_content() #when we need to come back to driver page



        time.sleep(3)

ds = DemoSliders()
ds.AlertPopUp()