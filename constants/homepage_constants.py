from selenium.webdriver.common.by import By

BASE_URL = "https://useinsider.com/"

ACCEPT_ALL_COOKIES = (By.ID, "wt-cli-accept-all-btn" )
COMPANY =  (By.CSS_SELECTOR, "ul li:nth-child(6)" )
CAREERS =  (By.CSS_SELECTOR, ".new-menu-dropdown-layout-6-mid-container a:nth-of-type(2)")
COMPANY_NAVBAR = (By.CSS_SELECTOR, "#navbarDropdownMenuLink")
CAREERS_BUTTON = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li.nav-item.dropdown.show > div > div.new-menu-dropdown-layout-6-mid-container > a:nth-child(2)")
