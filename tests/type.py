from typing import List 

def listado(numero:int)-> List[int]:
    return [i for i in range (0, numero + 1)]

listado(11)