import requests
from lib.Assertions import Assertions
from lib.BaseCase import BaseCase

class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    url1 = 'https://playground.learnqa.ru/api/user/login'
    url2 = 'https://playground.learnqa.ru/api/user/auth'

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post(url=self.url1, data=data)
        print(response1.cookies)
        print(response1.text)
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    def test_user_auth(self):
        response2 = requests.get(
            url=self.url2,
            headers={'x-csrf-token': self.token},
            cookies={'auth_sid': self.auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user from check method"
            )

