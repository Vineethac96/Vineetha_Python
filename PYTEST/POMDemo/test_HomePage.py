import pytest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Config.config import TestData

class Test_Home(BaseTest):


    def test_homepage_title(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD) #getting refernce from login page
        title = homepage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_homepage_home_header(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        header = homepage.get_homebtn_header_value()  #input is not needed as per that method
        assert header == TestData.HOME_BTN_HEADER

    def test_account_name(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        name = homepage.get_account_name_value()
        assert name == TestData.ACCOUNT_NAME


#not working
    # def test_search_bar_exists(self):
    #     self.loginpage = LoginPage(self.driver)
    #     homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
    #     assert homepage.is_searchbar_exists()





