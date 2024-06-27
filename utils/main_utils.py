from appium import webdriver

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


#NOTE: Set the testing data
class Constant():
        # Testing data for search
        SEARCH_LOGSHEETNO = 'DD30010924'
        POD_DOCKETNO_PHOTO = 'JD300129293'
        POD_DOCKETNO_UPLOAD = 'JD300129980'
        POD_DOCKETNO_SIGNATURE = 'JD300129988'
        FAIL_DOCKETNO = 'JD300129291'
        DELAY_DOCKETNO = 'JD300130143'
            
        # Testing data for assign
        ASSIGN_LOGSHEETNO = 'DD30010985'
            
        # Testing data for report
        REPORT_DATEFROM = '9, Tuesday, January 9, 2024'
        REPORT_DATETO = '30, Tuesday, April 30, 2024'


#NOTE: Components that been used for Staff & Driver
class Utils():
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    new_dockets = []
    
    #NOTE: This code is to use cancel button at UI
    def cancelButton(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.nse.project.nse_driver_flutter_app:id/btnBarcodeCaptureCancel"]').click()
    
    def homePagePresence(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Management Dashboard')))
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
    
    #TODO: estDateTime docket
    def nav_estDateTime(self, dockets):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, dockets).click()
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "Estimation")]'))).click()

        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            pass 
    
    #TODO: Check Signature
    def nav_checkSignature(self):
        pass
    
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
            print("Timeout: Elements did not appear within the expected time.")
        
        #Wait for the process to return back to homepage
        self.homePagePresence()
    
    def pod_upload(self):
        self.nav_pod()
        
        #Upload Photo
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
 
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()
 
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
        
        #Wait for the process to return back to homepage
        self.homePagePresence()
    
    def pod_signature(self):
        self.nav_pod()
        
        #Driver Signature
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Driver Signature').click()
        signature_element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(6)')
        location = signature_element.location
        size = signature_element.size
        x = location['x'] + size['width'] / 2
        y = location['y'] + size['height'] / 2
        
        
        actions = ActionChains(self.driver)
        # Move to the center of the signature element and start drawing
        actions.press(x=x, y=y).wait(100).move_to(x=x+270, y=y+1223).release().perform()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Clear Signature').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cancel').click()
        
    #NOTE: Navigation to do FAIL
    def nav_fail(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Fail').click()
        
        #Choose fail reason
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Fail Reason').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Store Closed'))).click()
        
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
        self.fail_attachment()
        self.remove_attachment()
        
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'SUBMIT').click()
        
        #Wait for the process to return back to homepage
        self.homePagePresence()
    
    def fail_attachment(self):
        #Take photo directly
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[1]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photos').click()
        self.driver.back()
    
        #Upload Do/Logsheet photo
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[1]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
                
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
        
        #Upload attachment
        for _ in range(2):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[2]'))).click()
                
            except TimeoutException:
                 print("Timeout: Elements did not appear within the expected time.")
            
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
                
            except TimeoutException:
                print("Timeout: Elements did not appear within the expected time.")
                self.driver.back()
    
    #NOTE: Navigation to do DELAY
    def nav_delay(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delay').click()
        
        #Choose delay reason
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Delay Reason:').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Truck breakdown'))).click()
        
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
        self.delay_attachment()
        self.remove_attachment()
        
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'SUBMIT').click()
        
        #Wait for the process to return back to homepage
        self.homeScreenPresence()
    
    def delay_attachment(self):
        #Take photo directly
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photo').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photos').click()
        self.driver.back()
    
        #Upload attachment
        for _ in range(2):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photo'))).click()

            except TimeoutException:
                 print("Timeout: Elements did not appear within the expected time.")
            
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
                
            except TimeoutException:
                print("Timeout: Elements did not appear within the expected time.")
                self.driver.back()
    
    def remove_logsheetPhoto(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView'))).click()

        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
    def remove_attachment(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]'))).click()

        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
    #NOTE: Get latest element that been display at the UI
    def get_DisplayedDocket(self):
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
            print("Timeout: Elements did not appear within the expected time.")