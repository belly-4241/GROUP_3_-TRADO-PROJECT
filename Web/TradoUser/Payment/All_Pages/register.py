import allure
import pytest
from selenium.webdriver.common.by import By
from Web.TradoUser.Base.base_test import BaseSetups


class TestRegister(BaseSetups):

    def login(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.fields(By.XPATH, self.PHONE_FIELD, "0502006336")
        self.checkbox(By.XPATH, self.CHECK_BOX)
        self.click(By.XPATH, self.CONNECT)
        self.fields(By.XPATH, self.FILL_ONE, self.code_generator())
        self.click(By.XPATH, self.AUTHENTICATION)

    def register_positive(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, '0526162710')
        self.fields(By.XPATH, self.BN_NUMBER, "51570246")
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        self.fields(By.XPATH, self.LOGIN_CODE1, self.code_registration())
        self.click(By.XPATH, self.ACCEPT_CODE_REGISTER)
        self.click(By.XPATH, self.REGI_STER)
        self.click(By.XPATH, self.REGI_CLICK)

    @allure.description('able to verify sign up with wrong credentials ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("phoneNo, BnNumber, messages", [('', '515074946', 'נא למלא שדה זה'),
                                                             ('', '', 'נא למלא שדה זה')])
    def test_negative_signup(self, phoneNo, BnNumber, messages):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, phoneNo)
        self.fields(By.XPATH, self.BN_NUMBER, BnNumber)
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        self.message(By.XPATH, self.ERROR_PATH)

    @allure.description('able to verify sign up with different invalid inputs  ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("phoneNo, BnNumber, messages", [('111', '515074946',  'מס׳ טלפון לא תקין'),
                                                             ('1111111111111', '12445747',  'מס׳ טלפון לא תקין'),
                                                             ('@#$12afsdj', '48568762', 'מס׳ טלפון לא תקין'),
                                                             ('abcdef123456', '36985214', 'מס׳ טלפון לא תקין'),
                                                             ('acvfrdefg', '45867129', 'מס׳ טלפון לא תקין')])
    def test_telephone_notfix_signup(self, phoneNo, BnNumber, messages):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, phoneNo)
        self.fields(By.XPATH, self.BN_NUMBER, BnNumber)
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        assert self.assertion(By.XPATH, self.ERROR_TELEPHONE_NOTFIX) == messages



    def without_checkbox(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, "0521234567")
        self.fields(By.XPATH, self.BN_NUMBER, "")
        self.click(By.XPATH, self.CHECK_BOX_TWO)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        assert self.message(By.XPATH, self.APPROVED_POLICY) == 'Please Approve Our Policy'

    @allure.description('able to verify sign up with out accepting policy ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("phoneNo, BnNumber, messages", [('0521234567', '515074946','שדה צריך להיות ייחודיי'),
                                                             ('0521234567', '515074946', 'שדה צריך להיות ייחודיי')])
    def test_with_two_checkbox_assign(self, phoneNo, BnNumber, messages):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, phoneNo)
        self.fields(By.XPATH, self.BN_NUMBER, BnNumber)
        self.checkbox(By.XPATH, self.REMIND_ME_BOX)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        assert self.message(By.XPATH, self.BN_NUMBER_ERROR) == messages

    def without_checkbox_assign(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.fields(By.XPATH, self.TELEPHONE_REGISTER, "0521234567")
        self.fields(By.XPATH, self.BN_NUMBER, "515074946")
        self.click(By.XPATH, self.CHECK_BOX_TWO)
        self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
        assert self.message(By.XPATH, self.APPROVED_POLICY) == 'Please Approve Our Policy'

    def register_with_google(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.click(By.XPATH, self.GOOGLE)
        assert self.assertion(By.XPATH, self.GO_404) == "שגיאה 400: redirect_uri_mismatch"

    def register_with_fb(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.click(By.XPATH, self.FB)

    def register_with_twitt(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
        self.click(By.XPATH, self.REGISTER_BTN)
        self.click(By.XPATH, self.TWITT)

    # def registration_form(self):
    #     self.setup_trado()
    #     self.click(By.XPATH, self.COCTAIL)
    #     self.click(By.XPATH, self.SAVE)
    #     self.click(By.CSS_SELECTOR, self.CONNECTION_REGISTER)
    #     self.fields(By.XPATH, self.PHONE_FIELD, "0502006336")
    #     self.checkbox(By.XPATH, self.CHECK_BOX)
    #     self.click(By.XPATH, self.CONNECT)
    #     self.fields(By.XPATH, self.FILL_ONE, self.code_generator())
    #     self.click(By.XPATH, self.AUTHENTICATION)
    #     self.click(By.XPATH, self.AZOR_EISHI)
    #     self.fields(By.XPATH, self.REGISTRATION_FNAME, "team333")
    #     self.fields(By.XPATH, self.REGISTRATION_LNAME, "group3")
    #     self.fields(By.XPATH, self.REGISTRATION_PHONE, "0523698520")
    #     self.fields(By.XPATH, self.EMAIL_REISTRATION, "team3@gmail.com")
    #     self.fields(By.XPATH, self.ID_REGISTRATION, "341343395")
    #     self.fields(By.XPATH, self.REGISTRATION_CITY, "beersheva")
    #     self.fields(By.XPATH, self.REGISTRATION_NUMBER, "6938524")



