import pytest
import requests

agents = [
    ('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),
    ('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),
    ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),
    ('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
]
platforms = [
    ('Mobile'),
    ('Mobile'),
    ('Googlebot'),
    ('Web'),
    ('Mobile')
]
browsers = [
    ('No'),
    ('Chrome'),
    ('Unknown'),
    ('Chrome'),
    ('No')
]
devices = [
    ('Android'),
    ('iOS'),
    ('Unknown'),
    ('No'),
    ('iPhone')
]


@pytest.mark.parametrize('agent, platform, browser, device', [
    pytest.param(
        agents[0], platforms[0], browsers[0], devices[0]
    ),
    pytest.param(
        agents[1], platforms[1], browsers[1], devices[1]
    ),
    pytest.param(
        agents[2], platforms[2], browsers[2], devices[2]
    ),
    pytest.param(
        agents[3], platforms[3], browsers[3], devices[3]
    ),
    pytest.param(
        agents[4], platforms[4], browsers[4], devices[4]
    ),
    ])
def test_user_agent(agent, platform, browser, device):
    url = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
    headers = {"User-Agent": agent}
    resp = requests.get(url, headers=headers)
    resp_dict = resp.json()
    assert resp.status_code == 200, "Wrong Code"

    print(resp_dict)
    assert 'platform' in resp_dict, "There is no field 'platform' in response"
    assert 'browser' in resp_dict, "There is no field 'browser' in response"
    assert 'device' in resp_dict, "There is no field 'device' in response"

    assert platform == resp_dict['platform'], f"Actual platform is {resp_dict['platform']}, expected {platform}"
    assert browser == resp_dict['browser'], f"Actual browser is {resp_dict['browser']}, expected {browser}"
    assert device == resp_dict['device'], f"Actual browser is {resp_dict['device']}, expected {device}"

