
import allure
import pytest
from Web.TradoUser.Footer.Pages.bussiness_pages import ALL_TESTS_BUSSINESS


class Test_RUN(ALL_TESTS_BUSSINESS):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_valid_fill_all_contact_requirements_then_click_on_send_button(self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.valid_fill_all_contact_requirements_then_click_on_send_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Your_Phone_Number_field_null_then_click_on_submit_button(self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Your_Phone_Number_field_null_then_click_on_submit_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Electronic_Mail_field_wrong_then_click_on_submit_button(self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Electronic_Mail_field_wrong_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_House_Number_field_long_number_then_click_on_submit_button(self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_House_Number_field_long_number_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Street_null_then_click_on_submit_button(self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Street_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_first_and_family_name_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_first_and_family_name_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_family_name_and_HPAM_field_null_then_click_on_submit_button(self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_family_name_and_HPAM_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_HPAM_and_Business_Name_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_HPAM_and_Business_Name_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Business_Name_and_Select_A_Category_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Business_Name_and_Select_A_Category_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Select_A_Category_and_Your_Phone_Number_field_wrong_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Select_A_Category_and_Your_Phone_Number_field_wrong_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Your_Phone_Number_And_Electronic_emai_our_Phone_Number_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Your_Phone_Number_And_Electronic_emai_our_Phone_Number_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Electronic_Mail_and_House_Number_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Electronic_Mail_and_House_Number_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_House_Number_and_Street_field_field_wrong_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_House_Number_and_Street_field_field_wrong_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_first_name_field_special_character_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_first_name_field_special_character_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_family_name_field_special_character_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_family_name_field_special_character_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_HPAM_select_0_field_null_then_click_on_submit_button(self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_HPAM_select_0_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Business_Name_field_special_character_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Business_Name_field_special_character_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Your_Phone_Number_field_special_character_field_null_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Your_Phone_Number_field_special_character_field_null_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_Electronic_Mail_field_without_AT_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_Electronic_Mail_field_without_AT_then_click_on_submit_button()
        bussiness_interface.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_insert_all_data_correctly_except_House_field_Numbermix_number_with_letter_then_click_on_submit_button(
            self):
        bussiness_interface = ALL_TESTS_BUSSINESS()
        bussiness_interface.test_invalid_insert_all_data_correctly_except_House_field_Numbermix_number_with_letter_then_click_on_submit_button()
        bussiness_interface.tear_down()



