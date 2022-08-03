'''
    Calcular la suma de los elementos de la diagonal principal de una matriz cuatro de hasta por cuatro (4 × 4). 
    Esto es llamada la traza de una matriz.
'''
def get_trace(matriz):
    if len(matriz)<=1:
        return 1
    acumulador=0
    for x in matriz:
        n=x
        for el in n:
            if type(el)==bool or type(el)==str or type(el)==type({"abc":123}):
                return 0
    for i in range(len(matriz)):
        acumulador=acumulador+matriz[i][i]
    return acumulador
