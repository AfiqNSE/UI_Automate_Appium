import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class OMSHomePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.list_order = []
        
    def nav_scan(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Scan Delivery Order"]'))).click()     
            time.sleep(2)
            
            self.driver.back()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Home nav button]")
            
    def nav_search(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()
            time.sleep(1)
            
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))

            element.send_keys('801')
            self.driver.press_keycode(66)
            
            #Get order
            self.get_orders()
            time.sleep(2)
            
            if len(self.list_order) > 0:
                try:
                    WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.list_order[0]))).click()
                    time.sleep(2)
                    
                    for _ in range(2):
                        self.driver.back()
                    
                except TimeoutException:
                    return("TimeoutException: Unable to locate element [Order list]")
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Search button]")
            
    def nav_notif(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[3]'))).click()     
            time.sleep(2)
 
            self.driver.back()

        except TimeoutException:
            return("TimeoutException: Unable to locate element [Notification button]")
            
    def status_filter(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Status"]'))).click()     
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="In Progress"]'))).click()
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button').click()
        
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Status filter button]")
        
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Status"]'))).click()     
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="On Delivery"]'))).click()
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button').click()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Status filter button]")
        
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Status"]'))).click()     
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Delayed"]'))).click()
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button').click()
        
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Status filter button]")
        
    def company_filter(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Company"]'))).click()     
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Daikin Malaysia"]'))).click()
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button').click()

        except TimeoutException:
            return("TimeoutException: Unable to locate element [Company filter button]")
    
    #TODO: Need to update oms BE
    def date_filter(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="All Date"]'))).click()     
            time.sleep(2)
            
            self.driver.back()

        except TimeoutException:
            return("TimeoutException: Unable to locate element [Date filter button]")
    
    def nav_order(self) -> str:
        #Get orders
        self.get_orders()
        time.sleep(3)
           
        if len(self.list_order) > 0:
            try:
                WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.list_order[0]))).click()
                time.sleep(2)
                
                self.driver.back()
                
            except TimeoutException:
                return("TimeoutException: Unable to locate element [Specific order]")
    
    def get_orders(self) -> str:
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "801")]')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "801")]')
            
            self.list_order = []
            for item in all_items:
                if item.is_displayed():
                    self.list_order.append(item.get_attribute('content-desc'))
            
            # print(len(self.list_order))
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Order list]")
    

    