import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv


class LoginPage:
    load_dotenv()
    staff_username = os.getenv("STAFF_USERNAME")
    driver_username = os.getenv('DRIVER_USERNAME')
    password = os.getenv("PASSWORD")

    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def enter_staff_username(self):
        textfield = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
        textfield.click()
        textfield.clear()
        textfield.send_keys(self.staff_username)
        self.driver.hide_keyboard()     
        
    def enter_driver_username(self):
        textfield = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
        textfield.click()
        textfield.clear()
        textfield.send_keys(self.driver_username)
        self.driver.hide_keyboard()   
        
    def enter_password(self):
        textfield = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
        textfield.click()
        textfield.clear()
        textfield.send_keys(self.password)
        self.driver.hide_keyboard()    

    def click_login(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Login"]').click()


