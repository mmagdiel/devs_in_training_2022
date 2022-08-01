'''
    Diseñar una función que reciba y retorne una serie de números distintos de cero. 
    La función debe terminar con un valor cero que no se debe retornar, debe el número de valores leídos.
'''
def show_any_number_distinc_zero(list):
    if list == [] or list== str(list):
        return [0]
    lista=[]
    contador=0
    for i in list:
        if i != 0:
            lista.append(i)
            contador = contador +1
        elif i == 0:
            break
    lista.append(contador)
    return lista