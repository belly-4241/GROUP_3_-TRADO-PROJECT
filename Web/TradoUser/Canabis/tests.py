

from time import sleep

import allure
import pytest
from Web.TradoUser.Canabis.pages import ALL_TESTS_CANNABIS_LINKS


class Test_RUN(ALL_TESTS_CANNABIS_LINKS):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_clickable_cannabis(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.clickable_cannabis()
        cannabis.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_clickable_sorting_low_price(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.clickable_sorting_low_price()
        cannabis.tear_down()
        sleep(2)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_clickable_sorting_high_price(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.clickable_sorting_high_price()
        cannabis.tear_down()
        sleep(2)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_grid_view_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_grid_view_is_clickable()
        cannabis.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_list_view_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_list_view_is_clickable()
        cannabis.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_Acadia_product_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_Acadia_product_is_clickable()
        cannabis.tear_down()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_add_button_added_the_product_to_cart(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_add_button_added_the_product_to_cart()
        cannabis.tear_down()
        sleep(2)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_cancel_button_clear_the_product_after_added(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_cancel_button_clear_the_product_after_added()
        cannabis.tear_down()
        sleep(2)

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_checkc_cannabis_Kush_Lemon_oilproduct_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.checkc_cannabis_Kush_Lemon_oilproduct_is_clickable()
        cannabis.tear_down()

    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_checkc_cannabis_OG_kush_product_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_OG_kush_product_is_clickable()
        cannabis.tear_down()

    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_lemon_kush_product_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_lemon_kush_product_is_clickable()
        cannabis.tear_down()

    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_gorilla_gal_product_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_gorila_galu_product_is_clickable()
        cannabis.tear_down()

    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_shplant_product_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_shplant_product_is_clickable()
        cannabis.tear_down()

    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_sheme_alpha_product_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_sheme_alpha_product_is_clickable()
        cannabis.tear_down()

    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_sheme_alpha_meyeled_product_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_sheme_alpha_meyeled_product_is_clickable()
        cannabis.tear_down()

    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_cannabis_ultra_product_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_cannabis_ultra_product_is_clickable()
        cannabis.tear_down()

    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_check_next_button_is_clickable(self):
        cannabis = ALL_TESTS_CANNABIS_LINKS()
        cannabis.check_next_button_is_clickable()
        cannabis.tear_down()
