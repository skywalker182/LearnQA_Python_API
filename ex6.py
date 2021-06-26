import requests

res = requests.get('https://playground.learnqa.ru/api/long_redirect')
redirects_count = len(res.history)
final_url = res.url
print(f'Количество редиректов = {redirects_count} \nКонечный URL = {final_url}')
