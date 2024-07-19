import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.oms.login_page import OMSLoginPage
from pages.oms.profile_page import OMSProfilePage


class TestOMSLoginLogout(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.oms_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.login_page = OMSLoginPage(self.driver)
        self.profile_page = OMSProfilePage(self.driver)
    
    def test_login(self):
        self.login_page.enter_username()
        self.login_page.enter_password()
        self.login_page.click_login()
        
    def test_logout(self):
        self.profile_page.nav_logout()
        
    def tearDown(self):
        self.driver.quit()