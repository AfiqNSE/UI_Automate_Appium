import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class OMSComponents:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    def refresh_page(self):
        el = self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]')
        actions = ActionChains(self.driver)
        actions.click_and_hold(el).move_by_offset(xoffset=0, yoffset=600).release().perform()  

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
            
     #NOTE: Get the company list
    def get_company(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')
            
            company_list = []
            for item in all_items:
                if item.is_displayed():
                    company_list.append(item.get_attribute('content-desc'))
            
            return company_list
        except TimeoutException:
            return None
    
    #NOTE: Get the branch list
    def get_branch(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')
            
            branch_list = []
            for item in all_items:
                if item.is_displayed():
                    branch_list.append(item.get_attribute('content-desc'))
            
            return branch_list   
        except TimeoutException:
            return None
    
    #NOTE: Get the dealer list
    def get_dealer(self):
        try: 
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText/android.view.View')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.EditText/android.view.View/android.view.View/android.view.View')
            
            dealer_list = []
            for item in all_items:
                if item.is_displayed():
                    dealer_list.append(item.get_attribute('content-desc'))
            
            return dealer_list   
        except TimeoutException:
            return None

    
    