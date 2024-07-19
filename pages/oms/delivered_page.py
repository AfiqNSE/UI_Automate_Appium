import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.oms_component import OMSComponents

class OMSDeliveredPage:
    def __init__(self, driver: webdriver.Remote):
        load_dotenv()
        self.reject_All = os.getenv("REJECT_ALL")
        self.reject_Partial = os.getenv("REJECT_PARTIAL")  
        self.driver = driver
        self.component = OMSComponents(self.driver)
    
    def nav_viewOrder(self):
        #Get orders
        orders = self.component.get_viewOrder()
        if len(orders) == 0: 
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
            return('Alert: Empty order list')
        
        try:
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, orders[0]))).click()
            time.sleep(2)
            
            self.driver.back()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Specific delivered order]")
        
    #NOTE: Reject order [All]    
    def nav_rejectAll(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button'))).click()     
            time.sleep(1)
            
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))

            element.clear()
            element.send_keys(self.reject_All)
            self.driver.press_keycode(66)
            time.sleep(1)
            
            try:
                orders = self.component.get_searchOrder()
                if len(orders) > 0: 
                    WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, orders[0]))).click()
                    
                else:
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                    return("Error: Cannot find the order needed")
                
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Timeline'))).click()
                
                items = self.component.get_deliveryItem()
                if len(items) > 0:
                    WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, items[0]))).click()
                else:
                    self.driver.back()
                    return("Error: Cannot find the order needed")
                
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Reject'))).click()
                
                #fill the reject form
                err = self.reject_form("Reject All")
                if err != None: 
                    for _ in range(2):
                        self.driver.back()
                        
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                    return(err)
                
            except TimeoutException:
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                return("TimeoutException: Unable to locate element [Specific delivered order]")
                
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Search button]")
    
    #NOTE: Reject order [Partial]
    def nav_rejectPartial(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button'))).click()     
            time.sleep(1)
            
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
            element.clear()
            element.send_keys(self.reject_Partial)
            self.driver.press_keycode(66)
            time.sleep(1)
            
            try:
                orders = self.component.get_searchOrder()
                if len(orders) > 0: 
                    WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, orders[0]))).click()
                    
                else:
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                    return("Error: Cannot find the order needed")
                
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Timeline'))).click()
                
                items = self.component.get_deliveryItem()
                if len(items) > 0:
                    WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, items[0]))).click()
                else:
                    self.driver.back()
                    return("Error: Cannot find the order needed")
                
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Reject'))).click()
                
                #fill the reject form
                err = self.reject_form("Reject Partial")
                if err != None: 
                    for _ in range(2):
                        self.driver.back()
                        
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                    return(err)
                
            except TimeoutException:
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                return("TimeoutException: Unable to locate element [Specific delivered order]")
                
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Search button]")
    
    #NOTE: Reject form for Partial and All     
    def reject_form(self, rejectType) -> str:
        try:
            #Select Reject type
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Select reject type'))).click()
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, rejectType))).click()
            
            #Select Reason
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Select reason'))).click()
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Other'))).click()
            
            #Details reason
            el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
            el.click()
            el.send_keys('Appium Testing')
            self.driver.hide_keyboard()
            time.sleep(2)
            
            #Photo of orders
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Add photos"])[1]'))).click()
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photo'))).click()
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
            
            #Photos of goods
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Add photos"])[2]'))).click()
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Open Gallery'))).click()
                        
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '1721352927625.jpg, 53.34 kB, 1:35 AM'))).click()
            
            #Send rejection request
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Send Rejection'))).click()
            time.sleep(2)
            
            for _ in range(2):
                self.driver.back()
                
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
            self.component.refresh_page()
                        
        except TimeoutException:
            return("TimeoutException: Unable to locate some elemenet in the form")
        
    def nav_filter(self) -> str:
        try: 
            err = self.filter_company()
            if err is None:
                self.filter_dealer()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button').click()
            
            else:
                return(err)
            
            err = self.filter_company() 
            if err is None:
                self.filter_branch()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button').click()
                
            else:
                return(err)
                
        except Exception:
            return("Error: Unable to perform filter process")   
    
    def filter_company(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Company"]'))).click()     
            
            #Get company list
            companies = self.component.get_company(page='delivered')
            if len(companies) == 0: 
                self.driver.back()
                return('Error: Cannot get list of companies')
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, companies[2]))).click()
            time.sleep(2)

        except TimeoutException:
            return("TimeoutException: Unable to locate element [Company filter button]")
    
    def filter_dealer(self):
        try: 
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Dealer"]'))).click()   
            
            #Get dealer list
            dealers = self.component.get_dealer(page='delivered')
            if len(dealers) == 0: 
                self.driver.back()
                return('Error: Cannot get list of dealers')
              
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, dealers[2]))).click()
            time.sleep(2)

        except TimeoutException:
            return("TimeoutException: Unable to locate element [Dealer filter button]")
    
    def filter_branch(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All branches"]'))).click()
            
            #Get branch list
            branches = self.component.get_branch(page='delivered')
            if len(branches) == 0: 
                self.driver.back()
                return('Error: Cannot get list of branches')
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, branches[2]))).click()
            time.sleep(2)

        except TimeoutException:
            return("TimeoutException: Unable to locate element [Branch filter button]")
      
    