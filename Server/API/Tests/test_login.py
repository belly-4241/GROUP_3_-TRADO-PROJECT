from Server.API.Constants.login_locator import  Login_API
import requests
import allure
@allure.description('Login correctly')
class Test_Language_Api(Login_API):
    def test_valid_login(self):
        url = Login_API.url_login
        data = Login_API.Valid_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_invalid_phone(self):
        url = Login_API.url_login
        data = Login_API.Invalid_phone
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_invalid_code(self):
        url = Login_API.url_login
        data = Login_API.Invalid_code
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_invalid_remember(self):
        url = Login_API.url_login
        data = Login_API.Invalid_remember
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_invalid_phone_code(self):
        url = Login_API.url_login
        data = Login_API.Invalid_phone_code
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_invalid_phone_remember(self):
        url = Login_API.url_login
        data = Login_API.Invalid_phone_remember
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_invalid_code_remember(self):
        url = Login_API.url_login
        data = Login_API.Invalid_code_remember
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_invalid_data(self):
        url = Login_API.url_login
        data = Login_API.Invalid_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_empty_phone(self):
        url = Login_API.url_login
        data = Login_API.Empty_phone
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_empty_code(self):
        url = Login_API.url_login
        data = Login_API.Empty_code
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_empty_phone_code(self):
        url = Login_API.url_login
        data = Login_API.Empty_phone_code
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
    def test_empty_phone_code_invalid_remember(self):
        url = Login_API.url_login
        data = Login_API.Emtpy_phone_code_invalid_remember
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10