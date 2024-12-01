import pytest
from pages.basepage import *
from constants.qa_page_constants import*
from time import sleep

@pytest.mark.usefixtures("setup")
class QAPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_see_all_qa_jobs(self):
        self.click_element(SEE_ALL_QA_JOBS_BUTTON)

    def select_location_istanbul(self):
        self.click_element(LOCATION_FILTER)
        self.wait_element_visibility(ISTANBUL_OPTION)
        self.click_element(ISTANBUL_OPTION)
    
    def select_department_quality_assurance(self):
        self.wait_element_text(DEPARTMENT_TEXT,'Quality Assurance')
        
    def scroll_to_open_positions(self):
        sleep(3)
        self.scroll_until_element(LOCATION_NAME)
    
    def get_view_rule_button_by_index(self):
        self.get_element_index(VIEW_ROLE_BUTTON, 0)
        self.scroll_and_click_to_element(VIEW_ROLE_BUTTON)
    