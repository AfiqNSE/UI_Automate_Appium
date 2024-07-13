from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class OMSLoginPage:

    def __init__(self, driver: webdriver.Remote) -> None:
        self.driver = driver
        
    def enter_username(self):
        try:
            textfield = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')))
            textfield.click()
            textfield.clear()
            textfield.send_keys('admin')
            self.driver.hide_keyboard()
            
        except TimeoutException:
            print("TimeoutEception: Unable to locate element [username textfield]")

    def enter_password(self):
        try:
            textfield = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')))
            textfield.click()
            textfield.clear()
            textfield.send_keys('Oms@1234')
            self.driver.hide_keyboard()
            
        except TimeoutException:
            print("TimeoutEception: Unable to locate element [password textfield]")
            
    def click_login(self):
        try:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Login').click()
        except TimeoutException:
            print("TimeoutEception: Unable to locate element [login button]")