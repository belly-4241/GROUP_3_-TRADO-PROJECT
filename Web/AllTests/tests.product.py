from Web.TradoAdmin.Product.pages import TestAll_Product
import allure
import pytest
class Test_Product(TestAll_Product):
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_valid_login(self):
        login = TestAll_Product()
        login.Valid_phone()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_invalid_phone(self):
        login = TestAll_Product()
        login.Invalid_phone()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_empty_phone(self):
        login = TestAll_Product()
        login.Empty_phone()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_character_phone(self):
        login = TestAll_Product()
        login.Character_phone()
    def test_valid_phone_code(self):
        login = TestAll_Product()
        login.Valid_phone_code()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_valid_phone_invalid_code(self):
        login = TestAll_Product()
        login.Valid_phone_invalid_code()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_valid_phone_empty_code(self):
        login = TestAll_Product()
        login.Valid_phone_empty_code()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_valid_phone_character_code(self):
        login = TestAll_Product()
        login.Valid_phone_character_code()

    def test_valid_phone_save(self):
        login = TestAll_Product()
        login.Valid_phone_code_save()
    def test_product(self):
        login = TestAll_Product()
        login.Product()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_search_button(self):
        product = TestAll_Product()
        product.Product_Search_Button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_number_input_serrch(self):
        search = TestAll_Product()
        search.Number_Input_Search()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_charactor_input_search(self):
        search = TestAll_Product()
        search.Charactor_Input_Search()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_charactor_number_search(self):
        search = TestAll_Product()
        search.Number_Chara_Search()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_one_elemnt(self):
        code = TestAll_Product()
        code.One_Element()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_to_forward(self):
        forward = TestAll_Product()
        forward.To_forward()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_to_backward(self):
        backward = TestAll_Product()
        backward.To_Backward()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_to_left(self):
        right = TestAll_Product()
        right.T0_Left_Side()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_to_right(self):
        left = TestAll_Product()
        left.To_Right_Side()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_left_corner(self):
        left = TestAll_Product()
        left.Left_corner()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_plus(self):
        plus = TestAll_Product()
        plus.Plus()


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_plus_symbol(self):
        plus = TestAll_Product()
        plus.Plus_symbol()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_download(self):
        download = TestAll_Product()
        download.Download()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_download_symbol(self):
        download = TestAll_Product()
        download.Download_Smbol()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_add_to_brand(self):
        add = TestAll_Product()
        add.Add_To_Brand()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_add_to_brand_symbol(self):
        add = TestAll_Product()
        add.Add_To_Brand_symbol()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_come(self):
        come = TestAll_Product()
        come.Come()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_come_symbol(self):
        come = TestAll_Product()
        come.Come_symbol()
    def test_pattern(self):
        pattern = TestAll_Product()
        pattern.Pattern()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_pattern_symbol(self):
        pattern = TestAll_Product()
        pattern.Pattern_Symbol()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_full_plus(self):
        plus = TestAll_Product()
        plus.Plus_Full()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_full_add_to_brand(self):
        add = TestAll_Product()
        add.Add_To_Brand_Full()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_come_import(self):
        come = TestAll_Product()
        come.Come_Import()
        come.SwitchAlert2()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_come_send(self):
        come = TestAll_Product()
        come.Come_Send()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_come_full(self):
        come = TestAll_Product()
        come.Come_Full()
        come.Come_Send()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_modify(self):
        modify = TestAll_Product()
        modify.Modify()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_barcode_modify(self):
        barcode = TestAll_Product()
        barcode.modify_barcode()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_name_modify(self):
        name = TestAll_Product()
        name.modify_name()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_expiredate_modify(self):
        expire = TestAll_Product()
        expire.modify_expiredate()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_photo_modify(self):
        photo = TestAll_Product()
        photo.modify_photo()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_price_modify(self):
        price = TestAll_Product()
        price.modify_price()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_description_modify(self):
        description = TestAll_Product()
        description.modify_description()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_part_one(self):
        partone = TestAll_Product()
        partone.part_one()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_next_button(self):
        butt = TestAll_Product()
        butt.next_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_promotion_modify(self):
        promotion = TestAll_Product()
        promotion.modify_promoption()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_department_modify(self):
        department = TestAll_Product()
        department.modify_department()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_dakgard_modify(self):
        dakgard = TestAll_Product()
        dakgard.modify_dakgard()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_catagory_modify(self):
        catagory = TestAll_Product()
        catagory.modify_catagory()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_productTag_modify(self):
        produc = TestAll_Product()
        produc.modify_productTag()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_parallel_modify(self):
        parallel = TestAll_Product()
        parallel.modify_parallel()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_next2_button(self):
        nextb = TestAll_Product()
        nextb.next2_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_carto_modify(self):
        carton = TestAll_Product()
        carton.modify_carton_amount()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_amount_modify(self):
        amount = TestAll_Product()
        amount.modify_amoun()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_minimium_carton_modify(self):
        minium = TestAll_Product()
        minium.modify_minimium_carton()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_next3_button(self):
        nxt3 = TestAll_Product()
        nxt3.next3_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_city_modify(self):
        city = TestAll_Product()
        city.modify_city()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_number_modify(self):
        numbe = TestAll_Product()
        numbe.modify_number()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_street_modify(self):
        street = TestAll_Product()
        street.modify_street()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_number_modify(self):
        contact = TestAll_Product()
        contact.modify_contact_number()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_next4_button(self):
        nextt = TestAll_Product()
        nextt.next4_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_back_button(self):
        back = TestAll_Product()
        back.back_button()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_button2(self):
        butt = TestAll_Product()
        butt.buttu2()
    def test_next42_button(self):
        nextb = TestAll_Product()
        nextb.next42_button()





