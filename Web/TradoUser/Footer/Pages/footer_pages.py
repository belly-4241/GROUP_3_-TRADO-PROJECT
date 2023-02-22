
from Web.TradoUser.Footer.Locators.footer_link_locators import Xpath_footer_links
from Web.TradoUser.Base.base_test import BaseSetups
from selenium.webdriver.common.by import By


class ALL_TESTS_FOOTER_LINKS(BaseSetups, Xpath_footer_links):
    def click_on_accessiblity_statement_then_verify_accessibility_page_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.ACCESSIBILITY_STATEMENT)

    def click_on_Payment_solutions_then_verify_accessibility_page_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.PAYMENT_SOLUTION)

    def Validating_click_on_Facebook_link_display_facebook_home_page(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.FACEBOOK)

    def Validating_click_on_Instagram_link_display_Instagram_home_page(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.INSTAGRAM)

    def Validating_click_on_Twitter_link_display_Twitter_home_page(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.TWITTER)

    def Validating_click_on_common_questions_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.COMMEN_QUESTION)

    def Validating_click_on_how_does_shipping_work_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.HOW_SHIPPING_WORK)

    def Validating_click_on_payment_solutions_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.PAYMENT_SOLUTION)

    def Validating_click_on_MAX_for_business_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.MAX_BUSSINESS)

    def Validating_click_on_Who_we_are_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.WHO_WE_ARE)

    def Validating_click_on_my_account_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.MY_ACCOUNT)

    def Validating_click_on_etrado_then_hello_guest_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.E_TRADO)

    def Validating_click_on_contact_us_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONCTACT_US)

    def Validating_click_on_business_interface_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.MAX_BUSSINESS)

    def Validating_click_on_whats_app_new_page_will_be_display(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.WHATS_APP)
