from Config.config import TestData
from Pages.BasePage import BasePage #from basepage file import basepage class
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    '''By locators'''

    HOME = (By.CSS_SELECTOR,"h1._eYtD2XCVieq6emjKBH3m")
    ACCOUNT_NAME = (By.CSS_SELECTOR,"span._2BMnTatQ5gjKGK5OWROgaG")
    SEARCH_BAR = (By.ID,"header-search-bar")

    def __init__(self, driver):
        super().__init__(driver)  # calling constructor of super/parent class

    '''Page actions for Home Page'''

    '''this is used to get the home page's title'''
    def get_home_page_title(self,title):
        return self.get_title(title)

    '''this is used to check search bar exists'''
    def is_searchbar_exists(self):
        return self.is_visible(self.SEARCH_BAR)

    '''this is used to get the home page's home button's title'''
    def get_homebtn_header_value(self):
        if self.is_visible(self.HOME):    #first chcek if it is visible on home page
            return self.get_element_text(self.HOME)

    '''this is used to get the account name'''
    def get_account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)






