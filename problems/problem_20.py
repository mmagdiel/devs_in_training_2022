'''
    Diseñar una función que retorne la moda de una lista de datos.
    La moda es el valor más repetido de una muestra dada
'''
from statistics import multimode
def get_mode(lista):
    if len(lista)==0:
        return "No existe"
    for i in lista:
        if type(i)==type("Lorem"):
            return "No existe"
    return(multimode(lista))

