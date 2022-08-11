import time

import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.testyou.in/SignUp.aspx')
driver.maximize_window()

path = "Login1.xlsx"

rows = XLUtils.getRowCount(path,'Sheet1') #as by default sheet 1 will be active/opened
col = XLUtils.getColCount(path,'Sheet1')

'''to print all values'''
# for r in range(2,rows+1):
#     for c in range(1,col+1):
#        print(XLUtils.readData(path,'Sheet1',r,c))

for r in range(2,rows+1):
       username = XLUtils.readData(path,'Sheet1',r,1) #here we have hardcoded column no
       password = XLUtils.readData(path,'Sheet1', r, 2) #here we have hardcoded column no

       driver.find_element(By.LINK_TEXT,'Login')
       driver.find_element(By.ID,'ctl00_indexLogin2_txtUserLogin').send_keys(username)
       driver.find_element(By.ID,'ctl00_indexLogin2_txtPassword').send_keys(password)
       driver.find_element(By.ID,'ctl00_indexLogin2_lnkbtnSiginIn').click()
       driver.implicitly_wait(5)
       time.sleep(2)
       if driver.title == "Student Dashboard | Test Maker - TestYou":
           XLUtils.writeData(path,'Sheet1',r,3,'Pass')
       else:
           XLUtils.writeData(path,'Sheet1',r,3,'Fail')

       #driver.find_element(By.LINK_TEXT,'Home').click()

