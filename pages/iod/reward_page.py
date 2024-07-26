import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from components.iod_component import IODComponents


class RewardPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = IODComponents(self.driver)
        
    def nav_reward(self) -> str:
        err = self.component.nav_sideBar()
        if err != None:
            return(err)
        
        try:
            #Navigate to reward page
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Reward"))).click()
            
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate element [Reward button]")

    #Driver leaderboard
    def nav_leaderboard(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Leaderboard'))).click()
            time.sleep(2)
           
            months = self.component.get_month()
            if months > 0:   
                #Select first month
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, months[0]).click()
                time.sleep(2)      
                self.driver.back()
            
            else:
                self.driver.back()
                return("Alert: No months available")
         
        except TimeoutException:
            return("TimeoutException: unable to locate element [Leaderboard button]")
    
    #Driver redeem
    def nav_redeem(self) -> str:
        valid = self.check_point()
        if valid == True:
            try:
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Redeem'))).click()
                
                err = self.redeem_slide()
                if err != None:
                    return(err)
                
                err = self.redeem_insert()
                if err != None:
                    return(err)
                
                self.driver.back()
                
            except TimeoutException:
                return("TimeoutException: unable to locate element [Redeem button]")
            
        else:
            return('Alert: No enough point to redeem')
           
    #Driver points history
    def nav_history(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'History'))).click()
            time.sleep(2)
           
            try:
               WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Earn\nTab 2 of 3'))).click()
               time.sleep(2)
               
               WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Redeem\nTab 3 of 3'))).click()
               time.sleep(2)
               
               WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'All\nTab 1 of 3'))).click()
               time.sleep(2)
               
               self.driver.back()
               
            except TimeoutException:
                self.driver.back()
                return("TimeoutException: unable to locate element [All/Earn/Redeem button]")
           
        except TimeoutException:
            return("TimeoutException: unable to locate element [History button]")
    
    #Check the driver points
    def check_point(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "Points")]')))

            element = self.driver.find_element(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "Points")]')
            point = element.get_attribute("content-desc").lstrip('Points: \n')
            
            print(point)
            if(int(point) > 1000):
                return True
            else:
                return False
            
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: unable to locate element [Points]")
    
    #Redeem by using slide
    def redeem_slide(self) -> str:
        try:
            slider_element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.SeekBar[@content-desc="0%"]')))
            
            actions = ActionChains(self.driver)
            x = 1
            y = 1490
            
            #Tap the slide and move to right
            actions.move_to_element(slider_element).click_and_hold()
            actions.move_by_offset(xoffset=x, yoffset=y).release().perform()
            
            self.redeem_button()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Dismiss').click()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: unable to locate element [Slide]")
    
    #Redeem by insert number        
    def redeem_insert(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'ENTER AMOUNT'))).click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('500')        
            IODComponents.submitButton(self)
                
            self.redeem_button()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Dismiss').click()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: unable to locate element [Enter Amount]")
              
    def redeem_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'REDEEM').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'REDEEM').click()

        