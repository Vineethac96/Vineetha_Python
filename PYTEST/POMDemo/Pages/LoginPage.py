from Config.config import TestData
from Pages.BasePage import BasePage #from basepage file import basepage class
from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage

class LoginPage(BasePage):    #base page is parent class

    '''By locators'''
    EMAIL = (By.ID,"loginUsername")
    PASSWORD = (By.ID, "loginPassword")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".AnimatedForm__submitButton.m-full-width")
    SIGN_UP_LINK = (By.XPATH, "//a[@class='BottomLink']")  #as by link,it was not working

    '''constructor of the login page class'''
    def __init__(self,driver):
        super().__init__(driver) #calling constructor of super/parent class
        self.driver.get(TestData.BASE_URL)

    '''Page actions for Login Page'''

    '''this is used to get the page title'''
    def get_login_page_title(self,title):
        return self.get_title(title)

    '''this is used to check signup link'''
    def is_signup_link_exists(self):
        return self.is_visible(self.SIGN_UP_LINK)

    '''this is used to login to app'''
    def do_login(self,username,password):
        self.do_sendkeys(self.EMAIL,username)
        self.do_sendkeys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)   #after login return a homepage class object