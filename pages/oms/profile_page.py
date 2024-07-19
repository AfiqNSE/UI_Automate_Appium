import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.oms_component import OMSComponents

class OMSProfilePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = OMSComponents(self.driver)
        
    def nav_logout(self):
        self.component.nav_profile()
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Logout"))).click()
        except TimeoutException:
            print("TimeoutException: Unable to locate element [logoutButton]")
        time.sleep(2)