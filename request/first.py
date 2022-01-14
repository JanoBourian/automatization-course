import requests

print(dir(requests))

res = requests.get('https://www.google.com')

print(res)
print(type(res))

print(res.headers)
print(res.status_code)
print(res.reason)
print(res.url) 
print(res.content)
print(res.encoding)
print(res.text)
print("*********************")
res = requests.post("https://httpbin.org/post", json = {"saludo": "Hola"})
print(res.json())
res.close()

with requests.get("https://www.pythonista.io") as sitio:
    print(sitio.status_code)
    print(sitio.headers)
    print(sitio.url)