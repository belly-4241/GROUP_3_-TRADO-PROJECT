import time
from Web.TradoAdmin.base.base import BaseSetups
from selenium.webdriver.common.by import By


class TestAll_pages(BaseSetups):
    def dashboard(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "walelgn")
        self.fields(By.XPATH, self.CODE, "234")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)



    def dashboard_1(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(1)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(1)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "")
        self.fields(By.XPATH, self.CODE, "")
        self.fields(By.XPATH, self.MINIMUM_SUM, "")
        self.fields(By.XPATH, self.DATE_START, "")
        self.fields(By.XPATH, self.DATE_END, "")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)
        assert self.assertion(By.XPATH, self.NAME_ASSERTION) == "???? ee???? ?????? ????xxx"
        # if self.assertion(By.XPATH, self.DASHBOARD_BOARD_ALL_EMPTY) == "???? ???????? ?????? ????xxx":
        #     print("p")
        # else:
        #     print("faild")


    def dashboard_2(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "")
        self.fields(By.XPATH, self.CODE, "234")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)
        assert self.assertion(By.XPATH, self.NAME_ASSERTION) == "???? ??????er?? ?????? ????xxx"
        # if self.assertion(By.XPATH, self.DASHBOARD_BOARD_ALL_EMPTY) == "???? ???????? ?????? ????xxx":
        #     print("p")
        # else:
        #     print("faild")



    def dashboard_3(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "walelgn ")
        self.fields(By.XPATH, self.CODE, "")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)
        assert self.assertion(By.XPATH, self.CODE_ASSERTION) == "???? ???????? ?????? ????wexxx"
        # if self.assertion(By.XPATH, self.DASHBOARD_BOARD_ALL_EMPTY) == "???? ???????? ?????? ????xxx":
        #     print("p")
        # else:
        #     print("faild")

    def dashboard_4(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "walelgn")
        self.fields(By.XPATH, self.CODE, "234")
        self.fields(By.XPATH, self.MINIMUM_SUM, "")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)
        assert self.assertion(By.XPATH, self.MINIMUM_SUM_ASSERTION) == "???? ???????? ?????? ????xxx44"

        #if self.assertion(By.XPATH, self.DASHBOARD_BOARD_ALL_EMPTY) == "???? ???????? ?????? ????xxx":

        #     print("p")
        # else:
        #     print("faild")

    def dashboard_5(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "walelgn ")
        self.fields(By.XPATH, self.CODE, "234")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)
        #if self.assertion(By.XPATH, self.DASHBOARD_BOARD_ALL_EMPTY) == "???? ???????? ?????? ????xxx":

        #     print("p")
        # else:
        #     print("faild")

    def dashboard_6(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, " walelgn")
        self.fields(By.XPATH, self.CODE, "234")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)
        # if self.assertion(By.XPATH, self.DASHBOARD_BOARD_ALL_EMPTY) == "???? ???????? ?????? ????xxx":

        #     print("p")
        # else:
        #     print("faild")

    def dashboard_7(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "walelgn ")
        self.fields(By.XPATH, self.CODE, "234")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)


    def dashboard_8(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "walel3gn34 ")
        self.fields(By.XPATH, self.CODE, "234")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)

    def dashboard_9(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "walelgn ")
        self.fields(By.XPATH, self.CODE, "2qwer34")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)

    def dashboard_10(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "876578 ")
        self.fields(By.XPATH, self.CODE, "234")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/2/2023")
        self.fields(By.XPATH, self.DATE_END, "7/4/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)

    def dashboard_11(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.ADD)
        self.fields(By.XPATH, self.NAME, "walelgn ")
        self.fields(By.XPATH, self.CODE, "edrtyu")
        self.fields(By.XPATH, self.MINIMUM_SUM, "4")
        self.fields(By.XPATH, self.DATE_START, "2/october/2023")
        self.fields(By.XPATH, self.DATE_END, "7/3/2023")
        self.fields(By.XPATH, self.DISCOUNT_SUM, "6")
        self.click(By.XPATH, self.TYPE)
        self.click(By.XPATH, self.SHEKEL)
        self.click(By.XPATH, self.ADD_END)

    def dashboard_12(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DOT)
        self.click(By.XPATH, self.DOWNLOAD)

    def dashboard_13(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.fields(By.XPATH, self.SEARCH, "walelgn")

    def dashboard_14(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.NAME_BUTTON)

    def dashboard_15(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.MINIMUM_SUM_CLICK)

    def dashboard_16(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.USER_ONCE_TIME)

    def dashboard_17(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.RANGE_DATE)

    def dashboard_18(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.ACTIVE)

    def dashboard_19(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DATE_STOP)

    def dashboard_20(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)
        self.click(By.XPATH, self.DISCOUNT)

    def dashboard_21(self):
        self.setup_trado()
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(1)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(1)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(1)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DASHBOARD_BOARD)
        self.click(By.XPATH, self.COUPONS)

