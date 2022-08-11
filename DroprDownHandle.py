import time
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.orangehrm.com/hris-hr-software-demo/")

#option_country = driver.find_element(By.ID,"Form_submitForm_Country")
#sel = Select(option_country)

#sel.select_by_value("Angola")
#sel.select_by_index(6)
#sel.select_by_visible_text("Angola")

'''to print without using select'''
dr = driver.find_elements(By.ID,"Form_submitForm_Country")
for i in dr:
    print(i.text)
'''but can't select using by.ID'''


'''usingxpath'''
#dr1 = driver.find_elements(By.XPATH,"//select[@id='Form_submitForm_Country']/option")
#print(len(dr1))

#for n in dr1:
   # print(n.text)
    #if (n.text == "Aruba"):
       # n.click()
        #break

'''To print all options using Select..Imp'''

#ListCountry = sel.options

'''for ii in ListCountry:
    print(ii.text)
    if (ii.text == "Zambia"):    #Select Zambia from the dropdown 
        ii.click()
        break'''






'''generic method to select using select'''

def select_values(option,value):
     ele = Select(option)
     ele.select_by_visible_text(value)


option_country = driver.find_element(By.ID,"Form_submitForm_Country")
select_values(option_country,"Angola")

'''generic method to select without using select'''

'''def select_values_from_list(dropdownoptionslist,value):
   print(len(dropdownoptionslist))
   for n in dropdownoptionslist:
     print(n.text)
     if (n.text == value):
       n.click()
       break




sel1 = driver.find_elements(By.XPATH,"//select[@id='Form_submitForm_Country']/option")
select_values_from_list(sel1,"Angola")'''






time.sleep(10)