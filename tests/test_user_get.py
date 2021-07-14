import requests
from lib.BaseCase import BaseCase
from lib.Assertions import Assertions

url = 'https://playground.learnqa.ru/api/user/'
url_for_login = 'https://playground.learnqa.ru/api/user/login'
expected_fields = ['email', 'firstName', 'lastName']


class TestUserGet(BaseCase):
    def test_user_details_not_auth(self):
        new_url = url + '2'
        response = requests.get(new_url)
        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_not_keys(response, expected_fields)


    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post(url_for_login, data=data)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        new_url = url + str(user_id_from_auth_method)
        response2 = requests.get(
                                 new_url,
                                 headers={'x-csrf-token': token},
                                 cookies={'auth_sid': auth_sid}
                                 )
        Assertions.assert_json_has_key(response2, 'username')
        Assertions.assert_json_has_keys(response2, expected_fields)

    def test_get_user_details_auth_as_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post(url_for_login, data=data)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, "user_id")
        new_url = url + str(1)
        response2 = requests.get(
            new_url,
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        Assertions.assert_json_has_key(response2, 'username')
        Assertions.assert_json_has_not_keys(response2, expected_fields)


