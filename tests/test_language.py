import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.language_page import LanguagePage

class TestStaffLanguage(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.language_page = LanguagePage(self.driver)

    def test_language(self):
        self.language_page.nav_staff_language()
        self.language_page.malay_language()
        self.language_page.nav_staff_language()
        self.language_page.english_language()
        

class TestDriverLanguage(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.language_page = LanguagePage(self.driver)

    def test_language(self):
        self.language_page.nav_driver_language()
        self.language_page.malay_language()
        self.language_page.nav_driver_language()
        self.language_page.english_language()

