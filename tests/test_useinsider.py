import pytest
from time import sleep
from pages.basepage import *
from pages.homepage import *
from pages.careers_page import *
from pages.qa_page import *
from pages.application_page import *
from constants import homepage_constants, careers_page_constants, qa_page_constants, application_page_constants

@pytest.mark.usefixtures("setup")
class TestInsider:
    def test_useinsider(self):
        basepage = BasePage(self.driver)
        homepage = HomePage(self.driver)
        careerspage = CareersPage(self.driver)
        qa_page = QAPage(self.driver)
        application_page = ApplicationPage(self.driver)

        #tüm çerezleri kabul et
        homepage.accept_all_cookies()

        #Anasayfanın açıldığını doğrula
        assert self.driver.current_url == "https://useinsider.com/", f"Expected 'https://useinsider.com/', but found '{self.driver.current_url}'"
        basepage.take_screenshot("screenshots/anasayfanin_acildigi_dogrulanmistir.png")
        
        #Company navigation barının görüntülendiği doğrulanır
        company_navbar = homepage.wait_element_visibility(homepage_constants.COMPANY_NAVBAR)
        assert company_navbar, "Company button is not visible on the homepage."
        #company navigation butonuna tıklanır
        homepage.click_navbar_company()
        
        # "Careers" butonunun görüntülendiği doğrulanır
        careers_button = homepage.wait_elements_visibility(homepage_constants.CAREERS_BUTTON)
        assert careers_button, "Careers button is not visible on the homepage."
        #careers seçeneğine tıklanır
        homepage.click_careers_option()

        # "Careers" sayfasının açıldığı doğrulanır.
        assert self.driver.current_url == "https://useinsider.com/careers/", "Career page URL did not match."
        basepage.take_screenshot("screenshots/careers_sayfasinin_acildigi_dogrulanmistir.png")

        #Sayfa "Teams" bölümüne kaydırılır ve varlığı doğrulanır
        careerspage.scroll_to_teams_section()
        teams_section = careerspage.wait_element_visibility(careers_page_constants.TEAMS_SECTION)
        assert teams_section, "Teams section is not visible on the Careers page."
        basepage.take_screenshot("screenshots/teams_bolumu_goruntulenmistir.png")

        #See all teams bölümüne tıklayarak bölüm genişletilir
        careerspage.click_see_all_teams()

        #Son elemana kadar sayfa kaydırılır
        careerspage.wait_for_all_teams_visible()

        #15 adet olan takımın tamamımın görüntülendiği doğrulanır
        all_teams = basepage.wait_elements_visibility(careers_page_constants.TEAMS_COUNT)
        assert len(all_teams) == 15, "Not all teams are visible on the Careers page."

        #Sayfa "Our Locations" bölümüne kaydırılır ve varlığı doğrulanır
        careerspage.scroll_to_our_locations_section()
        our_locations_section = careerspage.wait_element_visibility(careers_page_constants.OUR_LOCATIONS_SECTION)
        assert our_locations_section, "Locations section is not visible on the Careers page."
        basepage.take_screenshot("screenshots/our_locations_sayfasinin_acildigi_dogrulanmistir.png")
        careerspage.navigate_between_locations()

        #Sayfa Life at Insider bölümüne kaydırılır ve varlığı doğrulanır
        careerspage.scroll_to_life_at_insider_section()
        life_at_insider_section = careerspage.wait_element_visibility(careers_page_constants.LIFE_AT_INSIDER_SECTION)
        assert life_at_insider_section, "Life at Insider section is not visible on the Careers page."
        basepage.take_screenshot("screenshots/life_at_insider_sayfasinin_acildigi_dogrulanmistir.png")

        #https://useinsider.com/careers/quality-assurance/ adresine gidilir ve sayfanın açıldığı doğrulanır
        basepage.get_url("https://useinsider.com/careers/quality-assurance/")
        assert self.driver.current_url == "https://useinsider.com/careers/quality-assurance/", "QA page URL did not match."
        
        #Açılan sayfada"See all QA jobs" butonuna tıklanır
        qa_page.click_see_all_qa_jobs()
        basepage.take_screenshot("screenshots/see_all_job_butonu_goruntulenmistir.png")

        #Department kısmının Quality Assurance olarak geldiği doğrulanır
        basepage.wait_element_text(DEPARTMENT_TEXT, 'Quality Assurance')
        assert (quality_assurance_title := basepage.wait_element_visibility(DEPARTMENT_TEXT)).get_attribute("title") == "Quality Assurance", f"Expected title: 'Quality Assurance', but found: '{quality_assurance_title.get_attribute('title')}'"
        
        #Location İstanbul seçilir ve seçimin yapıldığı doğrulanır
        qa_page.select_location_istanbul()
        assert (quality_assurance_title := basepage.wait_element_visibility(LOCATION_TEXT)).get_attribute("title") == "Istanbul, Turkey", f"Expected title: 'Quality Assurance', but found: '{quality_assurance_title.get_attribute('title')}'"
        
        #Pozisyon ve departmanın "Quality Assurance" içerdiği ve lokasyonun "Istanbul, Turkey" olduğu doğrulanır. 
        qa_page.scroll_to_open_positions()
        assert "Quality Assurance" in basepage.wait_element_visibility(POSITION_NAME).text, "Position name does not match expected"
        assert "Quality Assurance" in basepage.wait_element_visibility(DEPARTMENT_NAME).text, "Department name does not match expected"
        assert basepage.wait_element_visibility(LOCATION_NAME).text == "Istanbul, Turkey", "Location name does not match expected"
        basepage.take_screenshot("screenshots/pozisyon_departman_ve_konum_dogrudur.png")
        
        #View role butonuna tıklanır
        qa_page.get_view_rule_button_by_index()

        #Application sayfasına ulaşıldığı title'dan doğrulanır
        application_page.switch_to_application_page()
        expected_title = "Insider. - Senior Software Quality Assurance Engineer"
        actual_title = self.driver.title
        assert actual_title == expected_title,f"Başlık beklenenden farklı: Olması gereken {actual_title}"
        basepage.take_screenshot("screenshots/application_sayfasinin_acildigi_dogrulanmistir.png")