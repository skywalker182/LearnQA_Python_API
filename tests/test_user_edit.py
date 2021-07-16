import requests
from lib.BaseCase import BaseCase
from lib.Assertions import Assertions

login_url = 'https://playground.learnqa.ru/api/user/login'
user_url = 'https://playground.learnqa.ru/api/user/'


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = requests.post(user_url, data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post(url=login_url, data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_name = "changedName"
        new_url = user_url + str(user_id)
        response3 = requests.put(
            new_url,
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={'firstName': new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # Get
        response4 = requests.get(
            new_url,
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of user after edit"
        )

    def test_edit_just_created_user_too_incorrect_email(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = requests.post(user_url, data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post(url=login_url, data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_email = "changedemail"
        new_url = user_url + str(user_id)
        response3 = requests.put(
            new_url,
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={'email': new_email}
        )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_response_text(response3, 'Invalid email format')

    def test_edit_just_created_user_too_short_name(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = requests.post(user_url, data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post(url=login_url, data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_name = "c"
        new_url = user_url + str(user_id)
        response3 = requests.put(
            new_url,
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={'firstName': new_name}
        )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_response_text(response3, '{"error":"Too short value for field firstName"}')

    def test_edit_just_created_user_without_auth(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = requests.post(user_url, data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Edit
        new_name = "changedName"
        new_url = user_url + str(user_id)
        response3 = requests.put(
            new_url,
            data={'firstName': new_name}
        )
        print(response3.text)

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_response_text(response3, "Auth token not supplied")

    def test_edit_just_created_user_with_wrong_token(self):
        # Register #1
        register_data1 = self.prepare_registration_data()
        response1 = requests.post(user_url, data=register_data1)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # Register #2
        register_data2 = self.prepare_registration_data()
        response1_2 = requests.post(user_url, data=register_data2)

        Assertions.assert_code_status(response1_2, 200)
        Assertions.assert_json_has_key(response1_2, "id")
        print(response1_2.text)

        email = register_data2['email']
        password = register_data2['password']

        # Login as second user
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post(url=login_url, data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_name = "changedName"
        new_url = user_url + str(user_id)
        response3 = requests.put(
            new_url,
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={'username': new_name}
        )

        Assertions.assert_code_status(response3, 200)  # а должно ли быть 200
        print("text after edit ", response3.text)

        # Get
        response4 = requests.get(
            new_url,
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        print(response4.text)

        Assertions.assert_json_value_by_name(
            response4,
            "username",
            new_name,
            "Wrong name of user after edit"
        )
