import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from components.iod_component import IODComponents

class LeaderboardPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = IODComponents(self.driver)

    def nav_leaderboard(self) -> str:
        self.scroll_analytics()
          
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Leaderboard'))).click()
            time.sleep(2)
            
            months = self.component.get_month()
            if len(months) > 0:   
                #Select first month
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, months[0]).click()
                time.sleep(2)      
                self.driver.back()
            
            else:
                self.driver.back()
                return("Alert: No months available") 

        except TimeoutException:
            return("TimeoutException: Unable to locate element [Leaderboard]")

        
    #Scroll to see leaderboard for small screen phone
    def scroll_analytics(self):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Assign\nPoints')))
        
        actions = ActionChains(self.driver)
        x = 800
        y = -1000

        actions.move_to_element(element)
        actions.click_and_hold()
        actions.move_by_offset(xoffset=x, yoffset=y)
        actions.release().perform()
        

