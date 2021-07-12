import json.decoder

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
