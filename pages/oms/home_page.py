import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class OMSHomePage:
    def __init__(self, driver):
        self.driver = driver
        
    def nav_home(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Home, Tab 1 of 4"]'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Home nav button]")
    
    def nav_delivered(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Delivered, Tab 2 of 4"]'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Delivered nav button]")
    
    def nav_users(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Users, Tab 3 of 4"]'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Users nav button]")
    
    def nav_profile(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Profile, Tab 4 of 4"]'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Profile nav button]")
    
    