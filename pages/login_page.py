from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from components.main_component import Constant

#Testing class for Login
class LoginPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def enter_staff_username(self):
        textfield = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
        textfield.click()
        textfield.send_keys(Constant.STAFF_USERNAME)
        self.driver.hide_keyboard()     
        
    def enter_driver_username(self):
        textfield = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
        textfield.click()
        textfield.send_keys(Constant.DRIVER_USERNAME)
        self.driver.hide_keyboard()   
        
    def enter_password(self):
        textfield = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
        textfield.click()
        textfield.send_keys(Constant.PASSWORD)
        self.driver.hide_keyboard()    

    def click_login(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Login"]').click()


