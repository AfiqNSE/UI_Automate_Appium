import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from components.main_component import Components

class ApproveRedeemPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def nav_redeem(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Approve\nRedeem').click()
        Components.cancelButton(self)
        time.sleep(2)

