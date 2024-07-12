import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.report_page import ReportsPage


class TestStaffReport(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.report_page = ReportsPage(self.driver)
        
    def test_report(self):
        self.report_page.iod_report()
        self.report_page.general_report()
