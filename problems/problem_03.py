'''
    Escribir una función para determinar el mínimo común múltiplo de dos números enteros.
'''

def mcm(number_1, number_2):

    minimo = max (number_1 , number_2)

    while (int (number_1) and int (number_2)):

        if (minimo % number_1 == 0) and (minimo % number_2 == 0):

            return minimo




