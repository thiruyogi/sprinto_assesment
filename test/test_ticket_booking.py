from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from expects import *
from base.BaseClass import BaseClass
from pages.searchflights import FlightSearchPage
import pytest
import pdb
from datetime import date 
from datetime import timedelta

class TestLogin(BaseClass):
    
    @pytest.fixture(scope='class',autouse=True)
    def beforeAllSetup(self,setup):
        self.__class__.flightSearch = FlightSearchPage(self.driver)

    def test_search_flight(self):
        self.flightSearch.close_login_modal()
        journey_details = {
            'From' : 'Bangalore',
            'To' : 'New Delhi',
            'Start Date' : (date.today()+timedelta(days=7)).strftime('%a %b %d %Y' )
        }
        self.flightSearch.search_flights(journey_details)
        # self.flightSearch.book_cheapest_flight()
        # expect(self.flightSearch.verify_booking_page_landing).to(be_true)
        expect(self.flightSearch.verify_no_flights_message_displayed()).to(be_true)