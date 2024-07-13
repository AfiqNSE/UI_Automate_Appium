import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.iod.approve_page import ApproveRedeemPage

class TestStaffApprove(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.approve_page = ApproveRedeemPage(self.driver)

    def test_approve(self):
        self.approve_page.nav_redeem()
