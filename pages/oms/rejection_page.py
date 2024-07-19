import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.oms_component import OMSComponents

class OMSRejectionPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = OMSComponents(self.driver)
        
    def nav_closeReject(self) -> str:
        try:
            self.component.refresh_page()
            
            #Filter the status to OPEN
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Status"]'))).click()
                
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="OPEN"]'))).click()
            
            #Get rejected orders
            rejectOrders = self.get_rejectOrder()
            
            if len(rejectOrders) > 0:
                try:
                    WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, rejectOrders[0]))).click()
                    
                    el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
                    el.click()
                    el.send_keys('Appium Test')
                    self.driver.hide_keyboard()
                    time.sleep(2)
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]').click()
                    
                    #Close filter
                    WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'))).click()
                    time.sleep(1)
                    self.component.refresh_page()
                    
                except TimeoutException:
                    return("TimeoutException: Unable to locate element [Specific rejected order]")
                
            else: 
                #Close filter
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'))).click()
                return("Alert: Empty reject order[OPEN] list")
            
        except Exception:
            return("Exception: Unable to perform to close rejection")
             
    def status_filter(self) -> str:  
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Status"]'))).click()
            
            #Filter [status: open]
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="OPEN"]'))).click()
            time.sleep(2)
            
            #Close filter
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'))).click()
            time.sleep(1)
            
        except TimeoutException:
            self.driver.back()
            return('TimeoutException: Cannot find [filter status open button]')
            
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Status"]'))).click()
            
            #Filter [status: closed]
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="CLOSED"]'))).click()
            time.sleep(2)
            
            #Close filter
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'))).click()
            time.sleep(1)
            
        except TimeoutException:
            self.driver.back()
            return('TimeoutException: Cannot find [filter status closed button]')
             
    
    def date_filter(self) -> str:  
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Date"]'))).click()
            
            #Filter "Last one week"
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Last One Week"]'))).click()
            time.sleep(2)
            
            #Close filter
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'))).click()
            time.sleep(1)
            
        except TimeoutException:
            self.driver.back()
            return('TimeoutException: Cannot find filter date [Last one week] button]')
        
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Date"]'))).click()
            
            #Filter "Last one week"
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Last One Month"]'))).click()
            time.sleep(2)
            
            #Close filter
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'))).click()
            time.sleep(1)
            
        except TimeoutException:
            self.driver.back()
            return('TimeoutException: Cannot find filter date [Last one month] button]')
        
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Date"]'))).click()
            
            #Filter "Select date"
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Select Date"]'))).click()
            
            #NOTE: Try to select range date later
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Apply"]'))).click()
            time.sleep(2)
            
            #Close filter
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button'))).click()
            time.sleep(1)
            
        except TimeoutException:
            self.driver.back()
            return('TimeoutException: Cannot find filter date [Last one month] button]')
    
    #Get list of reject order
    def get_rejectOrder(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "801")]')
            
            order_list = []
            for item in all_items:
                if item.is_displayed():
                    order_list.append(item.get_attribute('content-desc'))
            
            return order_list   
        except TimeoutException:
            return []