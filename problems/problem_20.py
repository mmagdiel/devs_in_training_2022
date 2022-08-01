'''
    Diseñar una función que retorne la moda de una lista de datos.
    La moda es el valor más repetido de una muestra dada
'''
def get_mode(lista):
    lista = [5, 6, 8, 9, 9, 9]
    valores = {valor:lista.count(valor) for valor in set(lista)}
    maximo = max(valores.values())
    modas = {k:v for k, v  in valores.items() if v == maximo}
    
    if len(modas) == 1:
        print(f"La moda es {list(modas)[0]}, con {maximo} ocurrencias")
    else:
        print("Las modas son: ")
        for k in modas.keys():
            print(f"Moda {k}, con {maximo} ocurrencias")
get_mode(1)
   