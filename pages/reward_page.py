from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


#TODO: Create Reward test module  
class RewardPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def nav_reward(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Reward").click()
        self.driver.back()

