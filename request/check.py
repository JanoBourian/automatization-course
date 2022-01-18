import requests

ruta = "https://pythonista-dev.uc.r.appspot.com/api"

respuesta = requests.get(ruta)

print(respuesta)
print(respuesta.url)
print(respuesta.status_code)
print(respuesta.json())

respuesta = requests.get(ruta + "/1231222")
print(respuesta)
print(respuesta.url)
print(respuesta.status_code)
print(respuesta.json())

respuesta = requests.get(ruta + "/api/3000")
print(respuesta)
print(respuesta.url)
print(respuesta.status_code)
print(respuesta.json())

# Crear datos
datos ={'nombre':'Juan',
        'primer_apellido': 'Escutia',
        'segundo_apellido':'Aventado', 
        'carrera':'Arquitectura',
        'semestre':1,
        'promedio':10,
        'al_corriente':True,}
respuesta = requests.post(ruta + "/1231226", json=datos)
print(respuesta)
print(respuesta.url)
print(respuesta.status_code)
print(respuesta.json())
