import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.reward_page import RewardPage

class TestIODReward(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.reward = RewardPage(self.driver)
        self.errorList = []
    
    def test_viewPoints(self):
        err = self.reward.nav_reward()
        if err != None:
            self.errorList.append(err)
            
        err = self.reward.nav_leaderboard()
        if err != None:
            self.errorList.append(err)
            
        err = self.reward.nav_history()
        if err != None:
            self.errorList.append(err)
            
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
      
    def test_redeemPoints(self):
        err = self.reward.nav_redeem()
        if err != None: print("\nError/Alert Detected:", err)
