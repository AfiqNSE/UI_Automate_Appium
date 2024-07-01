import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException



#NOTE: KIV since v2.5 got issue
# Testing part for Analytics
class AnalyticsPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    #Scroll to see analytics for small screen phone
    def scroll_analytics(self):
        signature_element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assign\nPoints')
        
        actions = ActionChains(self.driver)
        x = 800
        y = -1000

        #Tap the signature pad and clear it
        actions.move_to_element(signature_element)
        actions.click_and_hold()
        actions.move_by_offset(xoffset=x, yoffset=y)
        actions.release().perform()

    def nav_staff_analytics(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Analytics'))).click()
            time.sleep(1)

        except TimeoutException:
            raise ValueError("Timeout: Element (Analytics) did not appear within the expected time.")

        self.driver.back()

    #TODO: Create Analytics test module  
    def nav_driver_analytics(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Analytics").click()
        self.driver.back()
