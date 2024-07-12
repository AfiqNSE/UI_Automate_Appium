import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.iod.assign_page import AssignPointPage

class TestStaffAssign(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.assign_page = AssignPointPage(self.driver)

    def test_assign(self):
        self.assign_page.nav_assignPoint()
        self.assign_page.scan_logsheet()
        self.assign_page.insert_logsheet()
        self.assign_page.check_filter()
        self.assign_page.select_mode()
        self.assign_page.single_assign()
        self.assign_page.multiple_assign()

