import pytest
from pages.basepage import *
from constants.careers_page_constants import *
from time import sleep

@pytest.mark.usefixtures("setup")
class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def scroll_to_teams_section(self):
        self.scroll_until_element(TEAMS_SECTION)
        
    def click_see_all_teams(self):
        self.click_element(SEE_ALL_TEAMS)
        sleep(3)
    
    def wait_for_all_teams_visible(self):
        self.scroll_until_element(LAST_TEAM)

    def scroll_to_our_locations_section(self):
        self.scroll_until_element(OUR_LOCATIONS_SECTION)
        self.scroll_down(700)

    def navigate_between_locations(self):
        for _ in range(10):
            self.click_element(NAVIGATE_FORWARD_BUTTON)
    
    def scroll_to_life_at_insider_section(self):
        sleep(2)
        self.scroll_until_element(LIFE_AT_INSIDER_SECTION)
        self.scroll_down(700)
        
    

    
