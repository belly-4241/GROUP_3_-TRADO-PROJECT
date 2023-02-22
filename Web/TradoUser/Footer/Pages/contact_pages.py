
from Web.TradoUser.Footer.Locators.contact_locators import Xpath_contact_us
from Web.TradoUser.Base.base_test import BaseSetups
from selenium.webdriver.common.by import By


class ALL_TESTS_CONTACT_US(BaseSetups, Xpath_contact_us):
    def test_valid_fill_all_contact_requirements_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "beyenenigatu@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "srdtfyguhkjlkhgdfghjm<kj")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.SUCCESSFULLY_MESSAGE) == "הפרטים נקלטו בהצלחה"

    def test_invalid_insert_all_data_except_the_first_name_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "srdtfyguhkjlkhgdfghjm<kj")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_FIRST_NAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_family_name_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "srdtfyguhkjlkhgdfghjm<kj")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_SURNAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_electronic_email_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_bar()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "srdtfyguhkjlkhgdfghjm<kj")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_EMAIL) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_phone_number_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_PHONE_NUMBER) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_MESSAGE) == "נא למלא שדה זה"

    def test_invalid_all_contact_us_requirements_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "")
        self.fields(By.XPATH, self.TELEPHONE, "")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_FIRST_NAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_phone_number_field_special_character_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "#$%^FGHGFGT")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.CSS_SELECTOR, self.PHONE_INVALID) == "מס׳ טלפון לא תקין"

    def test_invalid_insert_all_data_except_the_phone_number_field_10_character_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "195222222212")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.CSS_SELECTOR, self.PHONE_INVALID) == "מס׳ טלפון לא תקין"

    def test_invalid_insert_all_data_except_the_first_and_family_name_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_FIRST_NAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_family_name_and_electronic_email_field_null_then_click_on_send_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_SURNAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_electronic_email_and_phone_number_field_null_then_click_on_send_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_PHONE_NUMBER) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_electronic_email_field_null_then_click_on_send_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_EMAIL) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_family_name_null_then_click_on_send_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_SURNAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_The_Content_Of_The_Inquiry_and_fist_name_field_null_then_click_on_send_button(
            self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_FIRST_NAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_phone_and_fist_name_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_PHONE_NUMBER) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_phone_and_family_name_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "byenenigatu303@gmail.com")
        self.fields(By.XPATH, self.TELEPHONE, "")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_SURNAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_phone_and_email_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "")
        self.fields(By.XPATH, self.TELEPHONE, "")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_EMAIL) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_family_and_email_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "Nigatu")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_SURNAME) == "נא למלא שדה זה"

    def test_invalid_insert_all_data_except_the_email_and_fist_name_field_null_then_click_on_send_button(self):
        self.setup_trado()
        self.click(By.XPATH, self.CONNECT)
        self.scroll_down()
        self.click(By.XPATH, self.CONTACT_US_LINK)
        self.fields(By.XPATH, self.FRIST_NAME, "")
        self.fields(By.CSS_SELECTOR, self.SURNAME, "Beyene")
        self.fields(By.XPATH, self.EMAIL_CONTACT, "")
        self.fields(By.XPATH, self.TELEPHONE, "1952222222")
        self.fields(By.XPATH, self.REFERANCE_MESSAGE, "let's start to send message")
        self.click(By.CLASS_NAME, self.SEND_BUTTON)
        assert self.assertion(By.XPATH, self.ERROR_FIRST_NAME) == "נא למלא שדה זה"




