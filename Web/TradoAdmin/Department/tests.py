from Web.TradoAdmin.Department.pages import TestAll_pages
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
    def test_department_search_id(self):
        self.project_object().department()

    def test_department_search_name(self):
        self.project_object().department_1()

    def test_department_download_file(self):
        self.project_object().department_2()

    def test_department_clickable_name(self):
        self.project_object().department_3()

    def test_department_clickable_id(self):
        self.project_object().department_4()

    def test_department_clickable_photo(self):
        self.project_object().department_5()

    def test_department_clickable_background_photo(self):
        self.project_object().department_6()

    def test_department_clickable_active(self):
        self.project_object().department_7()

    def test_department_clickable_date_finish(self):
        self.project_object().department_8()

    def test_department_clickable_date_insert_item(self):
        self.project_object().department_9()

    def test_department_clickable_date_insert_items(self):
        self.project_object().department_10()