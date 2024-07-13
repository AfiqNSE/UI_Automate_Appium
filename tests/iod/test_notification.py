import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.notification_page import NotificationPage

class TestNotification(unittest.TestCase):
    def test_notification(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.notification_page = NotificationPage(self.driver)
        
        self.notification_page.nav_notification()
 