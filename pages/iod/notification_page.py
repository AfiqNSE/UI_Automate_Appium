import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class IODNotificationPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def nav_notification(self) -> str:
        try: 
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()
            time.sleep(2)
            self.driver.back()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate [Notification icon]")