
import allure
import pytest
from Web.TradoUser.Footer.Pages.contact_pages import ALL_TESTS_CONTACT_US


class Test_RUN(ALL_TESTS_CONTACT_US):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_valid_fill_all_contact_requirements_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_valid_fill_all_contact_requirements_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("test_invalid_insert_all_data_except_the_first_name_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_first_name_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_first_name_field_null_then_click_on_send_button()
        # contactus.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("test_invalid_insert_all_data_except_the_family_name_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_family_name_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_family_name_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("test_invalid_insert_all_data_except_the_electronic_email_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_electronic_email_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_electronic_email_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("test_invalid_insert_all_data_except_the_phone_number_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_phone_number_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_phone_number_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("test_invalid_all_contact_us_requirements_null_then_click_on_send_button")
    def test_invalid_all_contact_us_requirements_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_all_contact_us_requirements_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_phone_number_field_special_character_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_phone_number_field_special_character_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_phone_number_field_special_character_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_phone_number_field_10_character_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_phone_number_field_10_character_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_phone_number_field_10_character_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_first_and_family_name_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_first_and_family_name_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_first_and_family_name_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_family_name_and_electronic_email_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_family_name_and_electronic_email_field_null_then_click_on_send_button(
            self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_family_name_and_electronic_email_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_electronic_email_and_phone_number_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_electronic_email_and_phone_number_field_null_then_click_on_send_button(
            self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_electronic_email_and_phone_number_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_electronic_email_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_electronic_email_field_null_then_click_on_send_button(
            self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_electronic_email_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_family_name_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_family_name_null_then_click_on_send_button(
            self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_family_name_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_phone_and_fist_name_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_phone_and_fist_name_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_phone_and_fist_name_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_phone_and_family_name_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_phone_and_family_name_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_phone_and_family_name_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("test_invalid_insert_all_data_except_the_phone_and_email_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_phone_and_email_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_phone_and_email_field_null_then_click_on_send_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(
        "test_invalid_insert_all_data_except_the_email_and_fist_name_field_null_then_click_on_send_button")
    def test_invalid_insert_all_data_except_the_email_and_fist_name_field_null_then_click_on_send_button(self):
        contactus = ALL_TESTS_CONTACT_US()
        contactus.test_invalid_insert_all_data_except_the_email_and_fist_name_field_null_then_click_on_send_button()



