import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

'''represting in terms of class and methods'''

class DemoFrames():
    def Frames(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://demoqa.com/slider/")
        driver.maximize_window()
        slider = driver.find_element(By.XPATH,"//input[@type='range']")
        act_chain = ActionChains(driver)
        act_chain.drag_and_drop_by_offset(slider,66,0).perform() #way-1
        #act_chain.click_and_hold(slider).pause(1).move_by_offset(67,0).release().perform() #way-2

        time.sleep(3)


'''Creating an object of class'''

ds = DemoFrames()
ds.Frames()
