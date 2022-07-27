'''
    Escribir una función para determinar el mínimo común múltiplo de dos números enteros.
'''

def mcm(number_1, number_2):
 if number_1 == str(number_1) or number_2 == str(number_2):
    return(0)
 elif number_1 == float(number_1) or number_2 == float(number_2):
     number_1 = int(number_1)
     number_2 = int(number_2)
     A = max(number_1, number_2)
     B = min(number_1, number_2)
     while B:
      mcd = B
      B = A % B
      A = mcd
      mcm =  (number_1 * number_2) // mcd

     return(mcm)

