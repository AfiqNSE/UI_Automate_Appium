import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.staff_page import LonghaulAcceptancePage

class TestLonghaul(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.longhaul_page = LonghaulAcceptancePage(self.driver)

    def test_longhaul(self):
        self.longhaul_page.nav_longhaul()