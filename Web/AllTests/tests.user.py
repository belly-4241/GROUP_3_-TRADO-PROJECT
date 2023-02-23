from Web.TradoAdmin.User.pages import Test_All_Users
import allure
import pytest
class TestUser(Test_All_Users):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_user(self):
        user = Test_All_Users()
        user.User_Link()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_serarch_user(self):
        search = Test_All_Users()
        search.search_button_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_search_charac(self):
        search = Test_All_Users()
        search.search_charactor()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_next_user(self):
        next = Test_All_Users()
        next.next_user()
    def test_back_user(self):
        back = Test_All_Users()
        back.back_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_forward(self):
        forward = Test_All_Users()
        forward.forward_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_backward(self):
        backward = Test_All_Users()
        backward.backward_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_photo_user(self):
        photo = Test_All_Users()
        photo.photo_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_first_name_user(self):
        first_name = Test_All_Users()
        first_name.first_name_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_last_name_user(self):
        last_name = Test_All_Users()
        last_name.last_name_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_phone_user(self):
        phone = Test_All_Users()
        phone.photo_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_shop_user(self):
        shop = Test_All_Users()
        shop.shop_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_email_user(self):
        email = Test_All_Users()
        email.email_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_additional_phone_user(self):
        aditional = Test_All_Users()
        aditional.additional_phone_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_city_user(self):
        city = Test_All_Users()
        city.city_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_street_user(self):
        street = Test_All_Users()
        street.street_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_class_user(self):
        classs = Test_All_Users()
        classs.class_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_city_hall_user(self):
        city_hall = Test_All_Users()
        city_hall.city_hall_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_building_user(self):
        building = Test_All_Users()
        building.building_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_floor_user(self):
        floor = Test_All_Users()
        floor.floor_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_account_owner_user(self):
        account = Test_All_Users()
        account.account_number_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_number_branch_user(self):
        branch = Test_All_Users()
        branch.number_branch_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_number_account_user(self):
        number_account = Test_All_Users()
        number_account.number_account_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_bank_number_user(self):
        bank = Test_All_Users()
        bank.bank_number_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_credit_account_user(self):
        credit = Test_All_Users()
        credit.credit_account_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_balance_user(self):
        balance = Test_All_Users()
        balance.balance_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_income_user(self):
        income = Test_All_Users()
        income.income_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_outcome_user(self):
        outcome = Test_All_Users()
        outcome.outcome_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_id_user(self):
        user_id = Test_All_Users()
        user_id.id_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_mailing_list_user(self):
        mailing = Test_All_Users()
        mailing.mailing_list_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_extra_user(self):
        extree = Test_All_Users()
        extree.extera_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_takanon(self):
        takanon = Test_All_Users()
        takanon.takanon_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_bussines_type_user(self):
        bussiness = Test_All_Users()
        bussiness.bussiness_type_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_button_user(self):
        button = Test_All_Users()
        button.button_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_ete_user(self):
        end = Test_All_Users()
        end.end_to_end_user()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description(" ")
    def test_firsname_numbe(self):
        fname_number = Test_All_Users()
        fname_number.first_name_nuber_user()




