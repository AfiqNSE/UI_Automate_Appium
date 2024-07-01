import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from components.main_component import Components
from config import Config
from pages.analytics_page import AnalyticsPage


class TestStaffAnalytics(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.analytics_page = AnalyticsPage(self.driver)
 
    def test_analytics(self):
        self.analytics_page.nav_staff_analytics()
        

class TestDriverAnalytics(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.analytics_page = AnalyticsPage(self.driver)
        self.component = Components(self.driver)
        
    def test_analytics(self):
        self.component.nav_sideBar()
        self.analytics_page.nav_driver_analytics()


