from dataclasses import dataclass
from json import dumps

@dataclass
class Alumno():
    nombre: str
    primer_apellido: str
    promedio: float
    segundo_apellido: str = ""
    inscrito: bool = True

alumnonuevo = Alumno(nombre="Juan", primer_apellido="Pérez", promedio=8.6)
print(alumnonuevo)