import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Components:
    load_dotenv()
    estDate = os.getenv("EST_DATE")
    estTime = os.getenv("EST_TIME")
    
    new_dockets = []
    all_details  = []
    sign_accessibilityID = ''
    est_accessibilityID = ''
    
    
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    #NOTE: This code is to use cancel button at UI
    def cancelButton(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.nse.project.nse_driver_flutter_app:id/btnBarcodeCaptureCancel"]').click()
    
    #Submit button
    def submitButton(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'SUBMIT'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to located [Submit Button]")
        
    #SideBar for driver page
    def nav_sideBar(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu'))).click()
        
        except TimeoutException:
            print("TimeoutException: Unable to locate [Navigation Menu]")
    
    #Logout button for staff
    def staff_logout(self):
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[3]').click()
        time.sleep(2)
        
    #Logout button for driver
    def driver_logout(self):
        self.nav_sideBar()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Logout').click()
        time.sleep(2)
        
    def nav_estDateTime(self):
        #NOTE: set single estDateTime docket
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.new_dockets[0]).click()
        self.get_displayedDetails()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.est_accessibilityID).click()
        
        actions = ActionChains(self.driver)

        #Set Date
        actions.w3c_actions.pointer_action.move_to_location(x=500, y=1050)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()
                
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.estDate))).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()
            
        except TimeoutException:
            raise ValueError("Timeout: Element (Date) did not appear within the expected time.")

        time.sleep(2)
        
        #Set Time
        actions.w3c_actions.pointer_action.move_to_location(x=500, y=1240)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'AM'))).click()    
                    
        except TimeoutException:
            raise ValueError("Timeout: Element (Date) did not appear within the expected time.")
        
        self.submitButton()
        self.driver.back()
        
        time.sleep(2)
        
        # #NOTE: Set all est date time
        self.nav_selectMode(self.new_dockets)
        self.select_all()
        
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.estDate))).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()
            
        except TimeoutException:
            raise ValueError("Timeout: unable to located [Date]")
        
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Estimate arrival time\nSelect time').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'PM'))).click()
                        
        except TimeoutException:
            raise ValueError("Timeout: unable to located [PM]")
        
        self.submitButton()
        
        time.sleep(2)
        
    def nav_viewSignature(self):
        self.get_displayedDetails()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.sign_accessibilityID).click()
        time.sleep(1)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Close').click()
    
    def nav_docketPreview(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Preview').click()
        
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))
           
        except TimeoutException:
            print("Timeout: Elements (Docket Image) did not appear within the expected time.")
        
        time.sleep(2)
        
        #Go back to homepage
        for _ in range(3):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Back').click()
    
    def nav_pod(self):
        #Click POD option
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'POD').click()
        
    def pod_photo(self):
        self.nav_pod()
        
        #Take photo directly
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photos').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Shutter').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Done').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()

        except TimeoutException:
            raise ValueError("Timeout: Element (Confirm Upload) did not appear within the expected time.")
    
    def pod_upload(self):
        self.nav_pod()
        
        #Upload Photo
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()
 
            except TimeoutException:
                raise ValueError("Timeout: Element (Confirm Upload) did not appear within the expected time.")

        except TimeoutException:
            raise ValueError("Timeout: Element (Image) did not appear within the expected time.")
            
    def pod_signature(self):
        self.nav_pod()
        
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Driver Signature').click()
        signature_element = self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')
        
        actions = ActionChains(self.driver)
        x = 530
        y = 1000

        #Tap the signature pad and clear it
        actions.move_to_element(signature_element)
        actions.click_and_hold()
        actions.move_by_offset(xoffset=x, yoffset=y)
        actions.release().perform()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Clear Signature').click()
        
        # #Tap the signature pad and submit
        actions.move_to_element(signature_element)
        actions.click_and_hold()
        actions.move_by_offset(xoffset=x, yoffset=y)
        actions.release().perform()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit Signature & Take Photo').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Shutter').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Done').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()

        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Confirm Upload]")

    #NOTE: Navigation to do FAIL
    def nav_fail(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Fail'))).click()
            
            #Choose fail reason
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Fail Reason').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Store Closed'))).click()
                
                self.fail_attachment()
                self.remove_attachment()
                self.submitButton()
                
            except TimeoutException:
                raise ValueError("TimeoutException: Unable to locate [Store Closed]")
            
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Fail Button]")
          
    def fail_attachment(self):
        ##Upload Do/Logsheet photo
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[1]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photos').click()

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [shutter icon]")
    
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[1]'))).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
             
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
                    
            except TimeoutException:
                raise ValueError("Timeout: Element (Image) did not appear within the expected time.")
        
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Take Photo Text]")       
       
        time.sleep(1)
        
        #Upload attachment
        for _ in range(2):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[2]'))).click()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
            
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
                    
                except TimeoutException:
                    raise ValueError("Timeout: Element (Image) did not appear within the expected time.")
                
            except TimeoutException:
                 raise ValueError("Timeout: Element (Take Photo) did not appear within the expected time.")
            
        time.sleep(1)
    
    #NOTE: Navigation to do DELAY
    def nav_delay(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delay').click()
        
        #Choose delay reason
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Delay Reason:').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Truck breakdown'))).click()

            self.delay_attachment()
            self.remove_attachment()
            self.submitButton()
            
        except TimeoutException:
            raise ValueError("Timeout: Element (Truck breakdown) did not appear within the expected time.")
            
    def delay_attachment(self):
        #Take photo directly
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photo').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photos').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [shutter icon]")

        time.sleep(2)
        
        #Upload attachment
        for _ in range(2):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photo'))).click()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
            
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
                    
                except TimeoutException:
                    raise ValueError("Timeout: Element (Image) did not appear within the expected time.")
                
            except TimeoutException:
                 raise ValueError("Timeout: Element (Take Photo) did not appear within the expected time.")
            
        time.sleep(2)
        
    def remove_logsheetPhoto(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView'))).click()

        except TimeoutException:
            raise ValueError("Timeout: Element (Image) did not appear within the expected time.")
            
    def remove_attachment(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]'))).click()

        except TimeoutException:
            raise ValueError("Timeout: Element (Image) did not appear within the expected time.")
       
    #NOTE: Select All & Deselect All button
    def nav_selectMode(self, dockets):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, dockets[0])))
        self.driver.execute_script('mobile: longClickGesture', {'elementId': element.id})
        
    def select_all(self):
        #Select All
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select All').click()

    def deselect_all(self):          
        #Deselect All
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Deselect All').click()
    
    def exit_selectMode(self):
         #Exit Select Mode
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)').click()
            
    #NOTE: Get latest element that been display at the UI
    def get_dockets(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            for item in all_items:
                if item.is_displayed():
                    docket = item.get_attribute("content-desc")
                    if "NEW" in docket:
                        self.new_dockets.append(docket)
            
        except TimeoutException:
            raise ValueError("Timeout: Elements (dockets) did not appear within the expected time.")
        
        time.sleep(2)
    
    #NOTE: Get details elements that been display at the UI
    def get_displayedDetails(self):
        try:
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Docket Details')))

            # Find all direct child views within the ScrollView
            all_items = self.driver.find_elements(AppiumBy.XPATH, './/android.widget.Button')
            
            for item in all_items:
                if item.is_displayed():
                    detail = item.get_attribute("content-desc")
                    self.all_details.append(detail)
                    if "Signature" in detail:
                        self.sign_accessibilityID = detail
                    if "Estimation" in detail:
                        self.est_accessibilityID = detail
                    
        except TimeoutException:
            raise ValueError("Timeout: Element (Docket Details) did not appear within the expected time.")
        
        time.sleep(2)

        
