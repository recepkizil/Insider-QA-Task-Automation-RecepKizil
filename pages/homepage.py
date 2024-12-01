import pytest
from pages.basepage import *
from constants.homepage_constants import *

@pytest.mark.usefixtures("setup")
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_navbar_company(self):
        self.click_element(COMPANY)
    
    def click_careers_option(self):
        self.click_element(CAREERS)
