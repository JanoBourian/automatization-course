import requests

with requests.get('https://pythonista-dev.uc.r.appspot.com/openapi.json') as r: 
    print(r.status_code)
    print(r.content)