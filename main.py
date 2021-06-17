import requests


def get_text():
    url = 'https://playground.learnqa.ru/api/get_text'
    return requests.get(url)


print(get_text().text)
