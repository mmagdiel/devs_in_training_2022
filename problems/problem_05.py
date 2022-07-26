'''
    Escribir una función que lea cuatro números y retorne el mayor de los cuatro.
'''
def max_of_four_number(number_1, number_2, number_3, number_4):
#n1>n2,n1>n3,n1>n4
#n2>n1,n2>n3,n2>n4
#n3>n1,n3>n2,n3>n4
#n4>n1,n4>n2,n4>n3
    if number_1>number_2 and number_1>number_3 and number_1>number_4:
        return number_1
    elif number_2>number_1 and number_2>number_3 and number_2>number_4:
        return number_2
    elif number_3>number_1 and number_3>number_2 and number_3>number_4:
        return number_3
    elif number_4>number_1 and number_4>number_2 and number_4>number_3:
        return number_4
