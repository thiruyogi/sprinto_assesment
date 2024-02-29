from selenium.webdriver.common.by import By

class FlightSearch:
    login_modal_close_button = (By.XPATH,"//div[contains(@class,'px-8')]//div[contains(@class,'px-1')]")
    where_from_dropdown = (By.XPATH,"//input[@placeholder='Where from?']")
    where_to_dropdown = (By.XPATH,"//input[@placeholder='Where to?']")
    search_flights_button = (By.XPATH,"//span[contains(text(),'Search flights')]")
    start_date_picker = (By.XPATH,"//div[contains(@class,'homeCalender')]/button/div[contains(@class,'inherit')]")
    flight_fares = (By.XPATH, "//div[@data-ct-handle='solutionPrice']//p")
    flight_blocks = (By.XPATH, "//div[@data-testid='airlineBlock']//button[text()='Book']")
    review_itinerary_header = (By.XPATH,"//h2[contains(text(),'Review your itinerary')]")
    no_flights_message = (By.XPATH, "//p[contains(text(),'Please reset your filters to see flights')]")
    
    @classmethod
    def airportDropdownValue(self, airportVenue):
        return (By.XPATH,"//ul[contains(@class,'airportList')]//p[contains(text(),'{0}')]".format(airportVenue))
    
    @classmethod
    def dateValue(self, date):
        return (By.XPATH,"//div[@aria-label='{0}']".format(date))
    
    @classmethod
    def bookFlightButton(self, fare):
        return (By.XPATH,"//p[contains(text(),'6,355')]/ancestor::div[contains(@class,'container__details__price')]/following-sibling::div//button")