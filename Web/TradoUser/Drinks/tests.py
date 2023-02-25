import allure
import pytest

from Web.TradoUser.Drinks.pages import Drinks_page


class Test_Drinks(Drinks_page):

    def final_object(self):
        final = Test_Drinks()
        return final

    # Drinks #

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks sorting popularity link is clickable")
    @pytest.mark.sanity
    def test_if_drinks_sorting_popularity_link_is_clickable(self):
        self.final_object().click_drinks_sorting_popularity_link()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks sorting from lowest price link is clickable")
    @pytest.mark.sanity
    def test_if_drinks_sorting_from_lowest_price_link_is_clickable(self):
        self.final_object().click_drinks_sorting_from_lowest_price_link()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks sorting from highest price link is clickable")
    @pytest.mark.sanity
    def test_if_drinks_sorting_from_highest_price_link_is_clickable(self):
        self.final_object().click_drinks_sorting_from_highest_price_link()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks list view is clickable")
    @pytest.mark.sanity
    def test_if_drinks_list_view_is_clickable(self):
        self.final_object().click_drinks_list_view()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks grid view is clickable")
    @pytest.mark.sanity
    def test_if_drinks_grid_view_is_clickable(self):
        self.final_object().click_drinks_grid_view()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks all products are clickable ")
    @pytest.mark.sanity
    def test_if_drinks_products_is_clickable(self):
        self.final_object().click_drinks_products()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks products are added to cart")
    @pytest.mark.sanity
    def test_if_drinks_products_added_to_cart(self):
        self.final_object().click_drinks_plus_button()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks products are cleared from cart")
    @pytest.mark.sanity
    def test_if_drinks_products_cleared_after_added(self):
        self.final_object().click_drinks_minus_button()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks products are added 2 times to cart")
    @pytest.mark.sanity
    def test_if_drinks_added_dubble_products(self):
        self.final_object().click_drinks_dubble_add_buttton()

    @allure.title("drinks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test drinks shopping cart clear button works")
    @pytest.mark.sanity
    def test_if_drinks_shopping_cart_removes_items(self):
        self.final_object().click_drinks_shopping_cart_remove_button()
