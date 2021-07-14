import pytest
import requests
from lib.BaseCase import BaseCase
from lib.Assertions import Assertions

url = 'https://playground.learnqa.ru/api/user/'
len_of_regular_email = 250
len_of_short_name = 1
len_of_long_name = 251


class TestUserRegister(BaseCase):
    def test_user_with_incorrect_email(self):
        data = self.prepare_registration_data(email=BaseCase.get_random_string(len_of_regular_email))
        response = requests.post(url=url, data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_text(response, "Invalid email format")

    def test_user_with_very_short_name(self):
        data = self.prepare_registration_data(firstname=BaseCase.get_random_string(len_of_short_name))
        response = requests.post(url=url, data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_text(response, "The value of 'firstName' field is too short")

    def test_user_with_very_long_name(self):
        data = self.prepare_registration_data(
            firstname=BaseCase.get_random_string(len_of_long_name))
        response = requests.post(url=url, data=data)
        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_text(response, "The value of 'firstName' field is too long")

    @pytest.mark.parametrize("key",
                             ['password', 'firstName', 'username', 'lastName', 'email'])
    def test_user_without_required_fields(self, key):
        data = self.prepare_registration_data()
        data[key] = None
        response = requests.post(url=url, data=data)
        Assertions.assert_code_status(response, 400)
        print(response.text)
        Assertions.assert_response_text(response, f"The following required params are missed: {key}")
