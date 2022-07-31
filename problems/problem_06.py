'''
    Escribir una función que recibe tres números y descubra si uno de ellos divide el producto de los otros dos.
'''
def is_divide_product_of_the_other(number_1, number_2, number_3):
    if number_1 == str(number_1) or number_2 == str(number_2) or number_3 == str(number_3):
        return False
    if number_1*number_2 % number_3 == 0 or number_1*number_3 % number_2 == 0 or number_2 * number_3 % number_1 == 0:   return True
    else:
        return False
