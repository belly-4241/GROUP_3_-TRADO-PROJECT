from Web.TradoUser.Footer.Locators.bussiness_locator import Xpath_bussiness
from Web.TradoUser.Base.base_test import BaseSetups
from selenium.webdriver.common.by import By


class ALL_TESTS_BUSSINESS(BaseSetups, Xpath_bussiness):
    def valid_fill_all_contact_requirements_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.wait_until_element_is_visible(By.XPATH, self.FRIST_NAME)
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "2")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_Your_Phone_Number_field_null_then_click_on_submit_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.CSS_SELECTOR, self.INVALID_PHONE) == "נא למלא שדה זה"
        # assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_Electronic_Mail_field_wrong_then_click_on_submit_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "sdfsdsd@gmail")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.INVALID_EMAILS) == "דוא״ל לא תקין"
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_House_Number_field_long_number_then_click_on_submit_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "3454898403945092385092304955")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_Street_null_then_click_on_submit_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234")
        self.fields(By.XPATH, self.STREET, "")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.STREET_ASSERTION) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_correctly_except_first_and_family_name_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "")
        self.fields(By.XPATH, self.SUR_NAME, "")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.FIRST_NAME_ASSERTION) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_correctly_except_family_name_and_HPAM_field_null_then_click_on_submit_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "5")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "Jerusalem")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.LAST_NAME_ASSERTION) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_correctly_except_HPAM_and_Business_Name_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "195222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.BUSINESS_NAME_ASSERTION) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_correctly_except_Business_Name_and_Select_A_Category_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "")
        self.click(By.XPATH, self.CATEGORY)
        self.fields(By.XPATH, self.PHONE, "!@#$%^&*()^&*")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.BUSINESS_NAME_ASSERTION) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_correctly_except_Select_A_Category_and_Your_Phone_Number_field_wrong_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        # self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "00000000000000000000000000000")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.CSS_SELECTOR, self.INVALID_PHONE) == "מס׳ טלפון לא תקין"
        # assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_Your_Phone_Number_And_Electronic_emai_our_Phone_Number_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, " WTWFWS3545454")
        self.fields(By.XPATH, self.EMAIL, "ADGDARG@rswe7gmail")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.CSS_SELECTOR, self.INVALID_PHONE) == "מס׳ טלפון לא תקין"
        assert self.assertion(By.XPATH, self.INVALID_EMAILS) == "דוא״ל לא תקין"
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_Electronic_Mail_and_House_Number_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "SDFSS@")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "345034509172309510359328457901340513")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.INVALID_EMAILS) == "דוא״ל לא תקין"

    def test_invalid_insert_all_data_correctly_except_House_Number_and_Street_field_field_wrong_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "13534869348673458973459834789347540")
        self.fields(By.XPATH, self.STREET, "EFSG%^%^$")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_first_name_field_special_character_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "@#$%^&*(")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_family_name_field_special_character_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "#$%^&*()")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_HPAM_select_0_field_null_then_click_on_submit_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        # self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_Business_Name_field_special_character_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "*&^%$%^&*(")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_Your_Phone_Number_field_special_character_field_null_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "@#$%^&*()_")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_Electronic_Mail_field_without_AT_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu@303gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "234567")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

    def test_invalid_insert_all_data_correctly_except_House_field_Numbermix_number_with_letter_then_click_on_submit_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.BUSSINESS_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.XPATH, self.SUR_NAME, "Beyene")
        self.clear(By.CSS_SELECTOR, self.HFEM)
        self.fields(By.CSS_SELECTOR, self.HFEM, "1")
        self.fields(By.XPATH, self.BUSSINESS_NAME, "CHOCOLATE")
        self.click(By.XPATH, self.CATEGORY)
        self.click(By.XPATH, self.SELECT_CATEGORY)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        self.fields(By.XPATH, self.EMAIL, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.HOUSE_NUMBER, "23#$%Vddcfbbz")
        self.fields(By.XPATH, self.STREET, "223")
        self.fields(By.XPATH, self.CITY, "JERUSALEM")
        self.click(By.CLASS_NAME, self.SUBMIT)
        assert self.assertion(By.XPATH, self.APPROVE_OUR_POLICY) == "Please Approve Our Policy"

