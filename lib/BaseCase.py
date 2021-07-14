import string
from datetime import datetime
import json.decoder
import random

from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name '{cookie_name}' in the response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find cookie with name '{header_name}' in the response"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON, response text is {response.text}"
        assert name in response_as_dict, f"response text doesn't have key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, email=None, username='learnqa', firstname='learnqa', lastname='leanqa'):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            "password": '1232',
            'username': username,
            'firstName': firstname,
            'lastName': lastname,
            'email': email
        }

    def get_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

