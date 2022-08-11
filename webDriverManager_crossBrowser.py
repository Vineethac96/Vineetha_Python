import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browserName = "Chrome"

if browserName == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().isntall())
else:
    print("please input correct browser name", +browserName)
    raise Exception("driver not found")

driver.implicitly_wait(5)
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.find_element(By.ID, 'ap_email').send_keys('vineethac96@gmail.com')
driver.find_element(By.ID,'continue').click()
driver.find_element(By.ID, 'ap_password').send_keys('vineethac96')
driver.find_element(By.ID,'signInSubmit').click()


time.sleep(3)
driver.quit()