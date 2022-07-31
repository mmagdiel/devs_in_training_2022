'''
    Mostrar la suma de dos números cualquiera, solo si estos son distintos.
'''
def sum_distinc_numbers(number_1, number_2):
    if type(number_1)==type(list()) or type(number_2)==type(list()): 
        return 0
    if number_1 == str(number_1) or number_2 == str(number_2):
        return 0
    if number_1 != number_2:
        return number_1+number_2
    else:
        return 0
