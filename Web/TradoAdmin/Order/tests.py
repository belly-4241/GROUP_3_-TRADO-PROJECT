from Web.TradoAdmin.Order.pages import TestAll_pages
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
    def test_order_clickable_receive_number(self):
        self.project_object().order()

    def test_order_clickable_receive_status(self):
        self.project_object().order_1()

    def test_order_clickable_receive_ismain(self):
        self.project_object().order_2()

    def test_order_clickable_receive_order(self):
        self.project_object().order_3()

    def test_order_clickable_receive_first_name(self):
        self.project_object().order_4()

    def test_order_clickable_receive_last_name(self):
        self.project_object().order_5()

    def test_order_clickable_receive_address(self):
        self.project_object().order_6()

    def test_order_clickable_receive_phone_number(self):
        self.project_object().order_7()

    def test_order_clickable_receive_sum(self):
        self.project_object().order_8()

    def test_order_clickable_receive_delivery_time(self):
        self.project_object().order_9()

    def test_order_clickable_receive_payment_type(self):
        self.project_object().order_10()

    def test_order_clickable_ready_number(self):
        self.project_object().order_11()

    def test_order_clickable_ready_status(self):
        self.project_object().order_12()

    def test_order_clickable_ready_ismain(self):
        self.project_object().order_13()

    def test_order_clickable_ready_order(self):
        self.project_object().order_14()

    def test_order_clickable_ready_first_name(self):
        self.project_object().order_15()

    def test_order_clickable_ready_last_name(self):
        self.project_object().order_16()

    def test_order_clickable_ready_address(self):
        self.project_object().order_17()

    def test_order_clickable_ready_phone_number(self):
        self.project_object().order_18()

    def test_order_clickable_ready_sum(self):
        self.project_object().order_19()

    def test_order_clickable_ready_delivery_time(self):
        self.project_object().order_20()

    def test_order_clickable_ready_payment_type(self):
        self.project_object().order_21()

    def test_order_clickable_finish_number(self):
        self.project_object().order_22()

    def test_order_clickable_finish_status(self):
        self.project_object().order_23()

    def test_order_clickable_finish_ismain(self):
        self.project_object().order_24()

    def test_order_clickable_finish_order(self):
        self.project_object().order_25()

    def test_order_clickable_finish_first_name(self):
        self.project_object().order_26()

    def test_order_clickable_finish_last_name(self):
        self.project_object().order_27()

    def test_order_clickable_finish_address(self):
        self.project_object().order_28()

    def test_order_clickable_finish_phone_number(self):
        self.project_object().order_29()

    def test_order_clickable_finish_sum(self):
        self.project_object().order_30()

    def test_order_clickable_finish_delivery_time(self):
        self.project_object().order_31()

    def test_order_clickable_finish_payment_type(self):
        self.project_object().order_32()

    def test_order_clickable_send_number(self):
        self.project_object().order_33()

    def test_order_clickable_send_status(self):
        self.project_object().order_34()

    def test_order_clickable_send_ismain(self):
        self.project_object().order_35()

    def test_order_clickable_send_order(self):
        self.project_object().order_36()

    def test_order_clickable_send_first_name(self):
        self.project_object().order_37()

    def test_order_clickable_send_last_name(self):
        self.project_object().order_38()

    def test_order_clickable_send_address(self):
        self.project_object().order_39()

    def test_order_clickable_send_phone_number(self):
        self.project_object().order_40()

    def test_order_clickable_send_sum(self):
        self.project_object().order_41()

    def test_order_clickable_send_delivery_time(self):
        self.project_object().order_42()

    def test_order_clickable_send_payment_type(self):
        self.project_object().order_43()

    def test_order_receive_download(self):
        self.project_object().order_44()

    def test_order_send_download(self):
        self.project_object().order_45()

    def test_order_finished_download(self):
        self.project_object().order_46()

    def test_order_ready_download(self):
        self.project_object().order_47()

    def test_order_receive_first_name_search(self):
        self.project_object().order_48()

    def test_order_receive_last_name_search(self):
        self.project_object().order_49()

    def test_order_receive_phone_number_search(self):
        self.project_object().order_50()

    def test_order_receive_payment_type_search(self):
        self.project_object().order_51()

    def test_order_ready_first_name_search(self):
        self.project_object().order_52()

    def test_order_ready_last_name_search(self):
        self.project_object().order_53()

    def test_order_ready_phone_number_search(self):
        self.project_object().order_54()

    def test_order_ready_payment_type_search(self):
        self.project_object().order_55()

    def test_order_send_first_name_search(self):
        self.project_object().order_56()

    def test_order_send_last_name_search(self):
        self.project_object().order_57()

    def test_order_send_phone_number_search(self):
        self.project_object().order_58()

    def test_order_send_payment_type_search(self):
        self.project_object().order_59()

    def test_order_finish_first_name_search(self):
        self.project_object().order_60()

    def test_order_finish_last_name_search(self):
        self.project_object().order_61()

    def test_order_finish_phone_number_search(self):
        self.project_object().order_62()

    def test_order_finish_payment_type_search(self):
        self.project_object().order_63()





