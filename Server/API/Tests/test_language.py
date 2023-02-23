# from Server.API.Constants.language_locator import  language
# import requests
# import allure
# @allure.description('Login correctly')
# class Test_Language_Api(language):
#     def test_valid_language(self):
#         url = language.ULR
#         data = language.Valid_data
#         res = requests.post(url, json=data)
#         res_data = res.json()
#         assert res.status_code == 200
#         assert res.elapsed.total_seconds() < 10
#     def test_invalid_language(self):
#         url = language.ULR
#         data = language.Invalid_language_data
#         res = requests.post(url, json=data)
#         res_data = res.json()
#         assert res.status_code == 200
#         assert res.elapsed.total_seconds() < 10
#     def test_empty_language(self):
#         url = language.ULR
#         data = language.Empty_language
#         res = requests.post(url, json=data)
#         res_data = res.json()
#         assert res.status_code == 200
#         assert res.elapsed.total_seconds() < 10