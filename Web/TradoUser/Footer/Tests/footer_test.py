
import allure
import pytest
from Web.TradoUser.Footer.Pages.footer_pages import ALL_TESTS_FOOTER_LINKS


class Test_RUN(ALL_TESTS_FOOTER_LINKS):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_click_on_accessiblity_statement_then_verify_accessibility_page_display(self):
        who_we_are = ALL_TESTS_FOOTER_LINKS()
        who_we_are.click_on_accessiblity_statement_then_verify_accessibility_page_display()
        who_we_are.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_click_on_Payment_solutions_then_verify_accessibility_page_display(self):
        payment = ALL_TESTS_FOOTER_LINKS()
        payment.click_on_Payment_solutions_then_verify_accessibility_page_display()
        payment.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_Facebook_link_display_facebook_home_page(self):
        facebook = ALL_TESTS_FOOTER_LINKS()
        facebook.Validating_click_on_Facebook_link_display_facebook_home_page()
        facebook.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_Instagram_link_display_Instagram_home_page(self):
        instagrma = ALL_TESTS_FOOTER_LINKS()
        instagrma.Validating_click_on_Instagram_link_display_Instagram_home_page()
        instagrma.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_Twitter_link_display_Twitter_home_page(self):
        twitter = ALL_TESTS_FOOTER_LINKS()
        twitter.Validating_click_on_Twitter_link_display_Twitter_home_page()
        twitter.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_common_questions_new_page_will_be_display(self):
        common_questions = ALL_TESTS_FOOTER_LINKS()
        common_questions.Validating_click_on_common_questions_new_page_will_be_display()
        common_questions.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_how_does_shipping_work_new_page_will_be_display(self):
        how_does_shipping_work = ALL_TESTS_FOOTER_LINKS()
        how_does_shipping_work.Validating_click_on_how_does_shipping_work_new_page_will_be_display()
        how_does_shipping_work.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_payment_solutions_new_page_will_be_display(self):
        payment_solutions = ALL_TESTS_FOOTER_LINKS()
        payment_solutions.Validating_click_on_payment_solutions_new_page_will_be_display()
        payment_solutions.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_MAX_for_business_new_page_will_be_display(self):
        MAX_for_business = ALL_TESTS_FOOTER_LINKS()
        MAX_for_business.Validating_click_on_MAX_for_business_new_page_will_be_display()
        MAX_for_business.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_Who_we_are_new_page_will_be_display(self):
        who_we_are = ALL_TESTS_FOOTER_LINKS()
        who_we_are.Validating_click_on_Who_we_are_new_page_will_be_display()
        who_we_are.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_my_account_new_page_will_be_display(self):
        my_account = ALL_TESTS_FOOTER_LINKS()
        my_account.Validating_click_on_my_account_new_page_will_be_display()
        my_account.tear_down()


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_contact_us_new_page_will_be_display(self):
        contact_us = ALL_TESTS_FOOTER_LINKS()
        contact_us.Validating_click_on_contact_us_new_page_will_be_display()
        contact_us.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_business_interface_new_page_will_be_display(self):
        business_interface = ALL_TESTS_FOOTER_LINKS()
        business_interface.Validating_click_on_business_interface_new_page_will_be_display()
        business_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_Validating_click_on_whats_app_new_page_will_be_display(self):
        whats_up = ALL_TESTS_FOOTER_LINKS()
        whats_up.Validating_click_on_whats_app_new_page_will_be_display()
        whats_up.tear_down()
