'''
    Diseñar una función que retorne, en orden inverso, cada múltiplo de 3 entre 1 y un número dado.
'''
def get_three_multiple_inverse_list(number):
    lista=[]
    i=1
    if type(number)==type(lista):
        return []
    if  number == str(number):
        return []
    while i<=number:
        if number%3==0:
            lista.append(number)
        number=number-1
    return(lista)
