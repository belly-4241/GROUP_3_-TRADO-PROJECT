import time
from selenium.webdriver.common.by import By
from Web.TradoUser.Base.base_test import BaseSetups
from Web.TradoUser.Drinks.locators import Drinks_locators


class Drinks_page(BaseSetups, Drinks_locators):

    def click_drinks_sorting_popularity_link(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks)
        time.sleep(2)
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks_sorting_popularity)
        time.sleep(2)

    def click_drinks_sorting_from_lowest_price_link(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks)
        time.sleep(2)
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks_sorting_lowest_price)
        time.sleep(2)
        self.click(By.XPATH, self.second_pop_up)
        time.sleep(2)

    def click_drinks_sorting_from_highest_price_link(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks)
        time.sleep(2)
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.snacks_sorting_highest_price)
        time.sleep(2)
        self.click(By.XPATH, self.second_pop_up)
        time.sleep(2)

    def click_drinks_list_view(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks)
        time.sleep(2)
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks_list_view)
        time.sleep(2)

    def click_drinks_grid_view(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks)
        time.sleep(2)
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.drinks_grid_view)
        time.sleep(2)

    def click_drinks_products(self):
        num = 0
        for products in range(2):
            self.setup_trado()
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.drinks)
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num + 1}]/div[1]/div[2]")
            time.sleep(2)
            self.click(By.XPATH, self.f2_pop_up)
            time.sleep(2)
            num += 1

    def click_drinks_plus_button(self):
        num = 0
        for products in range(2):
            self.setup_trado()
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.drinks)
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num + 1}]/div[1]/div[2]")
            time.sleep(2)
            self.click(By.XPATH, self.f2_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.add_button)
            time.sleep(2)
            num += 1

    def click_drinks_minus_button(self):
        num = 0
        for products in range(2):
            self.setup_trado()
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.drinks)
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num + 1}]/div[1]/div[2]")
            time.sleep(2)
            self.click(By.XPATH, self.f2_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.add_button)
            time.sleep(2)
            self.click(By.XPATH, self.minus_button)
            time.sleep(2)
            num += 1

    def click_drinks_dubble_add_buttton(self):
        num = 0
        for products in range(2):
            self.setup_trado()
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.drinks)
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num + 1}]/div[1]/div[2]")
            time.sleep(2)
            self.click(By.XPATH, self.f2_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.add_button)
            time.sleep(2)
            self.click(By.XPATH, self.add_button)
            time.sleep(2)
            num += 1

    def click_drinks_shopping_cart_remove_button(self):
        num = 0
        for products in range(2):
            self.setup_trado()
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.drinks)
            time.sleep(2)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/a[{num + 1}]/div[1]/div[2]")
            time.sleep(2)
            self.click(By.XPATH, self.f2_pop_up)
            time.sleep(2)
            self.click(By.XPATH, self.add_button)
            time.sleep(2)
            self.click(By.XPATH, self.snacks_shoping_clear_button)
            time.sleep(2)
            num += 1
