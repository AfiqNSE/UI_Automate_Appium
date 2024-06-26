import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.search_page import SearchPage
from utils.main_utils import Utils

class TestSearch(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.search_page = SearchPage(self.driver)

    def test_01_logsheet_search(self):
        self.search_page.nav_search()
        self.search_page.button_option()
        self.search_page.scan_logsheet() 
        self.search_page.insert_logsheet(Utils.Search_logsheetNo)
        # self.search_page.nav_estDateTime()
        
    def test_02_pod_docket(self):
        self.search_page.nav_search()
        self.search_page.button_option()
        self.search_page.scan_docket()  
        self.search_page.insert_docket(Utils.pod_docketNo)
        
    def test_03_fail_docket(self):
        self.search_page.nav_search()
        self.search_page.button_option()
        self.search_page.scan_docket() 
        self.search_page.insert_docket(Utils.fail_docketNo)
        self.search_page.nav_fail()
        
    def test_04_delay_docket(self):
        self.search_page.nav_search()
        self.search_page.button_option()
        self.search_page.scan_docket()  
        self.search_page.insert_docket(Utils.delay_docketNo)
        self.search_page.nav_delay()
        


