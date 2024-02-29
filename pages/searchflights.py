from locators.flight_search import FlightSearch
from pages.basePage import BasePage
import pdb

class FlightSearchPage(BasePage):
    def __init__(self, driver) -> None:
        super().__init__(driver)
        
    def search_flights(self,journey_details):
        for key,value in journey_details.items():
            if key == 'From':
                self.elementClick(FlightSearch.where_from_dropdown)
                self.clearAndSendKeys(FlightSearch.where_from_dropdown, value)
                self.elementClick(FlightSearch.airportDropdownValue(value))
            elif key == 'To':
                self.elementClick(FlightSearch.where_to_dropdown)
                self.clearAndSendKeys(FlightSearch.where_to_dropdown,value)
                self.elementClick(FlightSearch.airportDropdownValue(value))
            elif key == 'Start Date':
                self.elementClick(FlightSearch.start_date_picker)
                self.elementClick(FlightSearch.dateValue(value))
        self.elementClick(FlightSearch.search_flights_button)
        
    def book_cheapest_flight(self):
        flights = self.getElementsList(FlightSearch.flight_blocks)
        cheapest_flight = flights[0]
        self.clickOnElement(cheapest_flight)
        
    def verify_booking_page_landing(self):
        return self.isElementDisplayed(FlightSearch.review_itinerary_header)
    
    def verify_no_flights_message_displayed(self):
        return self.isElementDisplayed(FlightSearch.no_flights_message)
        
    