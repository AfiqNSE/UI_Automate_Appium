import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.leaderboard_page import LeaderboardPage


class TestIODLeaderboard(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.leaderboard = LeaderboardPage(self.driver)
 
    def test_leaderboard(self):
        err = self.leaderboard.nav_leaderboard()
        if err != None: print("\nError/Alert Detected:", err)
        
    def tearDown(self):
        self.driver.quit()