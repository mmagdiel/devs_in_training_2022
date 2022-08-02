'''
    Diseñar una función que reciba y retorne una serie de números distintos de cero. 
    La función debe terminar con un valor cero que no se debe retornar, debe el número de valores leídos.
'''
def show_any_number_distinc_zero(list):
    if len(list) == 0:
        return [0]  
    if list == str(list):
        return [0]
    contador =0
    lista=[]
    for numero in list:
        if numero != 0:
            contador = contador+1
            lista.append(numero)
        elif numero == 0:
            lista.append(contador)
            return lista
            break