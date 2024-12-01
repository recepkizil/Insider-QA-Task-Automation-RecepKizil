import pytest
from pages.basepage import *

@pytest.mark.usefixtures("setup")
class ApplicationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def switch_to_application_page(self):
        self.switch_to_window(1)