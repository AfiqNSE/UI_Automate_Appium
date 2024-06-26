import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.staff_page import StaffAnalyticsPage

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.analytics_page = StaffAnalyticsPage(self.driver)

    def test_login(self):
        self.analytics_page.nav_anlytics()
        


