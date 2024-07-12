import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.search_history_page import SearchHistoryPage

class TestStaffSearch(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.search_page = SearchHistoryPage(self.driver)

    def test_staff_search(self):
        self.search_page.staff_logsheet_search()
        self.search_page.staff_pod_photoDocket()
        self.search_page.staff_pod_uploadDocket()
        self.search_page.staff_pod_signatureDocket()
        self.search_page.staff_fail_docket()
        self.search_page.staff_delay_docket()
        self.search_page.staff_additional()

class TestDriverSearch(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.search_page = SearchHistoryPage(self.driver)
                
    def test_driver_search(self):
        self.search_page.driver_pod_photoDocket()
        self.search_page.driver_pod_uploadDocket()
        self.search_page.driver_pod_signatureDocket()
        self.search_page.driver_fail_docket()
        self.search_page.driver_delay_docket()
        self.search_page.driver_additional()
    

