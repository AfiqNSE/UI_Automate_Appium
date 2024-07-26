from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class IODLoginPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def enter_username(self, username):
        textfield = self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
        textfield.click()
        textfield.clear()
        textfield.send_keys(username)
        self.driver.hide_keyboard()   
        
    def enter_password(self, password):
        textfield = self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
        textfield.click()
        textfield.clear()
        textfield.send_keys(password)
        self.driver.hide_keyboard()    

    def click_login(self):
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Login"]').click()


