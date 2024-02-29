from time import sleep
import pdb
from base.selenium_driver import SeleniumDriver
from locators.flight_search import FlightSearch

class BasePage(SeleniumDriver):
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
        
    def close_login_modal(self):
        self.elementClick(FlightSearch.login_modal_close_button)