import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from components.main_component import Components


class RewardPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def nav_reward(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Reward").click()

    def load_rewardPage(self):
        # self.redeem_slide()
        # time.sleep(1)
        self.redeem_insert()
        # self.driver.back()
            
    def check_point(self) -> bool:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "POINT")]')))

            element = self.driver.find_element(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "POINT")]')
            point = element.get_attribute("content-desc").lstrip('POINT\n')
            
        except TimeoutException:
            print("TimeoutException: unable to located [Point]")

        if(int(point) > 1000):
            valid = True
        else:
            valid = False

        return valid
    
    def redeem_slide(self):
        if self.check_point() is True:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Redeem Points").click()
            
            slider_element = self.driver.find_element(AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc="0%"]')
        
            actions = ActionChains(self.driver)
            x = 1
            y = 1490
            
            #Tap the slide and move to right
            actions.move_to_element(slider_element).click_and_hold()
            actions.move_by_offset(xoffset=x, yoffset=y).release().perform()
            
            self.redeem_button()
            time.sleep(1)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Dismiss').click()
            self.driver.back()
            self.refresh_button()
            
        else:
            print("Not enough points to redeem")
            pass
            
    def redeem_insert(self):
        if self.check_point() is True:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Redeem Points").click()
            
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'ENTER AMOUNT').click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('500')        
            Components.submitButton(self)
                
            self.redeem_button()
            time.sleep(1)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Dismiss').click()
            self.driver.back()
            self.refresh_button()
            
        else:
            print("Not enough points to redeem")
            pass
              
    def redeem_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'REDEEM').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'REDEEM').click()
        
    def refresh_button(self):
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]').click()

        