'''
    Mostrar la suma de dos números cualquiera, solo si estos son distintos.
'''
def sum_distinc_numbers(number_1, number_2):
    if number_1 == str(number_1) or number_2 == str(number_2) or number_1 == number_2 or type(number_1)==list or type(number_2)==list:
        return 0
    elif number_1 != number_2:
        suma = number_1 + number_2
        return suma
