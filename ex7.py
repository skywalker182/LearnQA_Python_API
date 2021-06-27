import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
method_types = {'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS', 'CONNECT', 'TRACE'}


def part_1():
    res = requests.get(url)
    print(
        f'for {res.request.method}  method type and without param status code is {res.status_code} and response is {res.text}')
    res = requests.post(url)
    print(
        f'for {res.request.method}  method type and without param status code is {res.status_code} and response is {res.text}')
    res = requests.put(url)
    print(
        f'for {res.request.method}  method type and without param status code is {res.status_code} and response is {res.text}')
    res = requests.delete(url)
    print(
        f'for {res.request.method}  method type and without param status code is {res.status_code} and response is {res.text}')


def part_2():
    res = requests.head(url)
    print(
        f'for {res.request.method}  method type and without param status code is {res.status_code} and response is {res.text}')


def part_3():
    res = requests.get(url, params={"method": "GET"})
    print(
        f'for {res.request.method} method type and param GET status code is {res.status_code} and response is {res.text}')
    res = requests.post(url, data={"method": "POST"})
    print(
        f'for {res.request.method}  method type and param POST status code is {res.status_code} and response is {res.text}')
    res = requests.put(url, data={"method": "PUT"})
    print(
        f'for {res.request.method}  method type and param PUT status code is {res.status_code} and response is {res.text}')
    res = requests.delete(url, params={"method": "DELETE"})
    print(
        f'for {res.request.method}  method type and param DELETE status code is {res.status_code} and response is {res.text}')


def part_4():
    get_with_params()
    delete_with_params()
    post_with_params()
    put_with_params()


def get_with_params():
    for obj in method_types:
        res = requests.get(url, params={"method": obj})
        if res.request.method != obj and res.text != 'Wrong method provided':
            print(
                f'WARNING !!! for {res.request.method}  method type and param {obj} status code is {res.status_code} and response is {res.text}')
        else:
            print(
                f'for {res.request.method}  method type and param {obj} status code is {res.status_code} and response is {res.text}')


def delete_with_params():
    for obj in method_types:
        res = requests.delete(url, params={"method": obj})
        if res.request.method != obj and res.text != 'Wrong method provided':
            print(
                f'WARNING !!! for {res.request.method}  method type and param {obj} status code is {res.status_code} and response is {res.text}')
        else:
            print(
                f'for {res.request.method}  method type and param {obj} status code is {res.status_code} and response is {res.text}')


def post_with_params():
    for obj in method_types:
        res = requests.post(url, data={"method": obj})
        if res.request.method != obj and res.text != 'Wrong method provided':
            print(
                f'WARNING !!! for {res.request.method}  method type and param {obj} status code is {res.status_code} and response is {res.text}')
        else:
            print(
                f'for {res.request.method}  method type and param {obj} status code is {res.status_code} and response is {res.text}')


def put_with_params():
    for obj in method_types:
        res = requests.put(url, data={"method": obj})
        if res.request.method != obj and res.text != 'Wrong method provided':
            print(
                f'WARNING !!! for {res.request.method}  method type and param {obj} status code is {res.status_code} and response is {res.text}')
        else:
            print(
                f'for {res.request.method}  method type and param {obj} status code is {res.status_code} and response is {res.text}')


part_1()
print("\n")
part_2()
print("\n")
part_3()
print("\n")
part_4()
