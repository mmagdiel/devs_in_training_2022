'''
    Diseñar una función que retorne, en orden inverso, cada múltiplo de 3 entre 1 y un número dado.
'''
def get_three_multiple_inverse_list(number):
    list=[]
    i=1
    if type(number)==type(list):
        return []
    if  number == str(number):
        return []
    while i<=number:
        if number%3==0:
            list.append(number)
        number=number-1
    return(list)
