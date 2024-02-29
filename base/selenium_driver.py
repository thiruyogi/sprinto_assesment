import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pdb

class SeleniumDriver():
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def getElement(self, locator):
        element = self.driver.find_element(*locator)
        return element
    
    def getElementsList(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements
    
    def elementClick(self, locator):
        element = self.getElement(locator)
        element.click()
        
    def sendKeys(self, locator, value):
        element = self.getElement(locator)
        element.send_keys(value)
    
    def isElementDisplayed(self, locator):
        element = self.getElement(locator)
        return element.is_displayed()
    
    def clearField(self, locator):
        element = self.getElement(locator)
        while len(element.get_attribute('value'))>0:
            element.send_keys(Keys.BACK_SPACE)
        time.sleep(1)
    
    def clearAndSendKeys(self, locator, value):
        self.clearField(locator)
        self.sendKeys(locator, value)
        
    def getText(self, locator):
        element = self.getElement(locator)
        return element.text
    
    def clickOnElement(self, element):
        element.click()