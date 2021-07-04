import requests

url = "https://playground.learnqa.ru/api/homework_cookie"


def test_cookie():
    resp = requests.get(url)
    expected_cookie = 'hw_value'
    cookie_name = 'HomeWork'
    assert cookie_name in resp.cookies, f'There is no "{cookie_name}" cookie in response'
    actual_cookie = resp.cookies[cookie_name]
    assert actual_cookie == expected_cookie, f"Actual cookie is {actual_cookie}, expected {expected_cookie}"
