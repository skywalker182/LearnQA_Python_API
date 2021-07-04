import requests

url = 'https://playground.learnqa.ru/api/homework_header'


def test_headers():
    resp = requests.get(url)
    expected_header = 'Some secret value'
    header_name = 'x-secret-homework-header'
    assert resp.status_code == 200, "Wrong Status Code"
    assert header_name in resp.headers, f'There is no "{header_name}" header in response'
    actual_header = resp.headers[header_name]
    assert expected_header == actual_header, f'Actual header is {actual_header}, expected {expected_header}'

