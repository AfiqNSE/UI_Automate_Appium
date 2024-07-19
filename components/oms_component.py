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
        actions.click_and_hold(el).move_by_offset(xoffset=0, yoffset=700).release().perform()

    def nav_home(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Home, Tab 1 of 5'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Home nav button]")
    
    def nav_delivered(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Delivered, Tab 2 of 5'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Delivered nav button]")
            
    def nav_rejection(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Rejections, Tab 3 of 5'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Rejections nav button]")
    
    def nav_users(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Users, Tab 4 of 5'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Users nav button]")
    
    def nav_profile(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Profile, Tab 5 of 5'))).click()
            time.sleep(2)
            
        except TimeoutException:
            print("TimeoutException: Unable to locate element [Profile nav button]")
          
    #NOTE: Get the company list
    def get_company(self, page):
        try:
            
            #Get company list path based on page provided
            paths = self.get_companyPath(fromPage=page)
            
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, paths['xpathMain'])))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, paths['xpathSub'])
            
            company_list = []
            for item in all_items:
                if item.is_displayed():
                    company_list.append(item.get_attribute('content-desc'))
            return company_list
        except TimeoutException:
            return []
    
    #NOTE: Get the dealer list
    def get_dealer(self, page):
        try: 
            
            #Get dealer list path based on page provided
            paths = self.get_dealerPath(fromPage=page)
            
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, paths['xpathMain'])))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, paths['xpathSub'])
            
            dealer_list = []
            for item in all_items:
                if item.is_displayed():
                    dealer_list.append(item.get_attribute('content-desc'))
            
            return dealer_list   
        except TimeoutException:
            return []
        
    #NOTE: Get the branch list
    def get_branch(self, page):
        try:
            #Get branch list path based on page provided
            paths = self.get_branchPath(fromPage=page)
            
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, paths['xpathMain'])))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, paths['xpathSub'])
            
            branch_list = []
            for item in all_items:
                if item.is_displayed():
                    branch_list.append(item.get_attribute('content-desc'))
            
            return branch_list   
        except TimeoutException:
            return []

    #NOTE: Get the orders list at main view tab
    def get_viewOrder(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "801")]')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "801")]')
            
            order_list = []
            for item in all_items:
                if item.is_displayed():
                    order_list.append(item.get_attribute('content-desc'))
            
            return order_list
        except TimeoutException:
            return []

    #NOTE: Get the orders list at search feature
    def get_searchOrder(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "801")]')
            
            order_list = []
            for item in all_items:
                if item.is_displayed():
                    order_list.append(item.get_attribute('content-desc'))
                    
            return order_list   
        except TimeoutException:
            return []
    
    #NOTE: Get delivery items
    def get_deliveryItem(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[20]')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[20]/android.view.View')
            
            item_list = []
            for item in all_items:
                if item.is_displayed():
                    item_list.append(item.get_attribute('content-desc'))
            
            return item_list   
        except TimeoutException:
            return []
      
    #NOTE: Get company path for delivered and user pages   
    def get_companyPath(self, fromPage):
        paths = {}
        if fromPage == 'delivered':
            paths = {
                'xpathMain': '//android.view.View[@content-desc="Show orders from company..."]',
                'xpathSub': '//android.view.View[@content-desc="Show orders from company..."]/android.view.View'
            }
        elif fromPage == 'users':
            paths = {
                'xpathMain': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View',
                'xpathSub': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View'
            }
            
        return paths
    
    #NOTE: Get dealer path for delivered and user pages   
    def get_dealerPath(self, fromPage):
        paths = {}
        if fromPage == 'delivered':
            paths = {
                'xpathMain': '//android.view.View[@content-desc="Show orders from dealer..."]',
                'xpathSub': '//android.view.View[@content-desc="Show orders from dealer..."]/android.view.View'
            }
        elif fromPage == 'users':
            paths = {
                'xpathMain': '//android.widget.EditText/android.view.View',
                'xpathSub': '//android.widget.EditText/android.view.View/android.view.View/android.view.View'
            }
            
        return paths
    
    #NOTE: Get branch path for delivered and user pages   
    def get_branchPath(self, fromPage):
        paths = {}
        if fromPage == 'delivered':
            paths = {
                'xpathMain': '//android.view.View[@content-desc="Show orders from branch..."]',
                'xpathSub': '//android.view.View[@content-desc="Show orders from branch..."]/android.view.View'
            }
        elif fromPage == 'users':
            paths = {
                'xpathMain': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View',
                'xpathSub': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View'
            }

        return paths
            

    
    