import time
from selenium import webdriver
from selenium.webdriver import ActionChains,DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

'''IMPORTANT-QA'''

'''1'''
op = Options()
op.add_argument("--allow-running-insecure-content")
op.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)

'''2'''
dc = DesiredCapabilities().CHROME.copy()
dc['acceptInsecureCerts'] = True
driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=dc)

'''3'''
opt = Options()
opt.set_capability('acceptInsecureCerts',True)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)


driver.implicitly_wait(10)
driver.get("https://expired.badssl.com/")
print(driver.find_element(By.TAG_NAME,"h1").text)

time.sleep(3)