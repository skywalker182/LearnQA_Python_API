import requests
from lib.Assertions import Assertions
from lib.BaseCase import BaseCase
from lib.my_requests import MyRequests

login_url = '/user/login'
url_for_operations_with_user = '/user'

class TestUserDelete(BaseCase):
    def test_delete_user_with_id_lower_five(self):
        # Login
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post(login_url, data=data)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        # DELETE
        response2 = MyRequests.delete(
            url_for_operations_with_user + f'/{user_id_from_auth_method}',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_response_text(response2, 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.')

    def test_delete_just_created_user_with_same_id(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(url_for_operations_with_user, data=register_data)

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
        response2 = MyRequests.post(url=login_url, data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_name = "changedName"
        response3 = MyRequests.delete(
            url_for_operations_with_user + f'/{user_id}',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
        )

        Assertions.assert_code_status(response3, 200)

        # Get
        response4 = MyRequests.get(
            url_for_operations_with_user + f'/{user_id}',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )

        # проверяем, что удалился и не найден
        Assertions.assert_code_status(response4, 404)

    def test_delete_just_created_user_with_different_id(self):
        # Register #1
        register_data1 = self.prepare_registration_data()
        response1 = MyRequests.post(url_for_operations_with_user, data=register_data1)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")
        user_original_username = register_data1['username']

        # Register #2
        register_data2 = self.prepare_registration_data()
        response1_2 = MyRequests.post(url_for_operations_with_user, data=register_data2)

        Assertions.assert_code_status(response1_2, 200)
        Assertions.assert_json_has_key(response1_2, "id")

        email = register_data2['email']
        password = register_data2['password']

        # Login as second user
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post(url=login_url, data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # Edit
        new_name = "changedName"
        response3 = MyRequests.delete(
            url_for_operations_with_user + f'/{user_id}',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
        )

        Assertions.assert_code_status(response3, 200)

        # Get
        response4 = MyRequests.get(
            url_for_operations_with_user + f'/{user_id}',
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        # проверка, что не удалился
        Assertions.assert_code_status(response4, 200)

