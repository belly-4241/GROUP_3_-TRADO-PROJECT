
import time
import pymongo
import pytest
from pymongo import MongoClient
from selenium.webdriver.common.by import By

from Web.TradoUser.Base.base_test import BaseSetups


class TestHeaderPage(BaseSetups):
    def title_logo(self):
        self.setup_trado()
        try:
            assert 'trado' in self.driver.title
            print("trado title is verified")
        except:
            print("trado title is not verified")

    # def test_search(self):
    #     self.setup_trado()
    #     self.click(By.XPATH, self.COCTAIL)
    #     self.click(By.XPATH, self.SAVE)
    #     self.fields(By.XPATH, self.SEARCH_PRODUCTS, "גורילה גלו")
    #     self.click(By.XPATH, self.SEARCH_BUTTON)
    #     self.click(By.XPATH, self.SEARCH_LIST)
    #     assert self.assertion(By.CSS_SELECTOR, self.AMOUNT_IN_CARTON) == "כמות בקרטון: 1"


    def language(self):
        self.setup_trado()
        self.click(By.XPATH, self.RESTRAUNAT)
        self.click(By.XPATH, self.SAVE)
        self.click(By.XPATH, self.US_IL_LANGUAGE)

        self.setup_trado()
        self.color_check_up(By.XPATH, self.BACKGROUND_COLOR)

    def test_scroll(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.driver.execute_script("window.scrollBy(0, 100);")
        self.click(By.XPATH, self.NEXT_SLIDE)
        self.click(By.XPATH, self.BACK_SLIDE)



    def test_search_assert_price(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, "גורילה גלו")
        self.click(By.XPATH, self.SEARCH_BUTTON)
        self.click(By.XPATH, self.SEARCH_LIST)
        time.sleep(2)
        assert self.assertion(By.CSS_SELECTOR, self.PRICE_PRODUCT) == 'עלות לקרטון: ₪27.90'

    def test_cartoon_in_stock(self):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, "גורילה גלו")
        self.click(By.XPATH, self.SEARCH_BUTTON)
        self.click(By.XPATH, self.SEARCH_LIST)
        assert self.assertion(By.XPATH, self.CARTOON_IN_STOCK) == 'קרטונים במלאי:9976'

    @pytest.mark.parametrize("name,message",[('eggeggggg', '0 תוצאות'),
                                               ('corona', '0 תוצאות'),
                                               ('קורונה 335 מ"ל', '2 תוצאות'),
                                               ('בירה', '7 תוצאות'),
                                               ('','0 תוצאות'),
                                             ('@#$$#@', '0 תוצאות'),
                                             ('12456789', '0 תוצאות')
                                               ])
    def test_search_not_in_stock(self, name, message):
        self.setup_trado()
        self.click(By.XPATH, self.COCTAIL)
        self.click(By.XPATH, self.SAVE)
        self.fields(By.XPATH, self.SEARCH_PRODUCTS, name)
        self.click(By.XPATH, self.SEARCH_BUTTON)
        time.sleep(2)
        self.click(By.XPATH, self.SEARCH_LIST)
        assert self.message(By.XPATH, self.SEARCH_RESULT_MESSAGE) == message

    # def test_add_new_product(self):
    #     self.setup_trado()
    #     self.click(By.XPATH, self.COCTAIL)
    #     self.click(By.XPATH, self.SAVE)
    #     self.click(By.XPATH, self.ADD_PRODUCTS)
    #     self.fields(By.XPATH, self.PHONE_FIELD_NEW_PRODUCT, "0502006336")
    #     self.checkbox(By.XPATH, self.CHECK_BOX)
    #     self.click(By.XPATH, self.CONNECT)
    #     self.click(By.XPATH, self.CODE0)
    #     self.fields(By.XPATH, self.FILL_ONE, self.code_generator()[0])
    #     self.click(By.XPATH, self.CODE1)
    #     self.fields(By.XPATH, self.FILL_TWO, self.code_generator()[1])
    #     self.click(By.XPATH, self.CODE2)
    #     self.fields(By.XPATH, self.FILL_THREE, self.code_generator()[2])
    #     self.click(By.XPATH, self.CODE3)
    #     self.fields(By.XPATH, self.FILL_FOUR, self.code_generator()[3])
    #     self.click(By.XPATH, self.CODE4)
    #     self.fields(By.XPATH, self.FILL_FIVE, self.code_generator()[4])
    #     self.click(By.XPATH, self.AUTHENTICATION)
    #
    #     time.sleep(5)
    #
    #
    # def test_tell_us(self):
    #     self.setup_trado()
    #     self.click(By.XPATH, self.COCTAIL)
    #     self.click(By.XPATH, self.SAVE)
    #     self.click(By.XPATH, self.TELL_US_SOMETHING)
    #     self.click(By.XPATH, self.REGISTER_BTN)
    #     self.fields(By.XPATH, self.TELEPHONE_REGISTER, "0521234569")
    #     self.fields(By.XPATH, self.BN_NUMBER, "515074946")
    #     self.checkbox(By.XPATH, self.REMIND_ME_BOX)
    #     self.click(By.XPATH, self.CHECK_BOX_TWO)
    #     self.click(By.XPATH, self.CONNECT_REGISTER_BTN)
    #     self.fields(By.XPATH, self.LOGIN_CODE5, "")
    #     self.fields(By.XPATH, self.LOGIN_CODE4, "")
    #     self.fields(By.XPATH, self.LOGIN_CODE3, "")
    #     self.fields(By.XPATH, self.LOGIN_CODE2, "")
    #     self.fields(By.XPATH, self.LOGIN_CODE1, "")
    #     self.click(By.XPATH, self.ACCEPT_CODE_REGISTER)
    #
    # def test_join_us_max_card(self):
    #     self.setup_trado()
    #     self.click(By.XPATH, self.COCTAIL)
    #     self.click(By.XPATH, self.SAVE)
    #     self.click(By.XPATH, self.JOIN_US_MAX)
    #     self.fields(By.XPATH, self.BUSINESS_NAME, "max")
    #     self.fields(By.XPATH, self.LAST_NAME, "card")
    #     self.fields(By.XPATH, self.PHONE_NUMBER_BUSINESS, "1234567891")
    #     self.fields(By.XPATH, self.CITY_BUSINESS, "beersheva")
    #     self.fields(By.XPATH, self.STREET_BUSINESS, "45")
    #     self.fields(By.XPATH, self.TRADE_NAME, "hotel")
    #     self.fields(By.XPATH, self.BUSINESS_ID, "123456789")
    #     self.fields(By.XPATH, self.POSTAL_CODE_BUSINESS, "8442205")
    #     self.click(By.XPATH, self.SEND_PROFILES)
    #     self.click(By.XPATH, self.X_CLOSE_BTN_BUSINESS)
    #     time.sleep(5)
    #
    #
    # def test_total_product(self):
    #     self.setup_trado()
    #     self.click(By.XPATH, self.COCTAIL)
    #     self.click(By.XPATH, self.SAVE)
    #     self.click(By.XPATH, self.CANABIS_CATEGORY)
    #     products = self.driver.find_elements(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a")
    # #
    #     for x, y in enumerate(products):
    #         all = f"//body/div[@id='root']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{x+1}]"
    #         count = x + 1
    #         if count <= len(products):
    #             self.click(By.XPATH, all)
    #             self.click(By.XPATH, self.TOTAL_ADD)
    #             # self.click(By.XPATH, self.CANABIS_CATEGORY)
    #             self.click(By.XPATH, all)
    #             self.click(By.XPATH, "//header/div[1]/div[1]/a[2]/div[1]")
    #         else:
    #             break















