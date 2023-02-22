from Web.TradoAdmin.Dashboard.pages import TestAll_pages
import allure
import pytest


class Test_Link(TestAll_pages):

    def project_object(self):
        project = Test_Link()
        return project

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_dashboard_process_all_valid_items(self):
        self.project_object().dashboard()

    def test_dashboard_process_all_empty_items(self):
        self.project_object().dashboard_1()

    def test_dashboard_process_name_empty(self):
        self.project_object().dashboard_2()

    def test_dashboard_process_code_empty(self):
        self.project_object().dashboard_3()

    def test_dashboard_process_minimum_sum_empty(self):
        self.project_object().dashboard_4()

    def test_dashboard_process_start_date_empty(self):
        self.project_object().dashboard_5()

    def test_dashboard_process_end_date_empty(self):
        self.project_object().dashboard_6()

    def test_dashboard_process_discount_sum_empty(self):
        self.project_object().dashboard_7()

    def test_dashboard_process_letters_and_numbers_in_name(self):
        self.project_object().dashboard_8()

    def test_dashboard_process_letters_and_numbers_in_code(self):
        self.project_object().dashboard_9()

    def test_dashboard_process_numbers_in_name(self):
        self.project_object().dashboard_10()

    def test_dashboard_process_letters_in_code(self):
        self.project_object().dashboard_11()

    def test_dashboard_process_download(self):
        self.project_object().dashboard_12()

    def test_dashboard_process_search(self):
        self.project_object().dashboard_13()

    def test_dashboard_process_name_button(self):
        self.project_object().dashboard_14()

    def test_dashboard_process_minimum_sum_click(self):
        self.project_object().dashboard_15()

    def test_dashboard_process_user_once_time(self):
        self.project_object().dashboard_16()

    def test_dashboard_process_range_date(self):
        self.project_object().dashboard_17()

    def test_dashboard_process_active(self):
        self.project_object().dashboard_18()

    def test_dashboard_process_date_stop(self):
        self.project_object().dashboard_19()

    def test_dashboard_process_discount(self):
        self.project_object().dashboard_20()

    def test_dashboard_process_count(self):
        self.project_object().dashboard_21()
