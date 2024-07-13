import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.oms.login_page import OMSLoginPage


class TestOMSLogin(unittest.TestCase):
    def test_login(self):
        options = UiAutomator2Options().load_capabilities(Config.oms_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.login_page = OMSLoginPage(self.driver)
        
        self.login_page.enter_username()
        self.login_page.enter_password()
        self.login_page.click_login()
        
    def tearDown(self):
        self.driver.quit()