'''
    Diseñar una función que tome tres medidas en centímetros como entrada y devuelva el volumen en litros.
'''
def get_volumen_on_liters(number_1, number_2, number_3):
    if number_1==str(number_1) or number_2==str(number_2) or number_3==str(number_3):
            return 0
    if number_1< 0 or number_2<0 or number_3<0:
            return 0
    cm3= number_1*number_2*number_3
    litros = cm3/1000
    return litros
