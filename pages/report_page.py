import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from pages.home_page import StaffHomePage


class ReportsPage:
    load_dotenv()
    report_dateFrom = os.getenv("REPORT_DATEFROM")
    report_dateTo = os.getenv("REPORT_DATETO")
    
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.homepage = StaffHomePage(self.driver)
    
    #Main process for iod report
    def iod_report(self):
        self.nav_report()
        self.check_form()
        self.iod_form_data()
        self.iod_filter_truckNo()
        self.iod_filter_supplierName()
        self.iod_filter_lateDeliveryFor()
        self.iod_filter_zone()
        self.iod_lateDays_orderBy()
        time.sleep(2)
    
    #Main process for general report   
    def general_report(self):
        self.change_report()
        self.check_form()
        self.general_form_data()
        self.general_filter_truckNo()
        self.iod_filter_supplierName()
        self.general_filter_job()
        self.general_filter_est()
        self.driver.back()
        self.homepage.load_staffHome()
    
    def nav_report(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Report'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Report]")
    
    def change_report(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'General Report'))).click()
            self.driver.find_element(AppiumBy.XPATH, '(//android.view.View[@content-desc="General Report"])[1]').click()
                  
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Report option]")


    #Check if search form visible or not
    def check_form(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Submit')))
            
        except TimeoutException:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)').click()

    #IOD report form
    def iod_form_data(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Truck No').click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit').click()

        time.sleep(5)

    #Filter based on Truck No
    def iod_filter_truckNo(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Truck No"])[1]'))).click()
            
            # Locate the ScrollView container
            scroll_view = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView')

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            truck_numbers = []
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        truck_number = item.get_attribute('content-desc')
                        truck_numbers.append(truck_number)
                        
            
            for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, truck_numbers[i]).click()

            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
            time.sleep(2)
            
            #NOTE: Reset filter
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Filter TruckNo]")
        
            
    #Filter based on Supplier Name
    def iod_filter_supplierName(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Supplier Name'))).click()
            
            # Locate the ScrollView container
            scroll_view = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView')

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            supplier_Names = []
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        supplier_Name = item.get_attribute('content-desc')
                        supplier_Names.append(supplier_Name)
                        
            for i in range(2):
                    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, supplier_Names[i]).click()

            self.driver.back()
            time.sleep(2)

            #NOTE: Reset filter
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)'))).click()

        except:
            raise ValueError("TimeoutException: unable to located [Filter SupplierName]")

    #Filter based on Later Delivery For
    def iod_filter_lateDeliveryFor(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Late Delivery'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Less than 14 Days'))).click()
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
            time.sleep(2)
            
            #Reset back to show all
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Less than 14 Days'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Show All'))).click()
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located some elemenets in [Filter Late Delivery For]")
     

    #Filter based on Zone    
    def iod_filter_zone(self):
        try:
            #Tap the late delivery filter and swipe to left
            el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Late Delivery"]')))
            actions = ActionChains(self.driver)
            x = -400
            y = 0
            
            actions.move_to_element(el)
            actions.click_and_hold().move_by_offset(xoffset=x, yoffset=y).release().perform()
            
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Zone'))).click()
            
            # Locate the ScrollView container
            scroll_view  = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ScrollView')))

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            zone_list = []
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        zone = item.get_attribute('content-desc')
                        zone_list.append(zone)
            
            for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, zone_list[i]).click()
            
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
            time.sleep(2)
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located some elements in [Filter Zone]")
        
          
    def iod_lateDays_orderBy(self):
        #Multiple taps to show desc & asc order
        for _ in range(3):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Late Days').click()
        
    def general_form_data(self):
        try:
            # Insert Customer name
            customerName = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
            customerName.click()
            customerName.send_keys('DAIKIN')
            self.driver.hide_keyboard()
            
            
            # Pick Date From
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')))
            
            for _ in range(5):
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()

            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.report_dateFrom))).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()

            
            # Pick Date To
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.report_dateTo))).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()


            # Click show truck no
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Truck No').click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit').click()
            time.sleep(5)
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located some element in [General Form Data]]")


    #Filter truck no
    def general_filter_truckNo(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Truck No"])[1]'))).click()
            
            # Locate the ScrollView container
            scroll_view  = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ScrollView')))

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            truck_numbers = []
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        truck_number = item.get_attribute('content-desc')
                        truck_numbers.append(truck_number)

            for i in range(2):
                    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, truck_numbers[i]).click()

            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
            time.sleep(2)
            
            #NOTE: Reset filter
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)'))).click()
        
        except:
            raise ValueError("TimeoutException: unable to located some elements in [Filter TruckNo]")
            
            
    #Filter Job  
    def general_filter_job(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Job %"])[1]'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '60% to 90%'))).click()

            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
            time.sleep(2)

            #NOTE: Reset filter
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)'))).click()
        
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located some elements in [Filter Job]")

    
    #Filter Est
    def general_filter_est(self):
        try:
            #Tap the job filter and swipe to left
            el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Job %"])[1]')))
            actions = ActionChains(self.driver)
            x = -400
            y = 0
            
            actions.move_to_element(el)
            actions.click_and_hold().move_by_offset(xoffset=x, yoffset=y).release().perform()
            
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Est %"])[1]'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '60% to 90%'))).click()
            
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
            time.sleep(2)
            
            #NOTE: Reset filter
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located some elements in [Filter Est]")