import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from components.iod_component import IODComponents

class ApproveRedeemPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def nav_redeem(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Approve\nRedeem').click()
        IODComponents.cancelButton(self)
        time.sleep(2)

