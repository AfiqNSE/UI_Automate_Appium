import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class OMSHomePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def check_scan(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Home, Tab 1 of 4"]'))).click()
            time.sleep(2)
            
            self.driver.back()
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Home nav button]")

    