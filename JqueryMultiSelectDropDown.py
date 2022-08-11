import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(2)

driver.find_element(By.ID,"justAnInputBox").click()

drop_List = driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
# for ele in drop_List:
#   print(ele.text)
#  if ele.text == "choice 6 2 3":
#     ele.click()
#    break

'''to select all options'''
# for ele in drop_List:
#     print(ele.text)
#     ele.click()

'''Generic method to select multi options'''
# def multiselect(optionsList,value):
#     for ele in optionsList:
#     print(ele.text)
#     if ele.text == value:
#         ele.click()
#         break
# multiselect(drop_List,"choice 3")
# multiselect(drop_List,"choice 2 2")
# multiselect(drop_List,"choice 6 2 2")

'''Generic method to select multi options without calling one method multiple time,
instead calling method once by giving options in a list'''
def multiselectViaList(optionsList,value):
    if value[0] == "all":
    #         for ele in optionsList:
    #            print(ele.text)
    #            ele.click()
    # as this gives exception as with "comboTreeItemTitle" in html we have other options too, so it throws exception as elememt not iterable
        try:
            for ele in optionsList:
               print(ele.text)
               ele.click()
        except Exception as e:
               print(e)

    else:
        for ele in optionsList:
            print(ele.text)
            for k in range(len(value)):
               if ele.text == value[k]:
                  ele.click()
                  break

values_list1 = ["choice 1","choice 2 1","choice 6 1","choice 6 2 3"]#multi-selection
values_list2 = ["choice 3"]#single-selection
values_list3 =["all"]#select all options

multiselectViaList(drop_List,values_list1)
#multiselectViaList(drop_List,values_list2)
#multiselectViaList(drop_List,values_list3)

time.sleep(5)
driver.quit()

