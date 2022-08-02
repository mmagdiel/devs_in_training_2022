'''
    Diseñar una función que tome tres medidas en centímetros como entrada y devuelva el volumen en litros.
'''
def get_volumen_on_liters(number_1, number_2, number_3):
    
    if (number_1 == int):

        number1_litros = number_1 / 1000

        print (number1_litros)

    if (number_2 == int):

        number2_litros = number_2 / 1000

        print (number2_litros)
    
    if (number_3 == int):

        number3_litros = number_3 / 1000

        print (number3_litros)
    
    else:

        volumen = number1_litros * number2_litros * number3_litros

        return volumen