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
    listaauxiliar=[]
    for n in list:
        if n != 0:
            contador = contador+1
            listaauxiliar.append(n)
        elif n == 0:
            listaauxiliar.append(contador)
            return listaauxiliar
            break