import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://www.amazon.com/b?node=16225007011&pf_rd_r=JJBZB99ER1K1T931MC44&pf_rd_p=e5b0c85f-569c-4c90-a58f-0c0a260e45a0&pd_rd_r=66501725-97dc-4596-ac6a-e98a6b330f1f&pd_rd_w=4TNfD&pd_rd_wg=qhSbi&ref_=pd_gw_unk")

list1 = driver.find_element(By.CSS_SELECTOR,"div#s-refinements>div:nth-of-type(1)")
list2 = driver.find_element(By.CSS_SELECTOR,"div#s-refinements>div:nth-of-type(5)")
list3 = driver.find_elements(By.CSS_SELECTOR,"div#s-refinements>div:nth-of-type(n)")
print(list1.text)
print(list2.text)
print(list3[0])





