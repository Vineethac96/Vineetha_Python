import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class DemoSliders():
    def Frames(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)
        driver.get("http://www.londonfreelance.org/courses/frames/index.html")

        #driver.switch_to.frame("main") #as the web element in inside the frame and give the name/id of the frame
        #or
        frame_ele = driver.find_element(By.NAME,"main")
        driver.switch_to.frame(frame_ele)

        header = driver.find_element(By.CSS_SELECTOR, "body > h2").text
        print(header)

        driver.switch_to.default_content()
        driver.switch_to.parent_frame() #if there was any parent frame and we need to come back


        time.sleep(2)


ds = DemoSliders()
ds.Frames()