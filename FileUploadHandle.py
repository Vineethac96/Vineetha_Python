import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class DemoSliders():
    def AuthPopUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)
        driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

        # # type="file" shld be there while inspecting
        driver.find_element(By.NAME, 'upfile').send_keys('C:/Users/sumanth/Demo.txt')

        driver.find_element(By.XPATH, "//input[@type='submit']").click()


        time.sleep(2)


ds = DemoSliders()
ds.AuthPopUp()