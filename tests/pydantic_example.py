from pydantic import BaseModel

class Alumno(BaseModel):
    cuenta : int 
    nombre : str
    carrera : str = ''
    
datos = {
    "cuenta": 198, 
    "nombre": "Fernando"
}

alumno = Alumno(**datos)
print(alumno)
dict(alumno)
print(alumno.schema())
print(alumno.schema_json())