import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.language_page import LanguagePage

class TestLanguage(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.language_page = LanguagePage(self.driver)

    def test_staff_language(self):
        self.language_page.change_staff_language()
        

        


