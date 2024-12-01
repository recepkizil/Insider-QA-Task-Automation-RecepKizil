from selenium.webdriver.common.by import By

SEE_ALL_QA_JOBS_BUTTON = (By.CSS_SELECTOR, ".btn.btn-outline-secondary.mt-2.px-lg-5.py-3.rounded.text-medium.w-100.w-md-50")
DEPARTMENT_TEXT = (By.CSS_SELECTOR, "#select2-filter-by-department-container")
LOCATION_TEXT = (By.CSS_SELECTOR, "#select2-filter-by-location-container")
LOCATION_FILTER = (By.ID, "select2-filter-by-location-container")
ISTANBUL_OPTION = (By.XPATH, '//li[text()="Istanbul, Turkey"]')
POSITION_NAME = (By.CSS_SELECTOR, "#jobs-list > div > div > p")
DEPARTMENT_NAME = (By.CSS_SELECTOR, "#jobs-list > div > div > span")
LOCATION_NAME = (By.CSS_SELECTOR,"#jobs-list > div > div > div")
OPEN_POSITIONS = (By.CSS_SELECTOR, ".btn.btn-navy.pb-2.pl-5.pr-5.pt-2.rounded")
VIEW_ROLE_BUTTON = (By.CSS_SELECTOR,'a.btn.btn-navy.rounded.pt-2.pr-5.pb-2.pl-5')