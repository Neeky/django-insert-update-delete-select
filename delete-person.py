from datetime import datetime


import requests

session = requests.Session()
session.headers.update({'Accept': 'application/json'})

response = session.post(
    "http://127.0.0.1:8080/foo/api/person/delete/1", data={})
print(response.text)
