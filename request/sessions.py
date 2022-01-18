from requests import Session

ruta = "https://pythonista-dev.uc.r.appspot.com/api"
host = "https://pythonista-dev.uc.r.appspot.com"
s = Session()
datos_auth = {'username': 'admin', 'password': 'admin'}
s.post(f'{host}/auth/login', json=datos_auth)

respuesta = s.delete(f"{ruta}/1231221")
print(respuesta)
print(respuesta.url)
print(respuesta.status_code)

