import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from pages.iod.home_page import StaffHomePage


class ReportsPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        load_dotenv()
        self.report_dateFrom = os.getenv("REPORT_DATEFROM")
        self.report_dateTo = os.getenv("REPORT_DATETO")
        self.driver = driver
        self.homepage = StaffHomePage(self.driver)
    
    #Main process for iod report
    def iod_report(self) -> list:
        self.errorList = []
 
        errNav = self.nav_report()
        if errNav == None: 
            self.check_form()
            
            errForm = self.iod_form_data()
            if errForm != None: return(errForm)
            
            errTruck =  self.iod_filter_truckNo()
            if errTruck != None: self.errorList.append(errTruck)
            
            errSupp = self.iod_filter_supplierName()
            if errSupp != None: self.errorList.append(errSupp)
            
            errLate = self.iod_filter_lateDeliveryFor()
            if errLate != None: self.errorList.append(errLate)
            
            errZone = self.iod_filter_zone()
            if errZone != None: self.errorList.append(errZone)
            
            errSort = self.iod_lateDays_orderBy()
            if errSort != None: self.errorList.append(errSort)
            
            time.sleep(2)
            
        else: 
            self.errorList.append(errNav)

        return self.errorList

        
    #Main process for general report   
    def general_report(self):
        self.errorList = []

        errChange = self.change_report()
        if errChange == None:
            self.check_form()
            
            errForm = self.general_form_data()
            if errForm != None: self.errorList.append(errForm)

            errTruck = self.general_filter_truckNo()
            if errTruck != None: self.errorList.append(errTruck)
            
            errSupplier = self.iod_filter_supplierName()
            if errSupplier != None: self.errorList.append(errSupplier)
            
            errZone = self.general_filter_zone()
            if errZone != None: self.errorList.append(errZone)
            
            errPickup = self.general_filter_pickupPoint()
            if errPickup != None: self.errorList.append(errPickup)
            
            errJob = self.general_filter_job()
            if errJob != None: self.errorList.append(errJob)
            
            errEst = self.general_filter_est()
            if errEst != None: self.errorList.append(errEst)
            
            self.driver.back()
            self.homepage.load_staffHome()
            
        else: 
            self.driver.back()
            return(errChange)
        
        return self.errorList
        
    
    def nav_report(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Report'))).click()
            
        except TimeoutException:
            return("TimeoutException: unable to locate [Report button]")
    
    def change_report(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'General Report'))).click()
            self.driver.find_element(AppiumBy.XPATH, '(//android.view.View[@content-desc="General Report"])[1]').click()
                  
        except TimeoutException:
            return("TimeoutException: unable to locate [Report option]")

    #Check if search form visible or not
    def check_form(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Submit')))
            
        except TimeoutException:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)').click()

    #IOD report form
    def iod_form_data(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Show Truck No'))).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit').click()
            time.sleep(5)
            
        except TimeoutException:
            return("TimeoutException: unable to locate some element[IOD report form]")

    #Filter based on Truck No
    def iod_filter_truckNo(self) -> str:
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
                        truck_numbers.append(item.get_attribute('content-desc'))
                        
            for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, truck_numbers[i]).click()
            
            self.driver.back()
            time.sleep(2)

            err = self.reset_filter()
            if err != None: return(err)
            
        except TimeoutException:
            return("TimeoutException: unable to locate [Filter TruckNo]")
            
    #Filter based on Supplier Name
    def iod_filter_supplierName(self) -> str:
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
                        supplier_Names.append(item.get_attribute('content-desc'))
                        
            for i in range(2):
                    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, supplier_Names[i]).click()
                    
            self.driver.back()
            time.sleep(2)

            err = self.reset_filter()
            if err != None: return(err)

        except:
            return("TimeoutException: unable to locate [Filter SupplierName]")

    #Filter based on Later Delivery For
    def iod_filter_lateDeliveryFor(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Late Delivery'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Less than 14 Days'))).click()
            
            self.driver.back()
            time.sleep(2)
            
            err = self.reset_filter()
            if err != None: return(err)
            
        except TimeoutException:
            return("TimeoutException: unable to locate some elemenets in [Filter Late Delivery For]")
     
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
                        zone_list.append(item.get_attribute('content-desc'))
            
            for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, zone_list[i]).click()
                
            self.driver.back()
            time.sleep(2)
            
            err = self.reset_filter()
            if err != None: return(err)
            
        except TimeoutException:
            return("TimeoutException: unable to locate some elements in [Filter Zone]")
          
    def iod_lateDays_orderBy(self):
        #Multiple taps to show desc & asc order
        for _ in range(3):
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Late Days'))).click()
            
    def general_form_data(self) -> str:
        try:
            # Insert Customer name
            customerName = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
            customerName.click()
            customerName.clear()
            customerName.send_keys('DAIKIN')
            self.driver.hide_keyboard()
            
            # Pick Date From
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]'))).click()

            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Select year'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '2023'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'OK'))).click()

            # Pick Date To
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'OK'))).click()

            # Click show truck no
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Truck No').click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit').click()
            time.sleep(5)
            
        except TimeoutException:
            return("TimeoutException: unable to locate some element in [General Form Data]]")

    #Filter truck no
    def general_filter_truckNo(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Truck No"])[1]'))).click()
            
            try:
                # Locate the ScrollView container
                scroll_view  = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ScrollView')))

                # Find all direct child views within the ScrollView
                all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

                truck_numbers = []
                for item in all_items:
                    if item.is_displayed():
                        if item.get_attribute('content-desc') != "Show All":
                            truck_numbers.append(item.get_attribute('content-desc'))

                for i in range(2):
                        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, truck_numbers[i]).click()

                self.driver.back()
                time.sleep(2)
                
                err = self.reset_filter()
                if err != None: return(err)
                
            except TimeoutException:
                self.driver.back()
                return("TimeoutException: unable to locate list of truck No")
        
        except:
            return("TimeoutException: unable to locate some elements in [Filter TruckNo]")
    
    #Filter zone   
    def general_filter_zone(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Zone"]'))).click()
            
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'CENTRE PAHANG'))).click()

            self.driver.back()
            time.sleep(2)
            
            err = self.reset_filter()
            if err != None: return(err) 
            
        except TimeoutException:
            return("TimeoutException: unable to locate some element in [Filter Zone]")
    
    #Filter pickup point
    def general_filter_pickupPoint(self) -> str:
        try:
            #Tap the job filter and swipe to left
            el = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Zone"]')))
            actions = ActionChains(self.driver)
            x = -600
            y = 0
            
            actions.move_to_element(el)
            actions.click_and_hold().move_by_offset(xoffset=x, yoffset=y).release().perform()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Pickup Point"]'))).click()
                
                try:
                    # Locate the ScrollView container
                    scroll_view  = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ScrollView')))

                    # Find all direct child views within the ScrollView
                    all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

                    pickup_list = []
                    for item in all_items:
                        if item.is_displayed():
                            if item.get_attribute('content-desc') != "Show All":
                                pickup_list.append(item.get_attribute('content-desc'))

                    for i in range(2):
                            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, pickup_list[i]).click()

                    self.driver.back()
                    time.sleep(2)
                    
                    err = self.reset_filter()
                    if err != None: return(err)
                    
                except TimeoutException:
                    self.driver.back()
                    return("TimeoutException: unable to locate list of pickup point")
                 
            except TimeoutException:
                return("TimeoutException: unable to locate some element in [Filter Pickup Point]")
            
        except TimeoutException:
            return("TimeoutException: unable to slide to shows element")
                     
    #Filter Job  
    def general_filter_job(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Job %"])[1]'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '60% to 90%'))).click()

            self.driver.back()
            time.sleep(2)
            
            err = self.reset_filter()
            if err != None: return(err)
        
        except TimeoutException:
            return("TimeoutException: unable to locate some elements in [Filter Job]")

    #Filter Est
    def general_filter_est(self) -> str:
        try:  
            
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Est %"])[1]'))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, '60% to 90%'))).click()
            
            self.driver.back()
            time.sleep(2)
            
            err = self.reset_filter()
            if err != None: return(err)
            
        except TimeoutException:
            return("TimeoutException: unable to locate some elements in [Filter Est]")
        
    def reset_filter(self) -> str:
        try:
            #NOTE: Reset filter
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.Button[2]'))).click()
            
        except TimeoutException:
            return("TimeoutException: unable to locate element [Reset Filter]")