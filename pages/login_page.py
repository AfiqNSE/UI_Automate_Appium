from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

#Testing class for Login
class LoginPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def enter_username(self):
        pass    

    def enter_password(self):
        pass

    def click_login(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Login"]').click()


