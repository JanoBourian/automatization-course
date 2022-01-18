import jsonschema

esquema_alumno = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "Nombre": {"type": "string",
                   "minLength":1,
                   },
        "Primer Apellido": {"type": "string", 
                   "minLength":1,},
        "Segundo Apellido": {"type": "string", 
                   "minLength":1,},
        "Carrera": {"type": "string"},
        "Semestre": {"type": "number",
                   "minimum": 1,
                   "maximum": 50,},
        "Promedio": {"type": "number",
                   "minimum": 0,
                   "maximum": 10,},
        "Al Corriente": {"type": "boolean"},
    },
    "required": ["Nombre",  "Primer Apellido", "Carrera", "Semestre",
                 "Promedio", "Al Corriente"]
}


jsonschema.validate({'Al Corriente': False,
                     'Carrera': 'Arquitectura',
                     'Nombre': 'Pedro', 
                     'Primer Apellido': 'Solis', 
                     'Promedio': 7.8, 
                     'Semestre': 5,}, 
                    esquema_alumno)


jsonschema.validate({'Al Corriente': False,
                     'Carrera': 'Arquitectura',
                     'Nombre': 'Pedro', 
                     'Primer Apellido': 'Solis', 
                     'Promedio': 7.8, 
                     'Semestre': 5,
                     'Género': 'F',},
                    esquema_alumno)

jsonschema.validate({'Al Corriente': False, 
          'Carrera': 'Arquitectura', 
          'Nombre': 'Pedro', 
          'Primer Apellido': 'Solis', 
          'Promedio': 7.8, 
          'Semestre': -7,}, 
                    esquema_alumno)