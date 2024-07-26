import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class ApprovePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def nav_redeem(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Approve\nRedeem'))).click()
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Approve button]")

