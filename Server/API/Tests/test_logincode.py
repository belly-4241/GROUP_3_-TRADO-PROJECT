# from Server.API.Constants.logincode_locator import  Logincode
# import requests
# import allure
# @allure.description('Login correctly')
# class Test_Logincode_Api(Logincode):
#     def test_valid_logincode(self):
#         url = Logincode.URL_Logincode
#         data = Logincode.Valid_data
#         res = requests.post(url, json=data)
#         res_data = res.json()
#         assert res.status_code == 200
#         assert res.elapsed.total_seconds() < 10
#     def test_invalid_logincode(self):
#         url = Logincode.URL_Logincode
#         data = Logincode.Invalid_logincode
#         res = requests.post(url, json=data)
#         res_data = res.json()
#         assert res.status_code == 200
#         assert res.elapsed.total_seconds() < 10
#     def test_empty_logincode(self):
#         url = Logincode.URL_Logincode
#         data = Logincode.Empty_logincode
#         res = requests.post(url, json=data)
#         res_data = res.json()
#         assert res.status_code == 200
#         assert res.elapsed.total_seconds() < 10