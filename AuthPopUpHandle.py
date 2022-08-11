import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class DemoSliders():
    def AuthPopUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)
        driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
        time.sleep(2)


ds = DemoSliders()
ds.AuthPopUp()