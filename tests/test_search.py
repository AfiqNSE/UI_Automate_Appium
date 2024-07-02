import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from components.constant_component import Constant
from config import Config
from components.main_component import Components
from pages.search_history_page import SearchHistoryPage

class TestStaffSearch(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.search_page = SearchHistoryPage(self.driver)
        self.component = Components(self.driver)

    def test_01_logsheet_search(self):
        self.search_page.nav_search()
        self.search_page.option_buttonStaff()
        self.search_page.insert_logsheet(Constant.SEARCH_LOGSHEETNO)
        
    def test_02_pod_photoDocket(self):
        self.search_page.nav_search()
        self.search_page.option_buttonStaff()
        self.search_page.insert_docket(Constant.POD_DOCKETNO_PHOTO)
        self.component.pod_photo()
        
    def test_03_pod_uploadDocket(self):
        self.search_page.nav_search()  
        self.search_page.option_buttonStaff()
        self.search_page.insert_docket(Constant.POD_DOCKETNO_UPLOAD)
        self.component.pod_upload()
        
    def test_04_pod_signatureDocket(self):
        self.search_page.nav_search()        
        self.search_page.option_buttonStaff()
        self.search_page.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        self.component.pod_signature()

    def test_05_fail_docket(self):
        self.search_page.nav_search()
        self.search_page.option_buttonStaff()
        self.search_page.insert_docket(Constant.FAIL_DOCKETNO)
        self.component.nav_fail()
        
    def test_06_delay_docket(self):
        self.search_page.nav_search()
        self.search_page.option_buttonStaff()
        self.search_page.insert_docket(Constant.DELAY_DOCKETNO)
        self.component.nav_delay()
        
    def test_07_additional(self):
        self.search_page.nav_search()
        self.search_page.check_search_history()
        self.search_page.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        self.component.nav_viewSignature()
        self.component.nav_docketPreview()
        

class TestDriverHistory(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.history_page = SearchHistoryPage(self.driver)
        self.component = Components(self.driver)
        
    def test_01_pod_photoDocket(self):
        self.history_page.nav_history()
        self.history_page.option_buttonDriver()
        self.history_page.insert_docket(Constant.POD_DOCKETNO_PHOTO)
        self.component.pod_photo()
        
    def test_02_pod_uploadDocket(self):
        self.history_page.nav_history()
        self.history_page.option_buttonDriver()
        self.history_page.insert_docket(Constant.POD_DOCKETNO_UPLOAD)
        self.component.pod_upload()
        
    def test_03_pod_signatureDocket(self):
        self.history_page.nav_history()
        self.history_page.option_buttonDriver()
        self.history_page.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        self.component.pod_signature()

    def test_04_fail_docket(self):
        self.history_page.nav_history()
        self.history_page.option_buttonDriver()
        self.history_page.insert_docket(Constant.FAIL_DOCKETNO)
        self.component.nav_fail()
        
    def test_05_delay_docket(self):
        self.history_page.nav_history()
        self.history_page.option_buttonDriver()
        self.history_page.insert_docket(Constant.DELAY_DOCKETNO)
        self.component.nav_delay()
        
    def test_06_additional(self):
        self.history_page.nav_history()
        self.history_page.check_search_history()
        self.history_page.option_buttonDriver()
        self.history_page.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        self.component.nav_viewSignature()
        self.component.nav_docketPreview() 
    

