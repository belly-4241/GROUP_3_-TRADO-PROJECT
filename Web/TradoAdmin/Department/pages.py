import time

from Web.TradoAdmin.base.base import BaseSetups
from selenium.webdriver.common.by import By
class TestAll_pages(BaseSetups):

    def department(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.ID)
        self.fields(By.XPATH, self.SEARCH_DEPARTMENT, "u6z3r13kkkv9cqk3")
    def department_1(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.NAME)
        self.fields(By.XPATH, self.SEARCH_DEPARTMENT, "u6z3r13kkkv9cqk3")

    def department_2(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.CLICK_DOT)
        self.click(By.XPATH, self.DOWNLOAD)
    def department_3(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.ID)

    def department_4(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.NAME)

    def department_5(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.PHOTO)

    def department_6(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.ACTIVE)

    def department_7(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.DATE_FINISH)

    def department_8(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.PHOTO_BACKGROUND)

    def department_9(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.CLICK_DOT)
        self.click(By.XPATH, self.ADD_DOT)
        self.fields(By.XPATH, self.NAME_DPT, "atanaw")


    def department_10(self):
        self.setup_trado()
        time.sleep(2)
        self.fields(By.XPATH, self.PHONE, "1952222222")
        time.sleep(2)
        self.click(By.XPATH, self.PHONE_BUTTON)
        time.sleep(2)
        self.fields(By.XPATH, self.CODE_PHONE, "1234")
        time.sleep(2)
        self.click(By.XPATH, self.CONNECT)
        self.click(By.XPATH, self.DEPARTMENT)
        self.click(By.XPATH, self.CLICK_DOT)
        self.click(By.XPATH, self.ADD_DOT)
        self.fields(By.XPATH, self.NAME_DPT, " ")





