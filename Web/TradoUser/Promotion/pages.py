import time
from selenium.webdriver.common.by import By
from Web.TradoUser.Base.base_test import BaseSetups
from Web.TradoUser.Promotion.locators import Promotion_locators
from pymongo import MongoClient


class Promotion_pages(BaseSetups, Promotion_locators):

    def click_forward_button(self):
        self.setup_trado()
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.slide_forward_button)
        self.click(By.XPATH, self.slide_forward_button)
        # time.sleep(2)
        # self.wait_until_element_is_visible(By.XPATH, "//title[contains(text(),'trado')]")
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_backward_button(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.slide_backward_button)
        self.click(By.XPATH, self.slide_backward_button)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_max_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.max)
        self.click(By.XPATH, self.max)
        time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_stulk_with_goods_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.stulk_with_goods)
        self.click(By.XPATH, self.stulk_with_goods)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_do_you_have_good_to_sell_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.do_you_have_good_to_sell)
        self.click(By.XPATH, self.do_you_have_good_to_sell)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_trado_customers_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.trado_customers)
        self.click(By.XPATH, self.trado_customers)
        # time.sleep(2)
        assert self.assertion(By.XPATH, "/html/body/app-root/app-main-layout/section/section/app-card-page/div/div[1]/a/span") == "להזמנת כרטיס"
        self.tear_down()

    def click_annoneyems_arena_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.trado_customers)
        self.click(By.XPATH, self.trado_customers)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_join_the_reatail_revolution_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.join_the_reatail_revolution)
        self.click(By.XPATH, self.join_the_reatail_revolution)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_how_does_it_works_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.how_does_it_works)
        self.click(By.XPATH, self.how_does_it_works)
        time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_for_all_questions_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.for_all_questions_link)
        self.click(By.XPATH, self.for_all_questions_link)
        # time.sleep(2)
        # assert self.driver.title == "trado"
        assert self.assertion(By.XPATH, "//h4[contains(text(),'מכירת סחורה')]") == "מכירת סחורה"
        # self.tear_down()

    def click_contact_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.contact_link)
        self.click(By.XPATH, self.contact_link)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_how_does_shipping_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.how_does_shipping_work)
        self.click(By.XPATH, self.how_does_shipping_work)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_sorting_popularity_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.sorting_popularity)
        self.click(By.XPATH, self.sorting_popularity)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_sorting_from_lowest_price_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.sorting_price_from_the_lowest)
        self.click(By.XPATH, self.sorting_price_from_the_lowest)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
        self.click(By.XPATH, self.second_pop_up)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_sorting_from_highest_price_link(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.sorting_price_from_the_highest)
        self.click(By.XPATH, self.sorting_price_from_the_highest)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.second_pop_up)
        self.click(By.XPATH, self.second_pop_up)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_list_view(self):
        self.setup_trado()
        self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        self.wait_until_element_is_visible(By.XPATH, self.list_view)
        self.click(By.XPATH, self.list_view)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_grid_view(self):
        self.setup_trado()
        # self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.first_pop_up)
        # time.sleep(2)
        # self.wait_until_element_is_visible(By.XPATH, self.grid_view)
        self.click(By.XPATH, self.grid_view)
        # time.sleep(2)
        assert self.driver.title == "trado"
        # self.tear_down()

    def click_products(self):

        num = 0
        for products in range(20):
            self.setup_trado()
            # self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            # self.wait_until_element_is_visible(By.XPATH, self.forloop_path)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a[{num + 1}]/div[1]/div[2]/div[2]/div[1]")
            time.sleep(1)
            # self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            num += 1
            time.sleep(1)
            # assert self.assertion(By.CLASS_NAME, "product_product")
            # if num == 20:
            #     print("successful")
            # else:
            #     print("Fail")
            # # time.sleep(2)

    def click_plus_button(self):
        num = 0
        for products in range(20):
            self.setup_trado()
            time.sleep(2)
            # self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            # self.wait_until_element_is_visible(By.XPATH, self.forloop_path)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a[{num + 1}]/div[1]/div[2]/div[2]/div[1]")
            time.sleep(2)
            # self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(2)
            # self.wait_until_element_is_visible(By.XPATH, self.add_button)
            self.click(By.XPATH, self.plus_button)
            time.sleep(2)
            num += 1
            time.sleep(2)
            assert self.assertion(By.XPATH,
                                  "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/h4") == "סל הקניות שלך"
            # self.tear_down()

    def click_minus_button(self):
        num = 0
        for products in range(20):
            self.setup_trado()
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a[{num + 1}]/div[1]/div[2]/div[2]/div[1]")
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.plus_button)
            self.click(By.XPATH, self.plus_button)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.minus_button)
            self.click(By.XPATH, self.minus_button)
            time.sleep(1)
            num += 1
            # assert self.driver.title == "trado"
            # self.tear_down()

    def click_dubble_add_buttton(self):
        num = 0
        for products in range(20):
            self.setup_trado()
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            # self.wait_until_element_is_visible(By.XPATH, self.forloop_path)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a[{num + 1}]/div[1]/div[2]/div[2]/div[1]")
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.plus_button)
            self.click(By.XPATH, self.plus_button)
            time.sleep(1)
            self.wait_until_element_is_visible(By.XPATH, self.plus_button)
            self.click(By.XPATH, self.plus_button)
            time.sleep(1)
            num += 1
            # assert self.driver.title == "trado"
            # self.tear_down()

    def click_shopping_cart_remove_button(self):
        num = 0
        for products in range(20):
            self.setup_trado()
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            # time.sleep(2)
            self.click(By.XPATH,
                       f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/a[{num + 1}]/div[1]/div[2]/div[2]/div[1]")
            time.sleep(2)
            self.wait_until_element_is_visible(By.XPATH, self.first_pop_up)
            self.click(By.XPATH, self.first_pop_up)
            # time.sleep(2)
            self.wait_until_element_is_visible(By.XPATH, self.plus_button)
            self.click(By.XPATH, self.add_button)
            self.wait_until_element_is_visible(By.XPATH, self.remove_button)
            self.click(By.XPATH, self.remove_button)
            num += 1
            time.sleep(2)
            # assert self.assertion(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/h4") == "סל הקניות שלך"

    def code_generator(self):
        cluster = "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority"
        db_client = MongoClient(cluster)
        db = db_client['trado_qa']
        collection = db['users']
        results = collection.find({"phone": '0502006336'})
        for reset in results:
            login_code = (reset['loginCode'])
            return login_code

    def insert_phone_number(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.how_does_it_works)
        self.fields(By.XPATH, self.how_it_works_input, self.login_phone_number)
        self.click(By.XPATH, self.connect)
        assert self.assertion(By.XPATH, self.phone_assert) == "שלחו לי שוב, לא קיבלתי SMS"

    def insert_invalid_phone_number(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        time.sleep(2)
        self.click(By.XPATH, self.how_does_it_works)
        time.sleep(2)
        self.fields(By.XPATH, self.how_it_works_input, self.invalid_login_phone_number)
        time.sleep(2)
        self.click(By.XPATH, self.connect)
        assert self.assertion(By.XPATH, self.phone_assert) == "רק מוודאים שאנחנו מכירים"

    def insert_login_code(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.how_does_it_works)
        self.fields(By.XPATH, self.how_it_works_input, self.login_phone_number)
        self.click(By.XPATH, self.connect)
        self.fields(By.XPATH, self.login_1_code, self.code_generator())
        self.click(By.XPATH, self.perform_verification)
        self.click(By.XPATH, self.how_it_works_2)
        self.fields(By.XPATH, self.Manufactuer_suk, self.manufacturer_value)
        self.fields(By.XPATH, self.product_name, self.product_name_value)
        self.fields(By.XPATH, self.brand, self.brand_value)
        self.fields(By.XPATH, self.manufacturer, self.manufacturer_value)
        self.fields(By.XPATH, self.price, self.price_value)
        self.fields(By.XPATH, self.expiration_date, self.expiration_date_value)
        self.click(By.XPATH, self.add_button)
        assert self.assertion(By.XPATH,
                              "/html/body/div[1]/div/div[4]/div/div/div/div[2]/div[3]/h2") == "איך המוצר שלכם נמכר ? לפי יחידות או משקל"

    def add_products(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.how_does_it_works)
        self.fields(By.XPATH, self.how_it_works_input, self.login_phone_number)
        self.click(By.XPATH, self.connect)
        self.fields(By.XPATH, self.login_1_code, self.code_generator())
        self.click(By.XPATH, self.perform_verification)
        self.click(By.XPATH, self.how_it_works_2)
        self.fields(By.XPATH, self.Manufactuer_suk, self.Manufactuer_value)
        self.fields(By.XPATH, self.product_name, self.product_name_value)
        self.fields(By.XPATH, self.brand, self.brand_value)
        self.fields(By.XPATH, self.manufacturer, self.manufacturer_value)
        self.fields(By.XPATH, self.price, self.price_value)
        self.fields(By.XPATH, self.expiration_date, self.expiration_date_value)
        self.click(By.XPATH, self.add_button)
        self.fields(By.XPATH, self.quantity_in_carton, self.quantity_in_carton_value)
        self.fields(By.XPATH, self.number_of_cartons_in_stock, self.number_of_cartons_in_stock_value)
        self.fields(By.XPATH, self.minimum_cartons_on_order, self.minimum_cartons_on_order_value)
        self.click(By.XPATH, self.add_amount_button)
        self.fields(By.XPATH, self.city, self.city_value)
        self.fields(By.XPATH, self.street, self.street_value)
        self.fields(By.XPATH, self.number, self.number_value)
        self.fields(By.XPATH, self.entrance, self.entrance_value)
        self.fields(By.XPATH, self.commentary, self.commentary_value)
        self.fields(By.XPATH, self.floor, self.floor_value)
        self.fields(By.XPATH, self.contact_number, self.contact_number_value)
        self.fields(By.XPATH, self.your_phone_number, self.number_value)
        self.click(By.XPATH, self.add_button_2)
        assert self.assertion(By.XPATH,
                              "/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/h1") == "מבצעים"

    def add_products_with_invalid_value(self):
        self.setup_trado()
        self.click(By.XPATH, self.first_pop_up)
        self.click(By.XPATH, self.how_does_it_works)
        self.fields(By.XPATH, self.how_it_works_input, self.login_phone_number)
        self.click(By.XPATH, self.connect)
        self.fields(By.XPATH, self.login_1_code, self.code_generator())
        self.click(By.XPATH, self.perform_verification)
        self.click(By.XPATH, self.how_it_works_2)
        self.fields(By.XPATH, self.Manufactuer_suk, self.invalid_manufactuer_value)
        self.fields(By.XPATH, self.product_name, self.invalid_product_name_value)
        self.fields(By.XPATH, self.brand, self.brand_value)
        self.fields(By.XPATH, self.manufacturer, self.invalid_manufacturer_value)
        self.fields(By.XPATH, self.price, self.price_value)
        self.fields(By.XPATH, self.expiration_date, self.invalid_expiration_date_value)
        self.click(By.XPATH, self.add_button)
        self.fields(By.XPATH, self.quantity_in_carton, self.invalid_quantity_in_carton)
        self.fields(By.XPATH, self.number_of_cartons_in_stock, self.invalid_number_of_cartons_in_stock_value)
        self.fields(By.XPATH, self.minimum_cartons_on_order, self.invalid_minimum_cartons_on_order_value)
        self.click(By.XPATH, self.add_amount_button)
        self.fields(By.XPATH, self.city, self.invalid_city_value)
        self.fields(By.XPATH, self.street, self.invalid_street_value)
        self.fields(By.XPATH, self.number, self.invalid_number_value)
        self.fields(By.XPATH, self.entrance, self.invalid_entrance_value)
        self.fields(By.XPATH, self.commentary, self.invalid_commentary_value)
        self.fields(By.XPATH, self.floor, self.invalid_floor_value)
        self.fields(By.XPATH, self.contact_number, self.invalid_contact_number_value)
        self.fields(By.XPATH, self.your_phone_number, self.invalid_number_value)
        self.click(By.XPATH, self.add_button_2)
