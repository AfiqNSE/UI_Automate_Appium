import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class IODComponents:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        load_dotenv()
        self.estDate = os.getenv("EST_DATE")
        self.estTime = os.getenv("EST_TIME")
        self.driver = driver
        self.new_dockets = []
        self.all_details  = []
        self.sign_accessibilityID = ''
        self.est_accessibilityID = ''
    
    #NOTE: This code is to use cancel button at UI
    def cancelButton(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.nse.project.nse_driver_flutter_app:id/btnBarcodeCaptureCancel"]').click()
    
    #Back Button
    def backButton(self):
        self.driver.find_element(by=AppiumBy.XPATH, value='Back').click()

    #Submit button
    def submitButton(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'SUBMIT'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to located [Submit Button]")
        
    #SideBar for driver page
    def nav_sideBar(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu'))).click()
        
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Navigation Menu]")
    
    
    def nav_estDateTime(self, docket):
        try:
            #NOTE: set single estDateTime docket
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, docket))).click()
            
            accessibilityID = self.get_displayedDetails()
            if accessibilityID != {}:
                
                err = self.single_estDateTime(accessibilityID)
                if err is None:
                    self.submitButton()
                    time.sleep(2)
                    self.driver.back()
                    
                else:
                    self.driver.back()
                    print(err)
        
                err = self.all_estDateTime(docket)
                if err is None:
                    self.submitButton()
                    time.sleep(2)
                    self.driver.back()
                    
                else:    
                    self.driver.back()
                    print(err)

            else: 
                self.driver.back()
                return("Error: Unable to get docket details")
            
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate element [New Docket]")
        
    #NOTE: #Est date time for docket details  
    def single_estDateTime(self, accessibilityID) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibilityID["est"]))).click()
                  
            actions = ActionChains(self.driver)

            #Set Date
            actions.w3c_actions.pointer_action.move_to_location(x=500, y=1050)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pointer_up()
            actions.perform()
                    
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'OK'))).click()
                
            except TimeoutException:
                self.driver.back()
                return("TimeoutException: Element (OK) did not appear within the expected time.")
            
            #Set Time
            actions.w3c_actions.pointer_action.move_to_location(x=500, y=1240)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pointer_up()
            actions.perform()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'AM'))).click()    
                        
            except TimeoutException:
                self.driver.back()
                return("Timeout: Element (AM) did not appear within the expected time.")
             
        except TimeoutException:
            return("TimeoutException: Unable to locate some element [Est date time]")
    
    #NOTE: #Est date time for all dockts
    def all_estDateTime(self, docket) -> str:

        errActive = self.active_selectMode(docket=docket)
        if errActive is None: 
            
            errSelect = self.select_all()
            if errSelect is None:
                
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]'))).click()
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'OK'))).click()

                except TimeoutException:
                    return("TimeoutException: unable to located [Date]")
                
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Estimate arrival time\nSelect time'))).click()
                    
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'PM'))).click()

                except TimeoutException:
                    return("TimeoutException: unable to located [Time]")
                
            else:
                return errSelect
            
        else:
            return errActive
        
    def nav_viewSignature(self) -> str:
        accessibilityID = self.get_displayedDetails()
        if accessibilityID != {}:
            
            try:
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibilityID["signature"]))).click()
                time.sleep(2)
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Close').click()
                
            except TimeoutException:
                return("Timeout: Elements (Signature) did not appear within the expected time.")
            
        else:
            return("TimeoutException: unable to locate [Docket details]")
    
    def nav_docketPreview(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Preview'))).click()
            
            try:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))
                
                time.sleep(2)
                
                for _ in range(2):
                    self.driver.back()
            
            except TimeoutException:
                
                self.driver.back() 
                return("Timeout: Elements (Docket Image) did not appear within the expected time.")
            
        except TimeoutException:
            
            self.driver.back()  
            return("TimeoutException: unable to located [Docket preview]")
    
    #Click POD option
    def nav_pod(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'POD'))).click()

        except TimeoutException:
            self.driver.back
            return("Timeout: Element (POD button did not appear within the expected time.")
        
    def pod_photo(self) -> str:
        err = self.nav_pod()
        if err is None:
            
            try:
                #Take photo directly
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photos'))).click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
                
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()
                
            except TimeoutException:
                for _ in range(3):
                    self.driver.back()
                    
                return("TimeoutException: Unable to perform [pod photo]")
            
        else:
            return err
        
    def pod_upload(self) -> str:
        err = self.nav_pod()
        if err is None:
            
            try:
                #Upload Photo
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Upload Photo'))).click()
                
                images = self.get_images()
                if len(images) > 0:
                    
                    try:
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, images[0]))).click()
                        
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()
 
                    except TimeoutException:
                        self.driver.back()
                        return("Timeout: Element (Image) did not appear within the expected time.")
                    
                else:
                    self.driver.back()
                    return("No images found in the directory.")
                
            
            except TimeoutException:
                for _ in range(3):
                    self.driver.back()
                    
                return("TimeoutException: Unable to perform [pod upload]]")
            
        else:
            return err
            
    def pod_signature(self) -> str:
        err = self.nav_pod()
        if err is None:
            
            try:
                #Driver Signature
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Driver Signature'))).click()
                
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
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()

            except TimeoutException:
                for _ in range(3):
                    self.driver.back()
                    
                return("TimeoutException: Unable to perform [pod signature]]")

        else:
            return err
        
    #NOTE: Navigation to do FAIL
    def nav_fail(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Fail'))).click()
            
            #Choose fail reason
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Fail Reason').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Store Closed'))).click()
                
                errFail = self.fail_attachment()
                if errFail is None: 
                    
                    errRev = self.remove_attachment()
                    if errRev is not None: print(errRev)
                        
                    errEst = self.est_fail_delay()
                    if errEst is None:
                        self.submitButton()
                        
                    else:
                        for _ in range(2):
                            self.driver.back()
                        return errEst
                else:
                    for _ in range(2):
                        self.driver.back()
                    return errFail
                
            except TimeoutException:
                
                for _ in range(2):
                    self.driver.back()
                    
                return("TimeoutException: Unable to locate [Store Closed]")
            
        except TimeoutException: 
            self.driver.back
            return("TimeoutException: Unable to locate [Fail Button]")
          
    def fail_attachment(self) -> str:
        try:
            #Upload Do/Logsheet photo
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[1]'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photos'))).click()

            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
                
            except TimeoutException:
                self.driver.back()
                return("TimeoutException: Unable to locate [shutter icon]")    
        
            time.sleep(2)
            
            #Upload attachment
            for _ in range(2):
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[2]'))).click()
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Upload Photo'))).click()

                    images = self.get_images()
                    if len(images) > 0:
                        
                        try:
                            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, images[0]))).click()
                            
                        except TimeoutException:
                            self.driver.back()
                            return("Timeout: Element (Image) did not appear within the expected time.")
                        
                    else:
                        self.driver.back()
                        return("No images found in the directory.")
                    
                except TimeoutException:
                    self.driver.back()
                    return("TimeoutException: Element (Upload Photo) did not appear within the expected time.")
                
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Element (Take Photo) did not appear within the expected time.")
    
    #NOTE: Navigation to do DELAY
    def nav_delay(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Delay'))).click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Select Delay Reason:'))).click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Truck breakdown'))).click()
                
                errDelay = self.delay_attachment()
                if errDelay is None:
                    
                    errRev = self.remove_attachment()
                    if errRev is not None: print(errRev)
                    
                    errEst = self.est_fail_delay()
                    if errEst is None:
                        self.submitButton()
                        
                    else:
                        for _ in range(3):
                            self.driver.back()
                            
                        return errEst
                    
                else:
                    for _ in range(2):
                        self.driver.back()
                    return errDelay 
                
            except TimeoutException:
                
                for _ in range(2):
                    self.driver.back()
                    
                return("TimeoutException: Unable to locate [Truck breakdown]")
            
        except TimeoutException:
            self.driver.back
            return("TimeoutException: Unable to locate [Delay Button]")
            
    def delay_attachment(self):
        try:
            #Take photo directly
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photo'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photos'))).click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
                
            except TimeoutException:
                self.driver.back()
                return("TimeoutException: Unable to locate [shutter icon]")

            time.sleep(2)
            
            #Upload attachment
            for _ in range(2):
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photo'))).click()
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Upload Photo'))).click()
                    
                    images = self.get_images()
                    if len(images) > 0:
                        
                        try:
                            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, images[0]))).click()
                            
                        except TimeoutException:
                            self.driver.back()
                            return("Timeout: Element (Image) did not appear within the expected time.")
                        
                    else:
                        self.driver.back()
                        return("No images found in the directory.")
                    
                except TimeoutException:
                    self.driver.back()
                    return("Timeout: Element (Upload Photo) did not appear within the expected time.")
            
            time.sleep(2)
              
        except TimeoutException:
            return("TimeoutException: Element (Take Photo) did not appear within the expected time.")

    def est_fail_delay(self) -> str:
        try:
            
            #TODO: Fix this
            #Set est date
            # try:
            #     WebDriverWait(self.driver,5).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[5]'))).click()
                
            # except TimeoutException:
            #     WebDriverWait(self.driver,5).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@text="2024-07-26"]'))).click()
                            
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'OK'))).click()
            
            #Set est time
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Select time'))).click()
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'AM'))).click()
            
            except TimeoutException:
                try:
                    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'AM'))).click()
                    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'PM'))).click()
                    
                except TimeoutException:
                    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'PM'))).click()
                    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'AM'))).click()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Est date time]")
        
    def remove_logsheetPhoto(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView'))).click()

        except TimeoutException:
            return("TimeoutException: Element (Image) did not appear within the expected time.")
            
    def remove_attachment(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView[3]'))).click()

        except TimeoutException:
            return("TimeoutException: Element (Image) did not appear within the expected time.")
        
    #Active Select Mode
    def active_selectMode(self, docket) -> str:
        try:
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, docket)))
            self.driver.execute_script('mobile: longClickGesture', {'elementId': element.id})
            
        except TimeoutException:
            return("TimeoutException: Unable to perform long press gesture")
    
    #Select All
    def select_all(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()
        
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Select All'))).click()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Select All]")

    #Deselect All
    def deselect_all(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()
        
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Deselect All'))).click()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Deselect All]")
    
    #Deactive Select Mode
    def deactive_selectMode(self) ->str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]'))).click()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Exit Select Mode]")
        
    #NOTE: Get latest element that been display at the UI
    def get_dockets(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            dockets = []
            for item in all_items:
                if item.is_displayed():
                    dockets.append(item.get_attribute("content-desc"))
            
            return dockets
            
        except TimeoutException:
            return []
            
    #NOTE: Get latest element that been display at the UI
    def get_new_dockets(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            new_dockets = []
            for item in all_items:
                if item.is_displayed():
                    docket = item.get_attribute("content-desc")
                    if "NEW" in docket:
                        new_dockets.append(docket)
            
            return new_dockets
            
        except TimeoutException:
            return []
    
    #NOTE: Get details elements that been display at the UI
    def get_displayedDetails(self):
        try:
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Docket Details')))

            # Find all direct child views within the ScrollView
            all_items = self.driver.find_elements(AppiumBy.XPATH, './/android.widget.Button')
            
            accessibilityID = {
                "signature": "",
                "est": "",
            }
            
            for item in all_items:
                if item.is_displayed():
                    detail = item.get_attribute("content-desc")
                    self.all_details.append(detail)
                    if "Signature" in detail:
                        accessibilityID["signature"] = detail
                    if "Estimation" in detail:
                        accessibilityID["est"] = detail
                        
            return accessibilityID   
                 
        except TimeoutException:
            return {}
        
    def get_month(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()
                    
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View')))
            
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View//android.widget.Button')
            
            month_list =  []
            for item in all_items:
                if item.is_displayed():
                    month_list.append(item.get_attribute('content-desc'))
                    
            return month_list
        
        except TimeoutException:
            return []
        
    def get_images(self):
        try:       
            el = WebDriverWait(self.driver,15).until(EC.presence_of_element_located((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.google.android.documentsui:id/dir_list"]')))
            
            all_items = el.find_elements(AppiumBy.XPATH, '//android.widget.LinearLayout')
            
            images_list =  []
            for item in all_items:
                if item.is_displayed():
                    images_list.append(item.get_attribute('content-desc'))
                    
            return images_list

        except TimeoutException:
            self.driver.back()
            return []
            
        

        
