import time
from selenium.webdriver.common.by import By
from Web.TradoUser.Base.base_test import BaseSetups
from Web.TradoUser.Snacks.locators import Snack_locators


class Snacks_pages(BaseSetups, Snack_locators):

    def click_snacks_sorting_popularity_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks)
        self.click(By.XPATH, self.snacks)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks_sorting_popularity)
        self.click(By.XPATH, self.snacks_sorting_popularity)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_snacks_sorting_from_lowest_price_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks)
        self.click(By.XPATH, self.snacks)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks_sorting_lowest_price)
        self.click(By.XPATH, self.snacks_sorting_lowest_price)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
        self.click(By.XPATH, self.second_pop_up)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_snacks_sorting_from_highest_price_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks)
        self.click(By.XPATH, self.snacks)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks_sorting_highest_price)
        self.click(By.XPATH, self.snacks_sorting_highest_price)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
        self.click(By.XPATH, self.second_pop_up)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_snacks_list_view(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks)
        self.click(By.XPATH, self.snacks)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks_list_view)
        self.click(By.XPATH, self.snacks_list_view)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_snacks_grid_view(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks)
        self.click(By.XPATH, self.snacks)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.snacks_grid_view)
        self.click(By.XPATH, self.snacks_grid_view)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_snacks_products(self):
        num = 0
        for products in range(4):
            self.setup_trado()
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks)
            self.click(By.XPATH, self.snacks)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            # self.wait_until_element_is_visible(By.XPATH, self.forloop_path)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num+1}]/div[1]/div[2]")
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
            self.click(By.XPATH, self.second_pop_up)
            time.sleep(1)
            num += 1
            # assert self.driver.title == "trado"
            # self.tear_down()

    def click_snacks_plus_button(self):
        num = 0
        for products in range(4):
            self.setup_trado()
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks)
            self.click(By.XPATH, self.snacks)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            # self.wait_until_element_is_visible(By.XPATH, self.forloop_path)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num + 1}]/div[1]/div[2]")
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
            self.click(By.XPATH, self.second_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks_add_button)
            self.click(By.XPATH, self.snacks_add_button)
            time.sleep(1)
            num += 1
            # assert self.driver.title == "trado"
            # self.tear_down()

    def click_snacks_minus_button(self):
        num = 0
        for products in range(4):
            self.setup_trado()
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks)
            self.click(By.XPATH, self.snacks)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            # self.wait_until_element_is_visible(By.XPATH, self.forloop_path)
            self.click(By.XPATH,
                       f"/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/a[{num+1}]")
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
            self.click(By.XPATH, self.second_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks_add_button)
            self.click(By.XPATH, self.snacks_add_button)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks_minus_button)
            self.click(By.XPATH, self.snacks_minus_button)
            time.sleep(1)
            num += 1
            # assert self.driver.title == "trado"
            # self.tear_down()

    def click_snacks_dubble_add_buttton(self):
        num = 0
        for products in range(4):
            self.setup_trado()
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks)
            self.click(By.XPATH, self.snacks)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            # self.wait_until_element_is_visible(By.XPATH, self.forloop_path)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num + 1}]/div[1]/div[2]")
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
            self.click(By.XPATH, self.second_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks_add_button)
            self.click(By.XPATH, self.snacks_add_button)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks_add_button)
            self.click(By.XPATH, self.snacks_add_button)
            time.sleep(1)
            num += 1
            # assert self.driver.title == "trado"
            # self.tear_down()

    def click_snacks_shopping_cart_remove_button(self):
        num = 0
        for products in range(4):
            self.setup_trado()
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks)
            self.click(By.XPATH, self.snacks)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            # self.wait_until_element_is_visible(By.XPATH, self.forloop_path)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num + 1}]/div[1]/div[2]")
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
            self.click(By.XPATH, self.second_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks_add_button)
            self.click(By.XPATH, self.snacks_add_button)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.snacks_shoping_clear_button)
            self.click(By.XPATH, self.snacks_shoping_clear_button)
            time.sleep(1)
            num += 1
            # assert self.driver.title == "trado"
            # self.tear_down()
