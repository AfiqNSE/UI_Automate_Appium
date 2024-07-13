import time
import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.language_page import LanguagePage

class TestStaffLanguage(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.language_page = LanguagePage(self.driver)

    def test_language(self):
        self.language_page.nav_staff_language()
        self.language_page.malay_language()
        self.language_page.nav_staff_language()
        self.language_page.english_language()
        time.sleep(2)

#K.I.V untuk driver 
class TestDriverLanguage(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.language_page = LanguagePage(self.driver)

    def test_language(self):
        self.language_page.nav_driver_english()
        self.language_page.malay_language()
        self.language_page.nav_driver_bahasa()
        self.language_page.english_language()
