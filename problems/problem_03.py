'''
    Escribir una función para determinar el mínimo común múltiplo de dos números enteros.
'''
def mcm(number_1, number_2):
    if number_1==str(number_1) or number_2==str(number_2):
        return 0
    if number_1==float(number_1) or number_2==float(number_2):
        number_1 = int(number_1)
        number_2 = int(number_2)
    z = max(number_1, number_2)
    while True:
        if (z % number_1 == 0) and (z % number_2 == 0):
            return z
        else:       
          z += 1