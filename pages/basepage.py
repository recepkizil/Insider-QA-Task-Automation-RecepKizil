from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.homepage_constants import *
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def wait_element_visibility(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
    
    def wait_elements_visibility(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locator))

    def wait_element_text(self, locator, text, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def scroll_until_element(self, locator):
        ActionChains(self.driver).move_to_element(self.wait_element_visibility(locator)).perform()

    def scroll_and_click_to_element(self, locator):
        ActionChains(self.driver).move_to_element(self.wait_element_visibility(locator)).click().perform()
    
    def click_element(self, locator):
        self.wait_element_visibility(locator).click()

    def get_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def switch_to_window(self,page):
        self.driver.switch_to.window(self.driver.window_handles[page])

    def accept_all_cookies(self):
        self.click_element(ACCEPT_ALL_COOKIES)
    
    def get_element_index(self, locator, index):
        return self.find_elements(locator)[index]
    