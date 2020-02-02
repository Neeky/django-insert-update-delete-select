from datetime import datetime


import requests

session = requests.Session()
session.headers.update({'Accept': 'application/json'})
session.headers.update({'X-REQUESTED-WITH': 'XMLHttpRequest'})

print(session.headers)
# session.get("http://127.0.0.1:8080")api/person/create

data = {'name': datetime.now().isoformat()[:24], 'age': '16'}
response = session.post(
    "http://127.0.0.1:8080/foo/api/person/create", data=data)
print(response.text)
