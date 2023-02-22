import allure
import pytest

from Web.TradoUser.Promotion.pages import Promotion_pages


# from Trado_user.WEB.Tests.test_snacks import TestFinal
# from Trado_user.WEB.Pages.drink_pages import Drinks_page


class TestFinal(Promotion_pages):

    def final_object(self):
        final = TestFinal()
        return final

    # Promotions Test #

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test forward slide button is clickable")
    @pytest.mark.sanity
    def test_if_slide_forward_button_is_clickable(self):
        self.final_object().click_forward_button()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test backward slide button is clickable")
    @pytest.mark.sanity
    def test_if_slide_backward_button_is_clickable(self):
        self.final_object().click_backward_button()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test slide max button is clickable")
    @pytest.mark.sanity
    def test_if_slide_max_link_is_clickable(self):
        self.final_object().click_max_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test slide stuck with goods link is clickable")
    @pytest.mark.sanity
    def test_if_slide_stuck_with_goods_link_is_clickable(self):
        self.final_object().click_stulk_with_goods_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test slide do you have to sell ? link is clickable")
    @pytest.mark.sanity
    def test_if_do_you_have_good_to_sell_link_is_clickable(self):
        self.final_object().click_do_you_have_good_to_sell_link()

    # @allure.title("promotion page test")
    # @allure.link("https://qa.trado.co.il/")
    # @allure.description("Test trado customers link is clickable")
    # @pytest.mark.sanity
    # def test_if_trado_customers_link_is_clickable(self):
    #     self.final_object().click_trado_customers_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test annoneyemes arena link is clickable")
    @pytest.mark.sanity
    def test_if_annoneyems_arena_link_is_clickable(self):
        self.final_object().click_annoneyems_arena_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test join the retail revolution link is clickable")
    @pytest.mark.sanity
    def test_if_join_the_reatail_revolution_link_clickable(self):
        self.final_object().click_join_the_reatail_revolution_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test how it works link is clickable")
    @pytest.mark.sanity
    def test_if_how_it_works_link_is_clickable(self):
        self.final_object().click_how_does_it_works_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test how it works received phone number")
    @pytest.mark.sanity
    def test_if_how_it_works_received_phone_number(self):
        self.final_object().insert_phone_number()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test how it works received phone number")
    @pytest.mark.sanity
    def test_if_how_it_works_received_invalid_phone_number(self):
        self.final_object().insert_invalid_phone_number()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test how it works received login code")
    @pytest.mark.sanity
    def test_if_how_it_works_login_code_received(self):
        self.final_object().insert_login_code()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test how it works added product")
    @pytest.mark.sanity
    def test_if_how_it_works_add_product(self):
        self.final_object().add_products()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test how it works added product")
    @pytest.mark.sanity
    def test_if_how_it_works_add_product_with_invalid_value(self):
        self.final_object().add_products_with_invalid_value()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test for all questions link is clickable")
    @pytest.mark.sanity
    def test_if_for_all_questions_link_is_clickable(self):
        self.final_object().click_for_all_questions_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test contact link is clickable")
    @pytest.mark.sanity
    def test_if_contact_link_is_clickable(self):
        self.final_object().click_contact_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test how does shipping link is clickable")
    @pytest.mark.sanity
    def test_if_how_does_shipping_link_is_clickable(self):
        self.final_object().click_how_does_shipping_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test sorting popularity link is clickable")
    @pytest.mark.sanity
    def test_if_sorting_popularity_link_is_clickable(self):
        self.final_object().click_sorting_popularity_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test sorting from lowest price is clickable")
    @pytest.mark.sanity
    def test_if_sorting_from_lowest_price_link_is_clickable(self):
        self.final_object().click_sorting_from_lowest_price_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test sorting from highest price is clickable")
    @pytest.mark.sanity
    def test_if_sorting_from_highest_price_link_is_clickable(self):
        self.final_object().click_sorting_from_highest_price_link()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test list view is clickable")
    @pytest.mark.sanity
    def test_if_list_view_is_clickable(self):
        self.final_object().click_list_view()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test grid view is clickable")
    @pytest.mark.sanity
    def test_if_grid_view_is_clickable(self):
        self.final_object().click_grid_view()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test all products are clickable")
    @pytest.mark.sanity
    def test_if_products_are_clickable(self):
        self.final_object().click_products()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test products are added to cart")
    @pytest.mark.sanity
    def test_if_products_are_added_to_cart(self):
        self.final_object().click_plus_button()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test products are removed from cart ")
    @pytest.mark.sanity
    def test_if_added_products_removed_from_cart(self):
        self.final_object().click_minus_button()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test products are added 2 times")
    @pytest.mark.sanity
    def test_if_added_products_is_dubbled(self):
        self.final_object().click_dubble_add_buttton()

    @allure.title("promotion page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test shopping cart clear button works")
    @pytest.mark.sanity
    def test_if_shopping_cart_clear_button_works(self):
        self.final_object().click_shopping_cart_remove_button()

    # @allure.title("promotion page test")
    # @allure.link("https://qa.trado.co.il/")
    # @allure.description("Test forward slide button is clickable")
    # @pytest.mark.sanity
    # def test_if_how_it_works_received_phone_number(self):
    #     self.final_object().add_products()
