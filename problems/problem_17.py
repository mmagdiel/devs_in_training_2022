'''
    Diseñar una función que tome tres medidas en centímetros como entrada y devuelva el volumen en litros.
'''
from unittest import result


number_1 = 0
number_2 = 10
number_3 = 'lorem'
def get_volumen_on_liters(number_1, number_2, number_3):
    
     cmCubicos= number_1 * number_2 * number_3
     result = cmCubicos / 1000
     print(int(result))
get_volumen_on_liters(number_1,number_2,number_3)    
