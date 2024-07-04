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
        self.general_filter_jobNo()
        time.sleep(2)
        self.driver.back()
        self.homepage.load_staffHome()
    
    def nav_report(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Report'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Report]")
    
    def change_report(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'General Report').click()
        self.driver.find_element(AppiumBy.XPATH, '(//android.view.View[@content-desc="General Report"])[1]').click()

    #NOTE:Check if search form visible or not
    def check_form(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Submit')))
            
        except TimeoutException:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)').click()

    def iod_form_data(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Truck No').click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit').click()

        time.sleep(5)

    #NOTE:Filter based on Truck No
    def iod_filter_truckNo(self):
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Truck No"])[1]').click()

        try:
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

        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Filter TruckNo]")
            
        for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, truck_numbers[i]).click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)

        #NOTE: Reset filter
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()
    
    #NOTE:Filter based on Supplier Name
    def iod_filter_supplierName(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Supplier Name').click()

        try:
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

        except:
            raise ValueError("TimeoutException: unable to located [Filter SupplierName]")

        for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, supplier_Names[i]).click()

        self.driver.back()
        time.sleep(2)

        #NOTE: Reset filter
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()

    #NOTE:Filter based on Later Delivery For
    def iod_filter_lateDeliveryFor(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Late Delivery').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Less than 14 Days').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)
        
        #NOTE: Reset filter
        #TODO: Fix reset filter at FE for late delivery
        # self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Less than 14 Days').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show All').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()

    #NOTE:Filter based on Zone    
    #TODO: Fix Reset filter at FE at FE for zone
    def iod_filter_zone(self):
        el = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Late Delivery"]')
        
        actions = ActionChains(self.driver)
        x = -400
        y = 0
        
        #Tap the late delivery filter and swipe to left
        actions.move_to_element(el)
        actions.click_and_hold().move_by_offset(xoffset=x, yoffset=y).release().perform()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Zone'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Filter Zone]")
        
        try:
            # Locate the ScrollView container
            scroll_view = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView')

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            zone_list = []
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        zone = item.get_attribute('content-desc')
                        zone_list.append(zone)

        except:
            raise ValueError("TimeoutException: unable to located [Zone line]")
        
        for i in range(2):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, zone_list[i]).click()
            
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)
        
    def iod_lateDays_orderBy(self):
        #NOTE: Multiple taps to show desc & asc order
        for _ in range(3):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Late Days').click()
        
    def general_form_data(self):
        # Insert Customer name
        try:
            customerName = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
            customerName.click()
            customerName.send_keys('DAIKIN')
            self.driver.hide_keyboard()

        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Text field]")
  
        # Pick Date From
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')))
            
            for _ in range(5):
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.report_dateFrom).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()
                
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Date From]")
        
        # Pick Date To
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.report_dateTo))).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()

        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Date To]")

        # Click show truck no
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Truck No').click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit').click()

        time.sleep(5)

    def general_filter_truckNo(self):
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Truck No"])[1]').click()

        try:
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

        except:
            raise ValueError("TimeoutException: unable to located [Filter TruckNo]")
            
        for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, truck_numbers[i]).click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)
        
        #NOTE: Reset filter
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()

    def general_filter_jobNo(self):
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Job %"])[1]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '60% to 90%').click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)

        #NOTE: Reset filter
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()
        
       
