import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.staff_page import StaffSearchPage

class TestSearch(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.search_page = StaffSearchPage(self.driver)

    # def test_01_logsheet_search(self):
        # self.search_page.nav_search()
        # self.search_page.button_option()
        # self.search_page.scan_logsheet()
        # self.search_page.insert_logsheet()
        # self.search_page.delay_docket()
        # self.search_page.fail_docket()
        # self.search_page.pod_docket()
     
    def test_02_docket_search(self):
        # self.search_page.scan_docket()
        self.search_page.insert_docket()
        self.search_page.nav_delay()
