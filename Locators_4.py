import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.amazon.com/")

TotalLinks = driver.find_elements(By.TAG_NAME,"a")
print(len(TotalLinks))

for ele in TotalLinks:
    Text = ele.text
    print(Text)
    print(ele.get_attribute("href"))

TotalImg = driver.find_elements(By.TAG_NAME,"img")
print(len(TotalImg))

for img in TotalImg:
    print(img.get_attribute("src"))

driver.find_element(By.LINK_TEXT,"Sell").click()

listLinks = driver.find_elements(By.TAG_NAME,'h1')
print(len(listLinks))

for ele in listLinks:
    print(ele.text)
