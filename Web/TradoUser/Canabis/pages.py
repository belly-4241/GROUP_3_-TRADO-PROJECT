from time import sleep
from Web.TradoUser.Canabis.locators import Xpath_cannabis
from Web.TradoUser.Base.base_test import BaseSetups
from selenium.webdriver.common.by import By


class ALL_TESTS_CANNABIS_LINKS(BaseSetups, Xpath_cannabis):

    def clickable_cannabis(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.CANNABIS)

    def clickable_sorting_low_price(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.CSS_SELECTOR, self.SORTING)
        self.click(By.CSS_SELECTOR, self.SORTINGPRICE_LOW)

    def clickable_sorting_high_price(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.CSS_SELECTOR, self.SORTING)
        self.click(By.CSS_SELECTOR, self.SORTINGPRICE_HIGH)

    def check_cannabis_grid_view_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.GRID_VIEW)

    def check_cannabis_list_view_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.CSS_SELECTOR, self.LIST_VIEW)

    def check_cannabis_Acadia_product_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ACADIA_PRODUCT)

    def check_cannabis_add_button_added_the_product_to_cart(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ACADIA_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.ACADIA_PRODUCT_CART) == "אקדיה"

    def check_cannabis_cancel_button_clear_the_product_after_added(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ACADIA_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        self.click(By.XPATH, self.CLEAR_PRODUCT_CART)

    def check_Acadia_product_carton_cost_units_cardboard_unit_stock_anddelivery_time_presented(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ACADIA_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY) == "כמות במלאי"

    def checkc_cannabis_Kush_Lemon_oilproduct_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.KUSH_LEMON_OIL_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)

    def check_cannabis_OG_kush_product_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.OG_KUSH_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)

    def check_cannabis_lemon_kush_product_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.LEMON_KUSH_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)

    def check_cannabis_gorila_galu_product_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.GORILA_GALU_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)

    def check_cannabis_shplant_product_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.SHPLANT_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)

    def check_cannabis_sheme_alpha_product_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.SHEME_ALPHA_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)

    def check_cannabis_sheme_alpha_meyeled_product_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.SHEME_ALPHA_MIYELED_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)

    def check_cannabis_ultra_product_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ULTRA_PRODUCT)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)

    def check_next_button_is_clickable(self):
        self.setup_trado()
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.NEXT_BUTTON)
        self.click(By.XPATH, self.CANNABIS_CONNECT)
        self.click(By.XPATH, self.ADD_BUTTON)
        assert self.assertion(By.XPATH, self.QUANTITY)
