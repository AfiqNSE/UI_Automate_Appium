import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.staff_page import SearchPage
from components.main_components import Constant, Components

class TestStaffSearch(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.search_page = SearchPage(self.driver)
        self.component = Components(self.driver)

    def test_01_logsheet_search(self):
        self.search_page.nav_search()
            
        if Constant.SEARCH_LOGSHEETNO == '':
            raise ValueError("No logsheet number provided")
        self.search_page.insert_logsheet(Constant.SEARCH_LOGSHEETNO)
        
    def test_02_pod_photoDocket(self):
        self.search_page.nav_search()
        
        if Constant.POD_DOCKETNO_PHOTO == '':
            raise ValueError("No docket number provided")
        
        self.search_page.insert_docket(Constant.POD_DOCKETNO_PHOTO)
        self.component.pod_photo()
        
    def test_03_pod_uploadDocket(self):
        self.search_page.nav_search()  
          
        if Constant.POD_DOCKETNO_UPLOAD == '':
            raise ValueError("No docket number provided")

        self.search_page.insert_docket(Constant.POD_DOCKETNO_UPLOAD)
        self.component.pod_upload()
        
    def test_04_pod_signatureDocket(self):
        self.search_page.nav_search()      
          
        if Constant.POD_DOCKETNO_SIGNATURE == '':
            raise ValueError("No docket number provided")
        
        self.search_page.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        self.component.pod_signature()

    def test_05_fail_docket(self):
        self.search_page.nav_search()
        
        if Constant.FAIL_DOCKETNO == '':
            raise ValueError("No docket number provided")

        self.search_page.insert_docket(Constant.FAIL_DOCKETNO)
        self.component.nav_fail()
        
    def test_06_delay_docket(self):
        self.search_page.nav_search()
        
        if Constant.DELAY_DOCKETNO == '':
            raise ValueError("No docket number provided")

        self.search_page.insert_docket(Constant.DELAY_DOCKETNO)
        self.component.nav_delay()
        
    def test_07_additional(self):
        self.search_page.nav_search()
        self.search_page.check_search_history()
        
        if Constant.POD_DOCKETNO_SIGNATURE == '':
            raise ValueError("No docket number provided")
        
        self.search_page.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        self.component.nav_viewSignature()
        self.component.nav_docketPreview()
        


