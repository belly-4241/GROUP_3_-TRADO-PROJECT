import allure
import pytest

from Web.TradoUser.Snacks.pages import Snacks_pages


class TestFinal(Snacks_pages):

    def final_object(self):
        final = TestFinal()
        return final

    # Snacks #

    @allure.title("snacks page test")
    @allure.description("Test snacks sorting popularity link is clickable")
    @allure.link("https://qa.trado.co.il/")
    @pytest.mark.sanity
    def test_if_snacks_sorting_popularity_link_is_clickable(self):
        self.final_object().click_snacks_sorting_popularity_link()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks sorting from lowest price link is clickable")
    @pytest.mark.sanity
    def test_if_snacks_sorting_from_lowest_price_link_is_clickable(self):
        self.final_object().click_snacks_sorting_from_lowest_price_link()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks sorting from highest price link is clickable")
    @pytest.mark.sanity
    def test_if_snacks_sorting_from_highest_price_link_is_clickable(self):
        self.final_object().click_snacks_sorting_from_highest_price_link()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks list view is clickable")
    @pytest.mark.sanity
    def test_if_snacks_list_view_is_clickable(self):
        self.final_object().click_snacks_list_view()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks grid view is clickable")
    @pytest.mark.sanity
    def test_if_snacks_grid_view_is_clickable(self):
        self.final_object().click_snacks_grid_view()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks all products are clickable")
    @pytest.mark.sanity
    def test_if_snacks_products_are_clickable(self):
        self.final_object().click_snacks_products()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks products are added to cart")
    @pytest.mark.sanity
    def test_if_snacks_products_added_to_cart(self):
        self.final_object().click_snacks_plus_button()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks products cleared from cart")
    @pytest.mark.sanity
    def test_if_snacks_products_cleared_after_added(self):
        self.final_object().click_snacks_minus_button()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks products are added 2 times to cart")
    @pytest.mark.sanity
    def test_if_snacks_added_dabble_products(self):
        self.final_object().click_snacks_dubble_add_buttton()

    @allure.title("snacks page test")
    @allure.link("https://qa.trado.co.il/")
    @allure.description("Test snacks shopping cart removes button works")
    @pytest.mark.sanity
    def test_if_snacks_shopping_cart_removes_items(self):
        self.final_object().click_snacks_shopping_cart_remove_button()

