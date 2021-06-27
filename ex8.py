import requests
import json
import time

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

res = requests.get(url)
res_obj = json.loads(res.text)
token = res_obj["token"]
seconds = res_obj["seconds"]
res = requests.get(url, params={"token": token})
res_obj = json.loads(res.text)
assert res_obj["status"] == "Job is NOT ready"
time.sleep(seconds + 1)
res = requests.get(url, params={"token": token})
res_obj = json.loads(res.text)
assert res_obj["status"] == "Job is ready"
assert res_obj["result"] is not None
