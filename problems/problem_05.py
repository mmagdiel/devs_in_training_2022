'''
    Escribir una función que lea cuatro números y retorne el mayor de los cuatro.
'''
def max_of_four_number(number_1, number_2, number_3, number_4):
    if number_1 == str(number_1) or number_2 == str(number_2) or number_3 == str(number_3) or number_4 == str(number_4):
        return 0
    elif number_1 >= number_2 and number_1 >= number_3 and number_1 >= number_4:
    	return number_1
    elif number_2 >= number_1 and number_2 >= number_3 and number_2 >= number_4:
        return number_2
    elif number_3 >= number_1 and number_3 >= number_2 and number_3 >= number_4:
    	return number_3
    else: 
    	return number_4
