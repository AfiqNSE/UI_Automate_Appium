import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from components.main_component import Components
from config import Config
from pages.iod.home_page import DriverHomePage
from pages.iod.invalid_page import InvalidIODPage

class TestDriverInvalid(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.invalid_page = InvalidIODPage(self.driver)
        self.component = Components(self.driver)
        
    def test_invalid(self):
        self.component.nav_sideBar()
        self.invalid_page.nav_invalid()
        self.invalid_page.load_invalidPage()

      
