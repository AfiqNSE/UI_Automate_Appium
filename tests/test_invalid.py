import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from components.main_component import Components
from config import Config
from pages.invalid_page import InvalidIODPage

class TestDriverInvalid(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.invalid = InvalidIODPage(self.driver)
        self.component = Components(self.driver)
        
    def test_invalid(self):
        self.component.nav_sideBar()
        self.invalid.nav_invalid()
