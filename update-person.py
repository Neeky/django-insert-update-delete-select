from datetime import datetime


import requests

session = requests.Session()
session.headers.update({'Accept': 'application/json'})
#session.headers.update({'X-REQUESTED-WITH': 'XMLHttpRequest'})
data = {'name': 'tim cook'}
response = session.post(
    "http://127.0.0.1:8080/foo/api/person/update/1", data=data)
print(response.text)
