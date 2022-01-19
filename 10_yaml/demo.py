import yaml 

listado = {'personas': [
    {"id": 1001,
    'nombre': 'Juan',
    'primer_apellido': 'Pérez',
    'segundo_apellido': 'de la Rosa',
    'carrera': 'Derecho',
    'cursos': {
        'py101': 'AC',
        'py111': 'AC',
        'py121': 'NA',
        'py131': {
            'PN': {
                'clave_evento': 'py131-2007',
                'fecha_inicio': '15/07/2020',
                'requisitos': [
                    'py101', 
                    'py111']}},
        'py201': 'NA'}},
    {"id": 1002,
     'nombre': 'María',
     'primer_apellido': 'Mendoza',
     'segundo_apellido': '',
     'carrera': 'Derecho',
     'cursos': {
         'py101': 'AC', 
         'py111': 'AC', 
         'py121': 'AC'}}]}

listado['personas'][0]['cursos']

yaml.dump(listado, encoding="utf-8")

estructura = yaml.dump(listado, encoding="utf-8")

otra_estructura = yaml.load(estructura, yaml.Loader)

print(otra_estructura)

with open("archivo.yaml", "w") as f:
    yaml.dump(listado, f)