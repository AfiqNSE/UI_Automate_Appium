import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        self.login_page.click_login()
        


